'''
Manage data disks of a VMSS.
'''
from ... pyaz_utils import _call_az

def attach(resource_group, vmss_name, caching=None, disk=None, instance_id=None, lun=None, size_gb=None, sku=None):
    '''
    Attach managed data disks to a scale set or its instances.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vmss_name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`

    Optional Parameters:
    - caching -- Disk caching policy
    - disk -- existing disk name or ID to attach or detach from VM instances
    - instance_id -- Scale set VM instance id
    - lun -- 0-based logical unit number (LUN). Max value depends on the Virtual Machine instance size.
    - size_gb -- size in GB. Max size: 4095 GB (certain preview disks can be larger).
    - sku -- Underlying storage SKU
    '''
    return _call_az("az vmss disk attach", locals())


def detach(lun, resource_group, vmss_name, instance_id=None):
    '''
    Detach managed data disks from a scale set or its instances.

    Required Parameters:
    - lun -- 0-based logical unit number (LUN). Max value depends on the Virtual Machine instance size.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vmss_name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`

    Optional Parameters:
    - instance_id -- Scale set VM instance id
    '''
    return _call_az("az vmss disk detach", locals())

