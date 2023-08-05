'''
Manage load balancing rules.
'''
from .... pyaz_utils import _call_az

def list(lb_name, resource_group):
    '''
    List load balancing rules.

    Required Parameters:
    - lb_name -- The name of the load balancer.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network lb rule list", locals())


def show(lb_name, name, resource_group):
    '''
    Get the details of a load balancing rule.

    Required Parameters:
    - lb_name -- The name of the load balancer.
    - name -- The name of the load balancing rule
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network lb rule show", locals())


def delete(lb_name, name, resource_group):
    '''
    Delete a load balancing rule.

    Required Parameters:
    - lb_name -- The name of the load balancer.
    - name -- The name of the load balancing rule
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network lb rule delete", locals())


def create(backend_port, frontend_port, lb_name, name, protocol, resource_group, backend_pool_name=None, backend_pools_name=None, disable_outbound_snat=None, enable_tcp_reset=None, floating_ip=None, frontend_ip_name=None, idle_timeout=None, load_distribution=None, probe_name=None):
    '''
    Create a load balancing rule.

    Required Parameters:
    - backend_port -- Port number
    - frontend_port -- Port number
    - lb_name -- The load balancer name.
    - name -- The name of the load balancing rule
    - protocol -- Network transport protocol.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - backend_pool_name -- The name of the backend address pool. If only one exists, omit to use as default.
    - backend_pools_name -- List of name of the backend address pool
    - disable_outbound_snat -- Configures SNAT for the VMs in the backend pool to use the publicIP address specified in the frontend of the load balancing rule.
    - enable_tcp_reset -- Receive bidirectional TCP reset on TCP flow idle timeout or unexpected connection termination. Only used when protocol is set to TCP.
    - floating_ip -- Enable floating IP.
    - frontend_ip_name -- The name of the frontend IP configuration. If only one exists, omit to use as default.
    - idle_timeout -- Idle timeout in minutes.
    - load_distribution -- Affinity rule settings.
    - probe_name -- Name of an existing probe to associate with this rule.
    '''
    return _call_az("az network lb rule create", locals())


def update(lb_name, name, resource_group, add=None, backend_pool_name=None, backend_pools_name=None, backend_port=None, disable_outbound_snat=None, enable_tcp_reset=None, floating_ip=None, force_string=None, frontend_ip_name=None, frontend_port=None, idle_timeout=None, load_distribution=None, probe_name=None, protocol=None, remove=None, set=None):
    '''
    Update a load balancing rule.

    Required Parameters:
    - lb_name -- The load balancer name.
    - name -- The name of the load balancing rule
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - backend_pool_name -- The name of the backend address pool.
    - backend_pools_name -- List of name of the backend address pool
    - backend_port -- Port number
    - disable_outbound_snat -- Configures SNAT for the VMs in the backend pool to use the publicIP address specified in the frontend of the load balancing rule.
    - enable_tcp_reset -- Receive bidirectional TCP reset on TCP flow idle timeout or unexpected connection termination. Only used when protocol is set to TCP.
    - floating_ip -- Enable floating IP.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - frontend_ip_name -- The name of the frontend IP configuration.
    - frontend_port -- Port number
    - idle_timeout -- Idle timeout in minutes.
    - load_distribution -- Affinity rule settings.
    - probe_name -- Name of an existing probe to associate with this rule.
    - protocol -- Network transport protocol.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az network lb rule update", locals())

