'''
Manage permissions for a provider.
'''
from ... pyaz_utils import _call_az

def list(namespace):
    '''
    List permissions from a provider.

    Required Parameters:
    - namespace -- the resource namespace, aka 'provider'
    '''
    return _call_az("az provider permission list", locals())

