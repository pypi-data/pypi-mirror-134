from ... pyaz_utils import _call_az
from . import auth, gateway, peering, port


def delete(name, resource_group, no_wait=None):
    '''
    Delete an ExpressRoute circuit.

    Required Parameters:
    - name -- ExpressRoute circuit name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network express-route delete", locals())


def show(name, resource_group):
    '''
    Get the details of an ExpressRoute circuit.

    Required Parameters:
    - name -- ExpressRoute circuit name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network express-route show", locals())


def get_stats(name, resource_group):
    '''
    Get the statistics of an ExpressRoute circuit.

    Required Parameters:
    - name -- ExpressRoute circuit name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network express-route get-stats", locals())


def list_arp_tables(name, path, peering_name, resource_group):
    '''
    Show the current Address Resolution Protocol (ARP) table of an ExpressRoute circuit.

    Required Parameters:
    - name -- ExpressRoute circuit name.
    - path -- The path of the device
    - peering_name -- The name of the peering
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network express-route list-arp-tables", locals())


def list_route_tables(name, path, peering_name, resource_group):
    '''
    Show the current routing table of an ExpressRoute circuit peering.

    Required Parameters:
    - name -- ExpressRoute circuit name.
    - path -- The path of the device
    - peering_name -- The name of the peering
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network express-route list-route-tables", locals())


def list_route_tables_summary(name, path, peering_name, resource_group):
    '''
    Show the current routing table summary of an ExpressRoute circuit peering.

    Required Parameters:
    - name -- ExpressRoute circuit name.
    - path -- The path of the device
    - peering_name -- The name of the peering
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network express-route list-route-tables-summary", locals())


def create(bandwidth, name, peering_location, provider, resource_group, allow_classic_operations=None, allow_global_reach=None, express_route_port=None, location=None, no_wait=None, sku_family=None, sku_tier=None, tags=None):
    '''
    Create an ExpressRoute circuit.

    Required Parameters:
    - bandwidth -- Bandwidth of the circuit. Usage: INT {Mbps,Gbps}. Defaults to Mbps
    - name -- ExpressRoute circuit name.
    - peering_location -- Name of the peering location.
    - provider -- Name of the ExpressRoute Service Provider.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - allow_classic_operations -- Allow classic operations.
    - allow_global_reach -- Enable global reach on the circuit.
    - express_route_port -- Name or ID of an ExpressRoute port.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - no_wait -- Do not wait for the long-running operation to finish.
    - sku_family -- Chosen SKU family of ExpressRoute circuit.
    - sku_tier -- SKU Tier of ExpressRoute circuit.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az network express-route create", locals())


def list(resource_group=None):
    '''
    List all ExpressRoute circuits for the current subscription.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network express-route list", locals())


def list_service_providers():
    '''
    List available ExpressRoute service providers.
    '''
    return _call_az("az network express-route list-service-providers", locals())


def update(name, resource_group, add=None, allow_classic_operations=None, allow_global_reach=None, bandwidth=None, express_route_port=None, force_string=None, no_wait=None, peering_location=None, provider=None, remove=None, set=None, sku_family=None, sku_tier=None, tags=None):
    '''
    Update settings of an ExpressRoute circuit.

    Required Parameters:
    - name -- ExpressRoute circuit name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - allow_classic_operations -- Allow classic operations.
    - allow_global_reach -- Enable global reach on the circuit.
    - bandwidth -- Bandwidth of the circuit. Usage: INT {Mbps,Gbps}. Defaults to Mbps
    - express_route_port -- Name or ID of an ExpressRoute port.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - no_wait -- Do not wait for the long-running operation to finish.
    - peering_location -- Name of the peering location.
    - provider -- Name of the ExpressRoute Service Provider.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - sku_family -- Chosen SKU family of ExpressRoute circuit.
    - sku_tier -- SKU Tier of ExpressRoute circuit.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az network express-route update", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the ExpressRoute is met.

    Required Parameters:
    - name -- ExpressRoute circuit name.
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
    return _call_az("az network express-route wait", locals())

