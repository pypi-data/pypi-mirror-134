'''
Manage storage accounts.
'''
from ... pyaz_utils import _call_az
from . import sas_definition


def add(active_key_name, name, resource_id, vault_name, auto_regenerate_key=None, disabled=None, regeneration_period=None, tags=None):
    '''
    

    Required Parameters:
    - active_key_name -- Current active storage account key name.
    - name -- Name to identify the storage account in the vault.
    - resource_id -- Storage account resource id.
    - vault_name -- Name of the Vault.

    Optional Parameters:
    - auto_regenerate_key -- whether keyvault should manage the storage account for the user.
    - disabled -- Add the storage account in a disabled state.
    - regeneration_period -- The key regeneration time duration specified in ISO-8601 format, such as "P30D" for rotation every 30 days.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az keyvault storage add", locals())


def list(vault_name, maxresults=None):
    '''
    

    Required Parameters:
    - vault_name -- Name of the Vault.

    Optional Parameters:
    - maxresults -- Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    '''
    return _call_az("az keyvault storage list", locals())


def show(id=None, name=None, vault_name=None):
    '''
    

    Optional Parameters:
    - id -- Id of the storage account.  If specified all other 'Id' arguments should be omitted.
    - name -- Name to identify the storage account in the vault. Required if --id is not specified.
    - vault_name -- Name of the Key Vault. Required if --id is not specified.
    '''
    return _call_az("az keyvault storage show", locals())


def update(active_key_name=None, auto_regenerate_key=None, disabled=None, id=None, name=None, regeneration_period=None, tags=None, vault_name=None):
    '''
    

    Optional Parameters:
    - active_key_name -- The current active storage account key name.
    - auto_regenerate_key -- whether keyvault should manage the storage account for the user.
    - disabled -- Add the storage account in a disabled state.
    - id -- Id of the storage account.  If specified all other 'Id' arguments should be omitted.
    - name -- Name to identify the storage account in the vault. Required if --id is not specified.
    - regeneration_period -- The key regeneration time duration specified in ISO-8601 format, such as "P30D" for rotation every 30 days.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - vault_name -- Name of the Key Vault. Required if --id is not specified.
    '''
    return _call_az("az keyvault storage update", locals())


def remove(id=None, name=None, vault_name=None):
    '''
    Remove a Key Vault managed Azure Storage Account and all associated SAS definitions. This operation requires the storage/delete permission.

    Optional Parameters:
    - id -- Id of the storage account.  If specified all other 'Id' arguments should be omitted.
    - name -- Name to identify the storage account in the vault. Required if --id is not specified.
    - vault_name -- Name of the Key Vault. Required if --id is not specified.
    '''
    return _call_az("az keyvault storage remove", locals())


def regenerate_key(key_name, id=None, name=None, vault_name=None):
    '''
    

    Required Parameters:
    - key_name -- The storage account key name.

    Optional Parameters:
    - id -- Id of the storage account.  If specified all other 'Id' arguments should be omitted.
    - name -- Name to identify the storage account in the vault. Required if --id is not specified.
    - vault_name -- Name of the Key Vault. Required if --id is not specified.
    '''
    return _call_az("az keyvault storage regenerate-key", locals())


def list_deleted(vault_name, maxresults=None):
    '''
    

    Required Parameters:
    - vault_name -- Name of the Vault.

    Optional Parameters:
    - maxresults -- Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    '''
    return _call_az("az keyvault storage list-deleted", locals())


def show_deleted(name, vault_name):
    '''
    

    Required Parameters:
    - name -- Name to identify the storage account in the vault.
    - vault_name -- Name of the Vault.
    '''
    return _call_az("az keyvault storage show-deleted", locals())


def purge(name, vault_name):
    '''
    

    Required Parameters:
    - name -- Name to identify the storage account in the vault.
    - vault_name -- Name of the Vault.
    '''
    return _call_az("az keyvault storage purge", locals())


def recover(name, vault_name):
    '''
    

    Required Parameters:
    - name -- Name to identify the storage account in the vault.
    - vault_name -- Name of the Vault.
    '''
    return _call_az("az keyvault storage recover", locals())


def backup(file, id=None, name=None, vault_name=None):
    '''
    

    Required Parameters:
    - file -- Local file path in which to store storage account backup.

    Optional Parameters:
    - id -- Id of the storage account.  If specified all other 'Id' arguments should be omitted.
    - name -- Name to identify the storage account in the vault. Required if --id is not specified.
    - vault_name -- Name of the Key Vault. Required if --id is not specified.
    '''
    return _call_az("az keyvault storage backup", locals())


def restore(file, vault_name):
    '''
    

    Required Parameters:
    - file -- Local key backup from which to restore storage account.
    - vault_name -- Name of the Vault.
    '''
    return _call_az("az keyvault storage restore", locals())

