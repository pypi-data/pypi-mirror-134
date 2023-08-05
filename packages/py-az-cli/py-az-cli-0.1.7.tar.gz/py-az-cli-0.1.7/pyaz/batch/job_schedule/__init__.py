from ... pyaz_utils import _call_az

def create(account_endpoint=None, account_key=None, account_name=None, do_not_run_after=None, do_not_run_until=None, id=None, job_manager_task_command_line=None, job_manager_task_id=None, job_manager_task_resource_files=None, job_max_task_retry_count=None, job_max_wall_clock_time=None, json_file=None, max_parallel_tasks=None, metadata=None, on_all_tasks_complete=None, pool_id=None, priority=None, recurrence_interval=None, required_slots=None, start_window=None, uses_task_dependencies=None):
    '''
    Add a Batch job schedule to an account.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - do_not_run_after -- If you do not specify a doNotRunAfter time, and you are creating a recurring Job Schedule, the Job Schedule will remain active until you explicitly terminate it. Expected format is an ISO-8601 timestamp.
    - do_not_run_until -- If you do not specify a doNotRunUntil time, the schedule becomes ready to create Jobs immediately. Expected format is an ISO-8601 timestamp.
    - id -- Required. The ID can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. The ID is case-preserving and case-insensitive (that is, you may not have two IDs within an Account that differ only by case).
    - job_manager_task_command_line -- Required. The command line does not run under a shell, and therefore cannot take advantage of shell features such as environment variable expansion. If you want to take advantage of such features, you should invoke the shell in the command line, for example using "cmd /c MyCommand" in Windows or "/bin/sh -c MyCommand" in Linux. If the command line refers to file paths, it should use a relative path (relative to the Task working directory), or use the Batch provided environment variable (https://docs.microsoft.com/en-us/azure/batch/batch-compute-node-environment-variables).
    - job_manager_task_id -- Required. The ID can contain any combination of alphanumeric characters including hyphens and underscores and cannot contain more than 64 characters.
    - job_manager_task_resource_files -- Files listed under this element are located in the Task's working directory. There is a maximum size for the list of resource files.  When the max size is exceeded, the request will fail and the response error code will be RequestEntityTooLarge. If this occurs, the collection of ResourceFiles must be reduced in size. This can be achieved using .zip files, Application Packages, or Docker Containers. Space-separated resource references in filename=httpurl format.
    - job_max_task_retry_count -- The maximum number of times each Task may be retried. The Batch service retries a Task if its exit code is nonzero. Note that this value specifically controls the number of retries. The Batch service will try each Task once, and may then retry up to this limit. For example, if the maximum retry count is 3, Batch tries a Task up to 4 times (one initial try and 3 retries). If the maximum retry count is 0, the Batch service does not retry Tasks. If the maximum retry count is -1, the Batch service retries Tasks without limit. The default value is 0 (no retries).
    - job_max_wall_clock_time -- If the Job does not complete within the time limit, the Batch service terminates it and any Tasks that are still running. In this case, the termination reason will be MaxWallClockTimeExpiry. If this property is not specified, there is no time limit on how long the Job may run. Expected format is an ISO-8601 duration.
    - json_file -- A file containing the cloud job schedule specification in JSON (formatted to match the respective REST API body). If this parameter is specified, all 'Cloud Job Schedule Arguments' are ignored.
    - max_parallel_tasks -- The maximum number of tasks that can be executed in parallel for the job. The value of maxParallelTasks must be -1 or greater than 0 if specified. If not specified, the default value is -1, which means there's no limit to the number of tasks that can be run at once. You can update a job's maxParallelTasks after it has been created using the update job API. Default value: -1 .
    - metadata -- The Batch service does not assign any meaning to metadata; it is solely for the use of user code. Space-separated values in 'key=value' format.
    - on_all_tasks_complete -- The action the Batch service should take when all Tasks in a Job created under this schedule are in the completed state. Note that if a Job contains no Tasks, then all Tasks are considered complete. This option is therefore most commonly used with a Job Manager task; if you want to use automatic Job termination without a Job Manager, you should initially set onAllTasksComplete to noaction and update the Job properties to set onAllTasksComplete to terminatejob once you have finished adding Tasks. The default is noaction.
    - pool_id -- The id of an existing pool. All the tasks of the job will run on the specified pool.
    - priority -- The priority of Jobs created under this schedule. Priority values can range from -1000 to 1000, with -1000 being the lowest priority and 1000 being the highest priority. The default value is 0. This priority is used as the default for all Jobs under the Job Schedule. You can update a Job's priority after it has been created using by using the update Job API.
    - recurrence_interval -- Because a Job Schedule can have at most one active Job under it at any given time, if it is time to create a new Job under a Job Schedule, but the previous Job is still running, the Batch service will not create the new Job until the previous Job finishes. If the previous Job does not finish within the startWindow period of the new recurrenceInterval, then no new Job will be scheduled for that interval. For recurring Jobs, you should normally specify a jobManagerTask in the jobSpecification. If you do not use jobManagerTask, you will need an external process to monitor when Jobs are created, add Tasks to the Jobs and terminate the Jobs ready for the next recurrence. The default is that the schedule does not recur: one Job is created, within the startWindow after the doNotRunUntil time, and the schedule is complete as soon as that Job finishes. The minimum value is 1 minute. If you specify a lower value, the Batch service rejects the schedule with an error; if you are calling the REST API directly, the HTTP status code is 400 (Bad Request). Expected format is an ISO-8601 duration.
    - required_slots -- The number of scheduling slots that the Task requires to run. The default is 1. A Task can only be scheduled to run on a compute node if the node has enough free scheduling slots available. For multi-instance Tasks, this property is not supported and must not be specified.
    - start_window -- If a Job is not created within the startWindow interval, then the 'opportunity' is lost; no Job will be created until the next recurrence of the schedule. If the schedule is recurring, and the startWindow is longer than the recurrence interval, then this is equivalent to an infinite startWindow, because the Job that is 'due' in one recurrenceInterval is not carried forward into the next recurrence interval. The default is infinite. The minimum value is 1 minute. If you specify a lower value, the Batch service rejects the schedule with an error; if you are calling the REST API directly, the HTTP status code is 400 (Bad Request). Expected format is an ISO-8601 duration.
    - uses_task_dependencies -- Whether Tasks in the Job can define dependencies on each other. The default is false. True if flag present.
    '''
    return _call_az("az batch job-schedule create", locals())


