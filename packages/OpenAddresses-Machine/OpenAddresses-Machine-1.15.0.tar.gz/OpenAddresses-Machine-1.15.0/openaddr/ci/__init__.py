import logging; _L = logging.getLogger('openaddr.ci')

from ..compat import standard_library
from .. import jobs, __version__

from os.path import relpath, splitext
from collections import OrderedDict
from urllib.parse import urljoin
from datetime import timedelta
from functools import wraps
from uuid import uuid4, getnode
from time import sleep
import hashlib, hmac
import json, os

from flask import Flask, request, Response, current_app, jsonify, render_template
from uritemplate import expand
from requests import get, post
from dateutil.tz import tzutc
from psycopg2 import connect
from boto import connect_sns
from pq import PQ

def load_config():
    def truthy(value):
        return bool(value.lower() in ('yes', 'true'))
    
    secrets_string = os.environ.get('WEBHOOK_SECRETS', u'').encode('utf8')
    webhook_secrets = secrets_string.split(b',') if secrets_string else []

    return dict(GAG_GITHUB_STATUS=truthy(os.environ.get('GAG_GITHUB_STATUS', '')),
                GITHUB_AUTH=(os.environ['GITHUB_TOKEN'], 'x-oauth-basic'),
                DATABASE_URL=os.environ['DATABASE_URL'],
                WEBHOOK_SECRETS=webhook_secrets)

def log_application_errors(route_function):
    ''' Error-logging decorator for route functions.
    
        Don't do much, but get an error out to the logger.
    '''
    @wraps(route_function)
    def decorated_function(*args, **kwargs):
        try:
            return route_function(*args, **kwargs)
        except Exception as e:
            _L.error(e, exc_info=True)
            raise

    return decorated_function

def enforce_signature(route_function):
    ''' Look for a signature and bark if it's wrong.
    '''
    @wraps(route_function)
    def decorated_function(*args, **kwargs):
        if not current_app.config['WEBHOOK_SECRETS']:
            # No configured secrets means no signature needed.
            current_app.logger.info('No /hook signature required')
            return route_function(*args, **kwargs)
    
        if 'X-Hub-Signature' not in request.headers:
            # Missing required signature is an error.
            current_app.logger.warning('No /hook signature provided')
            return Response(json.dumps({'error': 'Missing signature'}),
                            401, content_type='application/json')

        def _sign(key):
            hash = hmac.new(key, request.data, hashlib.sha1)
            return 'sha1={}'.format(hash.hexdigest())

        actual = request.headers.get('X-Hub-Signature')
        expecteds = [_sign(k) for k in current_app.config['WEBHOOK_SECRETS']]
        expected = ', '.join(expecteds)
        
        if actual not in expecteds:
            # Signature mismatch is an error.
            current_app.logger.warning('Mismatched /hook signatures: {actual} vs. {expected}'.format(**locals()))
            return Response(json.dumps({'error': 'Invalid signature'}),
                            401, content_type='application/json')

        current_app.logger.info('Matching /hook signature: {actual}'.format(**locals()))
        return route_function(*args, **kwargs)

    return decorated_function

app = Flask(__name__)
app.config.update(load_config())

MAGIC_OK_MESSAGE = 'Everything is fine'
TASK_QUEUE, DONE_QUEUE, DUE_QUEUE = 'tasks', 'finished', 'due'

# Additional delay after JOB_TIMEOUT for due tasks.
DUETASK_DELAY = timedelta(minutes=5)

# Amount of time to reuse run results.
RUN_REUSE_TIMEOUT = timedelta(days=5)

# Time to chill out in pop_task_from_taskqueue() after sending Done task.
WORKER_COOLDOWN = timedelta(seconds=5)

@app.before_first_request
def app_prepare():
    setup_logger(os.environ.get('AWS_SNS_ARN'), logging.WARNING)

@app.route('/')
@log_application_errors
def app_index():
    return 'Yo.'

