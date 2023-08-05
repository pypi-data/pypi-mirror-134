'''
Restore backed up items from recovery points in a Recovery Services vault.
'''
from ... pyaz_utils import _call_az
from . import files


def restore_disks(container_name, item_name, resource_group, rp_name, storage_account, vault_name, disk_encryption_set_id=None, diskslist=None, mi_system_assigned=None, mi_user_assigned=None, rehydration_duration=None, rehydration_priority=None, restore_as_unmanaged_disks=None, restore_only_osdisk=None, restore_to_staging_storage_account=None, target_resource_group=None, target_zone=None, use_secondary_region=None):
    '''
    Restore disks of the backed VM from the specified recovery point.

    Required Parameters:
    - container_name -- Name of the backup container. Accepts 'Name' or 'FriendlyName' from the output of az backup container list command. If 'FriendlyName' is passed then BackupManagementType is required.
    - item_name -- Name of the backed up item.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rp_name -- Name of the recovery point.
    - storage_account -- Name or ID of the staging storage account. The VM configuration will be restored to this storage account. See the help for --restore-to-staging-storage-account parameter for more info.
    - vault_name -- Name of the Recovery services vault.

    Optional Parameters:
    - disk_encryption_set_id -- The disk encryption set id is used for encrypting restored disks. Please ensure access to disk encryption set id that is specified here.
    - diskslist -- List of disks to be excluded or included.
    - mi_system_assigned -- Use this flag to specify whether a system-assigned managed identity should be used for the restore operation. MI option is not applicable for restoring unmanaged disks.
    - mi_user_assigned -- ARM ID of the user-assigned managed identity to use for the restore operation. Specify a value for this parameter if you do not want to use a system-assigned MI for restoring the backup item.
    - rehydration_duration -- Set the maximum time, in days (between 10-30, both inclusive) for which the recovery point stays in hydrated state.
    - rehydration_priority -- The type of priority to be maintained while rehydrating a recovery point 
    - restore_as_unmanaged_disks -- Use this flag to specify to restore as unmanaged disks
    - restore_only_osdisk -- Use this flag to restore only OS disks of a backed up VM.
    - restore_to_staging_storage_account -- Use this flag when you want disks to be restored to the staging storage account using the --storage-account parameter. When not specified, disks will be restored to their original storage accounts. Default: false.
    - target_resource_group -- Use this to specify the target resource group in which the restored disks will be saved
    - target_zone -- A primary region currently can have three Azure availability zones. Use this argument to specify the target zone number while doing Cross Zonal Restore.
    - use_secondary_region -- Use this flag to restore from a recoverypoint in secondary region.
    '''
    return _call_az("az backup restore restore-disks", locals())


def restore_azurefileshare(container_name, item_name, resolve_conflict, resource_group, restore_mode, rp_name, vault_name, target_file_share=None, target_folder=None, target_storage_account=None):
    '''
    Restore backed up Azure file shares to the same file-share or another file-share in registered storage accounts.

    Required Parameters:
    - container_name -- Name of the backup container. Accepts 'Name' or 'FriendlyName' from the output of az backup container list command. If 'FriendlyName' is passed then BackupManagementType is required.
    - item_name -- Name of the backed up item.
    - resolve_conflict -- Instruction if there's a conflict with the restored data.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - restore_mode -- Specify the restore mode.
    - rp_name -- Name of the recovery point.
    - vault_name -- Name of the Recovery services vault.

    Optional Parameters:
    - target_file_share -- Destination file share to which content will be restored
    - target_folder -- Destination folder to which content will be restored. To restore content to root , leave the folder name empty
    - target_storage_account -- Destination storage account to which content will be restored
    '''
    return _call_az("az backup restore restore-azurefileshare", locals())


def restore_azurefiles(container_name, item_name, resolve_conflict, resource_group, restore_mode, rp_name, vault_name, source_file_path=None, source_file_type=None, target_file_share=None, target_folder=None, target_storage_account=None):
    '''
    Restore backed up Azure files within a file-share to the same file-share or another file-share in registered storage accounts.

    Required Parameters:
    - container_name -- Name of the backup container. Accepts 'Name' or 'FriendlyName' from the output of az backup container list command. If 'FriendlyName' is passed then BackupManagementType is required.
    - item_name -- Name of the backed up item.
    - resolve_conflict -- Instruction if there's a conflict with the restored data.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - restore_mode -- Specify the restore mode.
    - rp_name -- Name of the recovery point.
    - vault_name -- Name of the Recovery services vault.

    Optional Parameters:
    - source_file_path -- The absolute path of the file, to be restored within the file share, as a string. This path is the same path used in the 'az storage file download' or 'az storage file show' CLI commands.
    - source_file_type -- Specify the source file type to be selected
    - target_file_share -- Destination file share to which content will be restored
    - target_folder -- Destination folder to which content will be restored. To restore content to root , leave the folder name empty
    - target_storage_account -- Destination storage account to which content will be restored
    '''
    return _call_az("az backup restore restore-azurefiles", locals())


def restore_azurewl(recovery_config, resource_group, vault_name, rehydration_duration=None, rehydration_priority=None, use_secondary_region=None):
    '''
    Restore backed up Azure Workloads in a Recovery services vault to another registered container or to the same container.

    Required Parameters:
    - recovery_config -- Specify the recovery configuration of a backed up item. The configuration object can be obtained from 'backup recoveryconfig show' command.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vault_name -- Name of the Recovery services vault.

    Optional Parameters:
    - rehydration_duration -- Set the maximum time, in days (between 10-30, both inclusive) for which the recovery point stays in hydrated state.
    - rehydration_priority -- The type of priority to be maintained while rehydrating a recovery point 
    - use_secondary_region -- Use this flag to restore from a recoverypoint in secondary region.
    '''
    return _call_az("az backup restore restore-azurewl", locals())

