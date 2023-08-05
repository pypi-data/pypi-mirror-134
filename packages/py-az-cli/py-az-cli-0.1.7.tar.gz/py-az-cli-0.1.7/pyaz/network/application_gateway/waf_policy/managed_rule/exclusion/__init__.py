from ...... pyaz_utils import _call_az
from . import rule_set


def add(match_variable, policy_name, resource_group, selector, selector_match_operator):
    '''
    Add an OWASP CRS exclusion rule to the WAF policy managed rules.

    Required Parameters:
    - match_variable -- The variable to be excluded.
    - policy_name -- The name of the web application firewall policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - selector -- When matchVariable is a collection, operator used to specify which elements in the collection this exclusion applies to.
    - selector_match_operator -- When matchVariable is a collection, operate on the selector to specify which elements in the collection this exclusion applies to.
    '''
    return _call_az("az network application-gateway waf-policy managed-rule exclusion add", locals())


def remove(policy_name, resource_group):
    '''
    Remove all OWASP CRS exclusion rules that are applied on a Waf policy managed rules.

    Required Parameters:
    - policy_name -- The name of the web application firewall policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway waf-policy managed-rule exclusion remove", locals())


def list(policy_name, resource_group):
    '''
    List all OWASP CRS exclusion rules that are applied on a Waf policy managed rules.

    Required Parameters:
    - policy_name -- The name of the web application firewall policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway waf-policy managed-rule exclusion list", locals())

