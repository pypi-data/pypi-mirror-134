'''
Manage resource policy exemptions.
'''
from ... pyaz_utils import _call_az

def create(name, description=None, display_name=None, exemption_category=None, expires_on=None, metadata=None, policy_assignment=None, policy_definition_reference_ids=None, resource_group=None, scope=None):
    '''
    Create a policy exemption.

    Required Parameters:
    - name -- Name of the new policy exemption.

    Optional Parameters:
    - description -- Description of policy exemption.
    - display_name -- Display name of the policy exemption.
    - exemption_category -- The policy exemption category of the policy exemption
    - expires_on -- The expiration date and time (in UTC ISO 8601 format yyyy-MM-ddTHH:mm:ssZ) of the policy exemption.
    - metadata -- Metadata in space-separated key=value pairs.
    - policy_assignment -- The referenced policy assignment Id for the policy exemption.
    - policy_definition_reference_ids -- The policy definition reference ids to exempt in the initiative (policy set).
    - resource_group -- the resource group where the policy will be applied
    - scope -- Scope to which this policy exemption applies.
    '''
    return _call_az("az policy exemption create", locals())


def delete(name, resource_group=None, scope=None):
    '''
    Delete a policy exemption.

    Required Parameters:
    - name -- Name of the policy exemption.

    Optional Parameters:
    - resource_group -- the resource group where the policy will be applied
    - scope -- Scope to which this policy exemption applies.
    '''
    return _call_az("az policy exemption delete", locals())


def list(disable_scope_strict_match=None, resource_group=None, scope=None):
    '''
    List policy exemptions.

    Optional Parameters:
    - disable_scope_strict_match -- Include policy exemptions either inherited from parent scope or at child scope.
    - resource_group -- the resource group where the policy will be applied
    - scope -- Scope to which this policy exemption applies.
    '''
    return _call_az("az policy exemption list", locals())


def show(name, resource_group=None, scope=None):
    '''
    Show a policy exemption.

    Required Parameters:
    - name -- Name of the policy exemption.

    Optional Parameters:
    - resource_group -- the resource group where the policy will be applied
    - scope -- Scope to which this policy exemption applies.
    '''
    return _call_az("az policy exemption show", locals())


def update(name, description=None, display_name=None, exemption_category=None, expires_on=None, metadata=None, policy_definition_reference_ids=None, resource_group=None, scope=None):
    '''
    Update a policy exemption.

    Required Parameters:
    - name -- Name of the policy exemption.

    Optional Parameters:
    - description -- Description of policy exemption.
    - display_name -- Display name of the policy exemption.
    - exemption_category -- The policy exemption category of the policy exemption
    - expires_on -- The expiration date and time (in UTC ISO 8601 format yyyy-MM-ddTHH:mm:ssZ) of the policy exemption.
    - metadata -- Metadata in space-separated key=value pairs.
    - policy_definition_reference_ids -- The policy definition reference ids to exempt in the initiative (policy set).
    - resource_group -- the resource group where the policy will be applied
    - scope -- Scope to which this policy exemption applies.
    '''
    return _call_az("az policy exemption update", locals())

