from ..... pyaz_utils import _call_az
from . import match_condition


def create(action, name, policy_name, priority, resource_group, rule_type):
    '''
    Create an application gateway WAF policy custom rule.

    Required Parameters:
    - action -- Action to take.
    - name -- Name of the WAF policy rule.
    - policy_name -- The name of the application gateway WAF policy.
    - priority -- Rule priority. Lower values are evaluated prior to higher values.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_type -- Type of rule.
    '''
    return _call_az("az network application-gateway waf-policy custom-rule create", locals())


def delete(name, policy_name, resource_group):
    '''
    Delete an application gateway WAF policy custom rule.

    Required Parameters:
    - name -- Name of the WAF policy rule.
    - policy_name -- The name of the application gateway WAF policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway waf-policy custom-rule delete", locals())


def list(policy_name, resource_group):
    '''
    List application gateway WAF policy custom rules.

    Required Parameters:
    - policy_name -- The name of the application gateway WAF policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway waf-policy custom-rule list", locals())


def show(name, policy_name, resource_group):
    '''
    Get the details of an application gateway WAF policy custom rule.

    Required Parameters:
    - name -- Name of the WAF policy rule.
    - policy_name -- The name of the application gateway WAF policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway waf-policy custom-rule show", locals())


def update(name, policy_name, resource_group, action=None, add=None, force_string=None, priority=None, remove=None, rule_type=None, set=None):
    '''
    Update an application gateway WAF policy custom rule.

    Required Parameters:
    - name -- Name of the WAF policy rule.
    - policy_name -- The name of the application gateway WAF policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - action -- Action to take.
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - priority -- Rule priority. Lower values are evaluated prior to higher values.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - rule_type -- Type of rule.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az network application-gateway waf-policy custom-rule update", locals())

