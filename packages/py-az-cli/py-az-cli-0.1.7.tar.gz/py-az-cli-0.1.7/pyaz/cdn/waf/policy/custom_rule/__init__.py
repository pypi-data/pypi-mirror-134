from ..... pyaz_utils import _call_az

def set(action, name, policy_name, priority, resource_group, disabled=None):
    '''
    Add a custom rule to a CDN WAF policy.

    Required Parameters:
    - action -- None
    - name -- The name of the custom rule.
    - policy_name -- Name of the CDN WAF policy.
    - priority -- None
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - disabled -- None
    '''
    return _call_az("az cdn waf policy custom-rule set", locals())


def delete(name, policy_name, resource_group, yes=None):
    '''
    Remove a custom rule from a CDN WAF policy.

    Required Parameters:
    - name -- The name of the custom rule.
    - policy_name -- Name of the CDN WAF policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az cdn waf policy custom-rule delete", locals())


def list(policy_name, resource_group):
    '''
    List custom rules of a CDN WAF policy.

    Required Parameters:
    - policy_name -- Name of the CDN WAF policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cdn waf policy custom-rule list", locals())


def show(name, policy_name, resource_group):
    '''
    Show a custom rule of a CDN WAF policy.

    Required Parameters:
    - name -- The name of the custom rule.
    - policy_name -- Name of the CDN WAF policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cdn waf policy custom-rule show", locals())

