'''
Manage network interfaces.
'''
from ... pyaz_utils import _call_az
from . import ip_config


def create(name, resource_group, subnet, accelerated_networking=None, app_gateway_address_pools=None, application_security_groups=None, dns_servers=None, edge_zone=None, gateway_name=None, internal_dns_name=None, ip_forwarding=None, lb_address_pools=None, lb_inbound_nat_rules=None, lb_name=None, location=None, network_security_group=None, no_wait=None, private_ip_address=None, private_ip_address_version=None, public_ip_address=None, tags=None, vnet_name=None):
    '''
    Create a network interface.

    Required Parameters:
    - name -- The network interface (NIC).
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - subnet -- Name or ID of an existing subnet. If name specified, also specify --vnet-name. If you want to use an existing subnet in other resource group, please provide the ID instead of the name of the subnet

    Optional Parameters:
    - accelerated_networking -- Enable accelerated networking.
    - app_gateway_address_pools -- Space-separated list of names or IDs of application gateway backend address pools to associate with the NIC. If names are used, --gateway-name must be specified.
    - application_security_groups -- Space-separated list of application security groups.
    - dns_servers -- Space-separated list of DNS server IP addresses.
    - edge_zone -- The name of edge zone.
    - gateway_name -- The name of the application gateway to use when adding address pools by name (ignored when IDs are specified).
    - internal_dns_name -- The internal DNS name label.
    - ip_forwarding -- Enable IP forwarding.
    - lb_address_pools -- Space-separated list of names or IDs of load balancer address pools to associate with the NIC. If names are used, --lb-name must be specified.
    - lb_inbound_nat_rules -- Space-separated list of names or IDs of load balancer inbound NAT rules to associate with the NIC. If names are used, --lb-name must be specified.
    - lb_name -- The name of the load balancer to use when adding NAT rules or address pools by name (ignored when IDs are specified).
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - network_security_group -- Name or ID of an existing network security group, or none by default.
    - no_wait -- Do not wait for the long-running operation to finish.
    - private_ip_address -- Static private IP address to use.
    - private_ip_address_version -- The private IP address version to use.
    - public_ip_address -- Name or ID of an existing public IP address, or none by default.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - vnet_name -- The virtual network (VNet) name.
    '''
    return _call_az("az network nic create", locals())


def delete(name, resource_group, no_wait=None):
    '''
    Delete a network interface.

    Required Parameters:
    - name -- The network interface (NIC).
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network nic delete", locals())


def show(name, resource_group, expand=None):
    '''
    Get the details of a network interface.

    Required Parameters:
    - name -- The network interface (NIC).
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expand -- Expands referenced resources.
    '''
    return _call_az("az network nic show", locals())


def list(resource_group=None):
    '''
    List network interfaces.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network nic list", locals())


def show_effective_route_table(name, resource_group):
    '''
    Show the effective route table applied to a network interface.

    Required Parameters:
    - name -- The network interface (NIC).
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network nic show-effective-route-table", locals())


def list_effective_nsg(name, resource_group):
    '''
    List all effective network security groups applied to a network interface.

    Required Parameters:
    - name -- The network interface (NIC).
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network nic list-effective-nsg", locals())


def update(name, resource_group, accelerated_networking=None, add=None, dns_servers=None, force_string=None, internal_dns_name=None, ip_forwarding=None, network_security_group=None, no_wait=None, remove=None, set=None):
    '''
    Update a network interface.

    Required Parameters:
    - name -- The network interface (NIC).
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - accelerated_networking -- Enable accelerated networking.
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - dns_servers -- Space-separated list of DNS server IP addresses. Use ""('""' in PowerShell) to revert to default Azure servers.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - internal_dns_name -- The internal DNS name label.
    - ip_forwarding -- Enable IP forwarding.
    - network_security_group -- Name or ID of the associated network security group.
    - no_wait -- Do not wait for the long-running operation to finish.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az network nic update", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, expand=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the network interface is met.

    Required Parameters:
    - name -- The network interface (NIC).
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - expand -- Expands referenced resources.
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az network nic wait", locals())

