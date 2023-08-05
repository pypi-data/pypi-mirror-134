from ..... pyaz_utils import _call_az

def list(resource_group, workspace_name):
    '''
    List all the tables for the given Log Analytics workspace.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- Name of the Log Analytics Workspace.
    '''
    return _call_az("az monitor log-analytics workspace table list", locals())


def show(name, resource_group, workspace_name):
    '''
    Get a Log Analytics workspace table.

    Required Parameters:
    - name -- Name of the table.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- Name of the Log Analytics Workspace.
    '''
    return _call_az("az monitor log-analytics workspace table show", locals())


def update(name, resource_group, retention_time, workspace_name):
    '''
    Update the properties of a Log Analytics workspace table, currently only support updating retention time.

    Required Parameters:
    - name -- Name of the table.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - retention_time -- The data table data retention in days, between 30 and 730. Setting this property to null will default to the workspace
    - workspace_name -- Name of the Log Analytics Workspace.
    '''
    return _call_az("az monitor log-analytics workspace table update", locals())

