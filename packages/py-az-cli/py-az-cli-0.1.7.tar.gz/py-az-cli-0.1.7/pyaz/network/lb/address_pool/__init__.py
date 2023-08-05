from .... pyaz_utils import _call_az
from . import address, tunnel_interface


def create(lb_name, name, resource_group, backend_address=None, backend_addresses_config_file=None, vnet=None):
    '''
    Create an address pool.

    Required Parameters:
    - lb_name -- The load balancer name.
    - name -- The name of the backend address pool. If only one exists, omit to use as default.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - backend_address -- None
    - backend_addresses_config_file -- None
    - vnet -- Name or Id of the virtual network applied to all backend addresses.
    '''
    return _call_az("az network lb address-pool create", locals())


def update(lb_name, name, resource_group, add=None, backend_address=None, backend_addresses_config_file=None, force_string=None, remove=None, set=None, vnet=None):
    '''
    Update an address pool.

    Required Parameters:
    - lb_name -- The load balancer name.
    - name -- The name of the backend address pool. If only one exists, omit to use as default.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - backend_address -- None
    - backend_addresses_config_file -- None
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - vnet -- Name or Id of the virtual network applied to all backend addresses.
    '''
    return _call_az("az network lb address-pool update", locals())


def show(lb_name, name, resource_group):
    '''
    Get the details of an address pool.

    Required Parameters:
    - lb_name -- The load balancer name.
    - name -- The name of the backend address pool. If only one exists, omit to use as default.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network lb address-pool show", locals())


def list(lb_name, resource_group):
    '''
    List address pools.

    Required Parameters:
    - lb_name -- The load balancer name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network lb address-pool list", locals())


def delete(lb_name, name, resource_group):
    '''
    Delete an address pool.

    Required Parameters:
    - lb_name -- The load balancer name.
    - name -- The name of the backend address pool. If only one exists, omit to use as default.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network lb address-pool delete", locals())

