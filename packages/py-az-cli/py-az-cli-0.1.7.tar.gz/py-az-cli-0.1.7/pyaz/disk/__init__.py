'''
Manage Azure Managed Disks.
'''
from .. pyaz_utils import _call_az

def create(name, resource_group, accelerated_network=None, disk_access=None, disk_encryption_set=None, disk_iops_read_only=None, disk_iops_read_write=None, disk_mbps_read_only=None, disk_mbps_read_write=None, edge_zone=None, enable_bursting=None, encryption_type=None, for_upload=None, gallery_image_reference=None, gallery_image_reference_lun=None, hyper_v_generation=None, image_reference=None, image_reference_lun=None, location=None, logical_sector_size=None, max_shares=None, network_access_policy=None, no_wait=None, os_type=None, public_network_access=None, security_type=None, size_gb=None, sku=None, source=None, source_storage_account_id=None, support_hibernation=None, tags=None, tier=None, upload_size_bytes=None, zone=None):
    '''
    Create a managed disk.

    Required Parameters:
    - name -- The name of the managed disk
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - accelerated_network -- Customers can set on Managed Disks or Snapshots to enable the accelerated networking if the OS disk image support.
    - disk_access -- Name or ID of the disk access resource for using private endpoints on disks.
    - disk_encryption_set -- Name or ID of disk encryption set that is used to encrypt the disk.
    - disk_iops_read_only -- The total number of IOPS that will be allowed across all VMs mounting the shared disk as ReadOnly. One operation can transfer between 4k and 256k bytes
    - disk_iops_read_write -- The number of IOPS allowed for this disk. Only settable for UltraSSD disks. One operation can transfer between 4k and 256k bytes
    - disk_mbps_read_only -- The total throughput (MBps) that will be allowed across all VMs mounting the shared disk as ReadOnly. MBps means millions of bytes per second - MB here uses the ISO notation, of powers of 10
    - disk_mbps_read_write -- The bandwidth allowed for this disk. Only settable for UltraSSD disks. MBps means millions of bytes per second with ISO notation of powers of 10
    - edge_zone -- The name of edge zone.
    - enable_bursting -- Enable bursting beyond the provisioned performance target of the disk. Bursting is disabled by default, and it does not apply to Ultra disks.
    - encryption_type -- Encryption type. EncryptionAtRestWithPlatformKey: Disk is encrypted with XStore managed key at rest. It is the default encryption type. EncryptionAtRestWithCustomerKey: Disk is encrypted with Customer managed key at rest.
    - for_upload -- Create the disk for uploading blobs later on through storage commands. Run "az disk grant-access --access-level Write" to retrieve the disk's SAS token.
    - gallery_image_reference -- ID of the Compute Gallery image version from which to create a disk
    - gallery_image_reference_lun -- If the disk is created from an image's data disk, this is an index that indicates which of the data disks in the image to use. For OS disks, this field is null
    - hyper_v_generation -- The hypervisor generation of the Virtual Machine. Applicable to OS disks only.
    - image_reference -- ID or URN (publisher:offer:sku:version) of the image from which to create a disk
    - image_reference_lun -- If the disk is created from an image's data disk, this is an index that indicates which of the data disks in the image to use. For OS disks, this field is null
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`. If location is not specified and no default location specified, location will be automatically set as same as the resource group.
    - logical_sector_size -- Logical sector size in bytes for Ultra disks. Supported values are 512 ad 4096. 4096 is the default.
    - max_shares -- The maximum number of VMs that can attach to the disk at the same time. Value greater than one indicates a disk that can be mounted on multiple VMs at the same time
    - network_access_policy -- Policy for accessing the disk via network.
    - no_wait -- Do not wait for the long-running operation to finish.
    - os_type -- The Operating System type of the Disk.
    - public_network_access -- Customers can set on Managed Disks or Snapshots to control the export policy on the disk.
    - security_type -- The security type of the VM. Applicable for OS disks only.
    - size_gb -- size in GB. Max size: 4095 GB (certain preview disks can be larger).
    - sku -- Underlying storage SKU
    - source -- source to create the disk/snapshot from, including unmanaged blob uri, managed disk id or name, or snapshot id or name
    - source_storage_account_id -- used when source blob is in a different subscription
    - support_hibernation -- Indicate the OS on a disk supports hibernation.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - tier -- Performance tier of the disk (e.g, P4, S10) as described here: https://azure.microsoft.com/pricing/details/managed-disks/. Does not apply to Ultra disks.
    - upload_size_bytes -- The size (in bytes) of the contents of the upload including the VHD footer. Min value: 20972032. Max value: 35183298347520
    - zone -- Availability zone into which to provision the resource.
    '''
    return _call_az("az disk create", locals())


