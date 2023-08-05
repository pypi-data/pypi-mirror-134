from ... pyaz_utils import _call_az
from . import ipsec_policy, packet_capture, shared_key


def create(name, resource_group, vnet_gateway1, authorization_key=None, egress_nat_rule=None, enable_bgp=None, express_route_circuit2=None, express_route_gateway_bypass=None, ingress_nat_rule=None, local_gateway2=None, location=None, routing_weight=None, shared_key=None, tags=None, use_policy_based_traffic_selectors=None, validate=None, vnet_gateway2=None):
    '''
    Create a VPN connection.

    Required Parameters:
    - name -- Connection name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vnet_gateway1 -- None

    Optional Parameters:
    - authorization_key -- None
    - egress_nat_rule -- List of egress NatRules.
    - enable_bgp -- None
    - express_route_circuit2 -- None
    - express_route_gateway_bypass -- Bypass ExpressRoute gateway for data forwarding.
    - ingress_nat_rule -- List of ingress NatRules.
    - local_gateway2 -- None
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - routing_weight -- Connection routing weight
    - shared_key -- Shared IPSec key.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - use_policy_based_traffic_selectors -- Enable policy-based traffic selectors.
    - validate -- None
    - vnet_gateway2 -- None
    '''
    return _call_az("az network vpn-connection create", locals())


def delete(name, resource_group):
    '''
    Delete a VPN connection.

    Required Parameters:
    - name -- Connection name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network vpn-connection delete", locals())


def show(name, resource_group):
    '''
    Get the details of a VPN connection.

    Required Parameters:
    - name -- Connection name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network vpn-connection show", locals())


def list(resource_group, vnet_gateway=None):
    '''
    List all VPN connections.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - vnet_gateway -- Name of the VNet gateway.
    '''
    return _call_az("az network vpn-connection list", locals())


def update(name, resource_group, add=None, enable_bgp=None, express_route_gateway_bypass=None, force_string=None, remove=None, routing_weight=None, set=None, shared_key=None, tags=None, use_policy_based_traffic_selectors=None):
    '''
    Update a VPN connection.

    Required Parameters:
    - name -- Connection name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - enable_bgp -- Enable BGP (Border Gateway Protocol)
    - express_route_gateway_bypass -- Bypass ExpressRoute gateway for data forwarding.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - routing_weight -- Connection routing weight
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - shared_key -- Shared IPSec key.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - use_policy_based_traffic_selectors -- Enable policy-based traffic selectors.
    '''
    return _call_az("az network vpn-connection update", locals())


def list_ike_sas(name, resource_group):
    '''
    List IKE Security Associations for a VPN connection.

    Required Parameters:
    - name -- Connection name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network vpn-connection list-ike-sas", locals())


def show_device_config_script(device_family, firmware_version, name, resource_group, vendor):
    '''
    Get a XML format representation for VPN connection device configuration script.

    Required Parameters:
    - device_family -- The device family for the vpn device.
    - firmware_version -- The firmware version for the vpn device.
    - name -- Connection name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vendor -- The vendor for the VPN device.
    '''
    return _call_az("az network vpn-connection show-device-config-script", locals())

