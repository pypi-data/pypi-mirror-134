'''
Manage extensions on a VM scale set.
'''
from ... pyaz_utils import _call_az
from . import image


def delete(name, resource_group, vmss_name, no_wait=None):
    '''
    Delete an extension from a VMSS.

    Required Parameters:
    - name -- Name of the extension.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vmss_name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az vmss extension delete", locals())


def show(name, resource_group, vmss_name):
    '''
    Show details on a VMSS extension.

    Required Parameters:
    - name -- Name of the extension.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vmss_name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    '''
    return _call_az("az vmss extension show", locals())


def set(name, publisher, resource_group, vmss_name, enable_auto_upgrade=None, extension_instance_name=None, force_update=None, no_auto_upgrade_minor_version=None, no_wait=None, protected_settings=None, provision_after_extensions=None, settings=None, version=None):
    '''
    Add an extension to a VMSS or update an existing extension.

    Required Parameters:
    - name -- Name of the extension.
    - publisher -- The name of the extension publisher.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vmss_name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`

    Optional Parameters:
    - enable_auto_upgrade -- Indicate the extension should be automatically upgraded by the platform if there is a newer version of the extension available.
    - extension_instance_name -- Name of extension instance, which can be customized. Default: name of the extension.
    - force_update -- force to update even if the extension configuration has not changed.
    - no_auto_upgrade_minor_version -- If set, the extension service will not automatically pick or upgrade to the latest minor version, even if the extension is redeployed.
    - no_wait -- Do not wait for the long-running operation to finish.
    - protected_settings -- Protected settings in JSON format for sensitive information like credentials. A JSON file path is also accepted.
    - provision_after_extensions -- Space-separated list of extension names after which this extension should be provisioned. These extensions must already be set on the vm.
    - settings -- Extension settings in JSON format. A JSON file path is also accepted.
    - version -- The version of the extension. To pin extension version to this value, please specify --no-auto-upgrade-minor-version.
    '''
    return _call_az("az vmss extension set", locals())


def list(resource_group, vmss_name):
    '''
    List extensions associated with a VMSS.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vmss_name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    '''
    return _call_az("az vmss extension list", locals())


def upgrade(name, resource_group, no_wait=None):
    '''
    Upgrade all extensions for all VMSS instances to the latest version.

    Required Parameters:
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az vmss extension upgrade", locals())

