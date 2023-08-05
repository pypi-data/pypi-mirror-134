from ... pyaz_utils import _call_az
from . import aad, ipsec_policy, nat_rule, packet_capture, revoked_cert, root_cert, vpn_client


def create(name, public_ip_addresses, resource_group, vnet, aad_audience=None, aad_issuer=None, aad_tenant=None, address_prefixes=None, asn=None, bgp_peering_address=None, client_protocol=None, custom_routes=None, edge_zone=None, gateway_default_site=None, gateway_type=None, location=None, nat_rule=None, no_wait=None, peer_weight=None, radius_secret=None, radius_server=None, root_cert_data=None, root_cert_name=None, sku=None, tags=None, vpn_auth_type=None, vpn_gateway_generation=None, vpn_type=None):
    '''
    Create a virtual network gateway.

    Required Parameters:
    - name -- Name of the VNet gateway.
    - public_ip_addresses -- Specify a single public IP (name or ID) for an active-standby gateway. Specify two space-separated public IPs for an active-active gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vnet -- Name or ID of an existing virtual network which has a subnet named 'GatewaySubnet'.

    Optional Parameters:
    - aad_audience -- The AADAudience ID of the VirtualNetworkGateway.
    - aad_issuer -- The AAD Issuer URI of the VirtualNetworkGateway.
    - aad_tenant -- The AAD Tenant URI of the VirtualNetworkGateway.
    - address_prefixes -- Space-separated list of CIDR prefixes representing the address space for the P2S Vpnclient.
    - asn -- Autonomous System Number to use for the BGP settings.
    - bgp_peering_address -- IP address to use for BGP peering.
    - client_protocol -- Protocols to use for connecting
    - custom_routes -- Space-separated list of CIDR prefixes representing the custom routes address space specified by the customer for VpnClient.
    - edge_zone -- The name of edge zone.
    - gateway_default_site -- Name or ID of a local network gateway representing a local network site with default routes.
    - gateway_type -- The gateway type.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - nat_rule -- None
    - no_wait -- Do not wait for the long-running operation to finish.
    - peer_weight -- Weight (0-100) added to routes learned through BGP peering.
    - radius_secret -- Radius secret to use for authentication.
    - radius_server -- Radius server address to connect to.
    - root_cert_data -- Base64 contents of the root certificate file or file path.
    - root_cert_name -- Root certificate name
    - sku -- VNet gateway SKU.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - vpn_auth_type -- VPN authentication types enabled for the virtual network gateway.
    - vpn_gateway_generation -- The generation for the virtual network gateway. vpn_gateway_generation should not be provided if gateway_type is not Vpn.
    - vpn_type -- VPN routing type.
    '''
    return _call_az("az network vnet-gateway create", locals())


def update(name, resource_group, aad_audience=None, aad_issuer=None, aad_tenant=None, add=None, address_prefixes=None, asn=None, bgp_peering_address=None, client_protocol=None, custom_routes=None, enable_bgp=None, force_string=None, gateway_default_site=None, gateway_type=None, no_wait=None, peer_weight=None, public_ip_addresses=None, radius_secret=None, radius_server=None, remove=None, root_cert_data=None, root_cert_name=None, set=None, sku=None, tags=None, vnet=None, vpn_auth_type=None, vpn_type=None):
    '''
    Update a virtual network gateway.

    Required Parameters:
    - name -- Name of the VNet gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - aad_audience -- The AADAudience ID of the VirtualNetworkGateway.
    - aad_issuer -- The AAD Issuer URI of the VirtualNetworkGateway.
    - aad_tenant -- The AAD Tenant URI of the VirtualNetworkGateway.
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - address_prefixes -- Space-separated list of CIDR prefixes representing the address space for the P2S Vpnclient.
    - asn -- Autonomous System Number to use for the BGP settings.
    - bgp_peering_address -- IP address to use for BGP peering.
    - client_protocol -- Protocols to use for connecting
    - custom_routes -- Space-separated list of CIDR prefixes representing the custom routes address space specified by the customer for VpnClient.
    - enable_bgp -- Enable BGP (Border Gateway Protocol)
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - gateway_default_site -- Name or ID of a local network gateway representing a local network site with default routes.
    - gateway_type -- The gateway type.
    - no_wait -- Do not wait for the long-running operation to finish.
    - peer_weight -- Weight (0-100) added to routes learned through BGP peering.
    - public_ip_addresses -- Specify a single public IP (name or ID) for an active-standby gateway. Specify two space-separated public IPs for an active-active gateway.
    - radius_secret -- Radius secret to use for authentication.
    - radius_server -- Radius server address to connect to.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - root_cert_data -- Base64 contents of the root certificate file or file path.
    - root_cert_name -- Root certificate name
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - sku -- VNet gateway SKU.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - vnet -- Name or ID of a virtual network that contains a subnet named 'GatewaySubnet'.
    - vpn_auth_type -- VPN authentication types enabled for the virtual network gateway.
    - vpn_type -- VPN routing type.
    '''
    return _call_az("az network vnet-gateway update", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the virtual network gateway is met.

    Required Parameters:
    - name -- Name of the VNet gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az network vnet-gateway wait", locals())


def delete(name, resource_group, no_wait=None):
    '''
    Delete a virtual network gateway.

    Required Parameters:
    - name -- Name of the VNet gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network vnet-gateway delete", locals())


def show(name, resource_group):
    '''
    Get the details of a virtual network gateway.

    Required Parameters:
    - name -- Name of the VNet gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network vnet-gateway show", locals())


def list(resource_group):
    '''
    List virtual network gateways.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network vnet-gateway list", locals())


def reset(name, resource_group, gateway_vip=None):
    '''
    Reset a virtual network gateway.

    Required Parameters:
    - name -- Name of the VNet gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - gateway_vip -- Virtual network gateway vip address supplied to the begin reset of the active-active feature enabled gateway.
    '''
    return _call_az("az network vnet-gateway reset", locals())


def list_bgp_peer_status(name, resource_group, peer=None):
    '''
    Retrieve the status of BGP peers.

    Required Parameters:
    - name -- Name of the VNet gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - peer -- The IP address of the peer to retrieve the status of.
    '''
    return _call_az("az network vnet-gateway list-bgp-peer-status", locals())


def list_advertised_routes(name, peer, resource_group):
    '''
    List the routes of a virtual network gateway advertised to the specified peer.

    Required Parameters:
    - name -- Name of the VNet gateway.
    - peer -- The IP address of the peer.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network vnet-gateway list-advertised-routes", locals())


def list_learned_routes(name, resource_group):
    '''
    This operation retrieves a list of routes the virtual network gateway has learned, including routes learned from BGP peers.

    Required Parameters:
    - name -- Name of the VNet gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network vnet-gateway list-learned-routes", locals())


def show_supported_devices(name, resource_group):
    '''
    Get a xml format representation for supported vpn devices.

    Required Parameters:
    - name -- Name of the VNet gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network vnet-gateway show-supported-devices", locals())


def disconnect_vpn_connections(name, resource_group, vpn_connections, no_wait=None):
    '''
    Disconnect vpn connections of virtual network gateway.

    Required Parameters:
    - name -- Name of the VNet gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vpn_connections -- List of Name or ID of VPN connections.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network vnet-gateway disconnect-vpn-connections", locals())

