'''
Manage the virtual router. This feature supports both VirtualHub and VirtualRouter. Considering VirtualRouter is deprecated, we recommend to create VirtualRouter with --hosted-subnet instead
'''
from ... pyaz_utils import _call_az
from . import peering


def create(name, resource_group, hosted_gateway=None, hosted_subnet=None, location=None, tags=None):
    '''
    Create a virtual router.

    Required Parameters:
    - name -- The name of the Virtual Router.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - hosted_gateway -- Name or ID of the virtual network gateway with ExpressRouter on which VirtualRouter is hosted.
    - hosted_subnet -- The ID of a subnet where VirtualRouter would be deployed
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az network vrouter create", locals())


def update(name, resource_group, add=None, force_string=None, remove=None, set=None, tags=None):
    '''
    Update a virtual router.

    Required Parameters:
    - name -- The name of the Virtual Router.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az network vrouter update", locals())


def delete(name, resource_group):
    '''
    Delete a virtual router under a resource group.

    Required Parameters:
    - name -- The name of the Virtual Router.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network vrouter delete", locals())


def show(name, resource_group):
    '''
    Show a virtual router.

    Required Parameters:
    - name -- The name of the Virtual Router.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network vrouter show", locals())


def list(resource_group=None):
    '''
    List all virtual routers under a subscription or a resource group.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network vrouter list", locals())

