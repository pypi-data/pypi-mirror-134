from ..... pyaz_utils import _call_az
from . import ipv6_config


def create(address_prefix, circuit_name, name, peer_circuit, peering_name, resource_group, authorization_key=None):
    '''
    Create connections between two ExpressRoute circuits.

    Required Parameters:
    - address_prefix -- /29 IP address space to carve out customer addresses for tunnels.
    - circuit_name -- ExpressRoute circuit name.
    - name -- Name of the peering connection.
    - peer_circuit -- Name or ID of the peer ExpressRoute circuit.
    - peering_name -- Name of BGP peering (i.e. AzurePrivatePeering).
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - authorization_key -- The authorization key used when the peer circuit is in another subscription.
    '''
    return _call_az("az network express-route peering connection create", locals())


def delete(circuit_name, name, peering_name, resource_group):
    '''
    Delete an ExpressRoute circuit connection.

    Required Parameters:
    - circuit_name -- ExpressRoute circuit name.
    - name -- Name of the peering connection.
    - peering_name -- Name of BGP peering (i.e. AzurePrivatePeering).
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network express-route peering connection delete", locals())


def show(circuit_name, name, peering_name, resource_group):
    '''
    Get the details of an ExpressRoute circuit connection.

    Required Parameters:
    - circuit_name -- ExpressRoute circuit name.
    - name -- Name of the peering connection.
    - peering_name -- Name of BGP peering (i.e. AzurePrivatePeering).
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network express-route peering connection show", locals())


def list(circuit_name, peering_name, resource_group):
    '''
    List all global reach connections associated with a private peering in an express route circuit.

    Required Parameters:
    - circuit_name -- ExpressRoute circuit name.
    - peering_name -- Name of BGP peering (i.e. AzurePrivatePeering).
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network express-route peering connection list", locals())

