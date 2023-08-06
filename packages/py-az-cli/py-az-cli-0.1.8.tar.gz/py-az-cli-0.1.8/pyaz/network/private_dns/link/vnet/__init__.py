from ..... pyaz_utils import _call_az

def delete(name, resource_group, zone_name, if_match=None, no_wait=None, yes=None):
    '''
    Delete a virtual network link to the specified Private DNS zone.

    Required Parameters:
    - name -- The name of the virtual network link to the specified Private DNS zone.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - zone_name -- The name of the Private DNS zone.

    Optional Parameters:
    - if_match -- The ETag of the virtual network link to the Private DNS zone. Omit this value to always delete the current zone. Specify the last-seen ETag value to prevent accidentally deleting any concurrent changes.
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az network private-dns link vnet delete", locals())


def show(name, resource_group, zone_name):
    '''
    Get a virtual network link to the specified Private DNS zone.

    Required Parameters:
    - name -- The name of the virtual network link to the specified Private DNS zone.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - zone_name -- The name of the Private DNS zone.
    '''
    return _call_az("az network private-dns link vnet show", locals())


def list(resource_group, zone_name, top=None):
    '''
    List the virtual network links to the specified Private DNS zone.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - zone_name -- The name of the Private DNS zone.

    Optional Parameters:
    - top -- The maximum number of virtual network links to return. If not specified, returns up to 100 virtual network links.
    '''
    return _call_az("az network private-dns link vnet list", locals())


def create(name, registration_enabled, resource_group, virtual_network, zone_name, no_wait=None, tags=None):
    '''
    Create a virtual network link to the specified Private DNS zone.

    Required Parameters:
    - name -- The name of the virtual network link to the specified Private DNS zone.
    - registration_enabled -- Specify if the link is registration enabled.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - virtual_network -- Name or ID of the virtual network.
    - zone_name -- The name of the Private DNS zone.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az network private-dns link vnet create", locals())


def update(name, resource_group, zone_name, add=None, force_string=None, if_match=None, no_wait=None, registration_enabled=None, remove=None, set=None, tags=None):
    '''
    Update a virtual network link's properties. Does not modify virtual network within the link.

    Required Parameters:
    - name -- The name of the virtual network link to the specified Private DNS zone.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - zone_name -- The name of the Private DNS zone.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - if_match -- None
    - no_wait -- Do not wait for the long-running operation to finish.
    - registration_enabled -- Specify if the link is registration enabled.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az network private-dns link vnet update", locals())


def wait(name, resource_group, zone_name, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the virtual network link to the specified Private DNS zone is met.

    Required Parameters:
    - name -- The name of the virtual network link to the specified Private DNS zone.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - zone_name -- The name of the Private DNS zone.

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az network private-dns link vnet wait", locals())

