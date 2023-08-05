from .... pyaz_utils import _call_az
from . import rule


def list(gateway_name, resource_group):
    '''
    List URL path maps.

    Required Parameters:
    - gateway_name -- The name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway url-path-map list", locals())


def show(gateway_name, name, resource_group):
    '''
    Get the details of a URL path map.

    Required Parameters:
    - gateway_name -- The name of the application gateway.
    - name -- The name of the URL path map.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway url-path-map show", locals())


def delete(gateway_name, name, resource_group, no_wait=None):
    '''
    Delete a URL path map.

    Required Parameters:
    - gateway_name -- The name of the application gateway.
    - name -- The name of the URL path map.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network application-gateway url-path-map delete", locals())


def create(gateway_name, name, paths, resource_group, address_pool=None, default_address_pool=None, default_http_settings=None, default_redirect_config=None, default_rewrite_rule_set=None, http_settings=None, no_wait=None, redirect_config=None, rewrite_rule_set=None, rule_name=None, waf_policy=None):
    '''
    Create a URL path map.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- The name of the URL path map.
    - paths -- Space-separated list of paths to associate with the rule. Valid paths start and end with "/" (ex: "/bar/")
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - address_pool -- The name or ID of the backend address pool to use with the created rule.
    - default_address_pool -- The name or ID of the default backend address pool, if different from --address-pool.
    - default_http_settings -- The name or ID of the default HTTP settings, if different from --http-settings.
    - default_redirect_config -- The name or ID of the default redirect configuration.
    - default_rewrite_rule_set -- The name or ID of the default rewrite rule set, if different from --rewrite-rule-set.
    - http_settings -- The name or ID of the HTTP settings to use with the created rule.
    - no_wait -- Do not wait for the long-running operation to finish.
    - redirect_config -- The name or ID of the redirect configuration to use with the created rule.
    - rewrite_rule_set -- The name or ID of the rewrite rule set. If not specified, the default for the map will be used.
    - rule_name -- The name of the url-path-map rule.
    - waf_policy -- Name or ID of a Firewall Policy resource.
    '''
    return _call_az("az network application-gateway url-path-map create", locals())


def update(gateway_name, name, resource_group, add=None, default_address_pool=None, default_http_settings=None, default_redirect_config=None, default_rewrite_rule_set=None, force_string=None, no_wait=None, remove=None, set=None):
    '''
    Update a URL path map.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- The name of the URL path map.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - default_address_pool -- The name or ID of the default backend address pool.
    - default_http_settings -- The name or ID of the default HTTP settings.
    - default_redirect_config -- The name or ID of the default redirect configuration.
    - default_rewrite_rule_set -- The name or ID of the default rewrite rule set.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - no_wait -- Do not wait for the long-running operation to finish.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az network application-gateway url-path-map update", locals())

