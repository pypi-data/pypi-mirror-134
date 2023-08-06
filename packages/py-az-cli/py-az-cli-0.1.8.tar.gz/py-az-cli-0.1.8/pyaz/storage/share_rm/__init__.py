from ... pyaz_utils import _call_az

def create(name, storage_account, access_tier=None, enabled_protocols=None, metadata=None, quota=None, resource_group=None, root_squash=None):
    '''
    Create a new Azure file share under the specified storage account.

    Required Parameters:
    - name -- The file share name.
    - storage_account -- The name or ID of the storage account.

    Optional Parameters:
    - access_tier -- Access tier for specific share. GpV2 account can choose between TransactionOptimized (default), Hot, and Cool. FileStorage account can choose Premium.
    - enabled_protocols -- Immutable property for file shares protocol. NFS protocol will be only available for premium file shares (file shares in the FileStorage account type).
    - metadata -- Metadata in space-separated key=value pairs that is associated with the share. This overwrites any existing metadata
    - quota -- The maximum size of the share in gigabytes. Must be greater than 0, and less than or equal to 5TB (5120). For Large File Shares, the maximum size is 102400.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - root_squash -- Reduction of the access rights for the remote superuser.
    '''
    return _call_az("az storage share-rm create", locals())


def delete(name, storage_account, include=None, resource_group=None, snapshot=None, yes=None):
    '''
    Delete the specified Azure file share or share snapshot.

    Required Parameters:
    - name -- The file share name.
    - storage_account -- The name or ID of the storage account.

    Optional Parameters:
    - include -- Optional. Valid values are: snapshots, leased-snapshots, none. The default value is snapshots. For 'snapshots', the file share is deleted including all of its file share snapshots. If the file share contains leased-snapshots, the deletion fails. For 'leased-snapshots', the file share is deleted included all of its file share snapshots (leased/unleased). For 'none', the file share is deleted if it has no share snapshots. If the file share contains any snapshots (leased or unleased), the deletion fails.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - snapshot -- The DateTime value that specifies the share snapshot to retrieve.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az storage share-rm delete", locals())


def exists(name, storage_account, resource_group=None):
    '''
    Check for the existence of an Azure file share.

    Required Parameters:
    - name -- The file share name.
    - storage_account -- The name or ID of the storage account.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage share-rm exists", locals())


def list(storage_account, include_deleted=None, include_snapshot=None, resource_group=None):
    '''
    List the Azure file shares under the specified storage account.

    Required Parameters:
    - storage_account -- The name or ID of the storage account.

    Optional Parameters:
    - include_deleted -- Include soft deleted file shares when specified.
    - include_snapshot -- Include file share snapshots when specified.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage share-rm list", locals())


def show(name, storage_account, expand=None, resource_group=None, snapshot=None):
    '''
    Show the properties for a specified Azure file share or share snapshot.

    Required Parameters:
    - name -- The file share name.
    - storage_account -- The name or ID of the storage account.

    Optional Parameters:
    - expand -- Optional, used to expand the properties within share's properties. Valid values are: stats. Should be passed as a string with delimiter ','.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - snapshot -- The DateTime value that specifies the share snapshot to retrieve.
    '''
    return _call_az("az storage share-rm show", locals())


def update(name, storage_account, access_tier=None, add=None, force_string=None, metadata=None, quota=None, remove=None, resource_group=None, root_squash=None, set=None):
    '''
    Update the properties for an Azure file share.

    Required Parameters:
    - name -- The file share name.
    - storage_account -- The name or ID of the storage account.

    Optional Parameters:
    - access_tier -- Access tier for specific share. GpV2 account can choose between TransactionOptimized (default), Hot, and Cool. FileStorage account can choose Premium.
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - metadata -- Metadata in space-separated key=value pairs that is associated with the share. This overwrites any existing metadata
    - quota -- The maximum size of the share in gigabytes. Must be greater than 0, and less than or equal to 5TB (5120). For Large File Shares, the maximum size is 102400.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - root_squash -- Reduction of the access rights for the remote superuser.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az storage share-rm update", locals())


def stats(name, storage_account, resource_group=None):
    '''
    Get the usage bytes of the data stored on the share.

    Required Parameters:
    - name -- The file share name.
    - storage_account -- The name or ID of the storage account.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage share-rm stats", locals())


def restore(deleted_version, name, storage_account, resource_group=None, restored_name=None):
    '''
    Restore a file share within a valid retention days if share soft delete is enabled.

    Required Parameters:
    - deleted_version -- Identify the version of the deleted share that will be restored.
    - name -- The file share name. Identify the name of the deleted share that will be restored.
    - storage_account -- The name or ID of the storage account.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - restored_name -- A new file share name to be restored. If not specified, deleted share name will be used.
    '''
    return _call_az("az storage share-rm restore", locals())


def snapshot(name, storage_account, access_tier=None, enabled_protocols=None, metadata=None, quota=None, resource_group=None, root_squash=None):
    '''
    Create a snapshot of an existing share under the specified account.

    Required Parameters:
    - name -- The file share name.
    - storage_account -- The name or ID of the storage account.

    Optional Parameters:
    - access_tier -- Access tier for specific share. GpV2 account can choose between TransactionOptimized (default), Hot, and Cool. FileStorage account can choose Premium.
    - enabled_protocols -- Immutable property for file shares protocol. NFS protocol will be only available for premium file shares (file shares in the FileStorage account type).
    - metadata -- Metadata in space-separated key=value pairs that is associated with the share. This overwrites any existing metadata
    - quota -- The maximum size of the share in gigabytes. Must be greater than 0, and less than or equal to 5TB (5120). For Large File Shares, the maximum size is 102400.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - root_squash -- Reduction of the access rights for the remote superuser.
    '''
    return _call_az("az storage share-rm snapshot", locals())

