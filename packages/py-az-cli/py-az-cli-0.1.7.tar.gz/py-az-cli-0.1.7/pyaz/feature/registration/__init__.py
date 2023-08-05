'''
Manage resource provider feature registrations.
'''
from ... pyaz_utils import _call_az

def list(namespace=None):
    '''
    List feature registrations.

    Optional Parameters:
    - namespace -- the resource namespace, aka 'provider'
    '''
    return _call_az("az feature registration list", locals())


def show(name, provider_namespace):
    '''
    

    Required Parameters:
    - name -- the feature name
    - provider_namespace -- The provider namespace.
    '''
    return _call_az("az feature registration show", locals())


def create(name, namespace):
    '''
    Create a feature registration.

    Required Parameters:
    - name -- the feature name
    - namespace -- the resource namespace, aka 'provider'
    '''
    return _call_az("az feature registration create", locals())


def delete(name, namespace, yes=None):
    '''
    Delete a feature registration.

    Required Parameters:
    - name -- the feature name
    - namespace -- the resource namespace, aka 'provider'

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az feature registration delete", locals())

