'''
Manage role assignments.
'''
from .... pyaz_utils import _call_az

def delete(assignee=None, assignee_object_id=None, hsm_name=None, id=None, ids=None, name=None, role=None, scope=None):
    '''
    

    Optional Parameters:
    - assignee -- represent a user, group, or service principal. supported format: object id, user sign-in name, or service principal name
    - assignee_object_id -- Use this parameter instead of '--assignee' to bypass graph permission issues. This parameter only works with object ids for users, groups, service principals, and managed identities. For managed identities use the principal id. For service principals, use the object id and not the app id.
    - hsm_name -- Name of the HSM.
    - id -- Full URI of the HSM. If specified all other 'Id' arguments should be omitted.
    - ids -- space-separated role assignment ids
    - name -- Name of the role assignment.
    - role -- role name or id
    - scope -- scope at which the role assignment or definition applies to, e.g., "/" or "/keys" or "/keys/{keyname}"
    '''
    return _call_az("az keyvault role assignment delete", locals())


def list(assignee=None, assignee_object_id=None, hsm_name=None, id=None, role=None, scope=None):
    '''
    

    Optional Parameters:
    - assignee -- represent a user, group, or service principal. supported format: object id, user sign-in name, or service principal name
    - assignee_object_id -- Use this parameter instead of '--assignee' to bypass graph permission issues. This parameter only works with object ids for users, groups, service principals, and managed identities. For managed identities use the principal id. For service principals, use the object id and not the app id.
    - hsm_name -- Name of the HSM.
    - id -- Full URI of the HSM. If specified all other 'Id' arguments should be omitted.
    - role -- role name or id
    - scope -- scope at which the role assignment or definition applies to, e.g., "/" or "/keys" or "/keys/{keyname}"
    '''
    return _call_az("az keyvault role assignment list", locals())


def create(role, scope, assignee=None, assignee_object_id=None, assignee_principal_type=None, hsm_name=None, id=None, name=None):
    '''
    

    Required Parameters:
    - role -- role name or id
    - scope -- scope at which the role assignment or definition applies to, e.g., "/" or "/keys" or "/keys/{keyname}"

    Optional Parameters:
    - assignee -- represent a user, group, or service principal. supported format: object id, user sign-in name, or service principal name
    - assignee_object_id -- Use this parameter instead of '--assignee' to bypass graph permission issues. This parameter only works with object ids for users, groups, service principals, and managed identities. For managed identities use the principal id. For service principals, use the object id and not the app id.
    - assignee_principal_type -- The principal type of assignee.
    - hsm_name -- Name of the HSM.
    - id -- Full URI of the HSM. If specified all other 'Id' arguments should be omitted.
    - name -- Name of the role assignment.
    '''
    return _call_az("az keyvault role assignment create", locals())

