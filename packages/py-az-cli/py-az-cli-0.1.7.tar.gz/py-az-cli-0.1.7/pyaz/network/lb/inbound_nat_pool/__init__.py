from .... pyaz_utils import _call_az

def list(lb_name, resource_group):
    '''
    List inbound NAT address pools.

    Required Parameters:
    - lb_name -- The name of the load balancer.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network lb inbound-nat-pool list", locals())


def show(lb_name, name, resource_group):
    '''
    Get the details of an inbound NAT address pool.

    Required Parameters:
    - lb_name -- The name of the load balancer.
    - name -- The name of the inbound NAT pool
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network lb inbound-nat-pool show", locals())


def delete(lb_name, name, resource_group):
    '''
    Delete an inbound NAT address pool.

    Required Parameters:
    - lb_name -- The name of the load balancer.
    - name -- The name of the inbound NAT pool
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network lb inbound-nat-pool delete", locals())


def create(backend_port, frontend_port_range_end, frontend_port_range_start, lb_name, name, protocol, resource_group, enable_tcp_reset=None, floating_ip=None, frontend_ip_name=None, idle_timeout=None):
    '''
    Create an inbound NAT address pool.

    Required Parameters:
    - backend_port -- Port number
    - frontend_port_range_end -- Port number
    - frontend_port_range_start -- Port number
    - lb_name -- The load balancer name.
    - name -- The name of the inbound NAT pool
    - protocol -- Network transport protocol.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - enable_tcp_reset -- Receive bidirectional TCP reset on TCP flow idle timeout or unexpected connection termination. Only used when protocol is set to TCP.
    - floating_ip -- Enable floating IP.
    - frontend_ip_name -- The name of the frontend IP configuration. If only one exists, omit to use as default.
    - idle_timeout -- Idle timeout in minutes.
    '''
    return _call_az("az network lb inbound-nat-pool create", locals())


def update(lb_name, name, resource_group, add=None, backend_port=None, enable_tcp_reset=None, floating_ip=None, force_string=None, frontend_ip_name=None, frontend_port_range_end=None, frontend_port_range_start=None, idle_timeout=None, protocol=None, remove=None, set=None):
    '''
    Update an inbound NAT address pool.

    Required Parameters:
    - lb_name -- The load balancer name.
    - name -- The name of the inbound NAT pool
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - backend_port -- Port number
    - enable_tcp_reset -- Receive bidirectional TCP reset on TCP flow idle timeout or unexpected connection termination. Only used when protocol is set to TCP.
    - floating_ip -- Enable floating IP.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - frontend_ip_name -- The name of the frontend IP configuration.
    - frontend_port_range_end -- Port number
    - frontend_port_range_start -- Port number
    - idle_timeout -- Idle timeout in minutes.
    - protocol -- Network transport protocol.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az network lb inbound-nat-pool update", locals())

