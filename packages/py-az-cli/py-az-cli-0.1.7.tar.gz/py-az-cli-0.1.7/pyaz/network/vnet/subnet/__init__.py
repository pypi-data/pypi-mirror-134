'''
Manage subnets in an Azure Virtual Network.
'''
from .... pyaz_utils import _call_az

def create(address_prefixes, name, resource_group, vnet_name, delegations=None, disable_private_endpoint_network_policies=None, disable_private_link_service_network_policies=None, nat_gateway=None, network_security_group=None, route_table=None, service_endpoint_policy=None, service_endpoints=None):
    '''
    Create a subnet and associate an existing NSG and route table.

    Required Parameters:
    - address_prefixes -- Space-separated list of address prefixes in CIDR format.
    - name -- The subnet name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vnet_name -- The virtual network (VNet) name.

    Optional Parameters:
    - delegations -- Space-separated list of services to whom the subnet should be delegated. (e.g. Microsoft.Sql/servers)
    - disable_private_endpoint_network_policies -- Disable private endpoint network policies on the subnet.
    - disable_private_link_service_network_policies -- Disable private link service network policies on the subnet.
    - nat_gateway -- Name or ID of a NAT gateway to attach.
    - network_security_group -- Name or ID of a network security group (NSG).
    - route_table -- Name or ID of a route table to associate with the subnet.
    - service_endpoint_policy -- Space-separated list of names or IDs of service endpoint policies to apply.
    - service_endpoints -- None
    '''
    return _call_az("az network vnet subnet create", locals())


def delete(name, resource_group, vnet_name):
    '''
    Delete a subnet.

    Required Parameters:
    - name -- The subnet name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vnet_name -- The virtual network (VNet) name.
    '''
    return _call_az("az network vnet subnet delete", locals())


def show(name, resource_group, vnet_name, expand=None):
    '''
    Show details of a subnet.

    Required Parameters:
    - name -- The subnet name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vnet_name -- The virtual network (VNet) name.

    Optional Parameters:
    - expand -- Expands referenced resources.
    '''
    return _call_az("az network vnet subnet show", locals())


def list(resource_group, vnet_name):
    '''
    List the subnets in a virtual network.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vnet_name -- The virtual network (VNet) name.
    '''
    return _call_az("az network vnet subnet list", locals())


def update(name, resource_group, vnet_name, add=None, address_prefixes=None, delegations=None, disable_private_endpoint_network_policies=None, disable_private_link_service_network_policies=None, force_string=None, nat_gateway=None, network_security_group=None, remove=None, route_table=None, service_endpoint_policy=None, service_endpoints=None, set=None):
    '''
    Update a subnet.

    Required Parameters:
    - name -- The subnet name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vnet_name -- The virtual network (VNet) name.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - address_prefixes -- Space-separated list of address prefixes in CIDR format.
    - delegations -- Space-separated list of services to whom the subnet should be delegated. (e.g. Microsoft.Sql/servers)
    - disable_private_endpoint_network_policies -- Disable private endpoint network policies on the subnet.
    - disable_private_link_service_network_policies -- Disable private link service network policies on the subnet.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - nat_gateway -- Name or ID of a NAT gateway to attach.
    - network_security_group -- Name or ID of a network security group (NSG). Use empty string ""('""' in PowerShell) to detach it.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - route_table -- Name or ID of a route table to associate with the subnet. Use empty string ""('""' in PowerShell) to detach it. You can also append "--remove routeTable" in "az network vnet subnet update" to detach it.
    - service_endpoint_policy -- Space-separated list of names or IDs of service endpoint policies to apply.
    - service_endpoints -- None
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az network vnet subnet update", locals())


def list_available_delegations(location=None, resource_group=None):
    '''
    List the services available for subnet delegation.

    Optional Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network vnet subnet list-available-delegations", locals())

