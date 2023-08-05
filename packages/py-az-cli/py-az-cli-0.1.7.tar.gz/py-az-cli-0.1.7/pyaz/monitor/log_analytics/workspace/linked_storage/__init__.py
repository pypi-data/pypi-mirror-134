from ..... pyaz_utils import _call_az

def create(resource_group, storage_accounts, type, workspace_name):
    '''
    Create some linked storage accounts for log analytics workspace.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - storage_accounts -- List of Name or ID of Azure Storage Account.
    - type -- Data source type for the linked storage account.
    - workspace_name -- Name of the Log Analytics Workspace.
    '''
    return _call_az("az monitor log-analytics workspace linked-storage create", locals())


def add(resource_group, storage_accounts, type, workspace_name):
    '''
    Add some linked storage accounts with specific data source type for log analytics workspace.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - storage_accounts -- List of Name or ID of Azure Storage Account.
    - type -- Data source type for the linked storage account.
    - workspace_name -- Name of the Log Analytics Workspace.
    '''
    return _call_az("az monitor log-analytics workspace linked-storage add", locals())


def remove(resource_group, storage_accounts, type, workspace_name):
    '''
    Remove some linked storage accounts with specific data source type for log analytics workspace

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - storage_accounts -- List of Name or ID of Azure Storage Account.
    - type -- Data source type for the linked storage account.
    - workspace_name -- Name of the Log Analytics Workspace.
    '''
    return _call_az("az monitor log-analytics workspace linked-storage remove", locals())


def delete(resource_group, type, workspace_name, yes=None):
    '''
    Delete all linked storage accounts with specific data source type for log analytics workspace.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - type -- Data source type for the linked storage account.
    - workspace_name -- Name of the Log Analytics Workspace.

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az monitor log-analytics workspace linked-storage delete", locals())


def show(resource_group, type, workspace_name):
    '''
    List all linked storage accounts with specific data source type for a log analytics workspace.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - type -- Data source type for the linked storage account.
    - workspace_name -- Name of the Log Analytics Workspace.
    '''
    return _call_az("az monitor log-analytics workspace linked-storage show", locals())


def list(resource_group, workspace_name):
    '''
    List all linked storage accounts for a log analytics workspace.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- Name of the Log Analytics Workspace.
    '''
    return _call_az("az monitor log-analytics workspace linked-storage list", locals())

