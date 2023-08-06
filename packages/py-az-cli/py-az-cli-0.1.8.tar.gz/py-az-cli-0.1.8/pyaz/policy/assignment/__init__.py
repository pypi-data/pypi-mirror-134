'''
Manage resource policy assignments.
'''
from ... pyaz_utils import _call_az
from . import identity, non_compliance_message


def create(assign_identity=None, description=None, display_name=None, enforcement_mode=None, identity_scope=None, location=None, mi_system_assigned=None, mi_user_assigned=None, name=None, not_scopes=None, params=None, policy=None, policy_set_definition=None, resource_group=None, role=None, scope=None, sku=None):
    '''
    Create a resource policy assignment.

    Optional Parameters:
    - assign_identity -- Assigns a system assigned identity to the policy assignment. This argument will be deprecated, please use --mi-system-assigned instead
    - description -- Description of the policy assignment.
    - display_name -- Display name of the policy assignment.
    - enforcement_mode -- Enforcement mode of the policy assignment, e.g. Default, DoNotEnforce. Please visit https://aka.ms/azure-policyAssignment-enforcement-mode for more information.
    - identity_scope -- Scope that the system assigned identity can access
    - location -- The location of the policy assignment. Only required when utilizing managed identity.
    - mi_system_assigned -- Provide this flag to use system assigned identity for policy assignment. Check out help for more examples
    - mi_user_assigned -- UserAssigned Identity Id to be used for policy assignment. Check out help for more examples
    - name -- Name of the new policy assignment.
    - not_scopes -- Space-separated scopes where the policy assignment does not apply.
    - params -- JSON formatted string or a path to a file or uri with parameter values of the policy rule.
    - policy -- Name or id of the policy definition.
    - policy_set_definition -- Name or id of the policy set definition.
    - resource_group -- the resource group where the policy will be applied
    - role -- Role name or id that will be assigned to the managed identity
    - scope -- Scope to which this policy assignment applies.
    - sku -- policy sku.
    '''
    return _call_az("az policy assignment create", locals())


def delete(name, resource_group=None, scope=None):
    '''
    Delete a resource policy assignment.

    Required Parameters:
    - name -- Name of the policy assignment.

    Optional Parameters:
    - resource_group -- the resource group where the policy will be applied
    - scope -- Scope to which this policy assignment applies.
    '''
    return _call_az("az policy assignment delete", locals())


def list(disable_scope_strict_match=None, resource_group=None, scope=None):
    '''
    List resource policy assignments.

    Optional Parameters:
    - disable_scope_strict_match -- Include policy assignments either inherited from parent scope or at child scope.
    - resource_group -- the resource group where the policy will be applied
    - scope -- Scope to which this policy assignment applies.
    '''
    return _call_az("az policy assignment list", locals())


def show(name, resource_group=None, scope=None):
    '''
    Show a resource policy assignment.

    Required Parameters:
    - name -- Name of the policy assignment.

    Optional Parameters:
    - resource_group -- the resource group where the policy will be applied
    - scope -- Scope to which this policy assignment applies.
    '''
    return _call_az("az policy assignment show", locals())


def update(description=None, display_name=None, enforcement_mode=None, name=None, not_scopes=None, params=None, resource_group=None, scope=None, sku=None):
    '''
    Update a resource policy assignment.

    Optional Parameters:
    - description -- Description of the policy assignment.
    - display_name -- Display name of the policy assignment.
    - enforcement_mode -- Enforcement mode of the policy assignment, e.g. Default, DoNotEnforce. Please visit https://aka.ms/azure-policyAssignment-enforcement-mode for more information.
    - name -- Name of the policy assignment.
    - not_scopes -- Space-separated scopes where the policy assignment does not apply.
    - params -- JSON formatted string or a path to a file or uri with parameter values of the policy rule.
    - resource_group -- the resource group where the policy will be applied
    - scope -- Scope to which this policy assignment applies.
    - sku -- policy sku.
    '''
    return _call_az("az policy assignment update", locals())