@app.route('/hook', methods=['POST'])
@log_application_errors
@enforce_signature
def app_hook():
    github_auth = current_app.config['GITHUB_AUTH']
    webhook_payload = json.loads(request.data.decode('utf8'))
    
    if skip_payload(webhook_payload):
        return jsonify({'url': None, 'files': [], 'skip': True})
    
    commit_sha, status_url = get_commit_info(webhook_payload)
    if current_app.config['GAG_GITHUB_STATUS']:
        status_url = None
    
    try:
        files = process_payload_files(webhook_payload, github_auth)
    except Exception as e:
        message = 'Could not read source files: {}'.format(e)
        update_error_status(status_url, message, [], github_auth)
        _L.error(message, exc_info=True)
        return jsonify({'url': None, 'files': [], 'status_url': status_url})
    
    if not files:
        update_empty_status(status_url, github_auth)
        _L.warning('No files')
        return jsonify({'url': None, 'files': [], 'status_url': status_url})

    filenames = list(files.keys())
    job_url_template = urljoin(request.url, '/jobs/{id}')

    with db_connect(current_app.config['DATABASE_URL']) as conn:
        queue = db_queue(conn, TASK_QUEUE)
        try:
            job_id = create_queued_job(queue, files, job_url_template, commit_sha, status_url)
            job_url = expand(job_url_template, dict(id=job_id))
        except Exception as e:
            # Oops, tell Github something went wrong.
            update_error_status(status_url, str(e), filenames, github_auth)
            _L.error('Oops', exc_info=True)
            return Response(json.dumps({'error': str(e), 'files': files,
                                        'status_url': status_url}),
                            500, content_type='application/json')
        else:
            # That worked, tell Github we're working on it.
            update_pending_status(status_url, job_url, filenames, github_auth)
            return jsonify({'id': job_id, 'url': job_url, 'files': files,
                            'status_url': status_url})

@app.route('/jobs/<job_id>', methods=['GET'])
@log_application_errors
def app_get_job(job_id):
    '''
    '''
    with db_connect(current_app.config['DATABASE_URL']) as conn:
        with db_cursor(conn) as db:
            try:
                status, task_files, file_states, file_results, github_status_url = read_job(db, job_id)
            except TypeError:
                return Response('Job {} not found'.format(job_id), 404)
    
    statuses = False, None, True
    key_func = lambda _path: (statuses.index(file_states[_path[1]]), _path[1])
    file_tuples = [(sha, path) for (sha, path) in task_files.items()]

    ordered_files = OrderedDict(sorted(file_tuples, key=key_func))
    
    job = dict(status=status, task_files=ordered_files, file_states=file_states,
               file_results=file_results, github_status_url=github_status_url)
    
    return render_template('job.html', job=job)

def td2str(td):
    ''' Convert a timedelta to a string formatted like '3h'.
    
        Will not be necessary when https://github.com/malthe/pq/pull/5 is released.
    '''
    return '{}s'.format(td.seconds + td.days * 86400)

def get_touched_payload_files(payload):
    ''' Return a set of files modified in payload commits.
    '''
    touched = set()
    
    # Iterate over commits in chronological order.
    for commit in payload['commits']:
        for filelist in (commit['added'], commit['modified']):
            # Include any potentially-new files.
            touched.update(filelist)
        
        for filename in commit['removed']:
            # Skip files that no longer exist.
            if filename in touched:
                touched.remove(filename)
        
    current_app.logger.debug(u'Touched files {}'.format(', '.join(touched)))
    
    return touched

def get_touched_branch_files(payload, github_auth):
    ''' Return a set of files modified between master and payload head.
    '''
    branch_sha = payload['head_commit']['id']

    compare1_url = payload['repository']['compare_url']
    compare1_url = expand(compare1_url, dict(base='master', head=branch_sha))
    current_app.logger.debug('Compare URL 1 {}'.format(compare1_url))
    
    compare1 = get(compare1_url, auth=github_auth).json()
    merge_base_sha = compare1['merge_base_commit']['sha']
    
    # That's no branch.
    if merge_base_sha == branch_sha:
        return set()

    compare2_url = payload['repository']['compare_url']
    compare2_url = expand(compare2_url, dict(base=merge_base_sha, head=branch_sha))
    current_app.logger.debug('Compare URL 2 {}'.format(compare2_url))
    
    compare2 = get(compare2_url, auth=github_auth).json()
    touched = set([file['filename'] for file in compare2['files']])
    current_app.logger.debug(u'Touched files {}'.format(', '.join(touched)))
    
    return touched

