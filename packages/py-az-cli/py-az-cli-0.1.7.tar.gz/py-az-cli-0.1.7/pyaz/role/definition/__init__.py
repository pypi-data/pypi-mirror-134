'''
Manage role definitions.
'''
from ... pyaz_utils import _call_az

def list(custom_role_only=None, name=None, resource_group=None, scope=None):
    '''
    List role definitions.

    Optional Parameters:
    - custom_role_only -- custom roles only(vs. build-in ones)
    - name -- the role's name
    - resource_group -- use it only if the role or assignment was added at the level of a resource group
    - scope -- scope at which the role assignment or definition applies to, e.g., /subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333, /subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup, or /subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM
    '''
    return _call_az("az role definition list", locals())


def delete(name, custom_role_only=None, resource_group=None, scope=None):
    '''
    Delete a role definition.

    Required Parameters:
    - name -- the role's name

    Optional Parameters:
    - custom_role_only -- custom roles only(vs. build-in ones)
    - resource_group -- use it only if the role or assignment was added at the level of a resource group
    - scope -- scope at which the role assignment or definition applies to, e.g., /subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333, /subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup, or /subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM
    '''
    return _call_az("az role definition delete", locals())


def create(role_definition):
    '''
    Create a custom role definition.

    Required Parameters:
    - role_definition -- json formatted content which defines the new role.
    '''
    return _call_az("az role definition create", locals())


def update(role_definition):
    '''
    Update a role definition.

    Required Parameters:
    - role_definition -- json formatted content which defines the new role.
    '''
    return _call_az("az role definition update", locals())

