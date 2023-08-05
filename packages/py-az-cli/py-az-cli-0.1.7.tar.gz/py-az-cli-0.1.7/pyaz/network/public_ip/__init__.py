from ... pyaz_utils import _call_az
from . import prefix


def delete(name, resource_group):
    '''
    Delete a public IP address.

    Required Parameters:
    - name -- The name of the public IP address.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network public-ip delete", locals())


def show(name, resource_group, expand=None):
    '''
    Get the details of a public IP address.

    Required Parameters:
    - name -- The name of the public IP address.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expand -- Expands referenced resources.
    '''
    return _call_az("az network public-ip show", locals())


def list(resource_group=None):
    '''
    List public IP addresses.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network public-ip list", locals())


def create(name, resource_group, allocation_method=None, dns_name=None, edge_zone=None, idle_timeout=None, ip_address=None, ip_tags=None, location=None, public_ip_prefix=None, reverse_fqdn=None, sku=None, tags=None, tier=None, version=None, zone=None):
    '''
    Create a public IP address.

    Required Parameters:
    - name -- The name of the public IP address.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - allocation_method -- IP address allocation method
    - dns_name -- Globally unique DNS entry.
    - edge_zone -- The name of edge zone.
    - idle_timeout -- Idle timeout in minutes.
    - ip_address -- The IP address associated with the public IP address resource.
    - ip_tags -- Space-separated list of IP tags in 'TYPE=VAL' format.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - public_ip_prefix -- Name or ID of a public IP prefix.
    - reverse_fqdn -- Reverse FQDN (fully qualified domain name).
    - sku -- Name of a public IP address SKU
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - tier -- Tier of a public IP address SKU and Global tier is only supported for standard SKU public IP addresses
    - version -- IP address type.
    - zone -- Space-separated list of availability zones into which to provision the resource.
    '''
    return _call_az("az network public-ip create", locals())


def update(name, resource_group, add=None, allocation_method=None, dns_name=None, force_string=None, idle_timeout=None, ip_tags=None, public_ip_prefix=None, remove=None, reverse_fqdn=None, set=None, sku=None, tags=None, version=None):
    '''
    Update a public IP address.

    Required Parameters:
    - name -- The name of the public IP address.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - allocation_method -- IP address allocation method
    - dns_name -- Globally unique DNS entry.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - idle_timeout -- Idle timeout in minutes.
    - ip_tags -- Space-separated list of IP tags in 'TYPE=VAL' format.
    - public_ip_prefix -- Name or ID of a public IP prefix.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - reverse_fqdn -- Reverse FQDN (fully qualified domain name).
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - sku -- Public IP SKU
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - version -- IP address type.
    '''
    return _call_az("az network public-ip update", locals())