def get_touched_pullrequest_files(payload, github_auth):
    ''' Return a set of files modified between master and payload head.
    '''
    if payload['action'] == 'closed':
        return set()
    
    base_sha = payload['pull_request']['base']['sha']
    head_sha = payload['pull_request']['head']['sha']

    compare_url = payload['pull_request']['head']['repo']['compare_url']
    compare_url = expand(compare_url, dict(head=head_sha, base=base_sha))
    current_app.logger.debug('Compare URL {}'.format(compare_url))
    
    compare = get(compare_url, auth=github_auth).json()
    touched = set([file['filename'] for file in compare['files']])
    current_app.logger.debug(u'Touched files {}'.format(', '.join(touched)))
    
    return touched

def skip_payload(payload):
    ''' Return True if this payload should not be processed.
    '''
    if 'action' in payload and 'pull_request' in payload:
        return bool(payload['action'] == 'closed')
    
    if 'commits' in payload and 'head_commit' in payload:
        # Deleted refs will not have a status URL.
        return bool(payload.get('deleted') == True)
    
    return True

def process_payload_files(payload, github_auth):
    ''' Return a dictionary of file paths to raw JSON contents and file IDs.
    '''
    if 'action' in payload and 'pull_request' in payload:
        return process_pullrequest_payload_files(payload, github_auth)
    
    if 'commits' in payload and 'head_commit' in payload:
        return process_pushevent_payload_files(payload, github_auth)
    
    raise ValueError('Unintelligible webhook payload')

def process_pullrequest_payload_files(payload, github_auth):
    ''' Return a dictionary of files paths from a pull request event payload.
    
        https://developer.github.com/v3/activity/events/types/#pullrequestevent
    '''
    files = dict()
    touched = get_touched_pullrequest_files(payload, github_auth)
    
    commit_sha = payload['pull_request']['head']['sha']
    
    for filename in touched:
        if relpath(filename, 'sources').startswith('..'):
            # Skip things outside of sources directory.
            continue
        
        if splitext(filename)[1] != '.json':
            # Skip non-JSON files.
            continue

        contents_url = payload['pull_request']['head']['repo']['contents_url']
        try:
            contents_url = expand(contents_url, dict(path=filename))
        except UnicodeEncodeError:
            # Python 2 behavior
            contents_url = expand(contents_url, dict(path=filename.encode('utf8')))
        contents_url = '{contents_url}?ref={commit_sha}'.format(**locals())
        
        current_app.logger.debug('Contents URL {}'.format(contents_url))
        
        got = get(contents_url, auth=github_auth)
        contents = got.json()
        
        if got.status_code not in range(200, 299):
            current_app.logger.warning('Skipping {} - {}'.format(filename, got.status_code))
            continue
        
        if contents['encoding'] != 'base64':
            raise ValueError('Unrecognized encoding "{encoding}"'.format(**contents))
        
        current_app.logger.debug('Contents SHA {sha}'.format(**contents))
        files[filename] = contents['content'], contents['sha']
    
    return files

def process_pushevent_payload_files(payload, github_auth):
    ''' Return a dictionary of files paths from a push event payload.
    
        https://developer.github.com/v3/activity/events/types/#pushevent
    '''
    files = dict()
    touched = get_touched_payload_files(payload)
    touched |= get_touched_branch_files(payload, github_auth)
    
    commit_sha = payload['head_commit']['id']
    
    for filename in touched:
        if relpath(filename, 'sources').startswith('..'):
            # Skip things outside of sources directory.
            continue
        
        if splitext(filename)[1] != '.json':
            # Skip non-JSON files.
            continue
        
        contents_url = payload['repository']['contents_url']
        try:
            contents_url = expand(contents_url, dict(path=filename))
        except UnicodeEncodeError:
            # Python 2 behavior
            contents_url = expand(contents_url, dict(path=filename.encode('utf8')))
        contents_url = '{contents_url}?ref={commit_sha}'.format(**locals())
        
        current_app.logger.debug('Contents URL {}'.format(contents_url))
        
        got = get(contents_url, auth=github_auth)
        contents = got.json()
        
        if got.status_code not in range(200, 299):
            current_app.logger.warning('Skipping {} - {}'.format(filename, got.status_code))
            continue
        
        if contents['encoding'] != 'base64':
            raise ValueError('Unrecognized encoding "{encoding}"'.format(**contents))
        
        current_app.logger.debug('Contents SHA {sha}'.format(**contents))
        files[filename] = contents['content'], contents['sha']
    
    return files

