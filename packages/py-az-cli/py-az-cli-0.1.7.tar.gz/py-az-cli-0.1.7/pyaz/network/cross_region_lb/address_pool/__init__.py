from .... pyaz_utils import _call_az
from . import address


def create(lb_name, name, resource_group, backend_address=None, backend_addresses_config_file=None):
    '''
    Create an address pool.

    Required Parameters:
    - lb_name -- The load balancer name.
    - name -- The name of the backend address pool. If only one exists, omit to use as default.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - backend_address -- None
    - backend_addresses_config_file -- None
    '''
    return _call_az("az network cross-region-lb address-pool create", locals())


def show(lb_name, name, resource_group):
    '''
    

    Required Parameters:
    - lb_name -- The load balancer name.
    - name -- The name of the backend address pool. If only one exists, omit to use as default.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network cross-region-lb address-pool show", locals())


def list(lb_name, resource_group):
    '''
    

    Required Parameters:
    - lb_name -- The load balancer name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network cross-region-lb address-pool list", locals())


def delete(lb_name, name, resource_group):
    '''
    Delete an address pool.

    Required Parameters:
    - lb_name -- The load balancer name.
    - name -- The name of the backend address pool. If only one exists, omit to use as default.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network cross-region-lb address-pool delete", locals())

