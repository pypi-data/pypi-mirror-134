from .... pyaz_utils import _call_az

def delete(name, resource_group, if_match=None, no_wait=None, yes=None):
    '''
    Delete a Private DNS zone.

    Required Parameters:
    - name -- The name of the Private DNS zone.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - if_match -- The ETag of the Private DNS zone. Omit this value to always delete the current zone. Specify the last-seen ETag value to prevent accidentally deleting any concurrent changes.
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az network private-dns zone delete", locals())


def show(name, resource_group):
    '''
    Get a Private DNS zone.

    Required Parameters:
    - name -- The name of the Private DNS zone.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network private-dns zone show", locals())


def list(resource_group=None):
    '''
    List Private DNS zones.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network private-dns zone list", locals())


def import_(file_name, name, resource_group):
    '''
    Create a Private DNS zone using a DNS zone file.

    Required Parameters:
    - file_name -- Path to the Private DNS zone file to import
    - name -- The name of the Private DNS zone.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network private-dns zone import", locals())


def export(name, resource_group, file_name=None):
    '''
    Export a Private DNS zone as a DNS zone file.

    Required Parameters:
    - name -- The name of the Private DNS zone.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - file_name -- Path to the Private DNS zone file to save
    '''
    return _call_az("az network private-dns zone export", locals())


def create(name, resource_group, no_wait=None, tags=None):
    '''
    Create a Private DNS zone.

    Required Parameters:
    - name -- The name of the Private DNS zone.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az network private-dns zone create", locals())


def update(name, resource_group, add=None, force_string=None, if_match=None, no_wait=None, remove=None, set=None, tags=None):
    '''
    Update a Private DNS zone's properties. Does not modify Private DNS records or virtual network links within the zone.

    Required Parameters:
    - name -- The name of the Private DNS zone.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - if_match -- The ETag of the Private DNS zone. Omit this value to always overwrite the current zone. Specify the last-seen ETag value to prevent accidentally overwriting any concurrent changes.
    - no_wait -- Do not wait for the long-running operation to finish.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az network private-dns zone update", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the Private DNS zone is met.

    Required Parameters:
    - name -- The name of the Private DNS zone.
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
    return _call_az("az network private-dns zone wait", locals())

