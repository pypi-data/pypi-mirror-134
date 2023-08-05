'''
Manage delivery rule conditions for an endpoint.
'''
from ..... pyaz_utils import _call_az

def show(name, profile_name, resource_group):
    '''
    show delivery rules asscociate with the endpoint.

    Required Parameters:
    - name -- Name of the CDN endpoint.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cdn endpoint rule condition show", locals())


def add(match_variable, name, operator, profile_name, resource_group, rule_name, match_values=None, negate_condition=None, selector=None, transform=None):
    '''
    Add a condition to a delivery rule.

    Required Parameters:
    - match_variable -- Name of the match condition.
    - name -- Name of the CDN endpoint.
    - operator -- Operator of the match condition.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_name -- Name of the rule.

    Optional Parameters:
    - match_values -- Match values of the match condition (comma separated).
    - negate_condition -- If true, negates the condition
    - selector -- Selector of the match condition.
    - transform -- Transform to apply before matching.
    '''
    return _call_az("az cdn endpoint rule condition add", locals())


def remove(index, name, profile_name, resource_group, rule_name):
    '''
    Remove a condition from a delivery rule.

    Required Parameters:
    - index -- The index of the condition/action
    - name -- Name of the CDN endpoint.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_name -- Name of the rule.
    '''
    return _call_az("az cdn endpoint rule condition remove", locals())

