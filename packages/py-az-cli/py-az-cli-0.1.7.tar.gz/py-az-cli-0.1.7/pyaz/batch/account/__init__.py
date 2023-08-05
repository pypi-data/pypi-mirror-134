'''
Manage Azure Batch accounts.
'''
from ... pyaz_utils import _call_az
from . import autostorage_keys, keys


def list(resource_group=None):
    '''
    List the Batch accounts associated with a subscription or resource group.

    Optional Parameters:
    - resource_group -- Name of the resource group
    '''
    return _call_az("az batch account list", locals())


def show(name=None, resource_group=None):
    '''
    Get a specified Batch account or the currently set account.

    Optional Parameters:
    - name -- Name of the batch account to show. If not specified will display currently set account.
    - resource_group -- Name of the resource group. If not specified will display currently set account.
    '''
    return _call_az("az batch account show", locals())


def create(location, name, resource_group, encryption_key_identifier=None, encryption_key_source=None, identity_type=None, keyvault=None, no_wait=None, public_network_access=None, storage_account=None, tags=None):
    '''
    Create a Batch account with the specified parameters.

    Required Parameters:
    - location -- The region in which to create the account.
    - name -- Name of the Batch account.
    - resource_group -- Name of the resource group

    Optional Parameters:
    - encryption_key_identifier -- Part of the encryption configuration for the Batch account. Full path to the versioned secret. Example https://mykeyvault.vault.azure.net/keys/testkey/6e34a81fef704045975661e297a4c053.
    - encryption_key_source -- Part of the encryption configuration for the Batch account. Type of the key source. Can be either Microsoft.Batch or Microsoft.KeyVault
    - identity_type -- The type of identity used for the Batch account. Possible values include: 'SystemAssigned', 'None'.
    - keyvault -- The KeyVault name or resource ID to be used for an account with a pool allocation mode of 'User Subscription'.
    - no_wait -- Do not wait for the long-running operation to finish.
    - public_network_access -- The network access type for accessing Azure Batch account. Values can either be enabled or disabled.
    - storage_account -- The storage account name or resource ID to be used for auto storage.
    - tags -- Space-separated tags in 'key[=value]' format.
    '''
    return _call_az("az batch account create", locals())


def set(name, resource_group, encryption_key_identifier=None, encryption_key_source=None, identity_type=None, storage_account=None, tags=None):
    '''
    Update properties for a Batch account.

    Required Parameters:
    - name -- Name of the Batch account.
    - resource_group -- Name of the resource group

    Optional Parameters:
    - encryption_key_identifier -- Part of the encryption configuration for the Batch account. Full path to the versioned secret. Example https://mykeyvault.vault.azure.net/keys/testkey/6e34a81fef704045975661e297a4c053.
    - encryption_key_source -- Part of the encryption configuration for the Batch account. Type of the key source. Can be either Microsoft.Batch or Microsoft.KeyVault
    - identity_type -- The type of identity used for the Batch account. Possible values include: 'SystemAssigned', 'None'.
    - storage_account -- The storage account name or resource ID to be used for auto storage.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az batch account set", locals())


def delete(name, resource_group, no_wait=None, yes=None):
    '''
    

    Required Parameters:
    - name -- Name of the Batch account.
    - resource_group -- Name of the resource group

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az batch account delete", locals())


def login(name, resource_group, shared_key_auth=None, show=None):
    '''
    Log in to a Batch account through Azure Active Directory or Shared Key authentication.

    Required Parameters:
    - name -- Name of the Batch account.
    - resource_group -- Name of the resource group

    Optional Parameters:
    - shared_key_auth -- Using Shared Key authentication, if not specified, it will use Azure Active Directory authentication.
    - show -- Display the credential information for the Batch account.
    '''
    return _call_az("az batch account login", locals())


def outbound_endpoints(name, resource_group):
    '''
    List an account's outbound network dependencies.

    Required Parameters:
    - name -- Name of the Batch account.
    - resource_group -- Name of the resource group
    '''
    return _call_az("az batch account outbound-endpoints", locals())

