'''
Manage Batch pools.
'''
from ... pyaz_utils import _call_az
from . import all_statistics, autoscale, node_counts, supported_images, usage_metrics


def create(account_endpoint=None, account_key=None, account_name=None, application_licenses=None, application_package_references=None, auto_scale_formula=None, certificate_references=None, disk_encryption_targets=None, enable_inter_node_communication=None, id=None, image=None, json_file=None, metadata=None, node_agent_sku_id=None, offer=None, os_family=None, os_version=None, policy=None, publisher=None, resize_timeout=None, sku=None, start_task_command_line=None, start_task_resource_files=None, start_task_wait_for_success=None, target_dedicated_nodes=None, target_low_priority_nodes=None, targets=None, task_slots_per_node=None, version=None, virtual_machine_image_id=None, vm_size=None):
    '''
    Create a Batch pool in an account. When creating a pool, choose arguments from either Cloud Services Configuration or Virtual Machine Configuration.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - application_licenses -- The list of application licenses must be a subset of available Batch service application licenses. If a license is requested which is not supported, Pool creation will fail. Space-separated values.
    - application_package_references -- Changes to Package references affect all new Nodes joining the Pool, but do not affect Compute Nodes that are already in the Pool until they are rebooted or reimaged. There is a maximum of 10 Package references on any given Pool. Space-separated application IDs with optional version in 'id[#version]' format.
    - auto_scale_formula -- A formula for the desired number of compute nodes in the pool. The formula is checked for validity before the pool is created. If the formula is not valid, the Batch service rejects the request with detailed error information. For more information about specifying this formula, see https://azure.microsoft.com/documentation/articles/batch-automatic-scaling/.
    - certificate_references -- For Windows Nodes, the Batch service installs the Certificates to the specified Certificate store and location. For Linux Compute Nodes, the Certificates are stored in a directory inside the Task working directory and an environment variable AZ_BATCH_CERTIFICATES_DIR is supplied to the Task to query for this location. For Certificates with visibility of 'remoteUser', a 'certs' directory is created in the user's home directory (e.g., /home/{user-name}/certs) and Certificates are placed in that directory. Space-separated certificate thumbprints.
    - disk_encryption_targets -- A space separated list of DiskEncryptionTargets. current possible values include OsDisk and TemporaryDisk.
    - enable_inter_node_communication -- Whether the Pool permits direct communication between Compute Nodes. Enabling inter-node communication limits the maximum size of the Pool due to deployment restrictions on the Compute Nodes of the Pool. This may result in the Pool not reaching its desired size. The default value is false. True if flag present.
    - id -- Required. The ID can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. The ID is case-preserving and case-insensitive (that is, you may not have two Pool IDs within an Account that differ only by case).
    - image -- OS image reference. This can be either 'publisher:offer:sku[:version]' format, or a fully qualified ARM image id of the form '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Compute/images/{imageName}'. If 'publisher:offer:sku[:version]' format, version is optional and if omitted latest will be used. Valid values can be retrieved via 'az batch pool supported-images list'. For example: 'MicrosoftWindowsServer:WindowsServer:2012-R2-Datacenter:latest'
    - json_file -- A file containing the pool specification in JSON (formatted to match the respective REST API body). If this parameter is specified, all 'Pool Arguments' are ignored.
    - metadata -- The Batch service does not assign any meaning to metadata; it is solely for the use of user code. Space-separated values in 'key=value' format.
    - node_agent_sku_id -- Required. The Batch Compute Node agent is a program that runs on each Compute Node in the Pool, and provides the command-and-control interface between the Compute Node and the Batch service. There are different implementations of the Compute Node agent, known as SKUs, for different operating systems. You must specify a Compute Node agent SKU which matches the selected Image reference. To get the list of supported Compute Node agent SKUs along with their list of verified Image references, see the 'List supported Compute Node agent SKUs' operation.
    - offer -- ==SUPPRESS==
    - os_family -- Required. Possible values are: 2 - OS Family 2, equivalent to Windows Server 2008 R2 SP1. 3 - OS Family 3, equivalent to Windows Server 2012. 4 - OS Family 4, equivalent to Windows Server 2012 R2. 5 - OS Family 5, equivalent to Windows Server 2016. 6 - OS Family 6, equivalent to Windows Server 2019. For more information, see Azure Guest OS Releases (https://azure.microsoft.com/documentation/articles/cloud-services-guestos-update-matrix/#releases).
    - os_version -- The default value is * which specifies the latest operating system version for the specified OS family.
    - policy -- Node placement Policy type on Batch Pools. Allocation policy used by Batch Service to provision the nodes. If not specified, Batch will use the regional policy.
    - publisher -- ==SUPPRESS==
    - resize_timeout -- This timeout applies only to manual scaling; it has no effect when enableAutoScale is set to true. The default value is 15 minutes. The minimum value is 5 minutes. If you specify a value less than 5 minutes, the Batch service returns an error; if you are calling the REST API directly, the HTTP status code is 400 (Bad Request). Expected format is an ISO-8601 duration.
    - sku -- ==SUPPRESS==
    - start_task_command_line -- Required. The command line does not run under a shell, and therefore cannot take advantage of shell features such as environment variable expansion. If you want to take advantage of such features, you should invoke the shell in the command line, for example using "cmd /c MyCommand" in Windows or "/bin/sh -c MyCommand" in Linux. If the command line refers to file paths, it should use a relative path (relative to the Task working directory), or use the Batch provided environment variable (https://docs.microsoft.com/en-us/azure/batch/batch-compute-node-environment-variables).
    - start_task_resource_files -- Files listed under this element are located in the Task's working directory. Space-separated resource references in filename=httpurl format.
    - start_task_wait_for_success -- Whether the Batch service should wait for the StartTask to complete successfully (that is, to exit with exit code 0) before scheduling any Tasks on the Compute Node. If true and the StartTask fails on a Node, the Batch service retries the StartTask up to its maximum retry count (maxTaskRetryCount). If the Task has still not completed successfully after all retries, then the Batch service marks the Node unusable, and will not schedule Tasks to it. This condition can be detected via the Compute Node state and failure info details. If false, the Batch service will not wait for the StartTask to complete. In this case, other Tasks can start executing on the Compute Node while the StartTask is still running; and even if the StartTask fails, new Tasks will continue to be scheduled on the Compute Node. The default is true. True if flag present.
    - target_dedicated_nodes -- The desired number of dedicated Compute Nodes in the Pool. This property must not be specified if enableAutoScale is set to true. If enableAutoScale is set to false, then you must set either targetDedicatedNodes, targetLowPriorityNodes, or both.
    - target_low_priority_nodes -- The desired number of low-priority Compute Nodes in the Pool. This property must not be specified if enableAutoScale is set to true. If enableAutoScale is set to false, then you must set either targetDedicatedNodes, targetLowPriorityNodes, or both.
    - targets -- If omitted, no disks on the compute nodes in the pool will be encrypted. On Linux pool, only "TemporaryDisk" is supported; on Windows pool, "OsDisk" and "TemporaryDisk" must be specified. Space seperated target disks to be encrypted. Values can either be OsDisk or TemporaryDisk
    - task_slots_per_node -- The number of task slots that can be used to run concurrent tasks on a single compute node in the pool. The default value is 1. The maximum value is the smaller of 4 times the number of cores of the vmSize of the pool or 256.
    - version -- ==SUPPRESS==
    - virtual_machine_image_id -- ==SUPPRESS==
    - vm_size -- Required. For information about available sizes of virtual machines for Cloud Services Pools (pools created with cloudServiceConfiguration), see Sizes for Cloud Services (https://azure.microsoft.com/documentation/articles/cloud-services-sizes-specs/). Batch supports all Cloud Services VM sizes except ExtraSmall, A1V2 and A2V2. For information about available VM sizes for Pools using Images from the Virtual Machines Marketplace (pools created with virtualMachineConfiguration) see Sizes for Virtual Machines (Linux) (https://azure.microsoft.com/documentation/articles/virtual-machines-linux-sizes/) or Sizes for Virtual Machines (Windows) (https://azure.microsoft.com/documentation/articles/virtual-machines-windows-sizes/). Batch supports all Azure VM sizes except STANDARD_A0 and those with premium storage (STANDARD_GS, STANDARD_DS, and STANDARD_DSV2 series).
    '''
    return _call_az("az batch pool create", locals())


