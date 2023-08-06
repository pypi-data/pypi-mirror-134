from .... pyaz_utils import _call_az
from . import connection, peer_connection


def create(circuit_name, peer_asn, peering_type, primary_peer_subnet, resource_group, secondary_peer_subnet, vlan_id, advertised_public_prefixes=None, customer_asn=None, ip_version=None, legacy_mode=None, route_filter=None, routing_registry_name=None, shared_key=None):
    '''
    Create peering settings for an ExpressRoute circuit.

    Required Parameters:
    - circuit_name -- ExpressRoute circuit name.
    - peer_asn -- Autonomous system number of the customer/connectivity provider.
    - peering_type -- BGP peering type for the circuit.
    - primary_peer_subnet -- /30(ipv4) or /126(ipv6) subnet used to configure IP addresses for primary interface.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - secondary_peer_subnet -- /30(ipv4) or /126(ipv6) subnet used to configure IP addresses for secondary interface.
    - vlan_id -- Identifier used to identify the customer.

    Optional Parameters:
    - advertised_public_prefixes -- Space-separated list of prefixes to be advertised through the BGP peering.
    - customer_asn -- Autonomous system number of the customer.
    - ip_version -- The IP version to update Microsoft Peering settings for.
    - legacy_mode -- Integer representing the legacy mode of the peering.
    - route_filter -- Name or ID of a route filter to apply to the peering settings.
    - routing_registry_name -- Internet Routing Registry / Regional Internet Registry
    - shared_key -- Key for generating an MD5 for the BGP session.
    '''
    return _call_az("az network express-route peering create", locals())


def delete(circuit_name, name, resource_group):
    '''
    Delete peering settings.

    Required Parameters:
    - circuit_name -- ExpressRoute circuit name.
    - name -- The name of the peering
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network express-route peering delete", locals())


def show(circuit_name, name, resource_group):
    '''
    Get the details of an express route peering.

    Required Parameters:
    - circuit_name -- ExpressRoute circuit name.
    - name -- The name of the peering
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network express-route peering show", locals())


def list(circuit_name, resource_group):
    '''
    List peering settings of an ExpressRoute circuit.

    Required Parameters:
    - circuit_name -- ExpressRoute circuit name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network express-route peering list", locals())


def get_stats(circuit_name, name, resource_group):
    '''
    Get all traffic stats of an ExpressRoute peering.

    Required Parameters:
    - circuit_name -- ExpressRoute circuit name.
    - name -- The name of the peering
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network express-route peering get-stats", locals())


def update(circuit_name, name, resource_group, add=None, advertised_public_prefixes=None, customer_asn=None, force_string=None, ip_version=None, legacy_mode=None, peer_asn=None, primary_peer_subnet=None, remove=None, route_filter=None, routing_registry_name=None, secondary_peer_subnet=None, set=None, shared_key=None, vlan_id=None):
    '''
    Update peering settings of an ExpressRoute circuit.

    Required Parameters:
    - circuit_name -- ExpressRoute circuit name.
    - name -- The name of the peering
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - advertised_public_prefixes -- Space-separated list of prefixes to be advertised through the BGP peering.
    - customer_asn -- Autonomous system number of the customer.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - ip_version -- The IP version to update Microsoft Peering settings for.
    - legacy_mode -- Integer representing the legacy mode of the peering.
    - peer_asn -- Autonomous system number of the customer/connectivity provider.
    - primary_peer_subnet -- /30(ipv4) or /126(ipv6) subnet used to configure IP addresses for primary interface.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - route_filter -- Name or ID of a route filter to apply to the peering settings.
    - routing_registry_name -- Internet Routing Registry / Regional Internet Registry
    - secondary_peer_subnet -- /30(ipv4) or /126(ipv6) subnet used to configure IP addresses for secondary interface.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - shared_key -- Key for generating an MD5 for the BGP session.
    - vlan_id -- Identifier used to identify the customer.
    '''
    return _call_az("az network express-route peering update", locals())

