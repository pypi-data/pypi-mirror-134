'''
Manage Batch jobs.
'''
from ... pyaz_utils import _call_az
from . import all_statistics, prep_release_status, task_counts


def create(account_endpoint=None, account_key=None, account_name=None, id=None, job_manager_task_command_line=None, job_manager_task_environment_settings=None, job_manager_task_id=None, job_manager_task_resource_files=None, job_max_task_retry_count=None, job_max_wall_clock_time=None, json_file=None, max_parallel_tasks=None, metadata=None, pool_id=None, priority=None, required_slots=None, uses_task_dependencies=None):
    '''
    Add a job to a Batch account.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - id -- Required. The ID can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. The ID is case-preserving and case-insensitive (that is, you may not have two IDs within an Account that differ only by case).
    - job_manager_task_command_line -- Required. The command line does not run under a shell, and therefore cannot take advantage of shell features such as environment variable expansion. If you want to take advantage of such features, you should invoke the shell in the command line, for example using "cmd /c MyCommand" in Windows or "/bin/sh -c MyCommand" in Linux. If the command line refers to file paths, it should use a relative path (relative to the Task working directory), or use the Batch provided environment variable (https://docs.microsoft.com/en-us/azure/batch/batch-compute-node-environment-variables).
    - job_manager_task_environment_settings --  Space-separated values in 'key=value' format.
    - job_manager_task_id -- Required. The ID can contain any combination of alphanumeric characters including hyphens and underscores and cannot contain more than 64 characters.
    - job_manager_task_resource_files -- Files listed under this element are located in the Task's working directory. There is a maximum size for the list of resource files.  When the max size is exceeded, the request will fail and the response error code will be RequestEntityTooLarge. If this occurs, the collection of ResourceFiles must be reduced in size. This can be achieved using .zip files, Application Packages, or Docker Containers. Space-separated resource references in filename=httpurl format.
    - job_max_task_retry_count -- The maximum number of times each Task may be retried. The Batch service retries a Task if its exit code is nonzero. Note that this value specifically controls the number of retries. The Batch service will try each Task once, and may then retry up to this limit. For example, if the maximum retry count is 3, Batch tries a Task up to 4 times (one initial try and 3 retries). If the maximum retry count is 0, the Batch service does not retry Tasks. If the maximum retry count is -1, the Batch service retries Tasks without limit. The default value is 0 (no retries).
    - job_max_wall_clock_time -- If the Job does not complete within the time limit, the Batch service terminates it and any Tasks that are still running. In this case, the termination reason will be MaxWallClockTimeExpiry. If this property is not specified, there is no time limit on how long the Job may run. Expected format is an ISO-8601 duration.
    - json_file -- A file containing the job specification in JSON (formatted to match the respective REST API body). If this parameter is specified, all 'Job Arguments' are ignored.
    - max_parallel_tasks -- The maximum number of tasks that can be executed in parallel for the job. The value of maxParallelTasks must be -1 or greater than 0 if specified. If not specified, the default value is -1, which means there's no limit to the number of tasks that can be run at once. You can update a job's maxParallelTasks after it has been created using the update job API. Default value: -1 .
    - metadata -- The Batch service does not assign any meaning to metadata; it is solely for the use of user code. Space-separated values in 'key=value' format.
    - pool_id -- The id of an existing pool. All the tasks of the job will run on the specified pool.
    - priority -- The priority of the Job. Priority values can range from -1000 to 1000, with -1000 being the lowest priority and 1000 being the highest priority. The default value is 0.
    - required_slots -- The number of scheduling slots that the Task requires to run. The default is 1. A Task can only be scheduled to run on a compute node if the node has enough free scheduling slots available. For multi-instance Tasks, this property is not supported and must not be specified.
    - uses_task_dependencies -- Whether Tasks in the Job can define dependencies on each other. The default is false. True if flag present.
    '''
    return _call_az("az batch job create", locals())


def delete(job_id, account_endpoint=None, account_key=None, account_name=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None, yes=None):
    '''
    

    Required Parameters:
    - job_id -- The ID of the Job to delete.

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
    return _call_az("az batch job delete", locals())


def show(job_id, account_endpoint=None, account_key=None, account_name=None, expand=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None, select=None):
    '''
    

    Required Parameters:
    - job_id -- The ID of the Job.

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
    return _call_az("az batch job show", locals())