def list(account_endpoint=None, account_key=None, account_name=None, expand=None, filter=None, select=None):
    '''
    

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - expand -- An OData $expand clause.
    - filter -- An OData $filter clause. For more information on constructing this filter, see https://docs.microsoft.com/en-us/rest/api/batchservice/odata-filters-in-batch#list-pools.
    - select -- An OData $select clause.
    '''
    return _call_az("az batch pool list", locals())


def delete(pool_id, account_endpoint=None, account_key=None, account_name=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None, yes=None):
    '''
    

    Required Parameters:
    - pool_id -- The ID of the Pool to delete.

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
    return _call_az("az batch pool delete", locals())


def show(pool_id, account_endpoint=None, account_key=None, account_name=None, expand=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None, select=None):
    '''
    

    Required Parameters:
    - pool_id -- The ID of the Pool to get.

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
    return _call_az("az batch pool show", locals())


def set(pool_id, account_endpoint=None, account_key=None, account_name=None, application_package_references=None, certificate_references=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None, json_file=None, metadata=None, start_task_command_line=None, start_task_environment_settings=None, start_task_max_task_retry_count=None, start_task_resource_files=None, start_task_wait_for_success=None):
    '''
    Update the properties of a Batch pool. Updating a property in a subgroup will reset the unspecified properties of that group.

    Required Parameters:
    - pool_id -- The ID of the Pool to update.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - application_package_references -- Changes to Package references affect all new Nodes joining the Pool, but do not affect Compute Nodes that are already in the Pool until they are rebooted or reimaged. If this element is present, it replaces any existing Package references. If you specify an empty collection, then all Package references are removed from the Pool. If omitted, any existing Package references are left unchanged. Space-separated application IDs with optional version in 'id[#version]' format.
    - certificate_references -- If this element is present, it replaces any existing Certificate references configured on the Pool. If omitted, any existing Certificate references are left unchanged. For Windows Nodes, the Batch service installs the Certificates to the specified Certificate store and location. For Linux Compute Nodes, the Certificates are stored in a directory inside the Task working directory and an environment variable AZ_BATCH_CERTIFICATES_DIR is supplied to the Task to query for this location. For Certificates with visibility of 'remoteUser', a 'certs' directory is created in the user's home directory (e.g., /home/{user-name}/certs) and Certificates are placed in that directory. Space-separated certificate thumbprints.
    - if_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service exactly matches the value specified by the client.
    - if_modified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    - if_none_match -- An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource's current ETag on the service does not match the value specified by the client.
    - if_unmodified_since -- A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    - json_file -- A file containing the pool patch parameter specification in JSON (formatted to match the respective REST API body). If this parameter is specified, all 'Pool Arguments' are ignored.
    - metadata -- If this element is present, it replaces any existing metadata configured on the Pool. If you specify an empty collection, any metadata is removed from the Pool. If omitted, any existing metadata is left unchanged. Space-separated values in 'key=value' format.
    - start_task_command_line -- Required. The command line does not run under a shell, and therefore cannot take advantage of shell features such as environment variable expansion. If you want to take advantage of such features, you should invoke the shell in the command line, for example using "cmd /c MyCommand" in Windows or "/bin/sh -c MyCommand" in Linux. If the command line refers to file paths, it should use a relative path (relative to the Task working directory), or use the Batch provided environment variable (https://docs.microsoft.com/en-us/azure/batch/batch-compute-node-environment-variables).
    - start_task_environment_settings --  Space-separated values in 'key=value' format.
    - start_task_max_task_retry_count -- The maximum number of times the Task may be retried. The Batch service retries a Task if its exit code is nonzero. Note that this value specifically controls the number of retries. The Batch service will try the Task once, and may then retry up to this limit. For example, if the maximum retry count is 3, Batch tries the Task up to 4 times (one initial try and 3 retries). If the maximum retry count is 0, the Batch service does not retry the Task. If the maximum retry count is -1, the Batch service retries the Task without limit.
    - start_task_resource_files -- Files listed under this element are located in the Task's working directory. Space-separated resource references in filename=httpurl format.
    - start_task_wait_for_success -- Whether the Batch service should wait for the StartTask to complete successfully (that is, to exit with exit code 0) before scheduling any Tasks on the Compute Node. If true and the StartTask fails on a Node, the Batch service retries the StartTask up to its maximum retry count (maxTaskRetryCount). If the Task has still not completed successfully after all retries, then the Batch service marks the Node unusable, and will not schedule Tasks to it. This condition can be detected via the Compute Node state and failure info details. If false, the Batch service will not wait for the StartTask to complete. In this case, other Tasks can start executing on the Compute Node while the StartTask is still running; and even if the StartTask fails, new Tasks will continue to be scheduled on the Compute Node. The default is true. Specify either 'true' or 'false' to update the property.
    '''
    return _call_az("az batch pool set", locals())


