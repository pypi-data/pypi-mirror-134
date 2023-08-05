'''
Manage certificates.
'''
from ... pyaz_utils import _call_az
from . import contact, issuer, pending


def create(name, policy, vault_name, disabled=None, tags=None, validity=None):
    '''
    Create a Key Vault certificate.

    Required Parameters:
    - name -- Name of the certificate.
    - policy -- JSON encoded policy definition. Use @{file} to load from a file(e.g. @my_policy.json).
    - vault_name -- Name of the Vault.

    Optional Parameters:
    - disabled -- Create certificate in disabled state.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - validity -- Number of months the certificate is valid for. Overrides the value specified with --policy/-p
    '''
    return _call_az("az keyvault certificate create", locals())


def list(id=None, include_pending=None, maxresults=None, vault_name=None):
    '''
    

    Optional Parameters:
    - id -- Full URI of the Vault or HSM. If specified all other 'Id' arguments should be omitted.
    - include_pending -- Specifies whether to include certificates which are not completely provisioned.
    - maxresults -- Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    - vault_name -- Name of the Key Vault. Required if --id is not specified.
    '''
    return _call_az("az keyvault certificate list", locals())


def list_versions(id=None, maxresults=None, name=None, vault_name=None):
    '''
    

    Optional Parameters:
    - id -- Id of the certificate. If specified all other 'Id' arguments should be omitted.
    - maxresults -- Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    - name -- Name of the certificate. Required if --id is not specified.
    - vault_name -- Name of the Key Vault. Required if --id is not specified.
    '''
    return _call_az("az keyvault certificate list-versions", locals())


def list_deleted(vault_name, id=None, include_pending=None, maxresults=None):
    '''
    

    Required Parameters:
    - vault_name -- Name of the Vault.

    Optional Parameters:
    - id -- Full URI of the Vault. If specified all other 'Id' arguments should be omitted.
    - include_pending -- Specifies whether to include certificates which are not completely provisioned.
    - maxresults -- Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    '''
    return _call_az("az keyvault certificate list-deleted", locals())


def show(id=None, name=None, vault_name=None, version=None):
    '''
    

    Optional Parameters:
    - id -- Id of the certificate. If specified all other 'Id' arguments should be omitted.
    - name -- Name of the certificate. Required if --id is not specified.
    - vault_name -- Name of the Key Vault. Required if --id is not specified.
    - version -- The certificate version. If omitted, uses the latest version.
    '''
    return _call_az("az keyvault certificate show", locals())


def show_deleted(id=None, name=None, vault_name=None):
    '''
    

    Optional Parameters:
    - id -- The recovery id of the certificate. If specified all other 'Id' arguments should be omitted.
    - name -- Name of the certificate. Required if --id is not specified.
    - vault_name -- Name of the Vault. Required if --id is not specified.
    '''
    return _call_az("az keyvault certificate show-deleted", locals())


def delete(id=None, name=None, vault_name=None):
    '''
    

    Optional Parameters:
    - id -- Id of the certificate. If specified all other 'Id' arguments should be omitted.
    - name -- Name of the certificate. Required if --id is not specified.
    - vault_name -- Name of the Key Vault. Required if --id is not specified.
    '''
    return _call_az("az keyvault certificate delete", locals())


def purge(id=None, name=None, vault_name=None):
    '''
    

    Optional Parameters:
    - id -- The recovery id of the certificate. If specified all other 'Id' arguments should be omitted.
    - name -- Name of the certificate. Required if --id is not specified.
    - vault_name -- Name of the Vault. Required if --id is not specified.
    '''
    return _call_az("az keyvault certificate purge", locals())


def recover(id=None, name=None, vault_name=None):
    '''
    

    Optional Parameters:
    - id -- The recovery id of the certificate. If specified all other 'Id' arguments should be omitted.
    - name -- Name of the certificate. Required if --id is not specified.
    - vault_name -- Name of the Vault. Required if --id is not specified.
    '''
    return _call_az("az keyvault certificate recover", locals())


def set_attributes(certificate_attributes=None, enabled=None, id=None, name=None, policy=None, tags=None, vault_name=None, version=None):
    '''
    

    Optional Parameters:
    - certificate_attributes -- ==SUPPRESS==
    - enabled -- Enable the certificate.
    - id -- Id of the certificate. If specified all other 'Id' arguments should be omitted.
    - name -- Name of the certificate. Required if --id is not specified.
    - policy -- JSON encoded policy definition. Use @{file} to load from a file(e.g. @my_policy.json).
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - vault_name -- Name of the Key Vault. Required if --id is not specified.
    - version -- The certificate version. If omitted, uses the latest version.
    '''
    return _call_az("az keyvault certificate set-attributes", locals())


def import_(file, name, vault_name, disabled=None, password=None, policy=None, tags=None):
    '''
    Import a certificate into KeyVault.

    Required Parameters:
    - file -- PKCS12 file or PEM file containing the certificate and private key.
    - name -- Name of the certificate.
    - vault_name -- Name of the Vault.

    Optional Parameters:
    - disabled -- Import the certificate in disabled state.
    - password -- If the private key in certificate is encrypted, the password used for encryption.
    - policy -- JSON encoded policy definition. Use @{file} to load from a file(e.g. @my_policy.json).
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az keyvault certificate import", locals())


def download(file, encoding=None, id=None, name=None, vault_name=None, version=None):
    '''
    Download the public portion of a Key Vault certificate.

    Required Parameters:
    - file -- File to receive the binary certificate contents.

    Optional Parameters:
    - encoding -- Encoding of the certificate. DER will create a binary DER formatted x509 certificate, and PEM will create a base64 PEM x509 certificate.
    - id -- Id of the certificate. If specified all other 'Id' arguments should be omitted.
    - name -- Name of the certificate. Required if --id is not specified.
    - vault_name -- Name of the Key Vault. Required if --id is not specified.
    - version -- The certificate version. If omitted, uses the latest version.
    '''
    return _call_az("az keyvault certificate download", locals())


def get_default_policy(scaffold=None):
    '''
    Get the default policy for self-signed certificates.

    Optional Parameters:
    - scaffold -- create a fully formed policy structure with default values
    '''
    return _call_az("az keyvault certificate get-default-policy", locals())


def backup(file, id=None, name=None, vault_name=None):
    '''
    

    Required Parameters:
    - file -- Local file path in which to store certificate backup.

    Optional Parameters:
    - id -- Id of the certificate. If specified all other 'Id' arguments should be omitted.
    - name -- Name of the certificate. Required if --id is not specified.
    - vault_name -- Name of the Key Vault. Required if --id is not specified.
    '''
    return _call_az("az keyvault certificate backup", locals())


def restore(file, vault_name):
    '''
    

    Required Parameters:
    - file -- Local certificate backup from which to restore certificate.
    - vault_name -- Name of the Vault.
    '''
    return _call_az("az keyvault certificate restore", locals())

