from ... pyaz_utils import _call_az

def delete(name, resource_group, no_wait=None):
    '''
    Delete a local VPN gateway.

    Required Parameters:
    - name -- Name of the local network gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network local-gateway delete", locals())


def show(name, resource_group):
    '''
    Get the details of a local VPN gateway.

    Required Parameters:
    - name -- Name of the local network gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network local-gateway show", locals())


def list(resource_group):
    '''
    List all local VPN gateways in a resource group.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network local-gateway list", locals())


def create(gateway_ip_address, name, resource_group, asn=None, bgp_peering_address=None, local_address_prefixes=None, location=None, no_wait=None, peer_weight=None, tags=None):
    '''
    Create a local VPN gateway.

    Required Parameters:
    - gateway_ip_address -- Gateway's public IP address. (e.g. 10.1.1.1).
    - name -- Name of the local network gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - asn -- Autonomous System Number to use for the BGP settings.
    - bgp_peering_address -- IP address from the OnPremise VPN's subnet to use for BGP peering.
    - local_address_prefixes -- List of CIDR block prefixes representing the address space of the OnPremise VPN's subnet.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - no_wait -- Do not wait for the long-running operation to finish.
    - peer_weight -- Weight (0-100) added to routes learned through BGP peering.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az network local-gateway create", locals())


def update(name, resource_group, add=None, asn=None, bgp_peering_address=None, force_string=None, gateway_ip_address=None, local_address_prefixes=None, no_wait=None, peer_weight=None, remove=None, set=None, tags=None):
    '''
    Update a local VPN gateway.

    Required Parameters:
    - name -- Name of the local network gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - asn -- Autonomous System Number to use for the BGP settings.
    - bgp_peering_address -- IP address from the OnPremise VPN's subnet to use for BGP peering.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - gateway_ip_address -- Gateway's public IP address. (e.g. 10.1.1.1).
    - local_address_prefixes -- List of CIDR block prefixes representing the address space of the OnPremise VPN's subnet.
    - no_wait -- Do not wait for the long-running operation to finish.
    - peer_weight -- Weight (0-100) added to routes learned through BGP peering.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az network local-gateway update", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the local gateway is met.

    Required Parameters:
    - name -- Name of the local network gateway.
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
    return _call_az("az network local-gateway wait", locals())

