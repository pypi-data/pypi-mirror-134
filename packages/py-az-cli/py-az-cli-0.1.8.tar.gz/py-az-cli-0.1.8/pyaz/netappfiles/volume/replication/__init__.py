'''
Manage Azure NetApp Files (ANF) Volume replication operations.
'''
from .... pyaz_utils import _call_az

def approve(account_name, pool_name, resource_group, volume_name, remote_volume_resource_id=None):
    '''
    Authorize a volume as a replication destination for a specified source.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - volume_name -- Name of the ANF volume.

    Optional Parameters:
    - remote_volume_resource_id -- The id of the destination replication volume
    '''
    return _call_az("az netappfiles volume replication approve", locals())


def suspend(account_name, pool_name, resource_group, volume_name, force=None):
    '''
    Suspend/break a volume replication for the specified destination volume. The replication process is suspended until resumed or deleted.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - volume_name -- Name of the ANF volume.

    Optional Parameters:
    - force -- None
    '''
    return _call_az("az netappfiles volume replication suspend", locals())


def resume(account_name, pool_name, resource_group, volume_name):
    '''
    Resync a volume replication for the specified destination volume. The replication process is resumed from source to destination.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - volume_name -- Name of the ANF volume.
    '''
    return _call_az("az netappfiles volume replication resume", locals())


def remove(account_name, pool_name, resource_group, volume_name):
    '''
    Delete a volume replication for the specified destination volume. The data replication objects of source and destination volumes will be removed.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - volume_name -- Name of the ANF volume.
    '''
    return _call_az("az netappfiles volume replication remove", locals())


def status(account_name, pool_name, resource_group, volume_name):
    '''
    Get the replication status for the specified replication volume.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - volume_name -- Name of the ANF volume.
    '''
    return _call_az("az netappfiles volume replication status", locals())


def re_initialize(account_name, pool_name, resource_group, volume_name):
    '''
    Re-initialise a volume replication for the specified destination volume. The replication process is resumed from source to destination.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - volume_name -- Name of the ANF volume.
    '''
    return _call_az("az netappfiles volume replication re-initialize", locals())

