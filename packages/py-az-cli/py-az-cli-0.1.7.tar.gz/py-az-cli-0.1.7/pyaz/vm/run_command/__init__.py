from ... pyaz_utils import _call_az

def invoke(command_id, name, resource_group, parameters=None, scripts=None):
    '''
    Execute a specific run command on a vm.

    Required Parameters:
    - command_id -- The command id. Use 'az vm run-command list' to get the list
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - parameters -- space-separated parameters in the format of '[name=]value'
    - scripts -- Space-separated script lines. Use @{file} to load script from a file
    '''
    return _call_az("az vm run-command invoke", locals())


def list(expand=None, location=None, resource_group=None, vm_name=None):
    '''
    The operation to get all run commands of a Virtual Machine. And Lists all available run commands for a subscription in a location.

    Optional Parameters:
    - expand -- The expand expression to apply on the operation.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vm_name -- The name of the virtual machine
    '''
    return _call_az("az vm run-command list", locals())


def show(command_id=None, expand=None, instance_view=None, location=None, name=None, resource_group=None, vm_name=None):
    '''
    The operation to get the run command. And Gets specific run command for a subscription in a location.

    Optional Parameters:
    - command_id -- The command id.
    - expand -- The expand expression to apply on the operation.
    - instance_view -- Track the run command progress
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- The name of the virtual machine run command.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vm_name -- The name of the virtual machine
    '''
    return _call_az("az vm run-command show", locals())


def create(name, resource_group, vm_name, async_execution=None, command_id=None, error_blob_uri=None, location=None, no_wait=None, output_blob_uri=None, parameters=None, protected_parameters=None, run_as_password=None, run_as_user=None, script=None, script_uri=None, tags=None, timeout_in_seconds=None):
    '''
    The operation to create the run command.

    Required Parameters:
    - name -- The name of the virtual machine run command.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vm_name -- The name of the virtual machine

    Optional Parameters:
    - async_execution -- Optional. If set to true, provisioning will complete as soon as the script starts and will not wait for script to complete.
    - command_id -- Specify a command id of predefined script. All command ids can be listed using "list" command.
    - error_blob_uri -- Specify the Azure storage blob where script error stream will be uploaded.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - no_wait -- Do not wait for the long-running operation to finish.
    - output_blob_uri -- Specify the Azure storage blob where script output stream will be uploaded.
    - parameters -- Set custom parameters in a name-value pair.
    - protected_parameters -- Set custom parameters in a name-value pair. These parameters will be encrypted during transmission and will not be logged.
    - run_as_password -- Password if needed for using run-as-user parameter. It will be encrypted and not logged. 
    - run_as_user -- By default script process runs under system/root user. Specify custom user to host the process.
    - script -- Contain the powershell or bash script to execute on the VM.
    - script_uri -- Contain a uri to the script to execute on the VM. Uri can be any link accessible from the VM or a storage blob without SAS. If subscription has access to the storage blob, then SAS will be auto-generated. 
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - timeout_in_seconds -- The timeout in seconds to execute the run command.
    '''
    return _call_az("az vm run-command create", locals())


def update(name, resource_group, vm_name, async_execution=None, command_id=None, error_blob_uri=None, location=None, no_wait=None, output_blob_uri=None, parameters=None, protected_parameters=None, run_as_password=None, run_as_user=None, script=None, script_uri=None, tags=None, timeout_in_seconds=None):
    '''
    The operation to update the run command.

    Required Parameters:
    - name -- The name of the virtual machine run command.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vm_name -- The name of the virtual machine

    Optional Parameters:
    - async_execution -- Optional. If set to true, provisioning will complete as soon as the script starts and will not wait for script to complete.
    - command_id -- Specify a command id of predefined script. All command ids can be listed using "list" command.
    - error_blob_uri -- Specify the Azure storage blob where script error stream will be uploaded.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - no_wait -- Do not wait for the long-running operation to finish.
    - output_blob_uri -- Specify the Azure storage blob where script output stream will be uploaded.
    - parameters -- Set custom parameters in a name-value pair.
    - protected_parameters -- Set custom parameters in a name-value pair. These parameters will be encrypted during transmission and will not be logged.
    - run_as_password -- Password if needed for using run-as-user parameter. It will be encrypted and not logged. 
    - run_as_user -- By default script process runs under system/root user. Specify custom user to host the process.
    - script -- Contain the powershell or bash script to execute on the VM.
    - script_uri -- Contain a uri to the script to execute on the VM. Uri can be any link accessible from the VM or a storage blob without SAS. If subscription has access to the storage blob, then SAS will be auto-generated. 
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - timeout_in_seconds -- The timeout in seconds to execute the run command.
    '''
    return _call_az("az vm run-command update", locals())


def delete(name, resource_group, vm_name, no_wait=None, yes=None):
    '''
    The operation to delete the run command.

    Required Parameters:
    - name -- The name of the virtual machine run command.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vm_name -- The name of the virtual machine

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az vm run-command delete", locals())


def wait(command_id=None, created=None, custom=None, deleted=None, exists=None, expand=None, instance_view=None, interval=None, location=None, name=None, resource_group=None, timeout=None, updated=None, vm_name=None):
    '''
    Place the CLI in a waiting state until a condition of the res virtual-machine-run-command is met.

    Optional Parameters:
    - command_id -- The command id.
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - expand -- The expand expression to apply on the operation.
    - instance_view -- Track the run command progress
    - interval -- polling interval in seconds
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- The name of the virtual machine run command.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    - vm_name -- The name of the virtual machine
    '''
    return _call_az("az vm run-command wait", locals())

