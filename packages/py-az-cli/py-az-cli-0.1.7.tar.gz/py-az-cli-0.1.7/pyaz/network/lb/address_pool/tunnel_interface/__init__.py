from ..... pyaz_utils import _call_az

def add(address_pool, identifier, lb_name, protocol, resource_group, type, port=None):
    '''
    Add one tunnel interface into the load balance tunnel interface pool.

    Required Parameters:
    - address_pool -- The name of the backend address pool. If only one exists, omit to use as default.
    - identifier -- Identifier of gateway load balancer tunnel interface.
    - lb_name -- The load balancer name.
    - protocol -- Protocol of gateway load balancer tunnel interface.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - type -- Traffic type of gateway load balancer tunnel interface.

    Optional Parameters:
    - port -- Port of gateway load balancer tunnel interface.
    '''
    return _call_az("az network lb address-pool tunnel-interface add", locals())


def update(address_pool, index, lb_name, resource_group, identifier=None, port=None, protocol=None, type=None):
    '''
    update one tunnel interface of load balance tunnel interface pool.

    Required Parameters:
    - address_pool -- The name of the backend address pool. If only one exists, omit to use as default.
    - index -- Index of the tunnel interfaces to change
    - lb_name -- The load balancer name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - identifier -- Identifier of gateway load balancer tunnel interface.
    - port -- Port of gateway load balancer tunnel interface.
    - protocol -- Protocol of gateway load balancer tunnel interface.
    - type -- Traffic type of gateway load balancer tunnel interface.
    '''
    return _call_az("az network lb address-pool tunnel-interface update", locals())


def remove(address_pool, index, lb_name, resource_group):
    '''
    Remove one tunnel interface from the load balance tunnel interface pool.

    Required Parameters:
    - address_pool -- The name of the backend address pool. If only one exists, omit to use as default.
    - index -- Index of the tunnel interfaces to change
    - lb_name -- The load balancer name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network lb address-pool tunnel-interface remove", locals())


def list(address_pool, lb_name, resource_group):
    '''
    List all tunnel interfacees of the load balance tunnel interface pool.

    Required Parameters:
    - address_pool -- The name of the backend address pool. If only one exists, omit to use as default.
    - lb_name -- The load balancer name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network lb address-pool tunnel-interface list", locals())

