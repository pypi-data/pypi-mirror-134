from .... pyaz_utils import _call_az

def create(message, name, policy_definition_reference_id=None, resource_group=None, scope=None):
    '''
    Add a non-compliance message to a policy assignment.

    Required Parameters:
    - message -- Message that will be shown when a resource is denied by policy or evaluation details are inspected.
    - name -- Name of the policy assignment.

    Optional Parameters:
    - policy_definition_reference_id -- Policy definition reference ID within the assigned initiative (policy set) that the message applies to.
    - resource_group -- the resource group where the policy will be applied
    - scope -- Scope to which this policy assignment applies.
    '''
    return _call_az("az policy assignment non-compliance-message create", locals())


def list(name, resource_group=None, scope=None):
    '''
    List the non-compliance messages for a policy assignment.

    Required Parameters:
    - name -- Name of the policy assignment.

    Optional Parameters:
    - resource_group -- the resource group where the policy will be applied
    - scope -- Scope to which this policy assignment applies.
    '''
    return _call_az("az policy assignment non-compliance-message list", locals())


def delete(message, name, policy_definition_reference_id=None, resource_group=None, scope=None):
    '''
    Remove one or more non-compliance messages from a policy assignment.

    Required Parameters:
    - message -- Message that will be shown when a resource is denied by policy or evaluation details are inspected.
    - name -- Name of the policy assignment.

    Optional Parameters:
    - policy_definition_reference_id -- Policy definition reference ID within the assigned initiative (policy set) that the message applies to.
    - resource_group -- the resource group where the policy will be applied
    - scope -- Scope to which this policy assignment applies.
    '''
    return _call_az("az policy assignment non-compliance-message delete", locals())

