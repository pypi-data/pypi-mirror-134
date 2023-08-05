'''
Manage CDN WAF policies.
'''
from .... pyaz_utils import _call_az
from . import custom_rule, managed_rule_set, rate_limit_rule


def show(name, resource_group):
    '''
    Show details of a CDN WAF policy.

    Required Parameters:
    - name -- The name of the CDN WAF policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cdn waf policy show", locals())


def list(resource_group):
    '''
    List CDN WAF policies.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cdn waf policy list", locals())


def set(name, resource_group, block_response_body=None, block_response_status_code=None, disabled=None, mode=None, redirect_url=None, sku=None, tags=None):
    '''
    Create a new CDN WAF policy.

    Required Parameters:
    - name -- The name of the CDN WAF policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - block_response_body -- None
    - block_response_status_code -- None
    - disabled -- None
    - mode -- None
    - redirect_url -- None
    - sku -- None
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az cdn waf policy set", locals())


def delete(name, resource_group, yes=None):
    '''
    Delete a CDN WAF policy.

    Required Parameters:
    - name -- The name of the CDN WAF policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az cdn waf policy delete", locals())

