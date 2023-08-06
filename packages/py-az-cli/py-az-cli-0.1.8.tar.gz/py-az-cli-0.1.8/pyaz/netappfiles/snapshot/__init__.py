'''
Manage Azure NetApp Files (ANF) Snapshot Resources.
'''
from ... pyaz_utils import _call_az
from . import policy


def show(account_name, name, pool_name, resource_group, volume_name):
    '''
    Get the specified ANF snapshot.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - name -- The name of the ANF snapshot
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - volume_name -- Name of the ANF volume.
    '''
    return _call_az("az netappfiles snapshot show", locals())


def list(account_name, pool_name, resource_group, volume_name):
    '''
    List the snapshots of an ANF volume.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - volume_name -- The name of the ANF volume
    '''
    return _call_az("az netappfiles snapshot list", locals())


def delete(account_name, name, pool_name, resource_group, volume_name):
    '''
    Delete the specified ANF snapshot.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - name -- The name of the ANF snapshot
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - volume_name -- Name of the ANF volume.
    '''
    return _call_az("az netappfiles snapshot delete", locals())


def create(account_name, location, name, pool_name, resource_group, volume_name):
    '''
    Create a new Azure NetApp Files (ANF) snapshot.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- The name of the ANF snapshot
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - volume_name -- Name of the ANF volume.
    '''
    return _call_az("az netappfiles snapshot create", locals())


def update(account_name, body, name, pool_name, resource_group, volume_name):
    '''
    

    Required Parameters:
    - account_name -- Name of the ANF account.
    - body -- Snapshot object supplied in the body of the operation.
    - name -- The name of the ANF snapshot
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - volume_name -- Name of the ANF volume.
    '''
    return _call_az("az netappfiles snapshot update", locals())

