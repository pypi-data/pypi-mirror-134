from .... pyaz_utils import _call_az

def list(gateway_name, resource_group):
    '''
    List probes.

    Required Parameters:
    - gateway_name -- The name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway probe list", locals())


def show(gateway_name, name, resource_group):
    '''
    Get the details of a probe.

    Required Parameters:
    - gateway_name -- The name of the application gateway.
    - name -- The name of the probe.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway probe show", locals())


def delete(gateway_name, name, resource_group, no_wait=None):
    '''
    Delete a probe.

    Required Parameters:
    - gateway_name -- The name of the application gateway.
    - name -- The name of the probe.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network application-gateway probe delete", locals())


def create(gateway_name, name, path, protocol, resource_group, host=None, host_name_from_http_settings=None, interval=None, match_body=None, match_status_codes=None, min_servers=None, no_wait=None, port=None, threshold=None, timeout=None):
    '''
    Create a probe.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- The name of the probe.
    - path -- The relative path of the probe. Valid paths start from "/"
    - protocol -- The HTTP settings protocol.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - host -- The name of the host to send the probe.
    - host_name_from_http_settings -- Use host header from HTTP settings.
    - interval -- The time interval in seconds between consecutive probes.
    - match_body -- Body that must be contained in the health response.
    - match_status_codes -- Space-separated list of allowed ranges of healthy status codes for the health response.
    - min_servers -- Minimum number of servers that are always marked healthy.
    - no_wait -- Do not wait for the long-running operation to finish.
    - port -- Custom port which will be used for probing the backend servers. The valid value ranges from 1 to 65535. In case not set, port from http settings will be used. This property is valid for Standard_v2 and WAF_v2 only.
    - threshold -- The number of failed probes after which the back end server is marked down.
    - timeout -- The probe timeout in seconds.
    '''
    return _call_az("az network application-gateway probe create", locals())


def update(gateway_name, name, resource_group, add=None, force_string=None, host=None, host_name_from_http_settings=None, interval=None, match_body=None, match_status_codes=None, min_servers=None, no_wait=None, path=None, port=None, protocol=None, remove=None, set=None, threshold=None, timeout=None):
    '''
    Update a probe.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- The name of the probe.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - host -- The name of the host to send the probe.
    - host_name_from_http_settings -- Use host header from HTTP settings.
    - interval -- The time interval in seconds between consecutive probes.
    - match_body -- Body that must be contained in the health response.
    - match_status_codes -- Space-separated list of allowed ranges of healthy status codes for the health response.
    - min_servers -- Minimum number of servers that are always marked healthy.
    - no_wait -- Do not wait for the long-running operation to finish.
    - path -- The relative path of the probe. Valid paths start from "/"
    - port -- Custom port which will be used for probing the backend servers. The valid value ranges from 1 to 65535. In case not set, port from http settings will be used. This property is valid for Standard_v2 and WAF_v2 only.
    - protocol -- The HTTP settings protocol.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - threshold -- The number of failed probes after which the back end server is marked down.
    - timeout -- The probe timeout in seconds.
    '''
    return _call_az("az network application-gateway probe update", locals())

