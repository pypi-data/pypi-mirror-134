'''
Manage custom virtual machine images.
'''
from .. pyaz_utils import _call_az
from . import builder


def create(name, resource_group, source, data_disk_caching=None, data_disk_sources=None, edge_zone=None, hyper_v_generation=None, location=None, os_disk_caching=None, os_type=None, storage_sku=None, tags=None, zone_resilient=None):
    '''
    Create a custom Virtual Machine Image from managed disks or snapshots.

    Required Parameters:
    - name -- new image name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - source -- OS disk source from the same region, including a virtual machine ID or name, OS disk blob URI, managed OS disk ID or name, or OS snapshot ID or name

    Optional Parameters:
    - data_disk_caching -- Storage caching type for the image's data disk.
    - data_disk_sources -- Space-separated list of data disk sources, including unmanaged blob URI, managed disk ID or name, or snapshot ID or name
    - edge_zone -- The name of edge zone.
    - hyper_v_generation -- The hypervisor generation of the Virtual Machine created from the image.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - os_disk_caching -- Storage caching type for the image's OS disk.
    - os_type -- None
    - storage_sku -- The SKU of the storage account with which to create the VM image. Unused if source VM is specified.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - zone_resilient -- Specifies whether an image is zone resilient or not. Default is false. Zone resilient images can be created only in regions that provide Zone Redundant Storage
    '''
    return _call_az("az image create", locals())


def list(resource_group=None):
    '''
    List custom VM images.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az image list", locals())


def show(name, resource_group, expand=None):
    '''
    

    Required Parameters:
    - name -- The name of the image.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expand -- The expand expression to apply on the operation.
    '''
    return _call_az("az image show", locals())


def delete(name, resource_group):
    '''
    

    Required Parameters:
    - name -- The name of the image.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az image delete", locals())


def update(name, resource_group, add=None, force_string=None, remove=None, set=None, tags=None):
    '''
    Update custom VM images.

    Required Parameters:
    - name -- The name of the image.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az image update", locals())

