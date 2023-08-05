'''
Manage role definitions.
'''
from .... pyaz_utils import _call_az

def list(custom_role_only=None, hsm_name=None, scope=None):
    '''
    

    Optional Parameters:
    - custom_role_only -- Only show custom role definitions.
    - hsm_name -- Name of the HSM.
    - scope -- scope at which the role assignment or definition applies to, e.g., "/" or "/keys" or "/keys/{keyname}"
    '''
    return _call_az("az keyvault role definition list", locals())


def create(hsm_name, role_definition):
    '''
    Create a custom role definition.

    Required Parameters:
    - hsm_name -- Name of the HSM.
    - role_definition -- Description of a role as JSON, or a path to a file containing a JSON description.
    '''
    return _call_az("az keyvault role definition create", locals())


def update(hsm_name, role_definition):
    '''
    Update a role definition.

    Required Parameters:
    - hsm_name -- Name of the HSM.
    - role_definition -- Description of a role as JSON, or a path to a file containing a JSON description.
    '''
    return _call_az("az keyvault role definition update", locals())


def delete(hsm_name, name=None, role_id=None):
    '''
    Delete a role definition.

    Required Parameters:
    - hsm_name -- Name of the HSM.

    Optional Parameters:
    - name -- The role definition name. This is a GUID in the "name" property of a role definition.
    - role_id -- The role definition ID.
    '''
    return _call_az("az keyvault role definition delete", locals())


def show(hsm_name, name=None, role_id=None):
    '''
    Show the details of a role definition.

    Required Parameters:
    - hsm_name -- Name of the HSM.

    Optional Parameters:
    - name -- The role definition name. This is a GUID in the "name" property of a role definition.
    - role_id -- The role definition ID.
    '''
    return _call_az("az keyvault role definition show", locals())

