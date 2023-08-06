'''
Manage admin information for certificate issuers.
'''
from ..... pyaz_utils import _call_az

def list(issuer_name, vault_name):
    '''
    

    Required Parameters:
    - issuer_name -- Certificate issuer name.
    - vault_name -- Name of the Vault.
    '''
    return _call_az("az keyvault certificate issuer admin list", locals())


def add(email, issuer_name, vault_name, first_name=None, last_name=None, phone=None):
    '''
    

    Required Parameters:
    - email -- Admin e-mail address. Must be unique within the vault.
    - issuer_name -- Certificate issuer name.
    - vault_name -- Name of the Vault.

    Optional Parameters:
    - first_name -- Admin first name.
    - last_name -- Admin last name.
    - phone -- Admin phone number.
    '''
    return _call_az("az keyvault certificate issuer admin add", locals())


def delete(email, issuer_name, vault_name):
    '''
    

    Required Parameters:
    - email -- Admin e-mail address. Must be unique within the vault.
    - issuer_name -- Certificate issuer name.
    - vault_name -- Name of the Vault.
    '''
    return _call_az("az keyvault certificate issuer admin delete", locals())

