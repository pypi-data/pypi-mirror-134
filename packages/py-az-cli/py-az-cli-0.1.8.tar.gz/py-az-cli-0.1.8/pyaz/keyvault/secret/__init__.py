'''
Manage secrets.
'''
from ... pyaz_utils import _call_az

def list(id=None, include_managed=None, maxresults=None, vault_name=None):
    '''
    

    Optional Parameters:
    - id -- Full URI of the Vault or HSM. If specified all other 'Id' arguments should be omitted.
    - include_managed -- Include managed secrets. Default: false
    - maxresults -- Maximum number of results to return in a page. If not specified, the service will return up to 25 results.
    - vault_name -- Name of the Key Vault. Required if --id is not specified.
    '''
    return _call_az("az keyvault secret list", locals())


def list_versions(id=None, maxresults=None, name=None, vault_name=None):
    '''
    

    Optional Parameters:
    - id -- Id of the secret. If specified all other 'Id' arguments should be omitted.
    - maxresults -- Maximum number of results to return in a page. If not specified, the service will return up to 25 results.
    - name -- Name of the secret. Required if --id is not specified.
    - vault_name -- Name of the Key Vault. Required if --id is not specified.
    '''
    return _call_az("az keyvault secret list-versions", locals())


def list_deleted(vault_name, id=None, maxresults=None):
    '''
    

    Required Parameters:
    - vault_name -- Name of the Vault.

    Optional Parameters:
    - id -- Full URI of the Vault. If specified all other 'Id' arguments should be omitted.
    - maxresults -- Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    '''
    return _call_az("az keyvault secret list-deleted", locals())


def set(name, vault_name, description=None, disabled=None, encoding=None, expires=None, file=None, not_before=None, secret_attributes=None, tags=None, value=None):
    '''
    Create a secret (if one doesn't exist) or update a secret in a KeyVault.

    Required Parameters:
    - name -- Name of the secret.
    - vault_name -- Name of the Vault.

    Optional Parameters:
    - description -- Description of the secret contents (e.g. password, connection string, etc)
    - disabled -- Create secret in disabled state.
    - encoding -- Source file encoding. The value is saved as a tag (`file-encoding=<val>`) and used during download to automatically encode the resulting file.
    - expires -- Expiration UTC datetime  (Y-m-d'T'H:M:S'Z').
    - file -- Source file for secret. Use in conjunction with '--encoding'
    - not_before -- Key not usable before the provided UTC datetime  (Y-m-d'T'H:M:S'Z').
    - secret_attributes -- ==SUPPRESS==
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - value -- Plain text secret value. Cannot be used with '--file' or '--encoding'
    '''
    return _call_az("az keyvault secret set", locals())


def set_attributes(content_type=None, enabled=None, expires=None, id=None, name=None, not_before=None, secret_attributes=None, tags=None, vault_name=None, version=None):
    '''
    

    Optional Parameters:
    - content_type -- Type of the secret value such as a password.
    - enabled -- Enable the secret.
    - expires -- Expiration UTC datetime  (Y-m-d'T'H:M:S'Z').
    - id -- Id of the secret. If specified all other 'Id' arguments should be omitted.
    - name -- Name of the secret. Required if --id is not specified.
    - not_before -- Key not usable before the provided UTC datetime  (Y-m-d'T'H:M:S'Z').
    - secret_attributes -- ==SUPPRESS==
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - vault_name -- Name of the Key Vault. Required if --id is not specified.
    - version -- The secret version. If omitted, uses the latest version.
    '''
    return _call_az("az keyvault secret set-attributes", locals())


def show(id=None, name=None, vault_name=None, version=None):
    '''
    

    Optional Parameters:
    - id -- Id of the secret. If specified all other 'Id' arguments should be omitted.
    - name -- Name of the secret. Required if --id is not specified.
    - vault_name -- Name of the Key Vault. Required if --id is not specified.
    - version -- The secret version. If omitted, uses the latest version.
    '''
    return _call_az("az keyvault secret show", locals())


def show_deleted(id=None, name=None, vault_name=None):
    '''
    

    Optional Parameters:
    - id -- The recovery id of the secret. If specified all other 'Id' arguments should be omitted.
    - name -- Name of the secret. Required if --id is not specified.
    - vault_name -- Name of the Vault. Required if --id is not specified.
    '''
    return _call_az("az keyvault secret show-deleted", locals())


def delete(id=None, name=None, vault_name=None):
    '''
    

    Optional Parameters:
    - id -- Id of the secret. If specified all other 'Id' arguments should be omitted.
    - name -- Name of the secret. Required if --id is not specified.
    - vault_name -- Name of the Key Vault. Required if --id is not specified.
    '''
    return _call_az("az keyvault secret delete", locals())


def purge(id=None, name=None, vault_name=None):
    '''
    

    Optional Parameters:
    - id -- The recovery id of the secret. If specified all other 'Id' arguments should be omitted.
    - name -- Name of the secret. Required if --id is not specified.
    - vault_name -- Name of the Vault. Required if --id is not specified.
    '''
    return _call_az("az keyvault secret purge", locals())


def recover(id=None, name=None, vault_name=None):
    '''
    

    Optional Parameters:
    - id -- The recovery id of the secret. If specified all other 'Id' arguments should be omitted.
    - name -- Name of the secret. Required if --id is not specified.
    - vault_name -- Name of the Vault. Required if --id is not specified.
    '''
    return _call_az("az keyvault secret recover", locals())


def download(file, encoding=None, id=None, name=None, vault_name=None, version=None):
    '''
    

    Required Parameters:
    - file -- File to receive the secret contents.

    Optional Parameters:
    - encoding -- Encoding of the secret. By default, will look for the 'file-encoding' tag on the secret. Otherwise will assume 'utf-8'.
    - id -- Id of the secret. If specified all other 'Id' arguments should be omitted.
    - name -- Name of the secret. Required if --id is not specified.
    - vault_name -- Name of the Key Vault. Required if --id is not specified.
    - version -- The secret version. If omitted, uses the latest version.
    '''
    return _call_az("az keyvault secret download", locals())


def backup(file, id=None, name=None, vault_name=None):
    '''
    

    Required Parameters:
    - file -- File to receive the secret contents.

    Optional Parameters:
    - id -- Id of the secret. If specified all other 'Id' arguments should be omitted.
    - name -- Name of the secret. Required if --id is not specified.
    - vault_name -- Name of the Key Vault. Required if --id is not specified.
    '''
    return _call_az("az keyvault secret backup", locals())


def restore(file, vault_name):
    '''
    

    Required Parameters:
    - file -- File to receive the secret contents.
    - vault_name -- Name of the Vault.
    '''
    return _call_az("az keyvault secret restore", locals())

