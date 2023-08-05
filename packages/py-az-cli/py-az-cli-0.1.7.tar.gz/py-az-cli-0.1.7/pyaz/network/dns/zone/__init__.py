'''
Manage DNS zones.
'''
from .... pyaz_utils import _call_az

def delete(name, resource_group, if_match=None, yes=None):
    '''
    Delete a DNS zone and all associated records.

    Required Parameters:
    - name -- The name of the zone.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - if_match -- The etag of the DNS zone. Omit this value to always delete the current zone. Specify the last-seen etag value to prevent accidentally deleting any concurrent changes.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az network dns zone delete", locals())


def show(name, resource_group):
    '''
    Get a DNS zone parameters. Does not show DNS records within the zone.

    Required Parameters:
    - name -- The name of the zone.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network dns zone show", locals())


def list(resource_group=None):
    '''
    List DNS zones.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network dns zone list", locals())


def import_(file_name, name, resource_group):
    '''
    Create a DNS zone using a DNS zone file.

    Required Parameters:
    - file_name -- Path to the DNS zone file to import
    - name -- The name of the zone.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network dns zone import", locals())


def export(name, resource_group, file_name=None):
    '''
    Export a DNS zone as a DNS zone file.

    Required Parameters:
    - name -- The name of the zone.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - file_name -- Path to the DNS zone file to save
    '''
    return _call_az("az network dns zone export", locals())


def create(name, resource_group, if_none_match=None, parent_name=None, registration_vnets=None, resolution_vnets=None, tags=None, zone_type=None):
    '''
    Create a DNS zone.

    Required Parameters:
    - name -- The name of the zone.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - if_none_match -- None
    - parent_name -- Specify if parent zone exists for this zone and delegation for the child zone in the parent is to be added.
    - registration_vnets -- Space-separated names or IDs of virtual networks that register hostnames in this DNS zone. Number of private DNS zones with virtual network auto-registration enabled is 1. If you need to increase this limit, please contact Azure Support: https://docs.microsoft.com/en-us/azure/azure-subscription-service-limits
    - resolution_vnets -- Space-separated names or IDs of virtual networks that resolve records in this DNS zone.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - zone_type -- Type of DNS zone to create.
    '''
    return _call_az("az network dns zone create", locals())


def update(name, resource_group, add=None, force_string=None, if_match=None, registration_vnets=None, remove=None, resolution_vnets=None, set=None, tags=None, zone_type=None):
    '''
    Update a DNS zone properties. Does not modify DNS records within the zone.

    Required Parameters:
    - name -- The name of the zone.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - if_match -- The etag of the DNS zone. Omit this value to always overwrite the current zone. Specify the last-seen etag value to prevent accidentally overwriting any concurrent changes.
    - registration_vnets -- Space-separated names or IDs of virtual networks that register hostnames in this DNS zone. Number of private DNS zones with virtual network auto-registration enabled is 1. If you need to increase this limit, please contact Azure Support: https://docs.microsoft.com/en-us/azure/azure-subscription-service-limits
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - resolution_vnets -- Space-separated names or IDs of virtual networks that resolve records in this DNS zone.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - zone_type -- Type of DNS zone to create.
    '''
    return _call_az("az network dns zone update", locals())

