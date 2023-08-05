from .... pyaz_utils import _call_az

def list(gateway_name, resource_group):
    '''
    List address pools.

    Required Parameters:
    - gateway_name -- The name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway address-pool list", locals())


def show(gateway_name, name, resource_group):
    '''
    Get the details of an address pool.

    Required Parameters:
    - gateway_name -- The name of the application gateway.
    - name -- The name of the backend address pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway address-pool show", locals())


def delete(gateway_name, name, resource_group, no_wait=None):
    '''
    Delete an address pool.

    Required Parameters:
    - gateway_name -- The name of the application gateway.
    - name -- The name of the backend address pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network application-gateway address-pool delete", locals())


def create(gateway_name, name, resource_group, no_wait=None, servers=None):
    '''
    Create an address pool.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- The name of the backend address pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - servers -- Space-separated list of IP addresses or DNS names corresponding to backend servers.
    '''
    return _call_az("az network application-gateway address-pool create", locals())


def update(gateway_name, name, resource_group, add=None, force_string=None, no_wait=None, remove=None, servers=None, set=None):
    '''
    Update an address pool.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- The name of the backend address pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - no_wait -- Do not wait for the long-running operation to finish.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - servers -- Space-separated list of IP addresses or DNS names corresponding to backend servers.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az network application-gateway address-pool update", locals())

