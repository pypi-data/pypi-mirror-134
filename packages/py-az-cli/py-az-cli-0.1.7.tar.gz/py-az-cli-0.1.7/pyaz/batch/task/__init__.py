'''
Manage Batch tasks.
'''
from ... pyaz_utils import _call_az
from . import file, subtask


def create(job_id, account_endpoint=None, account_key=None, account_name=None, affinity_id=None, application_package_references=None, command_line=None, environment_settings=None, json_file=None, max_task_retry_count=None, max_wall_clock_time=None, resource_files=None, retention_time=None, task_id=None):
    '''
    Create Batch tasks.

    Required Parameters:
    - job_id -- The ID of the job containing the task.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- The Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- The Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - affinity_id -- Required. You can pass the affinityId of a Node to indicate that this Task needs to run on that Compute Node. Note that this is just a soft affinity. If the target Compute Node is busy or unavailable at the time the Task is scheduled, then the Task will be scheduled elsewhere.
    - application_package_references -- The space-separated list of IDs specifying the application packages to be installed. Space-separated application IDs with optional version in 'id[#version]' format.
    - command_line -- The command line of the task. The command line does not run under a shell, and therefore cannot take advantage of shell features such as environment variable expansion. If you want to take advantage of such features, you should invoke the shell in the command line, for example using "cmd /c MyCommand" in Windows or "/bin/sh -c MyCommand" in Linux.
    - environment_settings -- A list of environment variable settings for the task. Space-separated values in 'key=value' format.
    - json_file -- The file containing the task(s) to create in JSON(formatted to match REST API request body). When submitting multiple tasks, accepts either an array of tasks or a TaskAddCollectionParamater. If this parameter is specified, all other parameters are ignored.
    - max_task_retry_count -- The maximum number of times the Task may be retried. The Batch service retries a Task if its exit code is nonzero. Note that this value specifically controls the number of retries for the Task executable due to a nonzero exit code. The Batch service will try the Task once, and may then retry up to this limit. For example, if the maximum retry count is 3, Batch tries the Task up to 4 times (one initial try and 3 retries). If the maximum retry count is 0, the Batch service does not retry the Task after the first attempt. If the maximum retry count is -1, the Batch service retries the Task without limit.
    - max_wall_clock_time -- If this is not specified, there is no time limit on how long the Task may run.
    - resource_files -- A list of files that the Batch service will download to the compute node before running the command line. Space-separated resource references in filename=httpurl format, with httpurl being any HTTP url with public access or a SAS url with read access.
    - retention_time -- The default is 7 days, i.e. the Task directory will be retained for 7 days unless the Compute Node is removed or the Job is deleted.
    - task_id -- The ID of the task.
    '''
    return _call_az("az batch task create", locals())


def list(job_id, account_endpoint=None, account_key=None, account_name=None, expand=None, filter=None, select=None):
    '''
    

    Required Parameters:
    - job_id -- The ID of the Job.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - expand -- An OData $expand clause.
    - filter -- An OData $filter clause. For more information on constructing this filter, see https://docs.microsoft.com/en-us/rest/api/batchservice/odata-filters-in-batch#list-tasks.
    - select -- An OData $select clause.
    '''
    return _call_az("az batch task list", locals())


def delete(job_id, task_id, account_endpoint=None, account_key=None, account_name=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None, yes=None):
    '''
    

    Required Parameters:
    - job_id -- The ID of the Job from which to delete the Task.
    - task_id -- The ID of the Task to delete.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - if_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
    - if_modified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    - if_none_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
    - if_unmodified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az batch task delete", locals())


def show(job_id, task_id, account_endpoint=None, account_key=None, account_name=None, expand=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None, select=None):
    '''
    

    Required Parameters:
    - job_id -- The ID of the Job that contains the Task.
    - task_id -- The ID of the Task to get information about.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - expand -- An OData $expand clause.
    - if_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
    - if_modified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    - if_none_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
    - if_unmodified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    - select -- An OData $select clause.
    '''
    return _call_az("az batch task show", locals())


def reset(job_id, task_id, account_endpoint=None, account_key=None, account_name=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None, json_file=None, max_task_retry_count=None, max_wall_clock_time=None, retention_time=None):
    '''
    Reset the properties of a Batch task.

    Required Parameters:
    - job_id -- The ID of the Job containing the Task.
    - task_id -- The ID of the Task to update.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - if_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
    - if_modified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    - if_none_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
    - if_unmodified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    - json_file -- A file containing the constraints specification in JSON (formatted to match the respective REST API body). If this parameter is specified, all 'Constraints Arguments' are ignored.
    - max_task_retry_count -- The maximum number of times the Task may be retried. The Batch service retries a Task if its exit code is nonzero. Note that this value specifically controls the number of retries for the Task executable due to a nonzero exit code. The Batch service will try the Task once, and may then retry up to this limit. For example, if the maximum retry count is 3, Batch tries the Task up to 4 times (one initial try and 3 retries). If the maximum retry count is 0, the Batch service does not retry the Task after the first attempt. If the maximum retry count is -1, the Batch service retries the Task without limit.
    - max_wall_clock_time -- If this is not specified, there is no time limit on how long the Task may run. Expected format is an ISO-8601 duration.
    - retention_time -- The default is 7 days, i.e. the Task directory will be retained for 7 days unless the Compute Node is removed or the Job is deleted. Expected format is an ISO-8601 duration.
    '''
    return _call_az("az batch task reset", locals())


def reactivate(job_id, task_id, account_endpoint=None, account_key=None, account_name=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None):
    '''
    

    Required Parameters:
    - job_id -- The ID of the Job containing the Task.
    - task_id -- The ID of the Task to reactivate.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - if_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
    - if_modified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    - if_none_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
    - if_unmodified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    '''
    return _call_az("az batch task reactivate", locals())


def stop(job_id, task_id, account_endpoint=None, account_key=None, account_name=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None):
    '''
    

    Required Parameters:
    - job_id -- The ID of the Job containing the Task.
    - task_id -- The ID of the Task to terminate.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - if_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
    - if_modified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    - if_none_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
    - if_unmodified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    '''
    return _call_az("az batch task stop", locals())

