from .... pyaz_utils import _call_az

def list(gateway_name, resource_group):
    '''
    List frontend IP addresses.

    Required Parameters:
    - gateway_name -- The name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway frontend-ip list", locals())


def show(gateway_name, name, resource_group):
    '''
    Get the details of a frontend IP address.

    Required Parameters:
    - gateway_name -- The name of the application gateway.
    - name -- The name of the frontend IP configuration.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway frontend-ip show", locals())


def delete(gateway_name, name, resource_group, no_wait=None):
    '''
    Delete a frontend IP address.

    Required Parameters:
    - gateway_name -- The name of the application gateway.
    - name -- The name of the frontend IP configuration.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network application-gateway frontend-ip delete", locals())


def create(gateway_name, name, resource_group, no_wait=None, private_ip_address=None, public_ip_address=None, subnet=None, vnet_name=None):
    '''
    Create a frontend IP address.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- The name of the frontend IP configuration.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - private_ip_address -- Static private IP address to use.
    - public_ip_address -- The name or ID of the public IP address.
    - subnet -- The name or ID of the subnet.
    - vnet_name -- The name of the virtual network corresponding to the subnet.
    '''
    return _call_az("az network application-gateway frontend-ip create", locals())


def update(gateway_name, name, resource_group, add=None, force_string=None, no_wait=None, private_ip_address=None, public_ip_address=None, remove=None, set=None, subnet=None, vnet_name=None):
    '''
    Update a frontend IP address.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- The name of the frontend IP configuration.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - no_wait -- Do not wait for the long-running operation to finish.
    - private_ip_address -- Static private IP address to use.
    - public_ip_address -- The name or ID of the public IP address.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - subnet -- The name or ID of the subnet.
    - vnet_name -- The name of the virtual network corresponding to the subnet.
    '''
    return _call_az("az network application-gateway frontend-ip update", locals())

