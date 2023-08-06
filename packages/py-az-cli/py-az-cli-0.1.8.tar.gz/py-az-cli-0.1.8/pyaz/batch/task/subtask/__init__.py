'''
Manage subtask information of a Batch task.
'''
from .... pyaz_utils import _call_az

def list(job_id, task_id, account_endpoint=None, account_key=None, account_name=None, select=None):
    '''
    

    Required Parameters:
    - job_id -- The ID of the Job.
    - task_id -- The ID of the Task.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - select -- An OData $select clause.
    '''
    return _call_az("az batch task subtask list", locals())

