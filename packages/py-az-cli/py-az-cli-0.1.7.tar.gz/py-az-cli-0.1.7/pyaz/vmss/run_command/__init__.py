from ... pyaz_utils import _call_az

def invoke(command_id, instance_id, name, resource_group, parameters=None, scripts=None):
    '''
    Execute a specific run command on a Virtual Machine Scale Set instance.

    Required Parameters:
    - command_id -- The command id. Use 'az vmss run-command list' to get the list
    - instance_id -- None
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - parameters -- space-separated parameters in the format of '[name=]value'
    - scripts -- Space-separated script lines. Use @{file} to load script from a file
    '''
    return _call_az("az vmss run-command invoke", locals())


def list(instance_id, resource_group, vmss_name, expand=None):
    '''
    The operation to get all run commands of an instance in Virtual Machine Scaleset.

    Required Parameters:
    - instance_id -- The instance ID of the virtual machine.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vmss_name -- The name of the VM scale set.

    Optional Parameters:
    - expand -- The expand expression to apply on the operation.
    '''
    return _call_az("az vmss run-command list", locals())


def show(instance_id, name, resource_group, vmss_name, expand=None, instance_view=None):
    '''
    The operation to get the VMSS run command.

    Required Parameters:
    - instance_id -- The instance ID of the virtual machine.
    - name -- The name of the virtual machine run command.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vmss_name -- The name of the VM scale set.

    Optional Parameters:
    - expand -- The expand expression to apply on the operation.
    - instance_view -- Track the run command progress
    '''
    return _call_az("az vmss run-command show", locals())


def create(instance_id, name, resource_group, vmss_name, async_execution=None, command_id=None, error_blob_uri=None, location=None, no_wait=None, output_blob_uri=None, parameters=None, protected_parameters=None, run_as_password=None, run_as_user=None, script=None, script_uri=None, tags=None, timeout_in_seconds=None):
    '''
    The operation to Create the VMSS VM run command.

    Required Parameters:
    - instance_id -- The instance ID of the virtual machine.
    - name -- The name of the virtual machine run command.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vmss_name -- The name of the VM scale set.

    Optional Parameters:
    - async_execution -- Optional. If set to true, provisioning will complete as soon as the script starts and will not wait for script to complete.
    - command_id -- Specify a command id of predefined script. All command ids can be listed using "list" command.
    - error_blob_uri -- Uri (without SAS) to an append blob where the script error stream will be uploaded.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - no_wait -- Do not wait for the long-running operation to finish.
    - output_blob_uri -- Uri (without SAS) to an append blob where the script output will be uploaded.
    - parameters -- Set custom parameters in a name-value pair.
    - protected_parameters -- Set custom parameters in a name-value pair. These parameters will be encrypted during transmission and will not be logged.
    - run_as_password -- Password if needed for using run-as-user parameter. It will be encrypted and not logged. 
    - run_as_user -- By default script process runs under system/root user. Specify custom user to host the process.
    - script -- Contain the powershell or bash script to execute on the VM.
    - script_uri -- Contain a uri to the script to execute on the VM. Uri can be any link accessible from the VM or a storage blob without SAS. If subscription has access to the storage blob, then SAS will be auto-generated. 
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - timeout_in_seconds -- The timeout in seconds to execute the run command.
    '''
    return _call_az("az vmss run-command create", locals())


def update(instance_id, name, resource_group, vmss_name, async_execution=None, command_id=None, error_blob_uri=None, location=None, no_wait=None, output_blob_uri=None, parameters=None, protected_parameters=None, run_as_password=None, run_as_user=None, script=None, script_uri=None, tags=None, timeout_in_seconds=None):
    '''
    The operation to update the VMSS run command.

    Required Parameters:
    - instance_id -- The instance ID of the virtual machine.
    - name -- The name of the virtual machine run command.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vmss_name -- The name of the VM scale set.

    Optional Parameters:
    - async_execution -- Optional. If set to true, provisioning will complete as soon as the script starts and will not wait for script to complete.
    - command_id -- Specify a command id of predefined script. All command ids can be listed using "list" command.
    - error_blob_uri -- Uri (without SAS) to an append blob where the script error stream will be uploaded.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - no_wait -- Do not wait for the long-running operation to finish.
    - output_blob_uri -- Uri (without SAS) to an append blob where the script output will be uploaded.
    - parameters -- Set custom parameters in a name-value pair.
    - protected_parameters -- Set custom parameters in a name-value pair. These parameters will be encrypted during transmission and will not be logged.
    - run_as_password -- Password if needed for using run-as-user parameter. It will be encrypted and not logged. 
    - run_as_user -- By default script process runs under system/root user. Specify custom user to host the process.
    - script -- Contain the powershell or bash script to execute on the VM.
    - script_uri -- Contain a uri to the script to execute on the VM. Uri can be any link accessible from the VM or a storage blob without SAS. If subscription has access to the storage blob, then SAS will be auto-generated. 
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - timeout_in_seconds -- The timeout in seconds to execute the run command.
    '''
    return _call_az("az vmss run-command update", locals())


def delete(instance_id, name, resource_group, vmss_name, no_wait=None, yes=None):
    '''
    The operation to delete the run command.

    Required Parameters:
    - instance_id -- The instance ID of the virtual machine.
    - name -- The name of the virtual machine run command.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vmss_name -- The name of the VM scale set.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az vmss run-command delete", locals())

