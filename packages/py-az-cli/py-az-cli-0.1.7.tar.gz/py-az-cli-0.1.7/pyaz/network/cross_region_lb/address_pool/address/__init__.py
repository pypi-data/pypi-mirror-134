from ..... pyaz_utils import _call_az

def add(frontend_ip_address, lb_name, name, pool_name, resource_group):
    '''
    Add one backend address into the load balance backend address pool.

    Required Parameters:
    - frontend_ip_address -- Resource id of the frontend ip configuration defined in regional loadbalancer.
    - lb_name -- The load balancer name.
    - name -- Name of the backend address.
    - pool_name -- The name of the backend address pool. If only one exists, omit to use as default.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network cross-region-lb address-pool address add", locals())


def remove(lb_name, name, pool_name, resource_group):
    '''
    Remove one backend address from the load balance backend address pool.

    Required Parameters:
    - lb_name -- The load balancer name.
    - name -- Name of the backend address.
    - pool_name -- The name of the backend address pool. If only one exists, omit to use as default.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network cross-region-lb address-pool address remove", locals())


def list(lb_name, pool_name, resource_group):
    '''
    List all backend addresses of the load balance backend address pool.

    Required Parameters:
    - lb_name -- The load balancer name.
    - pool_name -- The name of the backend address pool. If only one exists, omit to use as default.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network cross-region-lb address-pool address list", locals())

