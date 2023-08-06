from ..... pyaz_utils import _call_az

def create(name, resource_group, workspace_name, no_wait=None, resource_id=None, write_access_resource_id=None):
    '''
    Create a linked service.

    Required Parameters:
    - name -- Name of the linkedServices resource. Supported values: cluster, automation.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- Name of the Log Analytics Workspace.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_id -- The resource id of the resource that will be linked to the workspace. This should be used for linking resources which require read access.
    - write_access_resource_id -- The resource id of the resource that will be linked to the workspace. This should be used for linking resources which require write access.
    '''
    return _call_az("az monitor log-analytics workspace linked-service create", locals())


def update(name, resource_group, workspace_name, add=None, force_string=None, no_wait=None, remove=None, resource_id=None, set=None, write_access_resource_id=None):
    '''
    Update a linked service.

    Required Parameters:
    - name -- Name of the linkedServices resource. Supported values: cluster, automation.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- Name of the Log Analytics Workspace.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - no_wait -- Do not wait for the long-running operation to finish.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - resource_id -- The resource id of the resource that will be linked to the workspace. This should be used for linking resources which require read access.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - write_access_resource_id -- The resource id of the resource that will be linked to the workspace. This should be used for linking resources which require write access.
    '''
    return _call_az("az monitor log-analytics workspace linked-service update", locals())


def show(name, resource_group, workspace_name):
    '''
    Show the properties of a linked service.

    Required Parameters:
    - name -- Name of the linkedServices resource. Supported values: cluster, automation.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- Name of the Log Analytics Workspace.
    '''
    return _call_az("az monitor log-analytics workspace linked-service show", locals())


def list(resource_group, workspace_name):
    '''
    Gets all the linked services in a workspace.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- Name of the Log Analytics Workspace.
    '''
    return _call_az("az monitor log-analytics workspace linked-service list", locals())


def delete(name, resource_group, workspace_name, no_wait=None, yes=None):
    '''
    Delete a linked service.

    Required Parameters:
    - name -- Name of the linkedServices resource. Supported values: cluster, automation.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- Name of the Log Analytics Workspace.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az monitor log-analytics workspace linked-service delete", locals())


def wait(name, resource_group, workspace_name, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the linked service is met.

    Required Parameters:
    - name -- Name of the linkedServices resource. Supported values: cluster, automation.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- Name of the Log Analytics Workspace.

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az monitor log-analytics workspace linked-service wait", locals())

