from ...... pyaz_utils import _call_az

def set(address_prefix, circuit_name, name, peering_name, resource_group):
    '''
    Set connection config to ExpressRoute circuit connection.

    Required Parameters:
    - address_prefix -- /125 IP address space to carve out customer addresses for global reach.
    - circuit_name -- ExpressRoute circuit name.
    - name -- Name of the peering connection.
    - peering_name -- Name of BGP peering (i.e. AzurePrivatePeering).
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network express-route peering connection ipv6-config set", locals())


def remove(circuit_name, name, peering_name, resource_group):
    '''
    Remove connection config to ExpressRoute circuit connection.

    Required Parameters:
    - circuit_name -- ExpressRoute circuit name.
    - name -- Name of the peering connection.
    - peering_name -- Name of BGP peering (i.e. AzurePrivatePeering).
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network express-route peering connection ipv6-config remove", locals())

