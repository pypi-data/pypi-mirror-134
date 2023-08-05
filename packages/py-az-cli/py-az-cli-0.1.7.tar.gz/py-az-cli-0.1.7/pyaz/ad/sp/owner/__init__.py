'''
Manage service principal owners.
'''
from .... pyaz_utils import _call_az

def list(id):
    '''
    List service principal owners.

    Required Parameters:
    - id -- service principal name, or object id or the service principal
    '''
    return _call_az("az ad sp owner list", locals())

