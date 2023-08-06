'''
Manage Synapse workspaces.
'''
from ... pyaz_utils import _call_az
from . import firewall_rule, key, managed_identity


def show(name, resource_group):
    '''
    Get a Synapse workspace.

    Required Parameters:
    - name -- The workspace name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az synapse workspace show", locals())


def list(resource_group=None):
    '''
    List all Synapse workspaces.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az synapse workspace list", locals())


def create(file_system, name, resource_group, sql_admin_login_password, sql_admin_login_user, storage_account, account_name=None, allowed_tenant_ids=None, collaboration_branch=None, enable_managed_vnet=None, host_name=None, key_identifier=None, key_name=None, location=None, no_wait=None, prevent_exfiltration=None, project_name=None, repository_name=None, repository_type=None, root_folder=None, tags=None, tenant_id=None):
    '''
    Create a Synapse workspace.

    Required Parameters:
    - file_system -- The file system of the data lake storage account.
    - name -- The workspace name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sql_admin_login_password -- The sql administrator login password.
    - sql_admin_login_user -- The sql administrator login user name.
    - storage_account -- The data lake storage account name or resource id.

    Optional Parameters:
    - account_name -- GitHub account name used for the repository or Azure devops organization name
    - allowed_tenant_ids -- The approved Azure AD tenants which outbound data traffic allowed to. The Azure AD tenant of the current user will be included by default. Use ('' in PowerShell) to disable all allowed tenant ids.
    - collaboration_branch -- The branch name where you will collaborate with others and from which you will publish.
    - enable_managed_vnet -- The flag indicates whether enable managed virtual network.
    - host_name -- If using github Enterprise Server, provide sever URL like https://github.mydomain.com.Do not use this option with GitHub Enterprise Cloud.
    - key_identifier -- The customer-managed key used to encrypt all data at rest in the workspace. Key identifier should be in the format of: https://{keyvaultname}.vault.azure.net/keys/{keyname}.
    - key_name -- The workspace customer-managed key display name. All existing keys can be found using "az synapse workspace key list" cmdlet.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - no_wait -- Do not wait for the long-running operation to finish.
    - prevent_exfiltration -- The flag indicates whether enable data exfiltration.
    - project_name -- The project name to which you are connecting.
    - repository_name -- The name of the repository to which you are connecting.
    - repository_type -- The repository configuration type.
    - root_folder -- The name of the folder to the location of your Azure synapse JSON resources are imported. Default is /
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - tenant_id -- The tenant id used to connect Azure devops
    '''
    return _call_az("az synapse workspace create", locals())


def update(name, resource_group, account_name=None, allowed_tenant_ids=None, collaboration_branch=None, host_name=None, key_name=None, no_wait=None, project_name=None, repository_name=None, repository_type=None, root_folder=None, sql_admin_login_password=None, tags=None, tenant_id=None):
    '''
    Update a Synapse workspace.

    Required Parameters:
    - name -- The workspace name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - account_name -- GitHub account name used for the repository or Azure devops organization name
    - allowed_tenant_ids -- The approved Azure AD tenants which outbound data traffic allowed to. The Azure AD tenant of the current user will be included by default. Use ('' in PowerShell) to disable all allowed tenant ids.
    - collaboration_branch -- The branch name where you will collaborate with others and from which you will publish.
    - host_name -- If using github Enterprise Server, provide sever URL like https://github.mydomain.com.Do not use this option with GitHub Enterprise Cloud.
    - key_name -- The workspace customer-managed key display name. All existing keys can be found using "az synapse workspace key list" cmdlet.
    - no_wait -- Do not wait for the long-running operation to finish.
    - project_name -- The project name to which you are connecting.
    - repository_name -- The name of the repository to which you are connecting.
    - repository_type -- The repository configuration type.
    - root_folder -- The name of the folder to the location of your Azure synapse JSON resources are imported. Default is /
    - sql_admin_login_password -- The sql administrator login password.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - tenant_id -- The tenant id used to connect Azure devops
    '''
    return _call_az("az synapse workspace update", locals())


def check_name(name):
    '''
    Check if a Synapse workspace name is available or not.

    Required Parameters:
    - name -- The name you wanted to check.
    '''
    return _call_az("az synapse workspace check-name", locals())


def delete(name, resource_group, no_wait=None, yes=None):
    '''
    Delete a Synapse workspace.

    Required Parameters:
    - name -- The workspace name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az synapse workspace delete", locals())


def activate(key_identifier, name, resource_group, workspace_name, no_wait=None):
    '''
    Activates a workspace and change it's state from pending to success state when the workspace is first being provisioned and double encryption is enabled.

    Required Parameters:
    - key_identifier -- The Key Vault Url of the workspace encryption key. should be in the format of: https://{keyvaultname}.vault.azure.net/keys/{keyname}.
    - name -- The workspace customer-managed key display name. All existing keys can be found using /"az synapse workspace key list/" cmdlet.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az synapse workspace activate", locals())


def wait(resource_group, workspace_name, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the workspace is met.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace.

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az synapse workspace wait", locals())

