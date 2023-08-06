from .... pyaz_utils import _call_az

def create(address_pool, frontend_ip_configs, lb_name, name, protocol, resource_group, enable_tcp_reset=None, idle_timeout=None, outbound_ports=None):
    '''
    Create an outbound-rule.

    Required Parameters:
    - address_pool -- Name or ID of the backend address pool.
    - frontend_ip_configs -- Space-separated list of frontend IP configuration names or IDs.
    - lb_name -- The load balancer name.
    - name -- The name of the outbound rule
    - protocol -- Network transport protocol.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - enable_tcp_reset -- Receive bidirectional TCP reset on TCP flow idle timeout or unexpected connection termination. Only used when protocol is set to TCP.
    - idle_timeout -- Idle timeout in minutes.
    - outbound_ports -- The number of outbound ports to be used for NAT.
    '''
    return _call_az("az network lb outbound-rule create", locals())


def update(lb_name, name, resource_group, add=None, address_pool=None, enable_tcp_reset=None, force_string=None, frontend_ip_configs=None, idle_timeout=None, outbound_ports=None, protocol=None, remove=None, set=None):
    '''
    Update an outbound-rule.

    Required Parameters:
    - lb_name -- The load balancer name.
    - name -- The name of the outbound rule
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - address_pool -- Name or ID of the backend address pool.
    - enable_tcp_reset -- Receive bidirectional TCP reset on TCP flow idle timeout or unexpected connection termination. Only used when protocol is set to TCP.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - frontend_ip_configs -- Space-separated list of frontend IP configuration names or IDs.
    - idle_timeout -- Idle timeout in minutes.
    - outbound_ports -- The number of outbound ports to be used for NAT.
    - protocol -- Network transport protocol.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az network lb outbound-rule update", locals())


def list(lb_name, resource_group):
    '''
    List outbound rules.

    Required Parameters:
    - lb_name -- The name of the load balancer.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network lb outbound-rule list", locals())


def show(lb_name, name, resource_group):
    '''
    Get the details of an outbound rule.

    Required Parameters:
    - lb_name -- The name of the load balancer.
    - name -- The name of the outbound rule
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network lb outbound-rule show", locals())


def delete(lb_name, name, resource_group):
    '''
    Delete an outbound-rule.

    Required Parameters:
    - lb_name -- The name of the load balancer.
    - name -- The name of the outbound rule
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network lb outbound-rule delete", locals())

