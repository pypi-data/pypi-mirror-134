'''
Manage Synapse's role scopes.
'''
from .... pyaz_utils import _call_az

def list(workspace_name):
    '''
    List role scopes.

    Required Parameters:
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse role scope list", locals())

