'''
Manage delivery rule conditions for a rule.
'''
from .... pyaz_utils import _call_az

def add(match_variable, operator, profile_name, resource_group, rule_name, rule_set_name, match_values=None, negate_condition=None, selector=None, transform=None):
    '''
    Add a condition to a delivery rule.

    Required Parameters:
    - match_variable -- Name of the match condition.
    - operator -- Operator of the match condition.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_name -- Name of the rule.
    - rule_set_name -- Name of the rule set.

    Optional Parameters:
    - match_values -- Match values of the match condition (comma separated).
    - negate_condition -- If true, negates the condition
    - selector -- Selector of the match condition.
    - transform -- Transform to apply before matching.
    '''
    return _call_az("az afd rule condition add", locals())


def remove(index, profile_name, resource_group, rule_name, rule_set_name):
    '''
    Remove a condition from a delivery rule.

    Required Parameters:
    - index -- The index of the condition/action
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_name -- Name of the rule.
    - rule_set_name -- Name of the rule set.
    '''
    return _call_az("az afd rule condition remove", locals())


def list(profile_name, resource_group, rule_name, rule_set_name):
    '''
    show condtions asscociated with the rule.

    Required Parameters:
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_name -- Name of the rule.
    - rule_set_name -- Name of the rule set.
    '''
    return _call_az("az afd rule condition list", locals())

