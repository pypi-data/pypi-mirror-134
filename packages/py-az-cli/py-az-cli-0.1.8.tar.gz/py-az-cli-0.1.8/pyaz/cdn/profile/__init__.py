'''
Manage CDN profiles to define an edge network.
'''
from ... pyaz_utils import _call_az

def show(name, resource_group):
    '''
    Show CDN profile details.

    Required Parameters:
    - name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cdn profile show", locals())


def usage(name, resource_group):
    '''
    

    Required Parameters:
    - name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cdn profile usage", locals())


def delete(name, resource_group):
    '''
    Delete a CDN profile.

    Required Parameters:
    - name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cdn profile delete", locals())


def list(resource_group=None):
    '''
    List CDN profiles.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cdn profile list", locals())


def create(name, resource_group, location=None, sku=None, tags=None):
    '''
    Create a new CDN profile.

    Required Parameters:
    - name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - sku -- None
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az cdn profile create", locals())


def update(name, resource_group, add=None, force_string=None, remove=None, set=None, tags=None):
    '''
    Update a CDN profile.

    Required Parameters:
    - name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az cdn profile update", locals())

