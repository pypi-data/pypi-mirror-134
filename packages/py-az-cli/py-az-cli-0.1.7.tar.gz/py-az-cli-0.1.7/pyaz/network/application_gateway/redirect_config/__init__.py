from .... pyaz_utils import _call_az

def list(gateway_name, resource_group):
    '''
    List redirect configurations.

    Required Parameters:
    - gateway_name -- The name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway redirect-config list", locals())


def show(gateway_name, name, resource_group):
    '''
    Get the details of a redirect configuration.

    Required Parameters:
    - gateway_name -- The name of the application gateway.
    - name -- The name of the redirect configuration.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway redirect-config show", locals())


def delete(gateway_name, name, resource_group, no_wait=None):
    '''
    Delete a redirect configuration.

    Required Parameters:
    - gateway_name -- The name of the application gateway.
    - name -- The name of the redirect configuration.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network application-gateway redirect-config delete", locals())


def create(gateway_name, name, resource_group, type, include_path=None, include_query_string=None, no_wait=None, target_listener=None, target_url=None):
    '''
    Create a redirect configuration.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- The name of the redirect configuration.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - type -- HTTP redirection type

    Optional Parameters:
    - include_path -- Include path in the redirected url.
    - include_query_string -- Include query string in the redirected url.
    - no_wait -- Do not wait for the long-running operation to finish.
    - target_listener -- Name or ID of the HTTP listener to redirect the request to.
    - target_url -- URL to redirect the request to.
    '''
    return _call_az("az network application-gateway redirect-config create", locals())


def update(gateway_name, name, resource_group, add=None, force_string=None, include_path=None, include_query_string=None, no_wait=None, remove=None, set=None, target_listener=None, target_url=None, type=None):
    '''
    Update a redirect configuration.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- The name of the redirect configuration.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - include_path -- Include path in the redirected url.
    - include_query_string -- Include query string in the redirected url.
    - no_wait -- Do not wait for the long-running operation to finish.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - target_listener -- Name or ID of the HTTP listener to redirect the request to.
    - target_url -- URL to redirect the request to.
    - type -- HTTP redirection type
    '''
    return _call_az("az network application-gateway redirect-config update", locals())

