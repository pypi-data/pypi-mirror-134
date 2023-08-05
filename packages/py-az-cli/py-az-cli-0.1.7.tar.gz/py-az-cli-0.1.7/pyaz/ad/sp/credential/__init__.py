'''
Manage a service principal's credentials.
'''
from .... pyaz_utils import _call_az

def reset(name, append=None, cert=None, create_cert=None, credential_description=None, end_date=None, keyvault=None, password=None, years=None):
    '''
    Reset a service principal credential.

    Required Parameters:
    - name -- None

    Optional Parameters:
    - append -- Append the new credential instead of overwriting.
    - cert -- None
    - create_cert -- None
    - credential_description -- the description of the password
    - end_date -- Finer grain of expiry time if '--years' is insufficient, e.g. '2020-12-31T11:59:59+00:00' or '2299-12-31'
    - keyvault -- None
    - password -- If missing, CLI will generate a strong password
    - years -- None
    '''
    return _call_az("az ad sp credential reset", locals())


def list(id, cert=None):
    '''
    List a service principal's credentials.

    Required Parameters:
    - id -- service principal name, or object id

    Optional Parameters:
    - cert -- a certificate based credential
    '''
    return _call_az("az ad sp credential list", locals())


def delete(id, key_id, cert=None):
    '''
    Delete a service principal's credential.

    Required Parameters:
    - id -- service principal name, or object id
    - key_id -- credential key id

    Optional Parameters:
    - cert -- a certificate based credential
    '''
    return _call_az("az ad sp credential delete", locals())

