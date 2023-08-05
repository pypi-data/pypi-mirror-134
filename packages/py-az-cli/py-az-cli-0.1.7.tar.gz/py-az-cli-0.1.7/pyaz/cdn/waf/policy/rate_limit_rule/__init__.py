from ..... pyaz_utils import _call_az

def set(action, duration, name, policy_name, priority, request_threshold, resource_group, disabled=None):
    '''
    Add a rate limit rule to a CDN WAF policy.

    Required Parameters:
    - action -- None
    - duration -- None
    - name -- The name of the rate limit rule.
    - policy_name -- Name of the CDN WAF policy.
    - priority -- None
    - request_threshold -- None
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - disabled -- None
    '''
    return _call_az("az cdn waf policy rate-limit-rule set", locals())


def delete(name, policy_name, resource_group, yes=None):
    '''
    Remove a rate limit rule from a CDN WAF policy.

    Required Parameters:
    - name -- The name of the rate limit rule.
    - policy_name -- Name of the CDN WAF policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az cdn waf policy rate-limit-rule delete", locals())


def list(policy_name, resource_group):
    '''
    List rate limit rules of a CDN WAF policy.

    Required Parameters:
    - policy_name -- Name of the CDN WAF policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cdn waf policy rate-limit-rule list", locals())


def show(name, policy_name, resource_group):
    '''
    Show a rate limit rule of a CDN WAF policy.

    Required Parameters:
    - name -- The name of the rate limit rule.
    - policy_name -- Name of the CDN WAF policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cdn waf policy rate-limit-rule show", locals())