def reset(pool_id, account_endpoint=None, account_key=None, account_name=None, application_package_references=None, certificate_references=None, json_file=None, metadata=None, start_task_command_line=None, start_task_environment_settings=None, start_task_max_task_retry_count=None, start_task_wait_for_success=None):
    '''
    Update the properties of a Batch pool. Unspecified properties which can be updated are reset to their defaults.

    Required Parameters:
    - pool_id -- The ID of the pool to update.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- The Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- The Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - application_package_references -- Required. The list replaces any existing Application Package references on the Pool. Changes to Application Package references affect all new Compute Nodes joining the Pool, but do not affect Compute Nodes that are already in the Pool until they are rebooted or reimaged. There is a maximum of 10 Application Package references on any given Pool. If omitted, or if you specify an empty collection, any existing Application Packages references are removed from the Pool. A maximum of 10 references may be specified on a given Pool.
    - certificate_references -- Required. This list replaces any existing Certificate references configured on the Pool. If you specify an empty collection, any existing Certificate references are removed from the Pool. For Windows Nodes, the Batch service installs the Certificates to the specified Certificate store and location. For Linux Compute Nodes, the Certificates are stored in a directory inside the Task working directory and an environment variable AZ_BATCH_CERTIFICATES_DIR is supplied to the Task to query for this location. For Certificates with visibility of 'remoteUser', a 'certs' directory is created in the user's home directory (e.g., /home/{user-name}/certs) and Certificates are placed in that directory.
    - json_file -- The file containing pool update properties parameter specification in JSON(formatted to match REST API request body). If this parameter is specified, all 'Pool Update Properties Parameter Arguments' are ignored.
    - metadata -- Required. This list replaces any existing metadata configured on the Pool. If omitted, or if you specify an empty collection, any existing metadata is removed from the Pool.
    - start_task_command_line -- The command line of the start task. The command line does not run under a shell, and therefore cannot take advantage of shell features such as environment variable expansion. If you want to take advantage of such features, you should invoke the shell in the command line, for example using "cmd /c MyCommand" in Windows or "/bin/sh -c MyCommand" in Linux.
    - start_task_environment_settings -- A list of environment variable settings for the start task. Space-separated values in 'key=value' format.
    - start_task_max_task_retry_count -- The maximum number of times the task may be retried.
    - start_task_wait_for_success -- Whether the Batch service should wait for the start task to complete successfully (that is, to exit with exit code 0) before scheduling any tasks on the compute node. True if flag present, otherwise defaults to False.
    '''
    return _call_az("az batch pool reset", locals())


