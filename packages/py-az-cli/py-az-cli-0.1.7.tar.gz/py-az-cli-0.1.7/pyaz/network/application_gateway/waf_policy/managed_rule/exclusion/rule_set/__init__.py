from ....... pyaz_utils import _call_az

def add(match_variable, policy_name, resource_group, selector, selector_match_operator, type, version, group_name=None, rule_ids=None):
    '''
    Add a managed rule set to an exclusion.

    Required Parameters:
    - match_variable -- The variable to be excluded.
    - policy_name -- The name of the web application firewall policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - selector -- When matchVariable is a collection, operator used to specify which elements in the collection this exclusion applies to.
    - selector_match_operator -- When matchVariable is a collection, operate on the selector to specify which elements in the collection this exclusion applies to.
    - type -- The type of the web application firewall rule set.
    - version -- The version of the web application firewall rule set type. 0.1 is used for Microsoft_BotManagerRuleSet

    Optional Parameters:
    - group_name -- The managed rule group for exclusion.
    - rule_ids -- List of rules that will be disabled. If provided, --group-name must be provided too.
    '''
    return _call_az("az network application-gateway waf-policy managed-rule exclusion rule-set add", locals())


def remove(match_variable, policy_name, resource_group, selector, selector_match_operator, type, version, group_name=None):
    '''
    Remove managed rule set within an exclusion.

    Required Parameters:
    - match_variable -- The variable to be excluded.
    - policy_name -- The name of the web application firewall policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - selector -- When matchVariable is a collection, operator used to specify which elements in the collection this exclusion applies to.
    - selector_match_operator -- When matchVariable is a collection, operate on the selector to specify which elements in the collection this exclusion applies to.
    - type -- The type of the web application firewall rule set.
    - version -- The version of the web application firewall rule set type. 0.1 is used for Microsoft_BotManagerRuleSet

    Optional Parameters:
    - group_name -- The managed rule group for exclusion.
    '''
    return _call_az("az network application-gateway waf-policy managed-rule exclusion rule-set remove", locals())


def list(policy_name, resource_group):
    '''
    List all managed rule sets of an exclusion.

    Required Parameters:
    - policy_name -- The name of the web application firewall policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway waf-policy managed-rule exclusion rule-set list", locals())

