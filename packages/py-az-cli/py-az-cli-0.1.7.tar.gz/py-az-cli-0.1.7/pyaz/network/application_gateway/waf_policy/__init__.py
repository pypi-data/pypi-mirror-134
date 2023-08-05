from .... pyaz_utils import _call_az
from . import custom_rule, policy_setting


def create(name, resource_group, location=None, tags=None, type=None, version=None):
    '''
    Create an application gateway WAF policy.

    Required Parameters:
    - name -- The name of the application gateway WAF policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - type -- The type of the web application firewall rule set.
    - version -- The version of the web application firewall rule set type. 0.1 is used for Microsoft_BotManagerRuleSet
    '''
    return _call_az("az network application-gateway waf-policy create", locals())


def delete(name, resource_group):
    '''
    Delete an application gateway WAF policy.

    Required Parameters:
    - name -- The name of the application gateway WAF policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway waf-policy delete", locals())


def show(name, resource_group):
    '''
    Get the details of an application gateway WAF policy.

    Required Parameters:
    - name -- The name of the application gateway WAF policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway waf-policy show", locals())


def list(resource_group=None):
    '''
    List application gateway WAF policies.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway waf-policy list", locals())


def update(name, resource_group, add=None, force_string=None, remove=None, set=None, tags=None):
    '''
    Update an application gateway WAF policy.

    Required Parameters:
    - name -- The name of the application gateway WAF policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az network application-gateway waf-policy update", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the application gateway WAF policy is met.

    Required Parameters:
    - name -- The name of the application gateway WAF policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az network application-gateway waf-policy wait", locals())

