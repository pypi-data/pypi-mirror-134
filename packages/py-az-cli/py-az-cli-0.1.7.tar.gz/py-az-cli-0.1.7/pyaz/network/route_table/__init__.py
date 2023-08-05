from ... pyaz_utils import _call_az
from . import route


def create(name, resource_group, disable_bgp_route_propagation=None, location=None, tags=None):
    '''
    Create a route table.

    Required Parameters:
    - name -- Name of the route table.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - disable_bgp_route_propagation -- Disable routes learned by BGP.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az network route-table create", locals())


def delete(name, resource_group):
    '''
    Delete a route table.

    Required Parameters:
    - name -- Name of the route table.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network route-table delete", locals())


def show(name, resource_group, expand=None):
    '''
    Get the details of a route table.

    Required Parameters:
    - name -- Name of the route table.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expand -- Expands referenced resources.
    '''
    return _call_az("az network route-table show", locals())


def list(resource_group=None):
    '''
    List route tables.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network route-table list", locals())


def update(name, resource_group, add=None, disable_bgp_route_propagation=None, force_string=None, remove=None, set=None, tags=None):
    '''
    Update a route table.

    Required Parameters:
    - name -- Name of the route table.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - disable_bgp_route_propagation -- Disable routes learned by BGP.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az network route-table update", locals())

