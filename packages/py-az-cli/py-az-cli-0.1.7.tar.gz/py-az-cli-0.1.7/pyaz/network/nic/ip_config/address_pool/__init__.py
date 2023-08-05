from ..... pyaz_utils import _call_az

def add(address_pool, ip_config_name, nic_name, resource_group, gateway_name=None, lb_name=None):
    '''
    Add an address pool to an IP configuration.

    Required Parameters:
    - address_pool -- The name or ID of an existing backend address pool.
    - ip_config_name -- The name of the IP configuration.
    - nic_name -- The network interface (NIC).
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - gateway_name -- The name of an application gateway containing the address pool (Omit if suppying an address pool ID).
    - lb_name -- The name of the load balancer containing the address pool (Omit if suppying an address pool ID).
    '''
    return _call_az("az network nic ip-config address-pool add", locals())


def remove(address_pool, ip_config_name, nic_name, resource_group, gateway_name=None, lb_name=None):
    '''
    Remove an address pool of an IP configuration.

    Required Parameters:
    - address_pool -- The name or ID of an existing backend address pool.
    - ip_config_name -- The name of the IP configuration.
    - nic_name -- The network interface (NIC).
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - gateway_name -- The name of an application gateway containing the address pool (Omit if suppying an address pool ID).
    - lb_name -- The name of the load balancer containing the address pool (Omit if suppying an address pool ID).
    '''
    return _call_az("az network nic ip-config address-pool remove", locals())

