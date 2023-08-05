from ..... pyaz_utils import _call_az

def list(resource_group, workspace_name):
    '''
    List all data export ruleses for a given workspace.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- Name of the Log Analytics Workspace.
    '''
    return _call_az("az monitor log-analytics workspace data-export list", locals())


def show(name, resource_group, workspace_name):
    '''
    Show a data export rule for a given workspace.

    Required Parameters:
    - name -- Name of the data export rule
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- Name of the Log Analytics Workspace.
    '''
    return _call_az("az monitor log-analytics workspace data-export show", locals())


def create(destination, name, resource_group, tables, workspace_name, enable=None):
    '''
    Create a data export rule for a given workspace.

    Required Parameters:
    - destination -- The destination resource ID. It should be a storage account, an event hub namespace or an event hub. If event hub namespace is provided, event hub would be created for each table automatically.
    - name -- Name of the data export rule
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - tables -- An array of tables to export.
    - workspace_name -- Name of the Log Analytics Workspace.

    Optional Parameters:
    - enable -- Enable this data export rule.
    '''
    return _call_az("az monitor log-analytics workspace data-export create", locals())


def update(name, resource_group, tables, workspace_name, add=None, destination=None, enable=None, force_string=None, remove=None, set=None):
    '''
    Update a data export rule for a given workspace.

    Required Parameters:
    - name -- Name of the data export rule
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - tables -- An array of tables to export.
    - workspace_name -- Name of the Log Analytics Workspace.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - destination -- The destination resource ID. It should be a storage account, an event hub namespace or an event hub. If event hub namespace is provided, event hub would be created for each table automatically.
    - enable -- Enable this data export rule.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az monitor log-analytics workspace data-export update", locals())


def delete(name, resource_group, workspace_name, yes=None):
    '''
    Delete a data export rule for a given workspace.

    Required Parameters:
    - name -- Name of the data export rule
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- Name of the Log Analytics Workspace.

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az monitor log-analytics workspace data-export delete", locals())

