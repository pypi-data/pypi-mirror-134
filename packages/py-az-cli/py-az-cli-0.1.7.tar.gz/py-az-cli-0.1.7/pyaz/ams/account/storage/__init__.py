'''
Manage storage for an Azure Media Services account.
'''
from .... pyaz_utils import _call_az

def add(account_name, name, resource_group):
    '''
    Attach a secondary storage to an Azure Media Services account.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name or resource ID of the secondary storage account to detach from the Azure Media Services account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams account storage add", locals())


def remove(account_name, name, resource_group):
    '''
    Detach a secondary storage from an Azure Media Services account.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name or resource ID of the secondary storage account to detach from the Azure Media Services account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams account storage remove", locals())


def set_authentication(account_name, resource_group, storage_auth):
    '''
    Set the authentication of a storage account attached to an Azure Media Services account.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - storage_auth -- The type of authentication for the storage account associated with the media services account.
    '''
    return _call_az("az ams account storage set-authentication", locals())


def sync_storage_keys(account_name, resource_group, storage_account_id):
    '''
    Synchronize storage account keys for a storage account associated with an Azure Media Services account.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - storage_account_id -- The storage account Id.
    '''
    return _call_az("az ams account storage sync-storage-keys", locals())