def get_commit_info(payload):
    ''' Get commit SHA and Github status API URL from webhook payload.
    '''
    if 'pull_request' in payload:
        commit_sha = payload['pull_request']['head']['sha']
        status_url = payload['pull_request']['statuses_url']
    
    elif 'head_commit' in payload:
        commit_sha = payload['head_commit']['id']
        status_url = payload['repository']['statuses_url']
        status_url = expand(status_url, dict(sha=commit_sha))
    
    else:
        raise ValueError('Unintelligible payload')
    
    current_app.logger.debug('Status URL {}'.format(status_url))
    
    return commit_sha, status_url

def post_github_status(status_url, status_json, github_auth):
    ''' POST status JSON to Github status API.
    '''
    if status_url is None:
        return
    
    # Github only wants 140 chars of description.
    status_json['description'] = status_json['description'][:140]
    
    posted = post(status_url, data=json.dumps(status_json), auth=github_auth,
                  headers={'Content-Type': 'application/json'})
    
    if posted.status_code not in range(200, 299):
        raise ValueError('Failed status post to {}'.format(status_url))
    
    if posted.json()['state'] != status_json['state']:
        raise ValueError('Mismatched status post to {}'.format(status_url))

def update_pending_status(status_url, job_url, filenames, github_auth):
    ''' Push pending status for head commit to Github status API.
    '''
    status = dict(context='openaddresses/hooked', state='pending',
                  description=u'Checking {}'.format(', '.join(filenames)),
                  target_url=job_url)
    
    return post_github_status(status_url, status, github_auth)

def update_error_status(status_url, message, filenames, github_auth):
    ''' Push error status for head commit to Github status API.
    '''
    status = dict(context='openaddresses/hooked', state='error',
                  description=u'Errored on {}: {}'.format(', '.join(filenames), message))
    
    return post_github_status(status_url, status, github_auth)

def update_failing_status(status_url, job_url, bad_files, filenames, github_auth):
    ''' Push failing status for head commit to Github status API.
    '''
    status = dict(context='openaddresses/hooked', state='failure',
                  description=u'Failed on {} from {}'.format(', '.join(bad_files), ', '.join(filenames)),
                  target_url=job_url)
    
    return post_github_status(status_url, status, github_auth)

def update_empty_status(status_url, github_auth):
    ''' Push success status for head commit to Github status API.
    '''
    status = dict(context='openaddresses/hooked', state='success',
                  description='Nothing to check')
    
    return post_github_status(status_url, status, github_auth)

def update_success_status(status_url, job_url, filenames, github_auth):
    ''' Push success status for head commit to Github status API.
    '''
    status = dict(context='openaddresses/hooked', state='success',
                  description=u'Succeeded on {}'.format(', '.join(filenames)),
                  target_url=job_url)
    
    return post_github_status(status_url, status, github_auth)

def calculate_job_id(files):
    '''
    '''
    return str(uuid4())
    
    #
    # Previously, we created a deterministic hash of
    # the files, but for now that might be too optimistic.
    #
    blob = json.dumps(files, ensure_ascii=True, sort_keys=True)
    job_id = sha1(blob).hexdigest()
    
    return job_id

def create_queued_job(queue, files, job_url_template, commit_sha, status_url):
    ''' Create a new job, and add its files to the queue.
    '''
    filenames = list(files.keys())
    file_states = {name: None for name in filenames}
    file_results = {name: None for name in filenames}

    job_id = calculate_job_id(files)
    job_url = job_url_template and expand(job_url_template, dict(id=job_id))
    job_status = None

    with queue as db:
        task_files = add_files_to_queue(queue, job_id, job_url, files, commit_sha)
        add_job(db, job_id, None, task_files, file_states, file_results, status_url)
    
    return job_id

