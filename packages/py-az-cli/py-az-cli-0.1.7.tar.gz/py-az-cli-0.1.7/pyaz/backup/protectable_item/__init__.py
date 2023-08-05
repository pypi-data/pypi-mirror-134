from ... pyaz_utils import _call_az

def show(name, protectable_item_type, resource_group, server_name, vault_name, workload_type):
    '''
    Retrieve the specified protectable item within the given container.

    Required Parameters:
    - name -- Name of the protectable item.
    - protectable_item_type -- Specify the type of applications within the Resource which should be discovered and protected by Azure Backup. 
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Parent Server name of the item.
    - vault_name -- Name of the Recovery services vault.
    - workload_type -- Specify the type of applications within the Resource which should be discovered and protected by Azure Backup. 
    '''
    return _call_az("az backup protectable-item show", locals())


def list(resource_group, vault_name, workload_type, backup_management_type=None, container_name=None, protectable_item_type=None, server_name=None):
    '''
    Retrieve all protectable items within a certain container or across all registered containers.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vault_name -- Name of the Recovery services vault.
    - workload_type -- Specify the type of applications within the Resource which should be discovered and protected by Azure Backup. 

    Optional Parameters:
    - backup_management_type -- Specify the backup management type. Define how Azure Backup manages the backup of entities within the ARM resource. For eg: AzureWorkloads refers to workloads installed within Azure VMs, AzureStorage refers to entities within Storage account. Required only if friendly name is used as Container name.
    - container_name -- Name of the backup container. Accepts 'Name' or 'FriendlyName' from the output of az backup container list command. If 'FriendlyName' is passed then BackupManagementType is required.
    - protectable_item_type -- Specify the type of applications within the Resource which should be discovered and protected by Azure Backup. 
    - server_name -- Parent Server name of the item.
    '''
    return _call_az("az backup protectable-item list", locals())


def initialize(container_name, resource_group, vault_name, workload_type):
    '''
    Trigger the discovery of any unprotected items of the given workload type in the given container.

    Required Parameters:
    - container_name -- Name of the backup container. Accepts 'Name' or 'FriendlyName' from the output of az backup container list command. If 'FriendlyName' is passed then BackupManagementType is required.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vault_name -- Name of the Recovery services vault.
    - workload_type -- Specify the type of applications within the Resource which should be discovered and protected by Azure Backup. 
    '''
    return _call_az("az backup protectable-item initialize", locals())

