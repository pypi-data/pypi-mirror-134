'''
Manage App Configurations.
'''
from .. pyaz_utils import _call_az
from . import credential, feature, identity, kv, revision


def create(location, name, resource_group, assign_identity=None, disable_local_auth=None, enable_public_network=None, sku=None, tags=None):
    '''
    Create an App Configuration.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- Name of the App Configuration. You can configure the default name using `az configure --defaults app_configuration_store=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - assign_identity -- Space-separated list of managed identities to be assigned. Use "[system]" to refer to system-assigned managed identity or a resource ID to refer to user-assigned managed identity. If this argument is provided without any value, system-assigned managed identity will be assigned by default. If this argument is not provided, no managed identities will be assigned to this App Configuration store.
    - disable_local_auth -- Disable all authentication methods other than AAD authentication.
    - enable_public_network -- When true, requests coming from public networks have permission to access this store while private endpoint is enabled. When false, only requests made through Private Links can reach this store.
    - sku -- The sku of App Configuration
    - tags -- Space-separated tags: key[=value] [key[=value] ...].
    '''
    return _call_az("az appconfig create", locals())


def delete(name, resource_group=None, yes=None):
    '''
    Delete an App Configuration.

    Required Parameters:
    - name -- Name of the App Configuration. You can configure the default name using `az configure --defaults app_configuration_store=<name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az appconfig delete", locals())


def update(name, disable_local_auth=None, enable_public_network=None, encryption_key_name=None, encryption_key_vault=None, encryption_key_version=None, identity_client_id=None, resource_group=None, sku=None, tags=None):
    '''
    Update an App Configuration.

    Required Parameters:
    - name -- Name of the App Configuration. You can configure the default name using `az configure --defaults app_configuration_store=<name>`

    Optional Parameters:
    - disable_local_auth -- Disable all authentication methods other than AAD authentication.
    - enable_public_network -- When true, requests coming from public networks have permission to access this store while private endpoint is enabled. When false, only requests made through Private Links can reach this store.
    - encryption_key_name -- The name of the KeyVault key.
    - encryption_key_vault -- The URI of the KeyVault.
    - encryption_key_version -- The version of the KeyVault key. Use the latest version by default.
    - identity_client_id -- Client ID of the managed identity with wrap and unwrap access to encryption key. Use system-assigned managed identity by default.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sku -- The sku of App Configuration
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az appconfig update", locals())


def list(resource_group=None):
    '''
    Lists all App Configurations under the current subscription.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az appconfig list", locals())


def show(name, resource_group=None):
    '''
    Show properties of an App Configuration.

    Required Parameters:
    - name -- Name of the App Configuration. You can configure the default name using `az configure --defaults app_configuration_store=<name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az appconfig show", locals())

