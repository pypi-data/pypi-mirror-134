'''
Manage Synapse's role definitions.
'''
from .... pyaz_utils import _call_az

def list(workspace_name, is_built_in=None):
    '''
    List role definitions.

    Required Parameters:
    - workspace_name -- The workspace name.

    Optional Parameters:
    - is_built_in -- Is a Synapse Built-In Role or not.
    '''
    return _call_az("az synapse role definition list", locals())


def show(role, workspace_name):
    '''
    Get role definition by role id/name.

    Required Parameters:
    - role -- The role name/id that is assigned to the principal.
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse role definition show", locals())