def delete(job_schedule_id, account_endpoint=None, account_key=None, account_name=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None, yes=None):
    '''
    

    Required Parameters:
    - job_schedule_id -- The ID of the Job Schedule to delete.

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
    return _call_az("az batch job-schedule delete", locals())


def show(job_schedule_id, account_endpoint=None, account_key=None, account_name=None, expand=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None, select=None):
    '''
    

    Required Parameters:
    - job_schedule_id -- The ID of the Job Schedule to get.

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
    return _call_az("az batch job-schedule show", locals())


def set(job_schedule_id, account_endpoint=None, account_key=None, account_name=None, do_not_run_after=None, do_not_run_until=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None, job_manager_task_application_package_references=None, job_manager_task_command_line=None, job_manager_task_environment_settings=None, job_manager_task_id=None, job_manager_task_resource_files=None, job_metadata=None, json_file=None, max_parallel_tasks=None, metadata=None, on_all_tasks_complete=None, pool_id=None, priority=None, recurrence_interval=None, required_slots=None, start_window=None, uses_task_dependencies=None):
    '''
    Update the properties of a job schedule.

    Required Parameters:
    - job_schedule_id -- The ID of the Job Schedule to update.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - do_not_run_after -- If you do not specify a doNotRunAfter time, and you are creating a recurring Job Schedule, the Job Schedule will remain active until you explicitly terminate it. Expected format is an ISO-8601 timestamp.
    - do_not_run_until -- If you do not specify a doNotRunUntil time, the schedule becomes ready to create Jobs immediately. Expected format is an ISO-8601 timestamp.
    - if_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
    - if_modified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    - if_none_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
    - if_unmodified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    - job_manager_task_application_package_references -- Application Packages are downloaded and deployed to a shared directory, not the Task working directory. Therefore, if a referenced Application Package is already on the Compute Node, and is up to date, then it is not re-downloaded; the existing copy on the Compute Node is used. If a referenced Application Package cannot be installed, for example because the package has been deleted or because download failed, the Task fails. Space-separated application IDs with optional version in 'id[#version]' format.
    - job_manager_task_command_line -- Required. The command line does not run under a shell, and therefore cannot take advantage of shell features such as environment variable expansion. If you want to take advantage of such features, you should invoke the shell in the command line, for example using "cmd /c MyCommand" in Windows or "/bin/sh -c MyCommand" in Linux. If the command line refers to file paths, it should use a relative path (relative to the Task working directory), or use the Batch provided environment variable (https://docs.microsoft.com/en-us/azure/batch/batch-compute-node-environment-variables).
    - job_manager_task_environment_settings --  Space-separated values in 'key=value' format.
    - job_manager_task_id -- Required. The ID can contain any combination of alphanumeric characters including hyphens and underscores and cannot contain more than 64 characters.
    - job_manager_task_resource_files -- Files listed under this element are located in the Task's working directory. There is a maximum size for the list of resource files.  When the max size is exceeded, the request will fail and the response error code will be RequestEntityTooLarge. If this occurs, the collection of ResourceFiles must be reduced in size. This can be achieved using .zip files, Application Packages, or Docker Containers. Space-separated resource references in filename=httpurl format.
    - job_metadata -- The Batch service does not assign any meaning to metadata; it is solely for the use of user code. Space-separated values in 'key=value' format.
    - json_file -- A file containing the job schedule patch parameter specification in JSON (formatted to match the respective REST API body). If this parameter is specified, all 'Job Schedule Arguments' are ignored.
    - max_parallel_tasks -- The maximum number of tasks that can be executed in parallel for the job. The value of maxParallelTasks must be -1 or greater than 0 if specified. If not specified, the default value is -1, which means there's no limit to the number of tasks that can be run at once. You can update a job's maxParallelTasks after it has been created using the update job API. Default value: -1 .
    - metadata -- If you do not specify this element, existing metadata is left unchanged. Space-separated values in 'key=value' format.
    - on_all_tasks_complete -- The action the Batch service should take when all Tasks in a Job created under this schedule are in the completed state. Note that if a Job contains no Tasks, then all Tasks are considered complete. This option is therefore most commonly used with a Job Manager task; if you want to use automatic Job termination without a Job Manager, you should initially set onAllTasksComplete to noaction and update the Job properties to set onAllTasksComplete to terminatejob once you have finished adding Tasks. The default is noaction.
    - pool_id -- The id of an existing pool. All the tasks of the job will run on the specified pool.
    - priority -- The priority of Jobs created under this schedule. Priority values can range from -1000 to 1000, with -1000 being the lowest priority and 1000 being the highest priority. The default value is 0. This priority is used as the default for all Jobs under the Job Schedule. You can update a Job's priority after it has been created using by using the update Job API.
    - recurrence_interval -- Because a Job Schedule can have at most one active Job under it at any given time, if it is time to create a new Job under a Job Schedule, but the previous Job is still running, the Batch service will not create the new Job until the previous Job finishes. If the previous Job does not finish within the startWindow period of the new recurrenceInterval, then no new Job will be scheduled for that interval. For recurring Jobs, you should normally specify a jobManagerTask in the jobSpecification. If you do not use jobManagerTask, you will need an external process to monitor when Jobs are created, add Tasks to the Jobs and terminate the Jobs ready for the next recurrence. The default is that the schedule does not recur: one Job is created, within the startWindow after the doNotRunUntil time, and the schedule is complete as soon as that Job finishes. The minimum value is 1 minute. If you specify a lower value, the Batch service rejects the schedule with an error; if you are calling the REST API directly, the HTTP status code is 400 (Bad Request). Expected format is an ISO-8601 duration.
    - required_slots -- The number of scheduling slots that the Task requires to run. The default is 1. A Task can only be scheduled to run on a compute node if the node has enough free scheduling slots available. For multi-instance Tasks, this property is not supported and must not be specified.
    - start_window -- If a Job is not created within the startWindow interval, then the 'opportunity' is lost; no Job will be created until the next recurrence of the schedule. If the schedule is recurring, and the startWindow is longer than the recurrence interval, then this is equivalent to an infinite startWindow, because the Job that is 'due' in one recurrenceInterval is not carried forward into the next recurrence interval. The default is infinite. The minimum value is 1 minute. If you specify a lower value, the Batch service rejects the schedule with an error; if you are calling the REST API directly, the HTTP status code is 400 (Bad Request). Expected format is an ISO-8601 duration.
    - uses_task_dependencies -- Whether Tasks in the Job can define dependencies on each other. The default is false. Specify either 'true' or 'false' to update the property.
    '''
    return _call_az("az batch job-schedule set", locals())


