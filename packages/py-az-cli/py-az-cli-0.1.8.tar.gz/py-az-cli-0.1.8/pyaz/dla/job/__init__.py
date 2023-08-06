'''
Manage Data Lake Analytics jobs.
'''
from ... pyaz_utils import _call_az
from . import pipeline, recurrence


def submit(account, job_name, script, compile_mode=None, compile_only=None, degree_of_parallelism=None, pipeline_id=None, pipeline_name=None, pipeline_uri=None, priority=None, recurrence_id=None, recurrence_name=None, run_id=None, runtime_version=None):
    '''
    Submit a job to a Data Lake Analytics account.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - job_name -- None
    - script -- The script to submit. This is either the script contents or use `@<file path>` to load the script from a file

    Optional Parameters:
    - compile_mode -- Indicates the type of compilation to be done on this job. Valid values are: 'Semantic' (Only performs semantic checks and necessary sanity checks), 'Full' (full compilation) and 'SingleBox' (Full compilation performed locally)
    - compile_only -- Indicates that the submission should only build the job and not execute if set to true.
    - degree_of_parallelism -- None
    - pipeline_id -- Job relationship pipeline GUID.
    - pipeline_name -- Friendly name of the job relationship pipeline.
    - pipeline_uri -- Unique pipeline URI which links to the originating service for this pipeline.
    - priority -- None
    - recurrence_id -- Recurrence GUID, unique per activity/script, regardless of iteration. Links different occurrences of the same job together.
    - recurrence_name -- Friendly recurrence nae for the correlation between jobs.
    - run_id -- GUID of the iteration of this pipeline.
    - runtime_version -- None
    '''
    return _call_az("az dla job submit", locals())


def wait(account, job_id, max_wait_time_sec=None, wait_interval_sec=None):
    '''
    Wait for a Data Lake Analytics job to finish.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - job_id -- None

    Optional Parameters:
    - max_wait_time_sec -- The maximum amount of time to wait before erroring out. Default value is to never timeout. Any value <= 0 means never timeout
    - wait_interval_sec -- The polling interval between checks for the job status, in seconds.
    '''
    return _call_az("az dla job wait", locals())


def show(account, job_identity):
    '''
    Get information for a Data Lake Analytics job.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - job_identity -- JobInfo ID.
    '''
    return _call_az("az dla job show", locals())


def cancel(account, job_identity):
    '''
    Cancel a Data Lake Analytics job.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - job_identity -- JobInfo ID to cancel.
    '''
    return _call_az("az dla job cancel", locals())


def list(account, name=None, pipeline_id=None, recurrence_id=None, result=None, state=None, submitted_after=None, submitted_before=None, submitter=None, top=None):
    '''
    List Data Lake Analytics jobs.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.

    Optional Parameters:
    - name -- A filter which returns jobs only by the specified friendly name.
    - pipeline_id -- A filter which returns jobs only containing the specified pipeline_id.
    - recurrence_id -- A filter which returns jobs only containing the specified recurrence_id.
    - result -- A filter which returns jobs with only the specified result(s).
    - state -- A filter which returns jobs with only the specified state(s).
    - submitted_after -- A filter which returns jobs only submitted after the specified time, in ISO-8601 format.
    - submitted_before -- A filter which returns jobs only submitted before the specified time, in ISO-8601 format.
    - submitter -- A filter which returns jobs only by the specified submitter.
    - top -- Maximum number of items to return.
    '''
    return _call_az("az dla job list", locals())

