'''
Manage point-in-time copies of managed disks, native blobs, or other snapshots.
'''
from .. pyaz_utils import _call_az

def create(name, resource_group, accelerated_network=None, copy_start=None, disk_access=None, disk_encryption_set=None, edge_zone=None, encryption_type=None, for_upload=None, hyper_v_generation=None, incremental=None, location=None, network_access_policy=None, no_wait=None, public_network_access=None, size_gb=None, sku=None, source=None, source_storage_account_id=None, tags=None):
    '''
    Create a snapshot.

    Required Parameters:
    - name -- The name of the snapshot
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - accelerated_network -- Customers can set on Managed Disks or Snapshots to enable the accelerated networking if the OS disk image support.
    - copy_start -- Create snapshot by using a deep copy process, where the resource creation is considered complete only after all data has been copied from the source.
    - disk_access -- Name or ID of the disk access resource for using private endpoints on disks.
    - disk_encryption_set -- Name or ID of disk encryption set that is used to encrypt the disk.
    - edge_zone -- The name of edge zone.
    - encryption_type -- Encryption type. EncryptionAtRestWithPlatformKey: Disk is encrypted with XStore managed key at rest. It is the default encryption type. EncryptionAtRestWithCustomerKey: Disk is encrypted with Customer managed key at rest.
    - for_upload -- Create the snapshot for uploading blobs later on through storage commands. Run "az snapshot grant-access --access-level Write" to retrieve the snapshot's SAS token.
    - hyper_v_generation -- The hypervisor generation of the Virtual Machine. Applicable to OS disks only.
    - incremental -- Whether a snapshot is incremental. Incremental snapshots on the same disk occupy less space than full snapshots and can be diffed
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`. If location is not specified and no default location specified, location will be automatically set as same as the resource group.
    - network_access_policy -- Policy for accessing the disk via network.
    - no_wait -- Do not wait for the long-running operation to finish.
    - public_network_access -- Customers can set on Managed Disks or Snapshots to control the export policy on the disk.
    - size_gb -- size in GB. Max size: 4095 GB (certain preview disks can be larger).
    - sku -- None
    - source -- source to create the disk/snapshot from, including unmanaged blob uri, managed disk id or name, or snapshot id or name
    - source_storage_account_id -- used when source blob is in a different subscription
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az snapshot create", locals())


def delete(name, resource_group):
    '''
    

    Required Parameters:
    - name -- The name of the snapshot
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az snapshot delete", locals())


def grant_access(duration_in_seconds, name, resource_group, access_level=None):
    '''
    Grant read access to a snapshot.

    Required Parameters:
    - duration_in_seconds -- Time duration in seconds until the SAS access expires
    - name -- The name of the snapshot
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - access_level -- access level
    '''
    return _call_az("az snapshot grant-access", locals())


def list(resource_group=None):
    '''
    List snapshots.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az snapshot list", locals())


def revoke_access(name, resource_group):
    '''
    Revoke read access to a snapshot.

    Required Parameters:
    - name -- The name of the snapshot
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az snapshot revoke-access", locals())


def show(name, resource_group):
    '''
    

    Required Parameters:
    - name -- The name of the snapshot
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az snapshot show", locals())


def update(name, resource_group, accelerated_network=None, add=None, disk_access=None, disk_encryption_set=None, encryption_type=None, force_string=None, network_access_policy=None, no_wait=None, public_network_access=None, remove=None, set=None, sku=None):
    '''
    Update a snapshot.

    Required Parameters:
    - name -- The name of the snapshot
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - accelerated_network -- Customers can set on Managed Disks or Snapshots to enable the accelerated networking if the OS disk image support.
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - disk_access -- Name or ID of the disk access resource for using private endpoints on disks.
    - disk_encryption_set -- Name or ID of disk encryption set that is used to encrypt the disk.
    - encryption_type -- Encryption type. EncryptionAtRestWithPlatformKey: Disk is encrypted with XStore managed key at rest. It is the default encryption type. EncryptionAtRestWithCustomerKey: Disk is encrypted with Customer managed key at rest.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - network_access_policy -- Policy for accessing the disk via network.
    - no_wait -- Do not wait for the long-running operation to finish.
    - public_network_access -- Customers can set on Managed Disks or Snapshots to control the export policy on the disk.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - sku -- None
    '''
    return _call_az("az snapshot update", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of a snapshot is met.

    Required Parameters:
    - name -- The name of the snapshot
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az snapshot wait", locals())