def reset(job_schedule_id, account_endpoint=None, account_key=None, account_name=None, do_not_run_after=None, do_not_run_until=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None, job_manager_task_application_package_references=None, job_manager_task_command_line=None, job_manager_task_environment_settings=None, job_manager_task_id=None, job_manager_task_resource_files=None, job_metadata=None, json_file=None, max_parallel_tasks=None, metadata=None, on_all_tasks_complete=None, pool_id=None, priority=None, recurrence_interval=None, required_slots=None, start_window=None, uses_task_dependencies=None):
    '''
    Reset the properties of a job schedule.  An updated job specification only applies to new jobs.

    Required Parameters:
    - job_schedule_id -- The ID of the Job Schedule to update.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - do_not_run_after -- If you do not specify a doNotRunAfter time, and you are creating a recurring Job Schedule, the Job Schedule will remain active until you explicitly terminate it. Expected format is an ISO-8601 timestamp.
    - do_not_run_until -- If you do not specify a doNotRunUntil time, the schedule becomes ready to create Jobs immediately. Expected format is an ISO-8601 timestamp.
    - if_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
    - if_modified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    - if_none_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
    - if_unmodified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    - job_manager_task_application_package_references -- Application Packages are downloaded and deployed to a shared directory, not the Task working directory. Therefore, if a referenced Application Package is already on the Compute Node, and is up to date, then it is not re-downloaded; the existing copy on the Compute Node is used. If a referenced Application Package cannot be installed, for example because the package has been deleted or because download failed, the Task fails. Space-separated application IDs with optional version in 'id[#version]' format.
    - job_manager_task_command_line -- Required. The command line does not run under a shell, and therefore cannot take advantage of shell features such as environment variable expansion. If you want to take advantage of such features, you should invoke the shell in the command line, for example using "cmd /c MyCommand" in Windows or "/bin/sh -c MyCommand" in Linux. If the command line refers to file paths, it should use a relative path (relative to the Task working directory), or use the Batch provided environment variable (https://docs.microsoft.com/en-us/azure/batch/batch-compute-node-environment-variables).
    - job_manager_task_environment_settings --  Space-separated values in 'key=value' format.
    - job_manager_task_id -- Required. The ID can contain any combination of alphanumeric characters including hyphens and underscores and cannot contain more than 64 characters.
    - job_manager_task_resource_files -- Files listed under this element are located in the Task's working directory. There is a maximum size for the list of resource files.  When the max size is exceeded, the request will fail and the response error code will be RequestEntityTooLarge. If this occurs, the collection of ResourceFiles must be reduced in size. This can be achieved using .zip files, Application Packages, or Docker Containers. Space-separated resource references in filename=httpurl format.
    - job_metadata -- The Batch service does not assign any meaning to metadata; it is solely for the use of user code. Space-separated values in 'key=value' format.
    - json_file -- A file containing the job schedule update parameter specification in JSON (formatted to match the respective REST API body). If this parameter is specified, all 'Job Schedule Arguments' are ignored.
    - max_parallel_tasks -- The maximum number of tasks that can be executed in parallel for the job. The value of maxParallelTasks must be -1 or greater than 0 if specified. If not specified, the default value is -1, which means there's no limit to the number of tasks that can be run at once. You can update a job's maxParallelTasks after it has been created using the update job API. Default value: -1 .
    - metadata -- If you do not specify this element, it takes the default value of an empty list; in effect, any existing metadata is deleted. Space-separated values in 'key=value' format.
    - on_all_tasks_complete -- The action the Batch service should take when all Tasks in a Job created under this schedule are in the completed state. Note that if a Job contains no Tasks, then all Tasks are considered complete. This option is therefore most commonly used with a Job Manager task; if you want to use automatic Job termination without a Job Manager, you should initially set onAllTasksComplete to noaction and update the Job properties to set onAllTasksComplete to terminatejob once you have finished adding Tasks. The default is noaction.
    - pool_id -- The id of an existing pool. All the tasks of the job will run on the specified pool.
    - priority -- The priority of Jobs created under this schedule. Priority values can range from -1000 to 1000, with -1000 being the lowest priority and 1000 being the highest priority. The default value is 0. This priority is used as the default for all Jobs under the Job Schedule. You can update a Job's priority after it has been created using by using the update Job API.
    - recurrence_interval -- Because a Job Schedule can have at most one active Job under it at any given time, if it is time to create a new Job under a Job Schedule, but the previous Job is still running, the Batch service will not create the new Job until the previous Job finishes. If the previous Job does not finish within the startWindow period of the new recurrenceInterval, then no new Job will be scheduled for that interval. For recurring Jobs, you should normally specify a jobManagerTask in the jobSpecification. If you do not use jobManagerTask, you will need an external process to monitor when Jobs are created, add Tasks to the Jobs and terminate the Jobs ready for the next recurrence. The default is that the schedule does not recur: one Job is created, within the startWindow after the doNotRunUntil time, and the schedule is complete as soon as that Job finishes. The minimum value is 1 minute. If you specify a lower value, the Batch service rejects the schedule with an error; if you are calling the REST API directly, the HTTP status code is 400 (Bad Request). Expected format is an ISO-8601 duration.
    - required_slots -- The number of scheduling slots that the Task requires to run. The default is 1. A Task can only be scheduled to run on a compute node if the node has enough free scheduling slots available. For multi-instance Tasks, this property is not supported and must not be specified.
    - start_window -- If a Job is not created within the startWindow interval, then the 'opportunity' is lost; no Job will be created until the next recurrence of the schedule. If the schedule is recurring, and the startWindow is longer than the recurrence interval, then this is equivalent to an infinite startWindow, because the Job that is 'due' in one recurrenceInterval is not carried forward into the next recurrence interval. The default is infinite. The minimum value is 1 minute. If you specify a lower value, the Batch service rejects the schedule with an error; if you are calling the REST API directly, the HTTP status code is 400 (Bad Request). Expected format is an ISO-8601 duration.
    - uses_task_dependencies -- Whether Tasks in the Job can define dependencies on each other. The default is false. True if flag present.
    '''
    return _call_az("az batch job-schedule reset", locals())