def add_files_to_queue(queue, job_id, job_url, files, commit_sha):
    ''' Make a new task for each file, return dict of file IDs to file names.
    '''
    tasks = {}
    
    for (file_name, (content_b64, file_id)) in files.items():
        task_data = dict(job_id=job_id, url=job_url, name=file_name,
                         content_b64=content_b64, file_id=file_id,
                         commit_sha=commit_sha)
    
        # Spread tasks out over time.
        delay = timedelta(len(tasks))

        queue.put(task_data, expected_at=td2str(delay))
        tasks[file_id] = file_name
    
    return tasks

def add_job(db, job_id, status, task_files, file_states, file_results, status_url):
    ''' Save information about a job to the database.
    
        Throws an IntegrityError exception if the job ID exists.
    '''
    db.execute('''INSERT INTO jobs
                  (task_files, file_states, file_results, github_status_url, status, id)
                  VALUES (%s::json, %s::json, %s::json, %s, %s, %s)''',
               (json.dumps(task_files), json.dumps(file_states),
                json.dumps(file_results), status_url, status, job_id))

def write_job(db, job_id, status, task_files, file_states, file_results, status_url):
    ''' Save information about a job to the database.
    '''
    db.execute('''UPDATE jobs
                  SET task_files=%s::json, file_states=%s::json,
                      file_results=%s::json, github_status_url=%s, status=%s
                  WHERE id = %s''',
               (json.dumps(task_files), json.dumps(file_states),
                json.dumps(file_results), status_url, status, job_id))

def read_job(db, job_id):
    ''' Read information about a job from the database.
    
        Returns (status, task_files, file_states, file_results, github_status_url) or None.
    '''
    db.execute('''SELECT status, task_files, file_states, file_results, github_status_url
                  FROM jobs WHERE id = %s''', (job_id, ))
    
    try:
        status, task_files, states, file_results, github_status_url = db.fetchone()
    except TypeError:
        return None
    else:
        return status, task_files, states, file_results, github_status_url

def is_completed_run(db, run_id, min_datetime):
    '''
    '''
    if min_datetime.tzinfo:
        # Convert known time zones to UTC.
        min_dtz = min_datetime.astimezone(tzutc())
    else:
        # Assume unspecified time zones are UTC.
        min_dtz = min_datetime.replace(tzinfo=tzutc())

    db.execute('''SELECT id, status FROM runs
                  WHERE id = %s AND status IS NOT NULL
                    AND datetime_tz >= %s''',
               (run_id, min_dtz))
    
    completed_run = db.fetchone()
    
    if completed_run:
        _L.debug('Found completed run {0} ({1}) since {min_datetime}'.format(*completed_run, **locals()))
    else:
        _L.debug('No completed run {run_id} since {min_datetime}'.format(**locals()))
    
    return bool(completed_run is not None)

def add_run(db):
    ''' Reserve a row in the runs table and return its new ID.
    '''
    db.execute("INSERT INTO runs (datetime_tz) VALUES (NOW())")
    db.execute("SELECT currval('runs_id_seq')")
    
    (run_id, ) = db.fetchone()
    
    return run_id

def set_run(db, run_id, filename, file_id, content_b64, run_state, run_status,
            job_id, commit_sha):
    ''' Populate an identitified row in the runs table.
    '''
    worker_id, code_version = hex(getnode()), __version__
    
    db.execute('''UPDATE runs SET
                  source_path = %s, source_data = %s, source_id = %s,
                  state = %s::json, status = %s, worker_id = %s,
                  code_version = %s, job_id = %s, commit_sha = %s,
                  datetime_tz = NOW()
                  WHERE id = %s''',
               (filename, content_b64, file_id,
               json.dumps(run_state), run_status, worker_id,
               code_version, job_id, commit_sha,
               run_id))

def copy_run(db, run_id):
    ''' Duplicate a previous run and return its new ID.
    '''
    db.execute('''INSERT INTO runs
                  (copy_of, source_path, source_id, source_data, state, status,
                   worker_id, code_version, job_id, datetime_tz)
                  SELECT id, source_path, source_id, source_data, state, status,
                         worker_id, code_version, job_id, NOW()
                  FROM runs
                  WHERE id = %s''',
               (run_id, ))

    db.execute("SELECT currval('runs_id_seq')")
    
    (run_id, ) = db.fetchone()
    
    return run_id

