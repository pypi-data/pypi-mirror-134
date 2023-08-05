'''
Manage protection of your items, enable protection or disable it, or take on-demand backups.
'''
from ... pyaz_utils import _call_az

def check_vm(resource_group=None, vm=None, vm_id=None):
    '''
    Find out whether the virtual machine is protected or not. If protected, it returns the recovery services vault ID, otherwise it returns empty.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vm -- Name or ID of the Virtual Machine to be protected.
    - vm_id -- ID of the virtual machine to be checked for protection.
    '''
    return _call_az("az backup protection check-vm", locals())


def enable_for_vm(policy_name, resource_group, vault_name, vm, disk_list_setting=None, diskslist=None, exclude_all_data_disks=None):
    '''
    Start protecting a previously unprotected Azure VM as per the specified policy to a Recovery services vault.

    Required Parameters:
    - policy_name -- Name of the backup policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vault_name -- Name of the Recovery services vault.
    - vm -- Name or ID of the Virtual Machine to be protected.

    Optional Parameters:
    - disk_list_setting -- option to decide whether to include or exclude the disk or reset any previous settings to default behavior
    - diskslist -- List of disks to be excluded or included.
    - exclude_all_data_disks -- Option to specify to backup OS disk only.
    '''
    return _call_az("az backup protection enable-for-vm", locals())


def update_for_vm(container_name, item_name, resource_group, vault_name, disk_list_setting=None, diskslist=None, exclude_all_data_disks=None):
    '''
    Update disk exclusion settings associated with a backed up VM item.

    Required Parameters:
    - container_name -- Name of the backup container. Accepts 'Name' or 'FriendlyName' from the output of az backup container list command. If 'FriendlyName' is passed then BackupManagementType is required.
    - item_name -- Name of the backed up item.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vault_name -- Name of the Recovery services vault.

    Optional Parameters:
    - disk_list_setting -- option to decide whether to include or exclude the disk or reset any previous settings to default behavior
    - diskslist -- List of disks to be excluded or included.
    - exclude_all_data_disks -- Option to specify to backup OS disk only.
    '''
    return _call_az("az backup protection update-for-vm", locals())


def backup_now(item_name, resource_group, vault_name, backup_management_type=None, backup_type=None, container_name=None, enable_compression=None, retain_until=None, workload_type=None):
    '''
    Perform an on-demand backup of a backed up item.

    Required Parameters:
    - item_name -- Name of the backed up item.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vault_name -- Name of the Recovery services vault.

    Optional Parameters:
    - backup_management_type -- Specify the backup management type. Define how Azure Backup manages the backup of entities within the ARM resource. For eg: AzureWorkloads refers to workloads installed within Azure VMs, AzureStorage refers to entities within Storage account. Required only if friendly name is used as Container name.
    - backup_type -- 'Full, Differential, Log, CopyOnlyFull' for backup Item type 'MSSQL'. 'Full, Differential' for backup item type 'SAPHANA'.
    - container_name -- Name of the backup container. Accepts 'Name' or 'FriendlyName' from the output of az backup container list command. If 'FriendlyName' is passed then BackupManagementType is required.
    - enable_compression -- Option to enable compression
    - retain_until -- The date until which this backed up copy will be available for retrieval, in UTC (d-m-Y). For SQL workload, retain-until can only be specified for backup-type 'CopyOnlyFull'. For HANA workload, user can't specify the value for retain-until. If not specified, 30 days will be taken as default value or as decided by service.
    - workload_type -- Specify the type of applications within the Resource which should be discovered and protected by Azure Backup. 
    '''
    return _call_az("az backup protection backup-now", locals())


