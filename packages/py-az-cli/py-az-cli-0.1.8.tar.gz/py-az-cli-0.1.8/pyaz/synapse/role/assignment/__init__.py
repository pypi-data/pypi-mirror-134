'''
Manage Synapse's role assignments.
'''
from .... pyaz_utils import _call_az

def create(role, workspace_name, assignee=None, assignee_object_id=None, assignee_principal_type=None, assignment_id=None, item=None, item_type=None, scope=None):
    '''
    Create a role assignment.

    Required Parameters:
    - role -- The role name/id that is assigned to the principal.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - assignee -- Represent a user or service principal. Supported format: object id, user sign-in name, or service principal name.
    - assignee_object_id -- Use this parameter instead of '--assignee' to bypass Graph API invocation in case of insufficient privileges. This parameter only works with object ids for users, groups, service principals, and managed identities. For managed identities use the principal id. For service principals, use the object id and not the app id.
    - assignee_principal_type -- use with --assignee-object-id to avoid errors caused by propagation latency in AAD Graph
    - assignment_id -- Custom role assignment id in guid format, if not specified, assignment id will be randomly generated.
    - item -- Item granted access in the workspace. Using with --item-type to combine the scope of assignment
    - item_type -- Item type granted access in the workspace. Using with --item to combine the scope of assignment.
    - scope -- A scope defines the resources or artifacts that the access applies to. Synapse supports hierarchical scopes. Permissions granted at a higher-level scope are inherited by objects at a lower level. In Synapse RBAC, the top-level scope is a workspace. Assigning a role with workspace scope grants permissions to all applicable objects in the workspace.
    '''
    return _call_az("az synapse role assignment create", locals())


def list(workspace_name, assignee=None, assignee_object_id=None, item=None, item_type=None, role=None, scope=None):
    '''
    List role assignments.

    Required Parameters:
    - workspace_name -- The workspace name.

    Optional Parameters:
    - assignee -- Represent a user or service principal. Supported format: object id, user sign-in name, or service principal name.
    - assignee_object_id -- Use this parameter instead of '--assignee' to bypass Graph API invocation in case of insufficient privileges. This parameter only works with object ids for users, groups, service principals, and managed identities. For managed identities use the principal id. For service principals, use the object id and not the app id.
    - item -- Item granted access in the workspace. Using with --item-type to combine the scope of assignment
    - item_type -- Item type granted access in the workspace. Using with --item to combine the scope of assignment.
    - role -- The role name/id that is assigned to the principal.
    - scope -- A scope defines the resources or artifacts that the access applies to. Synapse supports hierarchical scopes. Permissions granted at a higher-level scope are inherited by objects at a lower level. In Synapse RBAC, the top-level scope is a workspace. Assigning a role with workspace scope grants permissions to all applicable objects in the workspace.
    '''
    return _call_az("az synapse role assignment list", locals())


def show(id, workspace_name):
    '''
    Get a role assignment by id.

    Required Parameters:
    - id -- Id of the role that is assigned to the principal.
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse role assignment show", locals())


def delete(workspace_name, assignee=None, assignee_object_id=None, ids=None, item=None, item_type=None, role=None, scope=None, yes=None):
    '''
    Delete role assignments of workspace.

    Required Parameters:
    - workspace_name -- The workspace name.

    Optional Parameters:
    - assignee -- Represent a user or service principal. Supported format: object id, user sign-in name, or service principal name.
    - assignee_object_id -- Use this parameter instead of '--assignee' to bypass Graph API invocation in case of insufficient privileges. This parameter only works with object ids for users, groups, service principals, and managed identities. For managed identities use the principal id. For service principals, use the object id and not the app id.
    - ids -- space-separated role assignment ids. You should not provide --role or --assignee when --ids is provided.
    - item -- Item granted access in the workspace. Using with --item-type to combine the scope of assignment.Using az role assignment with filter condition before executing delete operation to be clearly aware of which assignments will be deleted.
    - item_type -- Item type granted access in the workspace. Using with --item to combine the scope of assignment.Using az role assignment with filter condition before executing delete operation to be clearly aware of which assignments will be deleted.
    - role -- The role name/id that is assigned to the principal.
    - scope -- A scope defines the resources or artifacts that the access applies to. Synapse supports hierarchical scopes. Permissions granted at a higher-level scope are inherited by objects at a lower level. In Synapse RBAC, the top-level scope is a workspace. Using az role assignment with filter condition before executing delete operation to be clearly aware of which assignments will be deleted.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az synapse role assignment delete", locals())

