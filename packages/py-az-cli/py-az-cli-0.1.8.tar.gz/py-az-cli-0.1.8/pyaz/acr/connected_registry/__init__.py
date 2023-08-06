from ... pyaz_utils import _call_az
from . import install, permissions


def create(name, registry, audit_logs_enabled=None, client_tokens=None, log_level=None, mode=None, parent=None, repository=None, resource_group=None, sync_message_ttl=None, sync_schedule=None, sync_token=None, sync_window=None):
    '''
    Create a connected registry for an Azure Container Registry.

    Required Parameters:
    - name -- Name for the connected registry. Name must be between 5 to 40 character long, start with a letter and contain only alphanumeric characters (including ‘_’ or ‘-’). Name must be unique under the Cloud ACR hierarchy.
    - registry -- The login server of the Cloud ACR registry. Must be the FQDN to support also Azure Stack.

    Optional Parameters:
    - audit_logs_enabled -- Indicate whether audit log synchronization is enabled. It is enabled by default.
    - client_tokens -- Specify the client access to the repositories in the connected registry. It can be in the format [TOKEN_NAME01] [TOKEN_NAME02]...
    - log_level -- Set the log level for logging on the instance. Accepted log levels are Debug, Information, Warning, Error, and None.
    - mode -- Determine the access it will have when synchronized.
    - parent -- The name of the parent connected registry.
    - repository -- Specify the repositories that need to be sync to the connected registry. It can be in the format [REPO01] [REPO02]...
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sync_message_ttl -- Determine how long the sync messages will be kept in the cloud. Uses ISO 8601 duration format.
    - sync_schedule -- Optional parameter to define the sync schedule. Uses cron expression to determine the schedule. If not specified, the instance is considered always online and attempts to sync every minute.
    - sync_token -- Specifies the sync token used to synchronize the connected registry with its parent. It most have only repo permissions and at least the actions required for its mode. It can include access for multiple repositories.
    - sync_window -- Required parameter if --sync-schedule is present. Used to determine the schedule duration. Uses ISO 8601 duration format.
    '''
    return _call_az("az acr connected-registry create", locals())


def delete(name, registry, cleanup=None, resource_group=None, yes=None):
    '''
    Delete a connected registry from Azure Container Registry.

    Required Parameters:
    - name -- Name for the connected registry. Name must be between 5 to 40 character long, start with a letter and contain only alphanumeric characters (including ‘_’ or ‘-’). Name must be unique under the Cloud ACR hierarchy.
    - registry -- The login server of the Cloud ACR registry. Must be the FQDN to support also Azure Stack.

    Optional Parameters:
    - cleanup -- It will aslo delete the sync token and the scope map resources.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az acr connected-registry delete", locals())


def show(name, registry, resource_group=None):
    '''
    Show connected registry details.

    Required Parameters:
    - name -- Name for the connected registry. Name must be between 5 to 40 character long, start with a letter and contain only alphanumeric characters (including ‘_’ or ‘-’). Name must be unique under the Cloud ACR hierarchy.
    - registry -- The login server of the Cloud ACR registry. Must be the FQDN to support also Azure Stack.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr connected-registry show", locals())