def disable(job_schedule_id, account_endpoint=None, account_key=None, account_name=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None):
    '''
    

    Required Parameters:
    - job_schedule_id -- The ID of the Job Schedule to disable.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - if_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
    - if_modified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    - if_none_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
    - if_unmodified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    '''
    return _call_az("az batch job-schedule disable", locals())


def enable(job_schedule_id, account_endpoint=None, account_key=None, account_name=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None):
    '''
    

    Required Parameters:
    - job_schedule_id -- The ID of the Job Schedule to enable.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - if_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
    - if_modified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    - if_none_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
    - if_unmodified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    '''
    return _call_az("az batch job-schedule enable", locals())


def stop(job_schedule_id, account_endpoint=None, account_key=None, account_name=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None):
    '''
    

    Required Parameters:
    - job_schedule_id -- The ID of the Job Schedule to terminates.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - if_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
    - if_modified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    - if_none_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
    - if_unmodified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    '''
    return _call_az("az batch job-schedule stop", locals())


def list(account_endpoint=None, account_key=None, account_name=None, expand=None, filter=None, select=None):
    '''
    

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - expand -- An OData $expand clause.
    - filter -- An OData $filter clause. For more information on constructing this filter, see https://docs.microsoft.com/en-us/rest/api/batchservice/odata-filters-in-batch#list-job-schedules.
    - select -- An OData $select clause.
    '''
    return _call_az("az batch job-schedule list", locals())

