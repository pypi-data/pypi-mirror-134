from ..... pyaz_utils import _call_az
from . import rule_group_override


def add(policy_name, resource_group, rule_set_type, rule_set_version):
    '''
    Add a managed rule set to a CDN WAF policy.

    Required Parameters:
    - policy_name -- Name of the CDN WAF policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_set_type -- The type of the managed rule set.
    - rule_set_version -- The version of the managed rule set.
    '''
    return _call_az("az cdn waf policy managed-rule-set add", locals())


def remove(policy_name, resource_group, rule_set_type, rule_set_version, yes=None):
    '''
    Remove a managed rule set from a CDN WAF policy.

    Required Parameters:
    - policy_name -- Name of the CDN WAF policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_set_type -- The type of the managed rule set.
    - rule_set_version -- The version of the managed rule set.

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az cdn waf policy managed-rule-set remove", locals())


def list(policy_name, resource_group):
    '''
    List managed rule sets added to a CDN WAF policy.

    Required Parameters:
    - policy_name -- Name of the CDN WAF policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cdn waf policy managed-rule-set list", locals())


def show(policy_name, resource_group, rule_set_type, rule_set_version):
    '''
    Show a managed rule of a CDN WAF policy.

    Required Parameters:
    - policy_name -- Name of the CDN WAF policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_set_type -- The type of the managed rule set.
    - rule_set_version -- The version of the managed rule set.
    '''
    return _call_az("az cdn waf policy managed-rule-set show", locals())


def list_available():
    '''
    List available CDN WAF managed rule sets.
    '''
    return _call_az("az cdn waf policy managed-rule-set list-available", locals())

