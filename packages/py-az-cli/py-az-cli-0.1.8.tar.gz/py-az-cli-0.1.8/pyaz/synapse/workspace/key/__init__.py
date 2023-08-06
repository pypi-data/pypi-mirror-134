'''
Manage workspace's keys.
'''
from .... pyaz_utils import _call_az

def list(resource_group, workspace_name):
    '''
    List keys under specified workspace.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse workspace key list", locals())


def show(name, resource_group, workspace_name):
    '''
    Show a workspace's key by name.

    Required Parameters:
    - name -- The workspace customer-managed key display name. All existing keys can be found using /"az synapse workspace key list/" cmdlet.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse workspace key show", locals())


def create(key_identifier, name, resource_group, workspace_name, no_wait=None):
    '''
    Create a workspace's key.

    Required Parameters:
    - key_identifier -- The Key Vault Url of the workspace encryption key. should be in the format of: https://{keyvaultname}.vault.azure.net/keys/{keyname}.
    - name -- The workspace customer-managed key display name. All existing keys can be found using /"az synapse workspace key list/" cmdlet.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az synapse workspace key create", locals())


def delete(name, resource_group, workspace_name, no_wait=None, yes=None):
    '''
    Delete a workspace's key. The key at active status can't be deleted.

    Required Parameters:
    - name -- The workspace customer-managed key display name. All existing keys can be found using /"az synapse workspace key list/" cmdlet.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az synapse workspace key delete", locals())


def wait(key_name, resource_group, workspace_name, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of a workspace key is met.

    Required Parameters:
    - key_name -- The name of the workspace key.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az synapse workspace key wait", locals())

