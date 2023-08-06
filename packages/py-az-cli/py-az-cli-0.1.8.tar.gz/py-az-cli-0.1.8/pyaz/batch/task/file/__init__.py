'''
Manage Batch task files.
'''
from .... pyaz_utils import _call_az

def delete(file_path, job_id, task_id, account_endpoint=None, account_key=None, account_name=None, recursive=None, yes=None):
    '''
    

    Required Parameters:
    - file_path -- The path to the Task file or directory that you want to delete.
    - job_id -- The ID of the Job that contains the Task.
    - task_id -- The ID of the Task whose file you want to delete.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - recursive -- Whether to delete children of a directory. If the filePath parameter represents a directory instead of a file, you can set recursive to true to delete the directory and all of the files and subdirectories in it. If recursive is false then the directory must be empty or deletion will fail.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az batch task file delete", locals())


def download(destination, file_path, job_id, task_id, account_endpoint=None, account_key=None, account_name=None, end_range=None, if_modified_since=None, if_unmodified_since=None, start_range=None):
    '''
    Download the content of a Batch task file.

    Required Parameters:
    - destination -- The path to the destination file or directory.
    - file_path -- The path to the Task file that you want to get the content of.
    - job_id -- The ID of the Job that contains the Task.
    - task_id -- The ID of the Task whose file you want to retrieve.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - end_range -- The byte range to be retrieved. If not set the file will be retrieved to the end.
    - if_modified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    - if_unmodified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    - start_range -- The byte range to be retrieved. If not set the file will be retrieved from the beginning.
    '''
    return _call_az("az batch task file download", locals())


def show(file_path, job_id, task_id, account_endpoint=None, account_key=None, account_name=None, if_modified_since=None, if_unmodified_since=None):
    '''
    

    Required Parameters:
    - file_path -- The path to the Task file that you want to get the properties of.
    - job_id -- The ID of the Job that contains the Task.
    - task_id -- The ID of the Task whose file you want to get the properties of.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - if_modified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    - if_unmodified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    '''
    return _call_az("az batch task file show", locals())


def list(job_id, task_id, account_endpoint=None, account_key=None, account_name=None, filter=None, recursive=None):
    '''
    

    Required Parameters:
    - job_id -- The ID of the Job that contains the Task.
    - task_id -- The ID of the Task whose files you want to list.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - filter -- An OData $filter clause. For more information on constructing this filter, see https://docs.microsoft.com/en-us/rest/api/batchservice/odata-filters-in-batch#list-task-files.
    - recursive -- Whether to list children of the Task directory. This parameter can be used in combination with the filter parameter to list specific type of files.
    '''
    return _call_az("az batch task file list", locals())

