'''
Manage extensions on VMs.
'''
from ... pyaz_utils import _call_az
from . import image


def delete(name, resource_group, vm_name, no_wait=None):
    '''
    Remove an extension attached to a VM.

    Required Parameters:
    - name -- Name of the extension.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vm_name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az vm extension delete", locals())


def show(name, resource_group, vm_name, expand=None):
    '''
    Display information about extensions attached to a VM.

    Required Parameters:
    - name -- Name of the extension.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vm_name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`

    Optional Parameters:
    - expand -- The expand expression to apply on the operation.
    '''
    return _call_az("az vm extension show", locals())


def set(name, publisher, resource_group, vm_name, enable_auto_upgrade=None, extension_instance_name=None, force_update=None, no_auto_upgrade_minor_version=None, no_wait=None, protected_settings=None, settings=None, version=None):
    '''
    Set extensions for a VM.

    Required Parameters:
    - name -- Name of the extension.
    - publisher -- The name of the extension publisher.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vm_name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`

    Optional Parameters:
    - enable_auto_upgrade -- Indicate the extension should be automatically upgraded by the platform if there is a newer version of the extension available.
    - extension_instance_name -- Name of extension instance, which can be customized. Default: name of the extension.
    - force_update -- force to update even if the extension configuration has not changed.
    - no_auto_upgrade_minor_version -- If set, the extension service will not automatically pick or upgrade to the latest minor version, even if the extension is redeployed.
    - no_wait -- Do not wait for the long-running operation to finish.
    - protected_settings -- Protected settings in JSON format for sensitive information like credentials. A JSON file path is also accepted.
    - settings -- Extension settings in JSON format. A JSON file path is also accepted.
    - version -- The version of the extension. To pin extension version to this value, please specify --no-auto-upgrade-minor-version.
    '''
    return _call_az("az vm extension set", locals())


def list(resource_group, vm_name):
    '''
    List the extensions attached to a VM.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vm_name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    '''
    return _call_az("az vm extension list", locals())


def wait(name, resource_group, vm_name, created=None, custom=None, deleted=None, exists=None, expand=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of a virtual machine extension is met.

    Required Parameters:
    - name -- Name of the extension.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vm_name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - expand -- The expand expression to apply on the operation.
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az vm extension wait", locals())

