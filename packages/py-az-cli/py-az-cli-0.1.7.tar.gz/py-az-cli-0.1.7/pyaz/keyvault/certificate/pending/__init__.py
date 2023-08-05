'''
Manage pending certificate creation operations.
'''
from .... pyaz_utils import _call_az

def merge(file, name, vault_name, certificate_attributes=None, disabled=None, expires=None, not_before=None, tags=None):
    '''
    

    Required Parameters:
    - file -- File containing the certificate or certificate chain to merge.
    - name -- Name of the pending certificate.
    - vault_name -- Name of the Vault.

    Optional Parameters:
    - certificate_attributes -- ==SUPPRESS==
    - disabled -- Create certificate in disabled state.
    - expires -- Expiration UTC datetime  (Y-m-d'T'H:M:S'Z').
    - not_before -- Key not usable before the provided UTC datetime  (Y-m-d'T'H:M:S'Z').
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az keyvault certificate pending merge", locals())


def show(name, vault_name):
    '''
    

    Required Parameters:
    - name -- Name of the pending certificate.
    - vault_name -- Name of the Vault.
    '''
    return _call_az("az keyvault certificate pending show", locals())


def delete(name, vault_name):
    '''
    

    Required Parameters:
    - name -- Name of the pending certificate.
    - vault_name -- Name of the Vault.
    '''
    return _call_az("az keyvault certificate pending delete", locals())

