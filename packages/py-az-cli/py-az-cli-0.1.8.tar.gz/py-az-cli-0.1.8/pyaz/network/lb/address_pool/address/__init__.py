from ..... pyaz_utils import _call_az

def add(ip_address, lb_name, name, pool_name, resource_group, subnet=None, vnet=None):
    '''
    Add one backend address into the load balance backend address pool.

    Required Parameters:
    - ip_address -- Ip Address within the Virtual Network.
    - lb_name -- The load balancer name.
    - name -- Name of the backend address.
    - pool_name -- The name of the backend address pool. If only one exists, omit to use as default.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - subnet -- Name or Id of the existing subnet.(If name is provided, vnet is also required;If id, vnet is not required)
    - vnet -- Name or Id of the virtual network.
    '''
    return _call_az("az network lb address-pool address add", locals())


def remove(lb_name, name, pool_name, resource_group):
    '''
    Remove one backend address from the load balance backend address pool.

    Required Parameters:
    - lb_name -- The load balancer name.
    - name -- Name of the backend address.
    - pool_name -- The name of the backend address pool. If only one exists, omit to use as default.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network lb address-pool address remove", locals())


def list(lb_name, pool_name, resource_group):
    '''
    List all backend addresses of the load balance backend address pool.

    Required Parameters:
    - lb_name -- The load balancer name.
    - pool_name -- The name of the backend address pool. If only one exists, omit to use as default.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network lb address-pool address list", locals())