def set(job_id, account_endpoint=None, account_key=None, account_name=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None, job_max_task_retry_count=None, job_max_wall_clock_time=None, json_file=None, max_parallel_tasks=None, metadata=None, on_all_tasks_complete=None, pool_id=None, priority=None):
    '''
    Update the properties of a Batch job. Updating a property in a subgroup will reset the unspecified properties of that group.

    Required Parameters:
    - job_id -- The ID of the Job whose properties you want to update.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - if_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
    - if_modified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    - if_none_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
    - if_unmodified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    - job_max_task_retry_count -- The maximum number of times each Task may be retried. The Batch service retries a Task if its exit code is nonzero. Note that this value specifically controls the number of retries. The Batch service will try each Task once, and may then retry up to this limit. For example, if the maximum retry count is 3, Batch tries a Task up to 4 times (one initial try and 3 retries). If the maximum retry count is 0, the Batch service does not retry Tasks. If the maximum retry count is -1, the Batch service retries Tasks without limit. The default value is 0 (no retries).
    - job_max_wall_clock_time -- If the Job does not complete within the time limit, the Batch service terminates it and any Tasks that are still running. In this case, the termination reason will be MaxWallClockTimeExpiry. If this property is not specified, there is no time limit on how long the Job may run. Expected format is an ISO-8601 duration.
    - json_file -- A file containing the job patch parameter specification in JSON (formatted to match the respective REST API body). If this parameter is specified, all 'Job Arguments' are ignored.
    - max_parallel_tasks -- The maximum number of tasks that can be executed in parallel for the job. The value of maxParallelTasks must be -1 or greater than 0 if specified. If not specified, the default value is -1, which means there's no limit to the number of tasks that can be run at once. You can update a job's maxParallelTasks after it has been created using the update job API.
    - metadata -- If omitted, the existing Job metadata is left unchanged. Space-separated values in 'key=value' format.
    - on_all_tasks_complete -- The action the Batch service should take when all Tasks in the Job are in the completed state. If omitted, the completion behavior is left unchanged. You may not change the value from terminatejob to noaction - that is, once you have engaged automatic Job termination, you cannot turn it off again. If you try to do this, the request fails with an 'invalid property value' error response; if you are calling the REST API directly, the HTTP status code is 400 (Bad Request).
    - pool_id -- The id of an existing pool. All the tasks of the job will run on the specified pool.
    - priority -- The priority of the Job. Priority values can range from -1000 to 1000, with -1000 being the lowest priority and 1000 being the highest priority. If omitted, the priority of the Job is left unchanged.
    '''
    return _call_az("az batch job set", locals())


def reset(job_id, account_endpoint=None, account_key=None, account_name=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None, job_max_task_retry_count=None, job_max_wall_clock_time=None, json_file=None, metadata=None, on_all_tasks_complete=None, pool_id=None, priority=None):
    '''
    Update the properties of a Batch job. Unspecified properties which can be updated are reset to their defaults.

    Required Parameters:
    - job_id -- The ID of the Job whose properties you want to update.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - if_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
    - if_modified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    - if_none_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
    - if_unmodified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    - job_max_task_retry_count -- The maximum number of times each Task may be retried. The Batch service retries a Task if its exit code is nonzero. Note that this value specifically controls the number of retries. The Batch service will try each Task once, and may then retry up to this limit. For example, if the maximum retry count is 3, Batch tries a Task up to 4 times (one initial try and 3 retries). If the maximum retry count is 0, the Batch service does not retry Tasks. If the maximum retry count is -1, the Batch service retries Tasks without limit. The default value is 0 (no retries).
    - job_max_wall_clock_time -- If the Job does not complete within the time limit, the Batch service terminates it and any Tasks that are still running. In this case, the termination reason will be MaxWallClockTimeExpiry. If this property is not specified, there is no time limit on how long the Job may run. Expected format is an ISO-8601 duration.
    - json_file -- A file containing the job update parameter specification in JSON (formatted to match the respective REST API body). If this parameter is specified, all 'Job Arguments' are ignored.
    - metadata -- If omitted, it takes the default value of an empty list; in effect, any existing metadata is deleted. Space-separated values in 'key=value' format.
    - on_all_tasks_complete -- The action the Batch service should take when all Tasks in the Job are in the completed state. If omitted, the completion behavior is set to noaction. If the current value is terminatejob, this is an error because a Job's completion behavior may not be changed from terminatejob to noaction. You may not change the value from terminatejob to noaction - that is, once you have engaged automatic Job termination, you cannot turn it off again. If you try to do this, the request fails and Batch returns status code 400 (Bad Request) and an 'invalid property value' error response. If you do not specify this element in a PUT request, it is equivalent to passing noaction. This is an error if the current value is terminatejob.
    - pool_id -- The id of an existing pool. All the tasks of the job will run on the specified pool.
    - priority -- The priority of the Job. Priority values can range from -1000 to 1000, with -1000 being the lowest priority and 1000 being the highest priority. If omitted, it is set to the default value 0.
    '''
    return _call_az("az batch job reset", locals())


def list(account_endpoint=None, account_key=None, account_name=None, expand=None, filter=None, job_schedule_id=None, select=None):
    '''
    List all of the jobs or job schedule in a Batch account.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- The Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- The Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - expand --  An OData $expand clause.
    - filter --  An OData $filter clause.
    - job_schedule_id -- The ID of the job schedule from which you want to get a list of jobs. If omitted, lists all jobs in the account.
    - select --  An OData $select clause.
    '''
    return _call_az("az batch job list", locals())


def disable(job_id, account_endpoint=None, account_key=None, account_name=None, disable_tasks=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None):
    '''
    

    Required Parameters:
    - job_id -- The ID of the Job to disable.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - disable_tasks -- Possible values include: 'requeue', 'terminate', 'wait'
    - if_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
    - if_modified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    - if_none_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
    - if_unmodified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    '''
    return _call_az("az batch job disable", locals())


def enable(job_id, account_endpoint=None, account_key=None, account_name=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None):
    '''
    

    Required Parameters:
    - job_id -- The ID of the Job to enable.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - if_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
    - if_modified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    - if_none_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
    - if_unmodified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    '''
    return _call_az("az batch job enable", locals())


def stop(job_id, account_endpoint=None, account_key=None, account_name=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None, terminate_reason=None):
    '''
    Stop a running Batch job.

    Required Parameters:
    - job_id -- The ID of the Job to terminate.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - if_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
    - if_modified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    - if_none_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
    - if_unmodified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    - terminate_reason -- 
    '''
    return _call_az("az batch job stop", locals())

