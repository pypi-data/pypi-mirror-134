from ... pyaz_utils import _call_az
from . import dns_zone_group


def create(connection_name, name, private_connection_resource_id, resource_group, subnet, edge_zone=None, group_id=None, location=None, manual_request=None, request_message=None, tags=None, vnet_name=None):
    '''
    Create a private endpoint.

    Required Parameters:
    - connection_name -- Name of the private link service connection.
    - name -- Name of the private endpoint.
    - private_connection_resource_id -- The resource id of the private endpoint to connect to
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - subnet -- Name or ID of an existing subnet. If name specified, also specify --vnet-name. If you want to use an existing subnet in other resource group or subscription, please provide the ID instead of the name of the subnet and do not specify the --vnet-name

    Optional Parameters:
    - edge_zone -- The name of edge zone.
    - group_id -- The ID of the group obtained from the remote resource that this private endpoint should connect to. You can use "az network private-link-resource list" to obtain the supported group ids. You must provide this except for PrivateLinkService
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - manual_request -- Use manual request to establish the connection. Configure it as 'true' when you don't have access to the subscription of private link service.
    - request_message -- A message passed to the owner of the remote resource with this connection request. Restricted to 140 chars.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - vnet_name -- The virtual network (VNet) associated with the subnet (Omit if supplying a subnet id).
    '''
    return _call_az("az network private-endpoint create", locals())


def delete(name, resource_group):
    '''
    Delete a private endpoint.

    Required Parameters:
    - name -- Name of the private endpoint.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network private-endpoint delete", locals())


def list(resource_group=None):
    '''
    List private endpoints.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network private-endpoint list", locals())


def show(name, resource_group):
    '''
    Get the details of a private endpoint.

    Required Parameters:
    - name -- Name of the private endpoint.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network private-endpoint show", locals())


def update(name, resource_group, add=None, force_string=None, remove=None, request_message=None, set=None, tags=None):
    '''
    Update a private endpoint.

    Required Parameters:
    - name -- Name of the private endpoint.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - request_message -- A message passed to the owner of the remote resource with this connection request. Restricted to 140 chars.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az network private-endpoint update", locals())


def list_types(location):
    '''
    

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    '''
    return _call_az("az network private-endpoint list-types", locals())

