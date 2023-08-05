from ... pyaz_utils import _call_az

def attach(resource_group, vm_name, caching=None, lun=None, name=None, new=None, size_gb=None, vhd_uri=None):
    '''
    Attach an unmanaged persistent disk to a VM.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vm_name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`

    Optional Parameters:
    - caching -- Disk caching policy
    - lun -- 0-based logical unit number (LUN). Max value depends on the Virtual Machine size.
    - name -- The data disk name.
    - new -- Create a new disk.
    - size_gb -- size in GB. Max size: 4095 GB (certain preview disks can be larger).
    - vhd_uri -- Virtual hard disk URI. For example: https://mystorage.blob.core.windows.net/vhds/d1.vhd
    '''
    return _call_az("az vm unmanaged-disk attach", locals())


def detach(name, resource_group, vm_name):
    '''
    Detach an unmanaged disk from a VM.

    Required Parameters:
    - name -- The data disk name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vm_name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    '''
    return _call_az("az vm unmanaged-disk detach", locals())


def list(resource_group, vm_name):
    '''
    List unmanaged disks of a VM.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vm_name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    '''
    return _call_az("az vm unmanaged-disk list", locals())

