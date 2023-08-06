from .... pyaz_utils import _call_az

def list(gateway_name, resource_group):
    '''
    List rules.

    Required Parameters:
    - gateway_name -- The name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway rule list", locals())


def show(gateway_name, name, resource_group):
    '''
    Get the details of a rule.

    Required Parameters:
    - gateway_name -- The name of the application gateway.
    - name -- The name of the request routing rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway rule show", locals())


def delete(gateway_name, name, resource_group, no_wait=None):
    '''
    Delete a rule.

    Required Parameters:
    - gateway_name -- The name of the application gateway.
    - name -- The name of the request routing rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network application-gateway rule delete", locals())


def create(gateway_name, name, resource_group, address_pool=None, http_listener=None, http_settings=None, no_wait=None, priority=None, redirect_config=None, rewrite_rule_set=None, rule_type=None, url_path_map=None):
    '''
    Create a rule.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- The name of the request routing rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - address_pool -- The name or ID of the backend address pool. If only one exists, omit to use as default.
    - http_listener -- The name or ID of the HTTP listener. If only one exists, omit to use as default.
    - http_settings -- The name or ID of the HTTP settings. If only one exists, omit to use as default.
    - no_wait -- Do not wait for the long-running operation to finish.
    - priority -- Priority of the request routing rule. Range from 1 to 2000
    - redirect_config -- The name or ID of the redirect configuration to use with the created rule.
    - rewrite_rule_set -- The name or ID of the rewrite rule set.
    - rule_type -- The rule type (Basic, PathBasedRouting).
    - url_path_map -- The name or ID of the URL path map.
    '''
    return _call_az("az network application-gateway rule create", locals())


def update(gateway_name, name, resource_group, add=None, address_pool=None, force_string=None, http_listener=None, http_settings=None, no_wait=None, priority=None, redirect_config=None, remove=None, rewrite_rule_set=None, rule_type=None, set=None, url_path_map=None):
    '''
    Update a rule.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- The name of the request routing rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - address_pool -- The name or ID of the backend address pool.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - http_listener -- The name or ID of the HTTP listener.
    - http_settings -- The name or ID of the backend HTTP settings.
    - no_wait -- Do not wait for the long-running operation to finish.
    - priority -- Priority of the request routing rule. Range from 1 to 2000
    - redirect_config -- The name or ID of the redirect configuration to use with the created rule.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - rewrite_rule_set -- The name or ID of the rewrite rule set.
    - rule_type -- The rule type (Basic, PathBasedRouting).
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - url_path_map -- The name or ID of the URL path map.
    '''
    return _call_az("az network application-gateway rule update", locals())

