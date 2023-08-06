from .... pyaz_utils import _call_az

def create(account_name, name, sas_type, template_uri, validity_period, vault_name, disabled=None, tags=None):
    '''
    

    Required Parameters:
    - account_name -- Name to identify the storage account in the vault.
    - name -- Name to identify the SAS definition in the vault.
    - sas_type -- The type of SAS token the SAS definition will create. Possible values include: 'account', 'service'
    - template_uri -- The SAS definition token template signed with the key 00000000. In the case of an account token this is only the sas token itself, for service tokens, the full service endpoint url along with the sas token.  Tokens created according to the SAS definition will have the same properties as the template.
    - validity_period -- The validity period of SAS tokens created according to the SAS definition in ISO-8601, such as "PT12H" for 12 hour tokens.
    - vault_name -- Name of the Vault.

    Optional Parameters:
    - disabled -- Add the storage account in a disabled state.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az keyvault storage sas-definition create", locals())


def list(account_name, vault_name, maxresults=None):
    '''
    

    Required Parameters:
    - account_name -- Name to identify the storage account in the vault.
    - vault_name -- Name of the Vault.

    Optional Parameters:
    - maxresults -- Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    '''
    return _call_az("az keyvault storage sas-definition list", locals())


def show(account_name=None, id=None, name=None, vault_name=None):
    '''
    

    Optional Parameters:
    - account_name -- Name to identify the storage account in the vault. Required if --id is not specified.
    - id -- Id of the SAS definition. If specified all other 'Id' arguments should be omitted.
    - name -- Name to identify the SAS definition in the vault. Required if --id is not specified.
    - vault_name -- Name of the Key Vault. Required if --id is not specified.
    '''
    return _call_az("az keyvault storage sas-definition show", locals())


def update(account_name=None, disabled=None, id=None, name=None, sas_type=None, tags=None, template_uri=None, validity_period=None, vault_name=None):
    '''
    

    Optional Parameters:
    - account_name -- Name to identify the storage account in the vault. Required if --id is not specified.
    - disabled -- Add the storage account in a disabled state.
    - id -- Id of the SAS definition. If specified all other 'Id' arguments should be omitted.
    - name -- Name to identify the SAS definition in the vault. Required if --id is not specified.
    - sas_type -- The type of SAS token the SAS definition will create. Possible values include: 'account', 'service'
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - template_uri -- The SAS definition token template signed with the key 00000000. In the case of an account token this is only the sas token itself, for service tokens, the full service endpoint url along with the sas token.  Tokens created according to the SAS definition will have the same properties as the template.
    - validity_period -- The validity period of SAS tokens created according to the SAS definition in ISO-8601, such as "PT12H" for 12 hour tokens.
    - vault_name -- Name of the Key Vault. Required if --id is not specified.
    '''
    return _call_az("az keyvault storage sas-definition update", locals())


def delete(account_name=None, id=None, name=None, vault_name=None):
    '''
    

    Optional Parameters:
    - account_name -- Name to identify the storage account in the vault. Required if --id is not specified.
    - id -- Id of the SAS definition. If specified all other 'Id' arguments should be omitted.
    - name -- Name to identify the SAS definition in the vault. Required if --id is not specified.
    - vault_name -- Name of the Key Vault. Required if --id is not specified.
    '''
    return _call_az("az keyvault storage sas-definition delete", locals())


def list_deleted(account_name, vault_name, maxresults=None):
    '''
    

    Required Parameters:
    - account_name -- Name to identify the storage account in the vault.
    - vault_name -- Name of the Vault.

    Optional Parameters:
    - maxresults -- Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    '''
    return _call_az("az keyvault storage sas-definition list-deleted", locals())


def show_deleted(account_name, name, vault_name):
    '''
    

    Required Parameters:
    - account_name -- Name to identify the storage account in the vault.
    - name -- Name to identify the SAS definition in the vault.
    - vault_name -- Name of the Vault.
    '''
    return _call_az("az keyvault storage sas-definition show-deleted", locals())


def recover(account_name, name, vault_name):
    '''
    

    Required Parameters:
    - account_name -- Name to identify the storage account in the vault.
    - name -- Name to identify the SAS definition in the vault.
    - vault_name -- Name of the Vault.
    '''
    return _call_az("az keyvault storage sas-definition recover", locals())

