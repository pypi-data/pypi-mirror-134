from ... pyaz_utils import _call_az
from . import node, vm_extension, vm_secret


def list(cluster_name, resource_group):
    '''
    List node types of a managed cluster.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sf managed-node-type list", locals())


def delete(cluster_name, resource_group):
    '''
    Delete node type from a cluster.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sf managed-node-type delete", locals())


def show(cluster_name, resource_group):
    '''
    Show the properties of a node type.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sf managed-node-type show", locals())


def create(cluster_name, instance_count, resource_group, application_end_port=None, application_start_port=None, capacity=None, disk_size=None, disk_type=None, ephemeral_end_port=None, ephemeral_start_port=None, is_stateless=None, multiple_placement_groups=None, placement_property=None, primary=None, vm_image_offer=None, vm_image_publisher=None, vm_image_sku=None, vm_image_version=None, vm_size=None):
    '''
    Delete a managed cluster.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - instance_count -- essage = "The number of nodes in the node type.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - application_end_port -- Application End port of a range of ports.
    - application_start_port -- Application start port of a range of ports.
    - capacity -- Capacity tags applied to the nodes in the node type as key/value pairs, the cluster resource manager uses these tags to understand how much resource a node has. Updating this will override the current values.for example: --capacity ClientConnections=65536 param2=value2
    - disk_size -- Disk size for each vm in the node type in GBs.
    - disk_type -- Managed data disk type. IOPS and throughput are given by the disk size, to see more information go to https://docs.microsoft.com/azure/virtual-machines/disks-types. Default StandardSSD_LRSStandard_LRS: Standard HDD locally redundant storage. Best for backup, non-critical, and infrequent access.StandardSSD_LRS: Standard SSD locally redundant storage. Best for web servers, lightly used enterprise applications and dev/test.Premium_LRS: Premium SSD locally redundant storage. Best for production and performance sensitive workloads.
    - ephemeral_end_port -- Ephemeral end port of a range of ports.
    - ephemeral_start_port -- Ephemeral start port of a range of ports.
    - is_stateless -- Indicates if the node type can only host Stateless workloads.
    - multiple_placement_groups -- Indicates if scale set associated with the node type can be composed of multiple placement groups.
    - placement_property -- Placement tags applied to nodes in the node type as key/value pairs, which can be used to indicate where certain services (workload) should run. Updating this will override the current values.for example: --placement-property NodeColor=Green SomeProperty=5
    - primary -- Specify if the node type is primary. On this node type will run system services. Only one node type should be marked as primary. Primary node type cannot be deleted or changed for existing clusters.
    - vm_image_offer -- The offer type of the Azure Virtual Machines Marketplace image.
    - vm_image_publisher -- The publisher of the Azure Virtual Machines Marketplace image.
    - vm_image_sku -- The SKU of the Azure Virtual Machines Marketplace image.
    - vm_image_version -- The version of the Azure Virtual Machines Marketplace image. 
    - vm_size -- The size of virtual machines in the pool. All virtual machines in a pool are the same size.
    '''
    return _call_az("az sf managed-node-type create", locals())


def update(cluster_name, resource_group, application_end_port=None, application_start_port=None, capacity=None, ephemeral_end_port=None, ephemeral_start_port=None, instance_count=None, placement_property=None):
    '''
    Update a managed cluster.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - application_end_port -- Application End port of a range of ports.
    - application_start_port -- Application start port of a range of ports.
    - capacity -- Capacity tags applied to the nodes in the node type as key/value pairs, the cluster resource manager uses these tags to understand how much resource a node has. Updating this will override the current values.for example: --capacity ClientConnections=65536 param2=value2
    - ephemeral_end_port -- Ephemeral end port of a range of ports.
    - ephemeral_start_port -- Ephemeral start port of a range of ports.
    - instance_count -- essage = "The number of nodes in the node type.
    - placement_property -- Placement tags applied to nodes in the node type as key/value pairs, which can be used to indicate where certain services (workload) should run. Updating this will override the current values.for example: --placement-property NodeColor=Green SomeProperty=5
    '''
    return _call_az("az sf managed-node-type update", locals())

