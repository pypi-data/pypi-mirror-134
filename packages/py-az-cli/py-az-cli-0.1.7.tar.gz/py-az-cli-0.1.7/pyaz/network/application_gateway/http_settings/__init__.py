from .... pyaz_utils import _call_az

def list(gateway_name, resource_group):
    '''
    List HTTP settings.

    Required Parameters:
    - gateway_name -- The name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway http-settings list", locals())


def show(gateway_name, name, resource_group):
    '''
    Get the details of a gateway's HTTP settings.

    Required Parameters:
    - gateway_name -- The name of the application gateway.
    - name -- The name of the backed HTTP settings.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway http-settings show", locals())


def delete(gateway_name, name, resource_group, no_wait=None):
    '''
    Delete HTTP settings.

    Required Parameters:
    - gateway_name -- The name of the application gateway.
    - name -- The name of the backed HTTP settings.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network application-gateway http-settings delete", locals())


def create(gateway_name, name, port, resource_group, affinity_cookie_name=None, auth_certs=None, connection_draining_timeout=None, cookie_based_affinity=None, enable_probe=None, host_name=None, host_name_from_backend_pool=None, no_wait=None, path=None, probe=None, protocol=None, root_certs=None, timeout=None):
    '''
    Create HTTP settings.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- The name of the backed HTTP settings.
    - port -- The port number.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - affinity_cookie_name -- Name used for the affinity cookie.
    - auth_certs -- Space-separated list of authentication certificates (names or IDs) to associate with the HTTP settings.
    - connection_draining_timeout -- The time in seconds after a backend server is removed during which on open connection remains active. Range: 0 (disabled) to 3600
    - cookie_based_affinity -- Enable or disable cookie-based affinity.
    - enable_probe -- Whether the probe is enabled.
    - host_name -- Host header sent to the backend servers.
    - host_name_from_backend_pool -- Use host name of the backend server as the host header.
    - no_wait -- Do not wait for the long-running operation to finish.
    - path -- Path that will prefix all HTTP requests.
    - probe -- Name or ID of the probe to associate with the HTTP settings.
    - protocol -- The HTTP settings protocol.
    - root_certs -- Space-separated list of trusted root certificates (names or IDs) to associate with the HTTP settings. --host-name or --host-name-from-backend-pool is required when this field is set.
    - timeout -- Request timeout in seconds.
    '''
    return _call_az("az network application-gateway http-settings create", locals())


def update(gateway_name, name, resource_group, add=None, affinity_cookie_name=None, auth_certs=None, connection_draining_timeout=None, cookie_based_affinity=None, enable_probe=None, force_string=None, host_name=None, host_name_from_backend_pool=None, no_wait=None, path=None, port=None, probe=None, protocol=None, remove=None, root_certs=None, set=None, timeout=None):
    '''
    Update HTTP settings.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- The name of the backed HTTP settings.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - affinity_cookie_name -- Name used for the affinity cookie.
    - auth_certs -- Space-separated list of authentication certificates (names or IDs) to associate with the HTTP settings.
    - connection_draining_timeout -- The time in seconds after a backend server is removed during which on open connection remains active. Range: 0 (disabled) to 3600
    - cookie_based_affinity -- Enable or disable cookie-based affinity.
    - enable_probe -- Whether the probe is enabled.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - host_name -- Host header sent to the backend servers.
    - host_name_from_backend_pool -- Use host name of the backend server as the host header.
    - no_wait -- Do not wait for the long-running operation to finish.
    - path -- Path that will prefix all HTTP requests.
    - port -- The port number.
    - probe -- Name or ID of the probe to associate with the HTTP settings.
    - protocol -- The HTTP settings protocol.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - root_certs -- Space-separated list of trusted root certificates (names or IDs) to associate with the HTTP settings. --host-name or --host-name-from-backend-pool is required when this field is set.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - timeout -- Request timeout in seconds.
    '''
    return _call_az("az network application-gateway http-settings update", locals())

