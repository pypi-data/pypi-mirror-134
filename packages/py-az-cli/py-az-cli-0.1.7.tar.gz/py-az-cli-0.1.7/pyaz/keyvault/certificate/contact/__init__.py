'''
Manage contacts for certificate management.
'''
from .... pyaz_utils import _call_az

def list(vault_name):
    '''
    

    Required Parameters:
    - vault_name -- Name of the Vault.
    '''
    return _call_az("az keyvault certificate contact list", locals())


def add(email, vault_name, name=None, phone=None):
    '''
    

    Required Parameters:
    - email -- Contact e-mail address. Must be unique.
    - vault_name -- Name of the Vault.

    Optional Parameters:
    - name -- Full contact name.
    - phone -- Contact phone number.
    '''
    return _call_az("az keyvault certificate contact add", locals())


def delete(email, vault_name):
    '''
    

    Required Parameters:
    - email -- Contact e-mail address. Must be unique.
    - vault_name -- Name of the Vault.
    '''
    return _call_az("az keyvault certificate contact delete", locals())

