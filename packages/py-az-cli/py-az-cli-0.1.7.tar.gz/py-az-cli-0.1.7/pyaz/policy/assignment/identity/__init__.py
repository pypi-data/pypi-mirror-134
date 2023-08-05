'''
Manage a policy assignment's managed identity.
'''
from .... pyaz_utils import _call_az

def assign(name, identity_scope=None, resource_group=None, role=None, scope=None, system_assigned=None, user_assigned=None):
    '''
    Add a system assigned identity or a user assigned identity to a policy assignment.

    Required Parameters:
    - name -- Name of the policy assignment.

    Optional Parameters:
    - identity_scope -- Scope that the system assigned identity can access
    - resource_group -- the resource group where the policy will be applied
    - role -- Role name or id that will be assigned to the managed identity
    - scope -- Scope to which this policy assignment applies.
    - system_assigned -- Provide this flag to use system assigned identity for policy assignment. Check out help for more examples
    - user_assigned -- UserAssigned Identity Id to be used for policy assignment. Check out help for more examples
    '''
    return _call_az("az policy assignment identity assign", locals())


def show(name, resource_group=None, scope=None):
    '''
    Show a policy assignment's managed identity.

    Required Parameters:
    - name -- Name of the policy assignment.

    Optional Parameters:
    - resource_group -- the resource group where the policy will be applied
    - scope -- Scope to which this policy assignment applies.
    '''
    return _call_az("az policy assignment identity show", locals())


def remove(name, resource_group=None, scope=None):
    '''
    Remove a managed identity from a policy assignment.

    Required Parameters:
    - name -- Name of the policy assignment.

    Optional Parameters:
    - resource_group -- the resource group where the policy will be applied
    - scope -- Scope to which this policy assignment applies.
    '''
    return _call_az("az policy assignment identity remove", locals())

