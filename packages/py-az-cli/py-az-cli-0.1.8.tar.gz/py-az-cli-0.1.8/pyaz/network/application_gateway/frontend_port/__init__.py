from .... pyaz_utils import _call_az

def list(gateway_name, resource_group):
    '''
    List frontend ports.

    Required Parameters:
    - gateway_name -- The name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway frontend-port list", locals())


def show(gateway_name, name, resource_group):
    '''
    Get the details of a frontend port.

    Required Parameters:
    - gateway_name -- The name of the application gateway.
    - name -- The name of the frontend port.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway frontend-port show", locals())


def delete(gateway_name, name, resource_group, no_wait=None):
    '''
    Delete a frontend port.

    Required Parameters:
    - gateway_name -- The name of the application gateway.
    - name -- The name of the frontend port.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network application-gateway frontend-port delete", locals())


def create(gateway_name, name, port, resource_group, no_wait=None):
    '''
    Create a frontend port.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- The name of the frontend port.
    - port -- The port number.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network application-gateway frontend-port create", locals())


def update(gateway_name, name, resource_group, add=None, force_string=None, no_wait=None, port=None, remove=None, set=None):
    '''
    Update a frontend port.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- The name of the frontend port.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - no_wait -- Do not wait for the long-running operation to finish.
    - port -- The port number.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az network application-gateway frontend-port update", locals())

