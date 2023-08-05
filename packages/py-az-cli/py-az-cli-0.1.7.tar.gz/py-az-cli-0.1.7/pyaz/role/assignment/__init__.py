'''
Manage role assignments.
'''
from ... pyaz_utils import _call_az

def delete(assignee=None, ids=None, include_inherited=None, resource_group=None, role=None, scope=None, yes=None):
    '''
    Delete role assignments.

    Optional Parameters:
    - assignee -- represent a user, group, or service principal. supported format: object id, user sign-in name, or service principal name
    - ids -- space-separated role assignment ids
    - include_inherited -- include assignments applied on parent scopes
    - resource_group -- use it only if the role or assignment was added at the level of a resource group
    - role -- role name or id
    - scope -- scope at which the role assignment or definition applies to, e.g., /subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333, /subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup, or /subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM
    - yes -- Continue to delete all assignments under the subscription
    '''
    return _call_az("az role assignment delete", locals())


def list(all=None, assignee=None, include_classic_administrators=None, include_groups=None, include_inherited=None, resource_group=None, role=None, scope=None):
    '''
    List role assignments.

    Optional Parameters:
    - all -- show all assignments under the current subscription
    - assignee -- represent a user, group, or service principal. supported format: object id, user sign-in name, or service principal name
    - include_classic_administrators -- list default role assignments for subscription classic administrators, aka co-admins
    - include_groups -- include extra assignments to the groups of which the user is a member(transitively).
    - include_inherited -- include assignments applied on parent scopes
    - resource_group -- use it only if the role or assignment was added at the level of a resource group
    - role -- role name or id
    - scope -- scope at which the role assignment or definition applies to, e.g., /subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333, /subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup, or /subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM
    '''
    return _call_az("az role assignment list", locals())


def create(role, assignee=None, assignee_object_id=None, assignee_principal_type=None, condition=None, condition_version=None, description=None, resource_group=None, scope=None):
    '''
    Create a new role assignment for a user, group, or service principal.

    Required Parameters:
    - role -- role name or id

    Optional Parameters:
    - assignee -- represent a user, group, or service principal. supported format: object id, user sign-in name, or service principal name
    - assignee_object_id -- Use this parameter instead of '--assignee' to bypass Graph API invocation in case of insufficient privileges. This parameter only works with object ids for users, groups, service principals, and managed identities. For managed identities use the principal id. For service principals, use the object id and not the app id.
    - assignee_principal_type -- use with --assignee-object-id to avoid errors caused by propagation latency in AAD Graph
    - condition -- Condition under which the user can be granted permission.
    - condition_version -- Version of the condition syntax. If --condition is specified without --condition-version, default to 2.0.
    - description -- Description of role assignment.
    - resource_group -- use it only if the role or assignment was added at the level of a resource group
    - scope -- scope at which the role assignment or definition applies to, e.g., /subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333, /subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup, or /subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM
    '''
    return _call_az("az role assignment create", locals())


def update(role_assignment):
    '''
    Update an existing role assignment for a user, group, or service principal.

    Required Parameters:
    - role_assignment -- Description of an existing role assignment as JSON, or a path to a file containing a JSON description.
    '''
    return _call_az("az role assignment update", locals())


def list_changelogs(end_time=None, start_time=None):
    '''
    List changelogs for role assignments.

    Optional Parameters:
    - end_time -- The end time of the query in the format of %Y-%m-%dT%H:%M:%SZ, e.g. 2000-12-31T12:59:59Z. Defaults to the current time
    - start_time -- The start time of the query in the format of %Y-%m-%dT%H:%M:%SZ, e.g. 2000-12-31T12:59:59Z. Defaults to 1 Hour prior to the current time
    '''
    return _call_az("az role assignment list-changelogs", locals())

