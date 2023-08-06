from .... pyaz_utils import _call_az
from . import address_pool, inbound_nat_rule


def create(name, nic_name, resource_group, app_gateway_address_pools=None, application_security_groups=None, gateway_name=None, lb_address_pools=None, lb_inbound_nat_rules=None, lb_name=None, make_primary=None, private_ip_address=None, private_ip_address_version=None, public_ip_address=None, subnet=None, vnet_name=None):
    '''
    Create an IP configuration.

    Required Parameters:
    - name -- The name of the IP configuration.
    - nic_name -- The network interface (NIC).
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - app_gateway_address_pools -- Space-separated list of names or IDs of application gateway backend address pools to associate with the NIC. If names are used, --gateway-name must be specified.
    - application_security_groups -- Space-separated list of application security groups.
    - gateway_name -- The name of the application gateway to use when adding address pools by name (ignored when IDs are specified).
    - lb_address_pools -- Space-separated list of names or IDs of load balancer address pools to associate with the NIC. If names are used, --lb-name must be specified.
    - lb_inbound_nat_rules -- Space-separated list of names or IDs of load balancer inbound NAT rules to associate with the NIC. If names are used, --lb-name must be specified.
    - lb_name -- The name of the load balancer to use when adding NAT rules or address pools by name (ignored when IDs are specified).
    - make_primary -- Set to make this configuration the primary one for the NIC.
    - private_ip_address -- Static IP address to use or ""('""' in PowerShell) to use a dynamic address.
    - private_ip_address_version -- None
    - public_ip_address -- Name or ID of the public IP to use.
    - subnet -- Name or ID of an existing subnet. If name is specified, also specify --vnet-name.
    - vnet_name -- The virtual network (VNet) associated with the subnet (Omit if supplying a subnet id).
    '''
    return _call_az("az network nic ip-config create", locals())


def update(name, nic_name, resource_group, add=None, app_gateway_address_pools=None, application_security_groups=None, force_string=None, gateway_lb=None, gateway_name=None, lb_address_pools=None, lb_inbound_nat_rules=None, lb_name=None, make_primary=None, private_ip_address=None, private_ip_address_version=None, public_ip_address=None, remove=None, set=None, subnet=None, vnet_name=None):
    '''
    Update an IP configuration.

    Required Parameters:
    - name -- The name of the IP configuration.
    - nic_name -- The network interface (NIC).
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - app_gateway_address_pools -- Space-separated list of names or IDs of application gateway backend address pools to associate with the NIC. If names are used, --gateway-name must be specified.
    - application_security_groups -- Space-separated list of application security groups.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - gateway_lb -- The reference to gateway load balancer frontend IP. If you want to delete it, input '""'(Powershell) or ""(Linux)
    - gateway_name -- The name of the application gateway to use when adding address pools by name (ignored when IDs are specified).
    - lb_address_pools -- Space-separated list of names or IDs of load balancer address pools to associate with the NIC. If names are used, --lb-name must be specified.
    - lb_inbound_nat_rules -- Space-separated list of names or IDs of load balancer inbound NAT rules to associate with the NIC. If names are used, --lb-name must be specified.
    - lb_name -- The name of the load balancer to use when adding NAT rules or address pools by name (ignored when IDs are specified).
    - make_primary -- Set to make this configuration the primary one for the NIC.
    - private_ip_address -- Static IP address to use or ""('""' in PowerShell) to use a dynamic address.
    - private_ip_address_version -- None
    - public_ip_address -- Name or ID of the public IP to use.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - subnet -- Name or ID of an existing subnet. If name is specified, also specify --vnet-name.
    - vnet_name -- The virtual network (VNet) associated with the subnet (Omit if supplying a subnet id).
    '''
    return _call_az("az network nic ip-config update", locals())


def list(nic_name, resource_group):
    '''
    List the IP configurations of a NIC.

    Required Parameters:
    - nic_name -- The network interface (NIC).
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network nic ip-config list", locals())


def show(name, nic_name, resource_group):
    '''
    Show the details of an IP configuration.

    Required Parameters:
    - name -- The name of the IP configuration.
    - nic_name -- The network interface (NIC).
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network nic ip-config show", locals())


def delete(name, nic_name, resource_group):
    '''
    Delete an IP configuration.

    Required Parameters:
    - name -- The name of the IP configuration.
    - nic_name -- The network interface (NIC).
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network nic ip-config delete", locals())

