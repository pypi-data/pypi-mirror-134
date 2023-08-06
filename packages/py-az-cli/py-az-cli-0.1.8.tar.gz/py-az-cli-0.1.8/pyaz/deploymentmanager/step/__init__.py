'''
Manage the steps.
'''
from ... pyaz_utils import _call_az

def create(resource_group, duration=None, location=None, step=None, step_name=None, tags=None):
    '''
    Creates the step.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - duration -- The duration of the wait step in ISO 8601 format.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - step -- The step object, specify either the path to a json file or provide a json string that forms the step resource. The json is expected to be of the same format as the output of the relevant `az deploymentmanager step show` command
    - step_name -- The name of the step
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az deploymentmanager step create", locals())


def delete(resource_group, step_name):
    '''
    

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - step_name -- The name of the step
    '''
    return _call_az("az deploymentmanager step delete", locals())


def show(resource_group, step_name):
    '''
    Get the details of the step.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - step_name -- The name of the step
    '''
    return _call_az("az deploymentmanager step show", locals())


def list(resource_group):
    '''
    List all steps in a resource group.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az deploymentmanager step list", locals())


def update(resource_group, step_name, add=None, duration=None, force_string=None, remove=None, set=None, step=None, tags=None):
    '''
    Updates the step.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - step_name -- The name of the step

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - duration -- The duration of the wait step in ISO 8601 format.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - step -- The step object, specify either the path to a json file or provide a json string that forms the step resource. The json is expected to be of the same format as the output of the relevant `az deploymentmanager step show` command
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az deploymentmanager step update", locals())