def deactivate(name, registry, resource_group=None, yes=None):
    '''
    Deactivate a connected registry from Azure Container Registry.

    Required Parameters:
    - name -- Name for the connected registry. Name must be between 5 to 40 character long, start with a letter and contain only alphanumeric characters (including ‘_’ or ‘-’). Name must be unique under the Cloud ACR hierarchy.
    - registry -- The login server of the Cloud ACR registry. Must be the FQDN to support also Azure Stack.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az acr connected-registry deactivate", locals())


def update(name, registry, add_client_tokens=None, audit_logs_enabled=None, log_level=None, remove_client_tokens=None, resource_group=None, sync_message_ttl=None, sync_schedule=None, sync_window=None):
    '''
    Update a connected registry for an Azure Container Registry.

    Required Parameters:
    - name -- Name for the connected registry. Name must be between 5 to 40 character long, start with a letter and contain only alphanumeric characters (including ‘_’ or ‘-’). Name must be unique under the Cloud ACR hierarchy.
    - registry -- The login server of the Cloud ACR registry. Must be the FQDN to support also Azure Stack.

    Optional Parameters:
    - add_client_tokens -- Client tokens to be added. Use the format "--add-client-tokens [TOKEN_NAME1 TOKEN_NAME2 ...]" per token id.
    - audit_logs_enabled -- Indicate whether audit log synchronization is enabled. It is enabled by default.
    - log_level -- Set the log level for logging on the instance. Accepted log levels are Debug, Information, Warning, Error, and None.
    - remove_client_tokens -- Client tokens to be removed. Use the format "--remove-client-tokens [TOKEN_NAME1 TOKEN_NAME2 ...]" per token id.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sync_message_ttl -- Determine how long the sync messages will be kept in the cloud. Uses ISO 8601 duration format.
    - sync_schedule -- Optional parameter to define the sync schedule. Uses cron expression to determine the schedule. If not specified, the instance is considered always online and attempts to sync every minute.
    - sync_window -- Used to determine the schedule duration. Uses ISO 8601 duration format.
    '''
    return _call_az("az acr connected-registry update", locals())


def get_settings(name, parent_protocol, registry, generate_password=None, resource_group=None, yes=None):
    '''
    Retrieve information required to activate a connected registry, and creates or rotates the sync token credentials.

    Required Parameters:
    - name -- Name for the connected registry. Name must be between 5 to 40 character long, start with a letter and contain only alphanumeric characters (including ‘_’ or ‘-’). Name must be unique under the Cloud ACR hierarchy.
    - parent_protocol -- Specify the protocol used to communicate with its parent.
    - registry -- The login server of the Cloud ACR registry. Must be the FQDN to support also Azure Stack.

    Optional Parameters:
    - generate_password -- Select which password you want to generate, and it is required to retrieve the password from the sync token.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az acr connected-registry get-settings", locals())


def list(registry, no_children=None, parent=None, resource_group=None):
    '''
    List all the connected registries under the current parent registry.

    Required Parameters:
    - registry -- The login server of the Cloud ACR registry. Must be the FQDN to support also Azure Stack.

    Optional Parameters:
    - no_children -- Used to remove all children from the list.
    - parent -- The name of the parent connected registry.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr connected-registry list", locals())


def list_client_tokens(name, registry, resource_group=None):
    '''
    List all the client tokens associated to a specific connected registries.

    Required Parameters:
    - name -- Name for the connected registry. Name must be between 5 to 40 character long, start with a letter and contain only alphanumeric characters (including ‘_’ or ‘-’). Name must be unique under the Cloud ACR hierarchy.
    - registry -- The login server of the Cloud ACR registry. Must be the FQDN to support also Azure Stack.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr connected-registry list-client-tokens", locals())


def repo(name, registry, add=None, remove=None, resource_group=None):
    '''
    Update all the necessary connected registry sync scope maps repository permissions.

    Required Parameters:
    - name -- Name for the connected registry. Name must be between 5 to 40 character long, start with a letter and contain only alphanumeric characters (including ‘_’ or ‘-’). Name must be unique under the Cloud ACR hierarchy.
    - registry -- The login server of the Cloud ACR registry. Must be the FQDN to support also Azure Stack.

    Optional Parameters:
    - add -- repository permissions to be added to the targeted connected registry and it's ancestors sync scope maps. Use the format "--add [REPO1 REPO2 ...]" per flag. Valid actions are {'metadata/read', 'metadata/write', 'content/write', 'content/delete', 'content/read'}
    - remove -- respsitory permissions to be removed from the targeted connected registry and it's succesors sync scope maps. Use the format "--remove [REPO1 REPO2 ...]" per flag. Valid actions are {'metadata/read', 'metadata/write', 'content/write', 'content/delete', 'content/read'}
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr connected-registry repo", locals())

