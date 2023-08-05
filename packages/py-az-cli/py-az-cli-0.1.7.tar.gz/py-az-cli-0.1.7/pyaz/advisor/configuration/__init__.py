'''
Manage Azure Advisor configuration.
'''
from ... pyaz_utils import _call_az

def list():
    '''
    List Azure Advisor configuration for the entire subscription.
    '''
    return _call_az("az advisor configuration list", locals())


def show(resource_group=None):
    '''
    Show Azure Advisor configuration for the given subscription or resource group.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az advisor configuration show", locals())


def update(add=None, configuration_name=None, exclude=None, force_string=None, include=None, low_cpu_threshold=None, remove=None, resource_group=None, set=None):
    '''
    Update Azure Advisor configuration.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - configuration_name -- Advisor configuration name. Value must be "default"
    - exclude -- Exclude from recommendation generation.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - include -- Include in recommendation generation.
    - low_cpu_threshold -- Value for low CPU threshold.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az advisor configuration update", locals())

