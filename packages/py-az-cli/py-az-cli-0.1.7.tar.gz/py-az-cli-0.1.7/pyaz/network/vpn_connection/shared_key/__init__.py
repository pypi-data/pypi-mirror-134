from .... pyaz_utils import _call_az

def show(connection_name, resource_group):
    '''
    Retrieve a VPN connection shared key.

    Required Parameters:
    - connection_name -- Connection name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network vpn-connection shared-key show", locals())


def reset(connection_name, key_length, resource_group=None):
    '''
    Reset a VPN connection shared key.

    Required Parameters:
    - connection_name -- Connection name.
    - key_length -- The virtual network connection reset shared key length, should between 1 and 128.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network vpn-connection shared-key reset", locals())


def update(connection_name, resource_group, value, add=None, force_string=None, remove=None, set=None):
    '''
    Update a VPN connection shared key.

    Required Parameters:
    - connection_name -- Connection name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - value -- The virtual network connection shared key value.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az network vpn-connection shared-key update", locals())

