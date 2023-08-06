'''
Manage certificate issuer information.
'''
from .... pyaz_utils import _call_az
from . import admin


def update(issuer_name, vault_name, account_id=None, enabled=None, organization_id=None, password=None, provider_name=None):
    '''
    

    Required Parameters:
    - issuer_name -- Certificate issuer name.
    - vault_name -- Name of the Vault.

    Optional Parameters:
    - account_id -- The issuer account id/username/etc.
    - enabled -- Set issuer enabled state.
    - organization_id -- The organization id.
    - password -- The issuer account password/secret/etc.
    - provider_name -- The certificate provider name. Must be registered with your tenant ID and in your region.
    '''
    return _call_az("az keyvault certificate issuer update", locals())


def list(vault_name, maxresults=None):
    '''
    

    Required Parameters:
    - vault_name -- Name of the Vault.

    Optional Parameters:
    - maxresults -- Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    '''
    return _call_az("az keyvault certificate issuer list", locals())


def create(issuer_name, provider_name, vault_name, account_id=None, disabled=None, organization_id=None, password=None):
    '''
    

    Required Parameters:
    - issuer_name -- Certificate issuer name.
    - provider_name -- The certificate provider name. Must be registered with your tenant ID and in your region.
    - vault_name -- Name of the Vault.

    Optional Parameters:
    - account_id -- The issuer account id/username/etc.
    - disabled -- Set issuer to disabled state.
    - organization_id -- The organization id.
    - password -- The issuer account password/secret/etc.
    '''
    return _call_az("az keyvault certificate issuer create", locals())


def show(issuer_name, vault_name):
    '''
    

    Required Parameters:
    - issuer_name -- Certificate issuer name.
    - vault_name -- Name of the Vault.
    '''
    return _call_az("az keyvault certificate issuer show", locals())


def delete(issuer_name, vault_name):
    '''
    

    Required Parameters:
    - issuer_name -- Certificate issuer name.
    - vault_name -- Name of the Vault.
    '''
    return _call_az("az keyvault certificate issuer delete", locals())

