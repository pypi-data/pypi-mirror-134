'''
Manage Proximity Placement Groups
'''
from .. pyaz_utils import _call_az

def show(name, resource_group, include_colocation_status=None):
    '''
    Get a proximity placement group

    Required Parameters:
    - name -- The name of the proximity placement group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - include_colocation_status -- Enable fetching the colocation status of all the resources in the proximity placement group.
    '''
    return _call_az("az ppg show", locals())


def create(name, resource_group, location=None, tags=None, type=None):
    '''
    Create a proximity placement group

    Required Parameters:
    - name -- The name of the proximity placement group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - type -- The type of the proximity placement group. Allowed values: Standard.
    '''
    return _call_az("az ppg create", locals())


def list(resource_group=None):
    '''
    List proximity placement groups

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ppg list", locals())


def update(name, resource_group, add=None, force_string=None, include_colocation_status=None, remove=None, set=None):
    '''
    Update a proximity placement group

    Required Parameters:
    - name -- The name of the proximity placement group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - include_colocation_status -- includeColocationStatus=true enables fetching the colocation status of all the resources in the proximity placement group.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az ppg update", locals())


def delete(name, resource_group):
    '''
    

    Required Parameters:
    - name -- The name of the proximity placement group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ppg delete", locals())