def get_previously_completed_run(db, file_id):
    ''' Look for an existing run on this file ID within the reuse timeout limit.
    '''
    interval = '{} seconds'.format(RUN_REUSE_TIMEOUT.seconds + RUN_REUSE_TIMEOUT.days * 86400)
    
    db.execute('''SELECT id, state, status FROM runs
                  WHERE source_id = %s
                    AND datetime_tz > NOW() - INTERVAL %s
                    AND status IS NOT NULL
                    AND copy_of IS NULL
                  ORDER BY id DESC LIMIT 1''',
               (file_id, interval))
    
    previous_run = db.fetchone()
    
    if previous_run:
        _L.debug('Found previous run {0} ({2}) for file {file_id}'.format(*previous_run, **locals()))
    else:
        _L.debug('No previous run for file {file_id}'.format(**locals()))

    return previous_run

def update_job_status(db, job_id, job_url, filenames, task_files, file_states, file_results, status_url, github_auth):
    '''
    '''
    if False in file_states.values():
        # Any task failure means the whole job has failed.
        job_status = False
    elif None in file_states.values():
        job_status = None
    else:
        job_status = True
    
    write_job(db, job_id, job_status, task_files, file_states, file_results, status_url)
    
    if not status_url:
        _L.warning('No status_url to tell about {} status of job {}'.format(job_status, job_id))
        return
    
    if job_status is False:
        bad_files = [name for (name, state) in file_states.items() if state is False]
        update_failing_status(status_url, job_url, bad_files, filenames, github_auth)
    
    elif job_status is None:
        update_pending_status(status_url, job_url, filenames, github_auth)
    
    elif job_status is True:
        update_success_status(status_url, job_url, filenames, github_auth)

def pop_task_from_taskqueue(s3, task_queue, done_queue, due_queue, output_dir):
    '''
    '''
    with task_queue as db:
        task = task_queue.get()

        # PQ will return NULL after 1 second timeout if not ask
        if task is None:
            return

        _L.info('Got job {job_id} from task queue'.format(**task.data))
        passed_on_keys = 'job_id', 'file_id', 'name', 'url', 'content_b64', 'commit_sha'
        passed_on_kwargs = {k: task.data.get(k) for k in passed_on_keys}
        previous_run = get_previously_completed_run(db, task.data.get('file_id'))
    
        if previous_run:
            # Make a copy of the previous run.
            previous_run_id, _, _ = previous_run
            passed_on_kwargs['run_id'] = copy_run(db, previous_run_id)
            
            # Don't send a due task, since we will not be doing any actual work.
        
        else:
            # Reserve space for a new run.
            passed_on_kwargs['run_id'] = add_run(db)

            # Send a Due task, possibly for later.
            due_task_data = dict(task_data=task.data, **passed_on_kwargs)
            due_queue.put(due_task_data, schedule_at=td2str(jobs.JOB_TIMEOUT + DUETASK_DELAY))
    
    if previous_run:
        # Re-use result from the previous run.
        run_id, state, status = previous_run
        message = MAGIC_OK_MESSAGE if status else 'Re-using failed previous run'
        result = dict(message=message, reused_run=run_id, output=state)

    else:
        # Run the task.
        from . import worker # <-- TODO: un-suck this.
        source_name, _ = splitext(relpath(passed_on_kwargs['name'], 'sources'))
        result = worker.do_work(s3, passed_on_kwargs['run_id'], source_name,
                                passed_on_kwargs['content_b64'], output_dir)

    # Send a Done task
    done_task_data = dict(result=result, **passed_on_kwargs)
    done_queue.put(done_task_data, expected_at=td2str(timedelta(0)))
    
    # Sleep a short time to allow done task to show up in runs table.
    # In a one-worker situation with repetitive pull request jobs,
    # this helps the next job take advantage of previous run results.
    sleep(WORKER_COOLDOWN.seconds + WORKER_COOLDOWN.days * 86400)

