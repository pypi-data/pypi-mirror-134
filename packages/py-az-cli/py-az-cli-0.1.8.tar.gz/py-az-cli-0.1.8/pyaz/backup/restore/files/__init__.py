'''
Gives access to all files of a recovery point.
'''
from .... pyaz_utils import _call_az

def mount_rp(container_name, item_name, resource_group, rp_name, vault_name):
    '''
    Download a script which mounts files of a recovery point.

    Required Parameters:
    - container_name -- Name of the backup container. Accepts 'Name' or 'FriendlyName' from the output of az backup container list command. If 'FriendlyName' is passed then BackupManagementType is required.
    - item_name -- Name of the backed up item.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rp_name -- Name of the recovery point.
    - vault_name -- Name of the Recovery services vault.
    '''
    return _call_az("az backup restore files mount-rp", locals())


def unmount_rp(container_name, item_name, resource_group, rp_name, vault_name):
    '''
    Close access to the recovery point.

    Required Parameters:
    - container_name -- Name of the backup container. Accepts 'Name' or 'FriendlyName' from the output of az backup container list command. If 'FriendlyName' is passed then BackupManagementType is required.
    - item_name -- Name of the backed up item.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rp_name -- Name of the recovery point.
    - vault_name -- Name of the Recovery services vault.
    '''
    return _call_az("az backup restore files unmount-rp", locals())

