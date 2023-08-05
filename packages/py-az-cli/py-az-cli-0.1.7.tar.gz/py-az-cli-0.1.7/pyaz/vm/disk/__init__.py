'''
Manage the managed data disks attached to a VM.
'''
from ... pyaz_utils import _call_az

def attach(name, resource_group, vm_name, caching=None, enable_write_accelerator=None, lun=None, new=None, size_gb=None, sku=None):
    '''
    Attach a managed persistent disk to a VM. Please note that --ids only supports one disk.

    Required Parameters:
    - name -- The name or ID of the managed disk
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vm_name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`

    Optional Parameters:
    - caching -- Disk caching policy
    - enable_write_accelerator -- enable write accelerator
    - lun -- 0-based logical unit number (LUN). Max value depends on the Virtual Machine size.
    - new -- create a new disk
    - size_gb -- size in GB. Max size: 4095 GB (certain preview disks can be larger).
    - sku -- Underlying storage SKU
    '''
    return _call_az("az vm disk attach", locals())


def detach(name, resource_group, vm_name):
    '''
    Detach a managed disk from a VM.

    Required Parameters:
    - name -- The data disk name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vm_name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    '''
    return _call_az("az vm disk detach", locals())

