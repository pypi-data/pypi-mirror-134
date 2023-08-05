'''
Manage recovery configuration of an Azure workload backed up item.
'''
from ... pyaz_utils import _call_az

def show(container_name, item_name, resource_group, restore_mode, vault_name, backup_management_type=None, filepath=None, from_full_rp_name=None, log_point_in_time=None, rp_name=None, target_container_name=None, target_item_name=None, target_resource_group=None, target_server_name=None, target_server_type=None, target_vault_name=None, workload_type=None):
    '''
    Construct the recovery configuration of an Azure workload backed up item.

    Required Parameters:
    - container_name -- Name of the backup container. Accepts 'Name' or 'FriendlyName' from the output of az backup container list command. If 'FriendlyName' is passed then BackupManagementType is required.
    - item_name -- Name of the backed up item.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - restore_mode -- Specify the restore mode.
    - vault_name -- Name of the Recovery services vault.

    Optional Parameters:
    - backup_management_type -- Specify the backup management type. Define how Azure Backup manages the backup of entities within the ARM resource. For eg: AzureWorkloads refers to workloads installed within Azure VMs, AzureStorage refers to entities within Storage account. Required only if friendly name is used as Container name.
    - filepath -- The path to which the DB should be restored as files.
    - from_full_rp_name -- Name of the starting Recovery point.
    - log_point_in_time -- Specify the point-in-time which will be restored.
    - rp_name -- Name of the recovery point.
    - target_container_name -- The target container to which the DB recovery point should be downloaded as files.
    - target_item_name -- Specify the target item name for the restore operation.
    - target_resource_group -- Specify the resource group of target item for Cross Region Restore. Default value will be same as --resource-group if not specified.
    - target_server_name -- Specify the parent server name of the target item.
    - target_server_type -- Specify the type of the server which should be discovered.
    - target_vault_name -- Specify the vault name of target item for Cross Region Restore. Default value will be same as --vault-name if not specified.
    - workload_type -- Specify the type of applications within the Resource which should be discovered and protected by Azure Backup. 
    '''
    return _call_az("az backup recoveryconfig show", locals())

