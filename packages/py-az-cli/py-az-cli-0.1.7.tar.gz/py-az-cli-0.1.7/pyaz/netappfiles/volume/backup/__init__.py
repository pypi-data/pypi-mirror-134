'''
Manage Azure NetApp Files (ANF) Volume Backup Resources.
'''
from .... pyaz_utils import _call_az

def show(account_name, backup_name, pool_name, resource_group, volume_name):
    '''
    Get the specified ANF Backup.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - backup_name -- The name of the backup.
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - volume_name -- Name of the ANF volume.
    '''
    return _call_az("az netappfiles volume backup show", locals())


def list(account_name, pool_name, resource_group, volume_name):
    '''
    List the ANF Backups for the specified volume.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - volume_name -- Name of the ANF volume.
    '''
    return _call_az("az netappfiles volume backup list", locals())


def delete(account_name, backup_name, pool_name, resource_group, volume_name):
    '''
    

    Required Parameters:
    - account_name -- Name of the ANF account.
    - backup_name -- The name of the backup.
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - volume_name -- Name of the ANF volume.
    '''
    return _call_az("az netappfiles volume backup delete", locals())


def status(account_name, pool_name, resource_group, volume_name):
    '''
    Get backup status of the specified ANF Volume.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - volume_name -- Name of the ANF volume.
    '''
    return _call_az("az netappfiles volume backup status", locals())


def restore_status(account_name, pool_name, resource_group, volume_name):
    '''
    Get backup restore status of the specified ANF Volume.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - volume_name -- Name of the ANF volume.
    '''
    return _call_az("az netappfiles volume backup restore-status", locals())


def update(account_name, backup_name, pool_name, resource_group, volume_name, label=None, tags=None, use_existing_snapshot=None):
    '''
    Update the specified ANF backup with the values provided.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - backup_name -- None
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - volume_name -- Name of the ANF volume.

    Optional Parameters:
    - label -- Label for backup.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - use_existing_snapshot -- Manual backup an already existing snapshot. This will always be false for scheduled backups and true/false for manual backups.
    '''
    return _call_az("az netappfiles volume backup update", locals())


def create(account_name, backup_name, location, pool_name, resource_group, volume_name, use_existing_snapshot=None):
    '''
    Create specified ANF volume backup.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - backup_name -- None
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - volume_name -- Name of the ANF volume.

    Optional Parameters:
    - use_existing_snapshot -- Manual backup an already existing snapshot. This will always be false for scheduled backups and true/false for manual backups.
    '''
    return _call_az("az netappfiles volume backup create", locals())

