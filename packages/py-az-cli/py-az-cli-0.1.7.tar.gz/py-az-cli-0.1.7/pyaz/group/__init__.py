'''
Manage resource groups and template deployments.
'''
from .. pyaz_utils import _call_az
from . import deployment, lock


def delete(name, force_deletion_types=None, no_wait=None, yes=None):
    '''
    Delete a resource group.

    Required Parameters:
    - name -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - force_deletion_types -- The resource types you want to force delete. Currently, only the following is supported: forceDeletionTypes=Microsoft.Compute/virtualMachines,Microsoft.Compute/virtualMachineScaleSets.
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az group delete", locals())


def show(name):
    '''
    

    Required Parameters:
    - name -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az group show", locals())


def exists(name):
    '''
    Check if a resource group exists.

    Required Parameters:
    - name -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az group exists", locals())


def list(tag=None):
    '''
    List resource groups.

    Optional Parameters:
    - tag -- a single tag in 'key[=value]' format. Use '' to clear existing tags.
    '''
    return _call_az("az group list", locals())


def create(location, name, managed_by=None, tags=None):
    '''
    Create a new resource group.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- name of the new resource group

    Optional Parameters:
    - managed_by -- The ID of the resource that manages this resource group.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az group create", locals())


def export(name, include_comments=None, include_parameter_default_value=None, resource_ids=None, skip_all_params=None, skip_resource_name_params=None):
    '''
    

    Required Parameters:
    - name -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - include_comments -- export template with comments.
    - include_parameter_default_value -- export template parameter with default value.
    - resource_ids -- space-separated resource ids to filter the export by. To export all resources, do not specify this argument or supply "*".
    - skip_all_params -- export template parameter and skip all parameterization.
    - skip_resource_name_params -- export template and skip resource name parameterization.
    '''
    return _call_az("az group export", locals())


def update(name, add=None, force_string=None, remove=None, set=None, tags=None):
    '''
    Update a resource group.

    Required Parameters:
    - name -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az group update", locals())


def wait(name, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the resource group is met.

    Required Parameters:
    - name -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az group wait", locals())

