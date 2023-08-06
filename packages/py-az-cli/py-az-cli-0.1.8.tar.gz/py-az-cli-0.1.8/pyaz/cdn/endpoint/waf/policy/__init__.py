'''
Apply a CDN WAF policy to a CDN endpoint.
'''
from ..... pyaz_utils import _call_az

def show(endpoint_name, profile_name, resource_group):
    '''
    Show which CDN WAF policy is applied to a CDN endpoint.

    Required Parameters:
    - endpoint_name -- Name of the CDN endpoint.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cdn endpoint waf policy show", locals())


def set(endpoint_name, profile_name, resource_group, waf_policy_id=None, waf_policy_name=None, waf_policy_resource_group_name=None, waf_policy_subscription_id=None):
    '''
    Set the CDN WAF policy applied to a CDN endpoint

    Required Parameters:
    - endpoint_name -- Name of the CDN endpoint.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - waf_policy_id -- None
    - waf_policy_name -- None
    - waf_policy_resource_group_name -- None
    - waf_policy_subscription_id -- None
    '''
    return _call_az("az cdn endpoint waf policy set", locals())


def remove(endpoint_name, profile_name, resource_group, yes=None):
    '''
    Remove a CDN WAF policy from a CDN endpoint.

    Required Parameters:
    - endpoint_name -- Name of the CDN endpoint.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az cdn endpoint waf policy remove", locals())

