'''
Manage Azure Network Security Groups (NSGs).
'''
from ... pyaz_utils import _call_az
from . import rule


def delete(name, resource_group):
    '''
    Delete a network security group.

    Required Parameters:
    - name -- Name of the network security group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network nsg delete", locals())


def show(name, resource_group, expand=None):
    '''
    Get information about a network security group.

    Required Parameters:
    - name -- Name of the network security group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expand -- Expands referenced resources.
    '''
    return _call_az("az network nsg show", locals())


def list(resource_group=None):
    '''
    List network security groups.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network nsg list", locals())


def create(name, resource_group, location=None, tags=None):
    '''
    Create a network security group.

    Required Parameters:
    - name -- Name of the network security group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az network nsg create", locals())


def update(name, resource_group, add=None, force_string=None, remove=None, set=None):
    '''
    Update a network security group.

    Required Parameters:
    - name -- Name of the network security group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az network nsg update", locals())