def pop_task_from_donequeue(queue, github_auth):
    ''' Look for a completed job in the "done" task queue, update Github status.
    '''
    with queue as db:
        task = queue.get()
    
        if task is None:
            return
    
        _L.info('Got job {job_id} from done queue'.format(**task.data))
        results = task.data['result']
        message = results['message']
        run_state = results.get('output', None)
        content_b64 = task.data['content_b64']
        commit_sha = task.data['commit_sha']
        job_url = task.data['url']
        filename = task.data['name']
        file_id = task.data['file_id']
        run_id = task.data['run_id']
        job_id = task.data['job_id']
        
        if is_completed_run(db, run_id, task.enqueued_at):
            # We are too late, this got handled.
            return
        
        run_status = bool(message == MAGIC_OK_MESSAGE)
        set_run(db, run_id, filename, file_id, content_b64, run_state,
                run_status, job_id, commit_sha)

        try:
            _, task_files, file_states, file_results, status_url = read_job(db, job_id)
        except TypeError:
            raise Exception('Job {} not found'.format(job_id))
    
        if filename not in file_states:
            raise Exception('Unknown file from job {}: "{}"'.format(job_id, filename))
        
        filenames = list(task_files.values())
        file_states[filename] = run_status
        file_results[filename] = results
        
        update_job_status(db, job_id, job_url, filenames, task_files,
                          file_states, file_results, status_url, github_auth)

def pop_task_from_duequeue(queue, github_auth):
    '''
    '''
    with queue as db:
        task = queue.get()
    
        if task is None:
            return
        
        _L.info('Got job {job_id} from due queue'.format(**task.data))
        original_task = task.data['task_data']
        content_b64 = task.data['content_b64']
        commit_sha = task.data['commit_sha']
        job_url = task.data['url']
        filename = task.data['name']
        file_id = task.data['file_id']
        run_id = task.data['run_id']
        job_id = task.data['job_id']
    
        if is_completed_run(db, run_id, task.enqueued_at):
            # Everything's fine, this got handled.
            return

        run_status = False
        set_run(db, run_id, filename, file_id, content_b64, None, run_status,
                job_id, commit_sha)

        try:
            _, task_files, file_states, file_results, status_url = read_job(db, job_id)
        except TypeError:
            raise Exception('Job {} not found'.format(job_id))
    
        if filename not in file_states:
            raise Exception('Unknown file from job {}: "{}"'.format(job_id, filename))
        
        filenames = list(task_files.values())
        file_states[filename] = run_status
        file_results[filename] = False
        
        update_job_status(db, job_id, job_url, filenames, task_files,
                          file_states, file_results, status_url, github_auth)

def db_connect(dsn):
    ''' Connect to database using DSN string.
    '''
    return connect(dsn)

def db_queue(conn, name):
    return PQ(conn, table='queue')[name]

def db_cursor(conn):
    return conn.cursor()

class SnsHandler(logging.Handler):
    ''' Logs to the given Amazon SNS topic; meant for errors.
    '''
    def __init__(self, arn, *args, **kwargs):
        super(SnsHandler, self).__init__(*args, **kwargs)
        
        # Rely on boto AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY variables.
        self.arn, self.sns = arn, connect_sns()

    def emit(self, record):
        subject = u'OpenAddr: {}: {}'.format(record.levelname, record.name)
        self.sns.publish(self.arn, self.format(record), subject[:79])

def setup_logger(sns_arn, log_level=logging.DEBUG):
    ''' Set up logging for openaddr code.
    '''
    # Get a handle for the openaddr logger and its children
    openaddr_logger = logging.getLogger('openaddr')

    # Default logging format.
    log_format = '%(asctime)s %(levelname)07s: %(message)s'

    # Set the logger level to show everything, and filter down in the handlers.
    openaddr_logger.setLevel(log_level)

    # Set up a logger to stderr
    handler1 = logging.StreamHandler()
    handler1.setLevel(log_level)
    handler1.setFormatter(logging.Formatter(log_format))
    openaddr_logger.addHandler(handler1)
    
    # Set up a second logger to SNS
    try:
        handler2 = SnsHandler(sns_arn)
    except:
        openaddr_logger.warning('Failed to authenticate SNS handler')
    else:
        handler2.setLevel(logging.ERROR)
        handler2.setFormatter(logging.Formatter(log_format))
        openaddr_logger.addHandler(handler2)

if __name__ == '__main__':
    app.run(debug=True)