def resize(pool_id, abort=None, account_endpoint=None, account_key=None, account_name=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None, node_deallocation_option=None, resize_timeout=None, target_dedicated_nodes=None, target_low_priority_nodes=None):
    '''
    Resize or stop resizing a Batch pool.

    Required Parameters:
    - pool_id -- The ID of the pool.

    Optional Parameters:
    - abort -- Stop the pool resize operation.
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- The Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- The Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - if_match -- The operation will be performed only if the resource's current ETag exactly matches the specified value.
    - if_modified_since -- The operation will be performed only if the resource has been modified since the specified timestamp.
    - if_none_match -- The operation will not be performed only if the resource's current ETag exactly matches the specified value.
    - if_unmodified_since -- The operation will not be performed only if the resource has been modified since the specified timestamp.
    - node_deallocation_option -- When nodes may be removed from the pool, if the pool size is decreasing.
    - resize_timeout -- The default value is 15 minutes. The minimum value is 5 minutes. If you specify a value less than 5 minutes, the Batch service returns an error; if you are calling the REST API directly, the HTTP status code is 400 (Bad Request).
    - target_dedicated_nodes -- The desired number of dedicated Compute Nodes in the Pool.
    - target_low_priority_nodes -- The desired number of low-priority Compute Nodes in the Pool.
    '''
    return _call_az("az batch pool resize", locals())

