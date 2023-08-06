from .... pyaz_utils import _call_az

def create(address_prefix, name, next_hop_type, resource_group, route_table_name, next_hop_ip_address=None):
    '''
    Create a route in a route table.

    Required Parameters:
    - address_prefix -- The destination CIDR to which the route applies.
    - name -- Route name
    - next_hop_type -- The type of Azure hop the packet should be sent to.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - route_table_name -- Route table name

    Optional Parameters:
    - next_hop_ip_address -- The IP address packets should be forwarded to when using the VirtualAppliance hop type.
    '''
    return _call_az("az network route-table route create", locals())


def delete(name, resource_group, route_table_name):
    '''
    Delete a route from a route table.

    Required Parameters:
    - name -- Route name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - route_table_name -- Route table name
    '''
    return _call_az("az network route-table route delete", locals())


def show(name, resource_group, route_table_name):
    '''
    Get the details of a route in a route table.

    Required Parameters:
    - name -- Route name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - route_table_name -- Route table name
    '''
    return _call_az("az network route-table route show", locals())


def list(resource_group, route_table_name):
    '''
    List routes in a route table.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - route_table_name -- Route table name
    '''
    return _call_az("az network route-table route list", locals())


def update(name, resource_group, route_table_name, add=None, address_prefix=None, force_string=None, next_hop_ip_address=None, next_hop_type=None, remove=None, set=None):
    '''
    Update a route in a route table.

    Required Parameters:
    - name -- Route name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - route_table_name -- Route table name

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - address_prefix -- The destination CIDR to which the route applies.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - next_hop_ip_address -- The IP address packets should be forwarded to when using the VirtualAppliance hop type.
    - next_hop_type -- The type of Azure hop the packet should be sent to.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az network route-table route update", locals())