def delete(name, resource_group, no_wait=None, yes=None):
    '''
    Delete a managed disk.

    Required Parameters:
    - name -- The name of the managed disk
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az disk delete", locals())


def grant_access(duration_in_seconds, name, resource_group, access_level=None):
    '''
    Grant a resource access to a managed disk.

    Required Parameters:
    - duration_in_seconds -- Time duration in seconds until the SAS access expires
    - name -- The name of the managed disk
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - access_level -- access level
    '''
    return _call_az("az disk grant-access", locals())


def list(resource_group=None):
    '''
    List managed disks.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az disk list", locals())


def revoke_access(name, resource_group):
    '''
    Revoke a resource's read access to a managed disk.

    Required Parameters:
    - name -- The name of the managed disk
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az disk revoke-access", locals())


def show(name, resource_group):
    '''
    

    Required Parameters:
    - name -- The name of the managed disk
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az disk show", locals())


def update(name, resource_group, accelerated_network=None, add=None, disk_access=None, disk_encryption_set=None, disk_iops_read_only=None, disk_iops_read_write=None, disk_mbps_read_only=None, disk_mbps_read_write=None, enable_bursting=None, encryption_type=None, force_string=None, max_shares=None, network_access_policy=None, no_wait=None, public_network_access=None, remove=None, set=None, size_gb=None, sku=None):
    '''
    Update a managed disk.

    Required Parameters:
    - name -- The name of the managed disk
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - accelerated_network -- Customers can set on Managed Disks or Snapshots to enable the accelerated networking if the OS disk image support.
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - disk_access -- Name or ID of the disk access resource for using private endpoints on disks.
    - disk_encryption_set -- Name or ID of disk encryption set that is used to encrypt the disk.
    - disk_iops_read_only -- The total number of IOPS that will be allowed across all VMs mounting the shared disk as ReadOnly. One operation can transfer between 4k and 256k bytes
    - disk_iops_read_write -- The number of IOPS allowed for this disk. Only settable for UltraSSD disks. One operation can transfer between 4k and 256k bytes
    - disk_mbps_read_only -- The total throughput (MBps) that will be allowed across all VMs mounting the shared disk as ReadOnly. MBps means millions of bytes per second - MB here uses the ISO notation, of powers of 10
    - disk_mbps_read_write -- The bandwidth allowed for this disk. Only settable for UltraSSD disks. MBps means millions of bytes per second with ISO notation of powers of 10
    - enable_bursting -- Enable bursting beyond the provisioned performance target of the disk. Bursting is disabled by default, and it does not apply to Ultra disks.
    - encryption_type -- Encryption type. EncryptionAtRestWithPlatformKey: Disk is encrypted with XStore managed key at rest. It is the default encryption type. EncryptionAtRestWithCustomerKey: Disk is encrypted with Customer managed key at rest.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - max_shares -- The maximum number of VMs that can attach to the disk at the same time. Value greater than one indicates a disk that can be mounted on multiple VMs at the same time
    - network_access_policy -- Policy for accessing the disk via network.
    - no_wait -- Do not wait for the long-running operation to finish.
    - public_network_access -- Customers can set on Managed Disks or Snapshots to control the export policy on the disk.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - size_gb -- size in GB. Max size: 4095 GB (certain preview disks can be larger).
    - sku -- Underlying storage SKU
    '''
    return _call_az("az disk update", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of a managed disk is met.

    Required Parameters:
    - name -- The name of the managed disk
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
    return _call_az("az disk wait", locals())

