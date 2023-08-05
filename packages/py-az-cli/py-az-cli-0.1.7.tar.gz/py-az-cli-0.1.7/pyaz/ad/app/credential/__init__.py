'''
manage an application's password or certificate credentials
'''
from .... pyaz_utils import _call_az

def reset(id, append=None, cert=None, create_cert=None, credential_description=None, end_date=None, keyvault=None, password=None, years=None):
    '''
    Append or overwrite an application's password or certificate credentials

    Required Parameters:
    - id -- identifier uri, application id, or object id

    Optional Parameters:
    - append -- Append the new credential instead of overwriting.
    - cert -- Certificate to use for credentials
    - create_cert -- Create a self-signed certificate to use for the credential
    - credential_description -- the description of the password
    - end_date -- Date or datetime after which credentials expire(e.g. '2017-12-31T11:59:59+00:00' or '2017-12-31'). Default value is one year after current time
    - keyvault -- Name or ID of a KeyVault to use for creating or retrieving certificates.
    - password -- app password, aka 'client secret'
    - years -- Number of years for which the credentials will be valid
    '''
    return _call_az("az ad app credential reset", locals())


def list(id, cert=None):
    '''
    List an application's password or certificate credential metadata. (The content of the password or certificate credential is not retrievable.)

    Required Parameters:
    - id -- identifier uri, application id, or object id

    Optional Parameters:
    - cert -- a certificate based credential
    '''
    return _call_az("az ad app credential list", locals())


def delete(id, key_id, cert=None):
    '''
    delete an application's password or certificate credentials

    Required Parameters:
    - id -- identifier uri, application id, or object id
    - key_id -- credential key id

    Optional Parameters:
    - cert -- a certificate based credential
    '''
    return _call_az("az ad app credential delete", locals())

