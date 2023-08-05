'''
Manage Azure Virtual Networks.
'''
from ... pyaz_utils import _call_az
from . import peering, subnet


def delete(name, resource_group):
    '''
    Delete a virtual network.

    Required Parameters:
    - name -- The virtual network (VNet) name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network vnet delete", locals())


def list(resource_group=None):
    '''
    List virtual networks.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network vnet list", locals())


def show(name, resource_group, expand=None):
    '''
    Get the details of a virtual network.

    Required Parameters:
    - name -- The virtual network (VNet) name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expand -- Expands referenced resources.
    '''
    return _call_az("az network vnet show", locals())


def check_ip_address(ip_address, name, resource_group):
    '''
    Check if a private IP address is available for use within a virtual network.

    Required Parameters:
    - ip_address -- The private IP address to be verified.
    - name -- The virtual network (VNet) name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network vnet check-ip-address", locals())


def create(name, resource_group, address_prefixes=None, bgp_community=None, ddos_protection=None, ddos_protection_plan=None, dns_servers=None, edge_zone=None, enable_encryption=None, encryption_enforcement_policy=None, flowtimeout=None, location=None, network_security_group=None, subnet_name=None, subnet_prefixes=None, tags=None, vm_protection=None):
    '''
    Create a virtual network.

    Required Parameters:
    - name -- The virtual network (VNet) name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - address_prefixes -- Space-separated list of IP address prefixes for the VNet.
    - bgp_community -- The BGP community associated with the virtual network.
    - ddos_protection -- Control whether DDoS protection is enabled.
    - ddos_protection_plan -- Name or ID of a DDoS protection plan to associate with the VNet.
    - dns_servers -- Space-separated list of DNS server IP addresses.
    - edge_zone -- The name of edge zone.
    - enable_encryption -- Enable encryption on the virtual network.
    - encryption_enforcement_policy -- To control if the Virtual Machine without encryption is allowed in encrypted Virtual Network or not.
    - flowtimeout -- The FlowTimeout value (in minutes) for the Virtual Network
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - network_security_group -- Name or ID of a network security group (NSG).
    - subnet_name -- Name of a new subnet to create within the VNet.
    - subnet_prefixes -- Space-separated list of address prefixes in CIDR format for the new subnet. If omitted, automatically reserves a /24 (or as large as available) block within the VNet address space.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - vm_protection -- Enable VM protection for all subnets in the VNet.
    '''
    return _call_az("az network vnet create", locals())


def update(name, resource_group, add=None, address_prefixes=None, bgp_community=None, ddos_protection=None, ddos_protection_plan=None, dns_servers=None, enable_encryption=None, encryption_enforcement_policy=None, flowtimeout=None, force_string=None, remove=None, set=None, vm_protection=None):
    '''
    Update a virtual network.

    Required Parameters:
    - name -- The virtual network (VNet) name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - address_prefixes -- Space-separated list of IP address prefixes for the VNet.
    - bgp_community -- The BGP community associated with the virtual network.
    - ddos_protection -- Control whether DDoS protection is enabled.
    - ddos_protection_plan -- Name or ID of a DDoS protection plan to associate with the VNet.
    - dns_servers -- Space-separated list of DNS server IP addresses.
    - enable_encryption -- Enable encryption on the virtual network.
    - encryption_enforcement_policy -- To control if the Virtual Machine without encryption is allowed in encrypted Virtual Network or not.
    - flowtimeout -- The FlowTimeout value (in minutes) for the Virtual Network
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - vm_protection -- Enable VM protection for all subnets in the VNet.
    '''
    return _call_az("az network vnet update", locals())


def list_endpoint_services(location):
    '''
    List which services support VNET service tunneling in a given region.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    '''
    return _call_az("az network vnet list-endpoint-services", locals())


def list_available_ips(name, resource_group):
    '''
    List some available ips in the vnet.

    Required Parameters:
    - name -- The virtual network (VNet) name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network vnet list-available-ips", locals())

