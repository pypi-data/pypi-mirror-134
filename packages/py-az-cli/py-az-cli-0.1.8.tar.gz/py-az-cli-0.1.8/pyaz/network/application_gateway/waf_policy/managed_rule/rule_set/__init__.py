from ...... pyaz_utils import _call_az

def add(policy_name, resource_group, type, version, group_name=None, rules=None):
    '''
    Add managed rule set to the WAF policy managed rules. For rule set and rules, please visit: https://docs.microsoft.com/azure/web-application-firewall/ag/application-gateway-crs-rulegroups-rules


    Required Parameters:
    - policy_name -- The name of the web application firewall policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - type -- The type of the web application firewall rule set.
    - version -- The version of the web application firewall rule set type. 0.1 is used for Microsoft_BotManagerRuleSet

    Optional Parameters:
    - group_name -- The name of the web application firewall rule set group.
    - rules -- List of rules that will be disabled. If provided, --group-name must be provided too
    '''
    return _call_az("az network application-gateway waf-policy managed-rule rule-set add", locals())


def update(policy_name, resource_group, type, version, add=None, force_string=None, group_name=None, remove=None, rules=None, set=None):
    '''
    Manage rules of a WAF policy. If --group-name and --rules are provided, override existing rules. If --group-name is provided, clear all rules under a certain rule group. If neither of them are provided, update rule set and clear all rules under itself. For rule set and rules, please visit: https://docs.microsoft.com/azure/web-application-firewall/ag/application-gateway-crs-rulegroups-rules


    Required Parameters:
    - policy_name -- The name of the web application firewall policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - type -- The type of the web application firewall rule set.
    - version -- The version of the web application firewall rule set type. 0.1 is used for Microsoft_BotManagerRuleSet

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - group_name -- The name of the web application firewall rule set group.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - rules -- List of rules that will be disabled. If provided, --group-name must be provided too
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az network application-gateway waf-policy managed-rule rule-set update", locals())


def remove(policy_name, resource_group, type, version, group_name=None):
    '''
    Remove a managed rule set by rule set group name if rule_group_name is specified. Otherwise, remove all rule set.


    Required Parameters:
    - policy_name -- The name of the web application firewall policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - type -- The type of the web application firewall rule set.
    - version -- The version of the web application firewall rule set type. 0.1 is used for Microsoft_BotManagerRuleSet

    Optional Parameters:
    - group_name -- The name of the web application firewall rule set group.
    '''
    return _call_az("az network application-gateway waf-policy managed-rule rule-set remove", locals())


def list(policy_name, resource_group):
    '''
    List all managed rule set.

    Required Parameters:
    - policy_name -- The name of the web application firewall policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway waf-policy managed-rule rule-set list", locals())

