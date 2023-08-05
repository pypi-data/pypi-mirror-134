from ... pyaz_utils import _call_az
from . import connection


def create(lb_frontend_ip_configs, name, resource_group, subnet, auto_approval=None, edge_zone=None, enable_proxy_protocol=None, fqdns=None, lb_name=None, location=None, private_ip_address=None, private_ip_address_version=None, private_ip_allocation_method=None, public_ip_address=None, tags=None, visibility=None, vnet_name=None):
    '''
    Create a private link service.

    Required Parameters:
    - lb_frontend_ip_configs -- Space-separated list of names or IDs of load balancer frontend IP configurations to link to. If names are used, also supply `--lb-name`.
    - name -- Name of the private link service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - subnet -- Name or ID of subnet to use. If name provided, also supply `--vnet-name`.

    Optional Parameters:
    - auto_approval -- Space-separated list of subscription IDs to auto-approve.
    - edge_zone -- The name of edge zone.
    - enable_proxy_protocol -- Enable proxy protocol for private link service.
    - fqdns -- Space-separated list of FQDNs.
    - lb_name -- Name of the load balancer to retrieve frontend IP configs from. Ignored if a frontend IP configuration ID is supplied.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - private_ip_address -- Static private IP address to use.
    - private_ip_address_version -- IP version of the private IP address.
    - private_ip_allocation_method -- Private IP address allocation method
    - public_ip_address -- Name or ID of the a public IP address to use.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - visibility -- Space-separated list of subscription IDs for which the private link service is visible.
    - vnet_name -- The virtual network (VNet) name.
    '''
    return _call_az("az network private-link-service create", locals())


def delete(name, resource_group):
    '''
    Delete a private link service.

    Required Parameters:
    - name -- Name of the private link service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network private-link-service delete", locals())


def list(resource_group=None):
    '''
    List private link services.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network private-link-service list", locals())


def show(name, resource_group, expand=None):
    '''
    Get the details of a private link service.

    Required Parameters:
    - name -- Name of the private link service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expand -- Expands referenced resources.
    '''
    return _call_az("az network private-link-service show", locals())


def update(name, resource_group, add=None, auto_approval=None, enable_proxy_protocol=None, force_string=None, fqdns=None, lb_frontend_ip_configs=None, lb_name=None, remove=None, set=None, tags=None, visibility=None):
    '''
    Update a private link service.

    Required Parameters:
    - name -- Name of the private link service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - auto_approval -- Space-separated list of subscription IDs to auto-approve.
    - enable_proxy_protocol -- Enable proxy protocol for private link service.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - fqdns -- Space-separated list of FQDNs.
    - lb_frontend_ip_configs -- Space-separated list of names or IDs of load balancer frontend IP configurations to link to. If names are used, also supply `--lb-name`.
    - lb_name -- Name of the load balancer to retrieve frontend IP configs from. Ignored if a frontend IP configuration ID is supplied.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - visibility -- Space-separated list of subscription IDs for which the private link service is visible.
    '''
    return _call_az("az network private-link-service update", locals())

