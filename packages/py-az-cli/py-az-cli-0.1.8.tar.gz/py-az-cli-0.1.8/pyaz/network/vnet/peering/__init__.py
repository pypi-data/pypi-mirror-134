'''
Manage peering connections between Azure Virtual Networks.
'''
from .... pyaz_utils import _call_az

def create(name, remote_vnet, resource_group, vnet_name, allow_forwarded_traffic=None, allow_gateway_transit=None, allow_vnet_access=None, use_remote_gateways=None):
    '''
    Create a virtual network peering connection.

    Required Parameters:
    - name -- The name of the VNet peering.
    - remote_vnet -- Resource ID or name of the remote VNet.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vnet_name -- The virtual network (VNet) name.

    Optional Parameters:
    - allow_forwarded_traffic -- Allows forwarded traffic from the local VNet to the remote VNet.
    - allow_gateway_transit -- Allows gateway link to be used in the remote VNet.
    - allow_vnet_access -- Allows access from the local VNet to the remote VNet.
    - use_remote_gateways -- Allows VNet to use the remote VNet's gateway. Remote VNet gateway must have --allow-gateway-transit enabled for remote peering. Only 1 peering can have this flag enabled. Cannot be set if the VNet already has a gateway.
    '''
    return _call_az("az network vnet peering create", locals())


def show(name, resource_group, vnet_name):
    '''
    Show details of a peering.

    Required Parameters:
    - name -- The name of the VNet peering.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vnet_name -- The virtual network (VNet) name.
    '''
    return _call_az("az network vnet peering show", locals())


def list(resource_group, vnet_name):
    '''
    List peerings.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vnet_name -- The virtual network (VNet) name.
    '''
    return _call_az("az network vnet peering list", locals())


def delete(name, resource_group, vnet_name):
    '''
    Delete a peering.

    Required Parameters:
    - name -- The name of the VNet peering.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vnet_name -- The virtual network (VNet) name.
    '''
    return _call_az("az network vnet peering delete", locals())


def update(name, resource_group, vnet_name, add=None, force_string=None, remove=None, set=None):
    '''
    Update a peering.

    Required Parameters:
    - name -- The name of the VNet peering.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vnet_name -- The virtual network (VNet) name.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az network vnet peering update", locals())

