from .... pyaz_utils import _call_az

def list(gateway_name, resource_group):
    '''
    List HTTP listeners.

    Required Parameters:
    - gateway_name -- The name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway http-listener list", locals())


def show(gateway_name, name, resource_group):
    '''
    Get the details of an HTTP listener.

    Required Parameters:
    - gateway_name -- The name of the application gateway.
    - name -- The name of the HTTP listener.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway http-listener show", locals())


def delete(gateway_name, name, resource_group, no_wait=None):
    '''
    Delete an HTTP listener.

    Required Parameters:
    - gateway_name -- The name of the application gateway.
    - name -- The name of the HTTP listener.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network application-gateway http-listener delete", locals())


def create(frontend_port, gateway_name, name, resource_group, frontend_ip=None, host_name=None, host_names=None, no_wait=None, ssl_cert=None, ssl_profile_id=None, waf_policy=None):
    '''
    Create an HTTP listener.

    Required Parameters:
    - frontend_port -- The name or ID of the frontend port.
    - gateway_name -- Name of the application gateway.
    - name -- The name of the HTTP listener.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - frontend_ip -- The name or ID of the frontend IP configuration. If only one exists, omit to use as default.
    - host_name -- Host name to use for multisite gateways.
    - host_names -- Space-separated list of host names that allows special wildcard characters as well.
    - no_wait -- Do not wait for the long-running operation to finish.
    - ssl_cert -- The name or ID of the SSL certificate to use.
    - ssl_profile_id -- SSL profile resource of the application gateway.
    - waf_policy -- Name or ID of a Firewall Policy resource.
    '''
    return _call_az("az network application-gateway http-listener create", locals())


def update(gateway_name, name, resource_group, add=None, force_string=None, frontend_ip=None, frontend_port=None, host_name=None, host_names=None, no_wait=None, remove=None, set=None, ssl_cert=None, ssl_profile_id=None, waf_policy=None):
    '''
    Update an HTTP listener.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- The name of the HTTP listener.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - frontend_ip -- The name or ID of the frontend IP configuration.
    - frontend_port -- The name or ID of the frontend port.
    - host_name -- Host name to use for multisite gateways.
    - host_names -- Space-separated list of host names that allows special wildcard characters as well.
    - no_wait -- Do not wait for the long-running operation to finish.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - ssl_cert -- The name or ID of the SSL certificate to use.
    - ssl_profile_id -- SSL profile resource of the application gateway.
    - waf_policy -- Name or ID of a Firewall Policy resource.
    '''
    return _call_az("az network application-gateway http-listener update", locals())

