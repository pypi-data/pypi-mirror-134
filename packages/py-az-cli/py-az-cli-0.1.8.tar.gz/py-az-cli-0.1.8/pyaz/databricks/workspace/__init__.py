'''
Commands to manage databricks workspace.
'''
from ... pyaz_utils import _call_az
from . import vnet_peering


def create(location, name, resource_group, sku, enable_no_public_ip=None, managed_resource_group=None, no_wait=None, prepare_encryption=None, private_subnet=None, public_subnet=None, require_infrastructure_encryption=None, tags=None, vnet=None):
    '''
    Create a new workspace.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- The name of the workspace.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sku -- The SKU tier name.

    Optional Parameters:
    - enable_no_public_ip -- Flag to enable the no public ip feature.
    - managed_resource_group -- The managed resource group to create. It can be either a name or a resource ID.
    - no_wait -- Do not wait for the long-running operation to finish.
    - prepare_encryption -- Flag to enable the Managed Identity for managed storage account to prepare for CMK encryption.
    - private_subnet -- The name of a Private Subnet within the Virtual Network.
    - public_subnet -- The name of a Public Subnet within the Virtual Network.
    - require_infrastructure_encryption -- Flag to enable the DBFS root file system with secondary layer of encryption with platform managed keys for data at rest.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - vnet -- Virtual Network name or resource ID.
    '''
    return _call_az("az databricks workspace create", locals())


def update(name, resource_group, key_name=None, key_source=None, key_vault=None, key_version=None, no_wait=None, prepare_encryption=None, tags=None):
    '''
    Update the workspace.

    Required Parameters:
    - name -- The name of the workspace.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - key_name -- The name of KeyVault key.
    - key_source -- The encryption key source (provider).
    - key_vault -- The Uri of KeyVault.
    - key_version -- The version of KeyVault key. It is optional when updating CMK.
    - no_wait -- Do not wait for the long-running operation to finish.
    - prepare_encryption -- Flag to enable the Managed Identity for managed storage account to prepare for CMK encryption.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az databricks workspace update", locals())


def delete(name, resource_group, no_wait=None, yes=None):
    '''
    Delete the workspace.

    Required Parameters:
    - name -- The name of the workspace.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az databricks workspace delete", locals())


def show(name, resource_group):
    '''
    Show the workspace.

    Required Parameters:
    - name -- The name of the workspace.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az databricks workspace show", locals())


def list(resource_group=None):
    '''
    Get all the workspaces.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az databricks workspace list", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the Databricks workspace is met.

    Required Parameters:
    - name -- The name of the workspace.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az databricks workspace wait", locals())

