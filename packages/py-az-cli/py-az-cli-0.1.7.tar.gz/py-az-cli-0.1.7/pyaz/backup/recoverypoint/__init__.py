'''
A snapshot of data at that point-of-time, stored in Recovery Services Vault, from which you can restore information.
'''
from ... pyaz_utils import _call_az

def show(container_name, item_name, name, resource_group, vault_name, backup_management_type=None, use_secondary_region=None, workload_type=None):
    '''
    Shows details of a particular recovery point.

    Required Parameters:
    - container_name -- Name of the backup container. Accepts 'Name' or 'FriendlyName' from the output of az backup container list command. If 'FriendlyName' is passed then BackupManagementType is required.
    - item_name -- Name of the backed up item.
    - name -- Name of the recovery point. You can use the backup recovery point list command to get the name of a backed up item.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vault_name -- Name of the Recovery services vault.

    Optional Parameters:
    - backup_management_type -- Specify the backup management type. Define how Azure Backup manages the backup of entities within the ARM resource. For eg: AzureWorkloads refers to workloads installed within Azure VMs, AzureStorage refers to entities within Storage account. Required only if friendly name is used as Container name.
    - use_secondary_region -- Use this flag to show recoverypoints in secondary region.
    - workload_type -- Specify the type of applications within the Resource which should be discovered and protected by Azure Backup. 
    '''
    return _call_az("az backup recoverypoint show", locals())


def list(container_name, item_name, resource_group, vault_name, backup_management_type=None, end_date=None, is_ready_for_move=None, recommended_for_archive=None, start_date=None, target_tier=None, tier=None, use_secondary_region=None, workload_type=None):
    '''
    List all recovery points of a backed up item.

    Required Parameters:
    - container_name -- Name of the backup container. Accepts 'Name' or 'FriendlyName' from the output of az backup container list command. If 'FriendlyName' is passed then BackupManagementType is required.
    - item_name -- Name of the backed up item.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vault_name -- Name of the Recovery services vault.

    Optional Parameters:
    - backup_management_type -- Specify the backup management type. Define how Azure Backup manages the backup of entities within the ARM resource. For eg: AzureWorkloads refers to workloads installed within Azure VMs, AzureStorage refers to entities within Storage account. Required only if friendly name is used as Container name.
    - end_date -- The end date of the range in UTC (d-m-Y).
    - is_ready_for_move -- Use this flag to retrieve the recoverypoints that are ready to be moved to destination-tier.
    - recommended_for_archive -- Use this flag to retrieve recommended archivable recoverypoints.
    - start_date -- The start date of the range in UTC (d-m-Y).
    - target_tier --  The destination/target tier to which a particular recovery point has to be moved.
    - tier --  Provide 'tier' parameter to filter recovery points.
    - use_secondary_region -- Use this flag to list recoverypoints in secondary region.
    - workload_type -- Specify the type of applications within the Resource which should be discovered and protected by Azure Backup. 
    '''
    return _call_az("az backup recoverypoint list", locals())


def move(container_name, destination_tier, item_name, name, resource_group, source_tier, vault_name, backup_management_type=None, workload_type=None):
    '''
    Move a particular recovery point of a backed up item from one tier to another tier.

    Required Parameters:
    - container_name -- Name of the backup container. Accepts 'Name' or 'FriendlyName' from the output of az backup container list command. If 'FriendlyName' is passed then BackupManagementType is required.
    - destination_tier --  The destination/target tier to which a particular recovery point has to be moved.
    - item_name -- Name of the backed up item.
    - name -- Name of the recovery point.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - source_tier -- The source tier from which a particular recovery point has to be moved.
    - vault_name -- Name of the Recovery services vault.

    Optional Parameters:
    - backup_management_type -- Specify the backup management type. Define how Azure Backup manages the backup of entities within the ARM resource. For eg: AzureWorkloads refers to workloads installed within Azure VMs, AzureStorage refers to entities within Storage account. Required only if friendly name is used as Container name.
    - workload_type -- Specify the type of applications within the Resource which should be discovered and protected by Azure Backup. 
    '''
    return _call_az("az backup recoverypoint move", locals())


def show_log_chain(container_name, item_name, resource_group, vault_name, backup_management_type=None, end_date=None, start_date=None, use_secondary_region=None, workload_type=None):
    '''
    List the start and end points of the unbroken log chain(s) of the given backup item.

    Required Parameters:
    - container_name -- Name of the backup container. Accepts 'Name' or 'FriendlyName' from the output of az backup container list command. If 'FriendlyName' is passed then BackupManagementType is required.
    - item_name -- Name of the backed up item.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vault_name -- Name of the Recovery services vault.

    Optional Parameters:
    - backup_management_type -- Specify the backup management type. Define how Azure Backup manages the backup of entities within the ARM resource. For eg: AzureWorkloads refers to workloads installed within Azure VMs, AzureStorage refers to entities within Storage account. Required only if friendly name is used as Container name.
    - end_date -- The end date of the range in UTC (d-m-Y).
    - start_date -- The start date of the range in UTC (d-m-Y).
    - use_secondary_region -- Use this flag to list recoverypoints in secondary region.
    - workload_type -- Specify the type of applications within the Resource which should be discovered and protected by Azure Backup. 
    '''
    return _call_az("az backup recoverypoint show-log-chain", locals())

