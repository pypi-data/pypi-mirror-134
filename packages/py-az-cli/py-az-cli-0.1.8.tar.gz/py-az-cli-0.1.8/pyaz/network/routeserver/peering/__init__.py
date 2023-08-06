'''
Manage the route server peering.
'''
from .... pyaz_utils import _call_az

def create(name, peer_asn, peer_ip, resource_group, routeserver, no_wait=None):
    '''
    Create a route server peering.

    Required Parameters:
    - name -- The name of the Route Server Peering
    - peer_asn -- Peer ASN. Its range is from 1 to 4294967295.
    - peer_ip -- Peer IP address.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - routeserver -- The name of the Route Server.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network routeserver peering create", locals())


def update(name, resource_group, routeserver, add=None, force_string=None, peer_asn=None, peer_ip=None, remove=None, set=None):
    '''
    Update a route server peering.

    Required Parameters:
    - name -- The name of the Route Server Peering
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - routeserver -- The name of the Route Server.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - peer_asn -- Peer ASN. Its range is from 1 to 4294967295.
    - peer_ip -- Peer IP address.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az network routeserver peering update", locals())


def delete(name, resource_group, routeserver, no_wait=None, yes=None):
    '''
    Delete a route server peering.

    Required Parameters:
    - name -- The name of the Route Server Peering
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - routeserver -- The name of the Route Server.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az network routeserver peering delete", locals())


def show(name, resource_group, routeserver):
    '''
    Show a route server peering

    Required Parameters:
    - name -- The name of the Route Server Peering
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - routeserver -- The name of the Route Server.
    '''
    return _call_az("az network routeserver peering show", locals())


def wait(name, resource_group, routeserver, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the route server peering is met.

    Required Parameters:
    - name -- The name of the Route Server Peering
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - routeserver -- The name of the Route Server.

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az network routeserver peering wait", locals())


def list(resource_group, routeserver):
    '''
    List all route server peerings under a resource group.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - routeserver -- The name of the Route Server.
    '''
    return _call_az("az network routeserver peering list", locals())


def list_learned_routes(name, resource_group, routeserver):
    '''
    List all routes the route server bgp connection has learned.

    Required Parameters:
    - name -- The name of the Route Server Peering
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - routeserver -- The name of the Route Server.
    '''
    return _call_az("az network routeserver peering list-learned-routes", locals())


def list_advertised_routes(name, resource_group, routeserver):
    '''
    List all routes the route server bgp connection is advertising to the specified peer.

    Required Parameters:
    - name -- The name of the Route Server Peering
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - routeserver -- The name of the Route Server.
    '''
    return _call_az("az network routeserver peering list-advertised-routes", locals())