def disable(container_name, item_name, resource_group, vault_name, backup_management_type=None, delete_backup_data=None, workload_type=None, yes=None):
    '''
    Stop protecting a backed up item. Can retain the backed up data forever or choose to delete it.

    Required Parameters:
    - container_name -- Name of the backup container. Accepts 'Name' or 'FriendlyName' from the output of az backup container list command. If 'FriendlyName' is passed then BackupManagementType is required.
    - item_name -- Name of the backed up item.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vault_name -- Name of the Recovery services vault.

    Optional Parameters:
    - backup_management_type -- Specify the backup management type. Define how Azure Backup manages the backup of entities within the ARM resource. For eg: AzureWorkloads refers to workloads installed within Azure VMs, AzureStorage refers to entities within Storage account. Required only if friendly name is used as Container name.
    - delete_backup_data -- Option to delete existing backed up data in the Recovery services vault.
    - workload_type -- Specify the type of applications within the Resource which should be discovered and protected by Azure Backup. 
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az backup protection disable", locals())


def enable_for_azurefileshare(azure_file_share, policy_name, resource_group, storage_account, vault_name):
    '''
    Start protecting a previously unprotected Azure File share within an Azure Storage account as per the specified policy to a Recovery services vault.

    Required Parameters:
    - azure_file_share -- Name of the Azure FileShare.
    - policy_name -- Name of the backup policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - storage_account -- Name of the Storage Account of the FileShare.
    - vault_name -- Name of the Recovery services vault.
    '''
    return _call_az("az backup protection enable-for-azurefileshare", locals())


def enable_for_azurewl(policy_name, protectable_item_name, protectable_item_type, resource_group, server_name, vault_name, workload_type):
    '''
    Start protecting a previously unprotected workload within an Azure VM as per the specified policy to a Recovery services vault. Provide the workload details as a protectable item.

    Required Parameters:
    - policy_name -- Name of the backup policy.
    - protectable_item_name -- Specify the resource name to be protected by Azure Backup service.
    - protectable_item_type -- Specify the type of applications within the Resource which should be discovered and protected by Azure Backup. 
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Parent Server name of the item.
    - vault_name -- Name of the Recovery services vault.
    - workload_type -- Specify the type of applications within the Resource which should be discovered and protected by Azure Backup. 
    '''
    return _call_az("az backup protection enable-for-azurewl", locals())


def auto_enable_for_azurewl(policy_name, protectable_item_name, protectable_item_type, resource_group, server_name, vault_name, workload_type):
    '''
    Automatically protect all existing unprotected DBs and any DB which will be added later with the given policy.

    Required Parameters:
    - policy_name -- Name of the backup policy.
    - protectable_item_name -- Specify the resource name to be protected by Azure Backup service.
    - protectable_item_type -- Specify the type of applications within the Resource which should be discovered and protected by Azure Backup. 
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Parent Server name of the item.
    - vault_name -- Name of the Recovery services vault.
    - workload_type -- Specify the type of applications within the Resource which should be discovered and protected by Azure Backup. 
    '''
    return _call_az("az backup protection auto-enable-for-azurewl", locals())


def auto_disable_for_azurewl(protectable_item_name, protectable_item_type, resource_group, server_name, vault_name, workload_type):
    '''
    Disable auto-protection for the specified protectable item.

    Required Parameters:
    - protectable_item_name -- Specify the resource name to be protected by Azure Backup service.
    - protectable_item_type -- Specify the type of applications within the Resource which should be discovered and protected by Azure Backup. 
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Parent Server name of the item.
    - vault_name -- Name of the Recovery services vault.
    - workload_type -- Specify the type of applications within the Resource which should be discovered and protected by Azure Backup. 
    '''
    return _call_az("az backup protection auto-disable-for-azurewl", locals())


def resume(container_name, item_name, policy_name, resource_group, vault_name, backup_management_type=None, workload_type=None):
    '''
    Resume backup for the associated backup item. Use this to change the policy associated with the backup item.

    Required Parameters:
    - container_name -- Name of the backup container. Accepts 'Name' or 'FriendlyName' from the output of az backup container list command. If 'FriendlyName' is passed then BackupManagementType is required.
    - item_name -- Name of the backed up item.
    - policy_name -- Name of the backup policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vault_name -- Name of the Recovery services vault.

    Optional Parameters:
    - backup_management_type -- Specify the backup management type. Define how Azure Backup manages the backup of entities within the ARM resource. For eg: AzureWorkloads refers to workloads installed within Azure VMs, AzureStorage refers to entities within Storage account. Required only if friendly name is used as Container name.
    - workload_type -- Specify the type of applications within the Resource which should be discovered and protected by Azure Backup. 
    '''
    return _call_az("az backup protection resume", locals())


def undelete(container_name, item_name, resource_group, vault_name, backup_management_type=None, workload_type=None):
    '''
    Rehydrate an item from softdeleted state to stop protection with retained data state.

    Required Parameters:
    - container_name -- Name of the backup container. Accepts 'Name' or 'FriendlyName' from the output of az backup container list command. If 'FriendlyName' is passed then BackupManagementType is required.
    - item_name -- Name of the backed up item.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vault_name -- Name of the Recovery services vault.

    Optional Parameters:
    - backup_management_type -- Specify the backup management type. Define how Azure Backup manages the backup of entities within the ARM resource. For eg: AzureWorkloads refers to workloads installed within Azure VMs, AzureStorage refers to entities within Storage account. Required only if friendly name is used as Container name.
    - workload_type -- Specify the type of applications within the Resource which should be discovered and protected by Azure Backup. 
    '''
    return _call_az("az backup protection undelete", locals())

