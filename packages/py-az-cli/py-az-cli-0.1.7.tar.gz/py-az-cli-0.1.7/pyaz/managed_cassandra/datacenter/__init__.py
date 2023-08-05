from ... pyaz_utils import _call_az

def create(cluster_name, data_center_location, data_center_name, delegated_subnet_id, node_count, resource_group, availability_zone=None, backup_storage_customer_key_uri=None, base64_encoded_cassandra_yaml_fragment=None, disk_capacity=None, disk_sku=None, managed_disk_customer_key_uri=None, no_wait=None, sku=None):
    '''
    Create a Datacenter in an Azure Managed Cassandra Cluster.

    Required Parameters:
    - cluster_name -- Cluster Name
    - data_center_location -- Azure Location of the Datacenter
    - data_center_name -- Datacenter Name
    - delegated_subnet_id -- The resource id of a subnet where ip addresses of the Cassandra virtual machines will be allocated. This must be in the same region as data_center_location.
    - node_count -- The number of Cassandra virtual machines in this data center. The minimum value is 3.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - availability_zone -- If the data center haves Availability Zone feature, apply it to the Virtual Machine ScaleSet that host the data center virtual machines.
    - backup_storage_customer_key_uri -- Indicates the Key Uri of the customer key to use for encryption of the backup storage account.
    - base64_encoded_cassandra_yaml_fragment -- This is a Base64 encoded yaml file that is a subset of cassandra.yaml.  Supported fields will be honored and others will be ignored.
    - disk_capacity -- Number of disk used for data centers. Default value is 4.
    - disk_sku -- Disk SKU used for data centers. Default value is P30.
    - managed_disk_customer_key_uri -- Key uri to use for encryption of managed disks. Ensure the system assigned identity of the cluster has been assigned appropriate permissions(key get/wrap/unwrap permissions) on the key.
    - no_wait -- Do not wait for the long-running operation to finish.
    - sku -- Virtual Machine SKU used for data centers. Default value is Standard_DS14_v2
    '''
    return _call_az("az managed-cassandra datacenter create", locals())


def update(cluster_name, data_center_name, resource_group, backup_storage_customer_key_uri=None, base64_encoded_cassandra_yaml_fragment=None, managed_disk_customer_key_uri=None, no_wait=None, node_count=None):
    '''
    Update a Datacenter in an Azure Managed Cassandra Cluster.

    Required Parameters:
    - cluster_name -- Cluster Name
    - data_center_name -- Datacenter Name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - backup_storage_customer_key_uri -- Indicates the Key Uri of the customer key to use for encryption of the backup storage account.
    - base64_encoded_cassandra_yaml_fragment -- This is a Base64 encoded yaml file that is a subset of cassandra.yaml.  Supported fields will be honored and others will be ignored.
    - managed_disk_customer_key_uri -- Key uri to use for encryption of managed disks. Ensure the system assigned identity of the cluster has been assigned appropriate permissions(key get/wrap/unwrap permissions) on the key.
    - no_wait -- Do not wait for the long-running operation to finish.
    - node_count -- The number of Cassandra virtual machines in this data center. The minimum value is 3.
    '''
    return _call_az("az managed-cassandra datacenter update", locals())


def list(cluster_name, resource_group):
    '''
    List the Managed Cassandra Datacenters in a given Cluster.

    Required Parameters:
    - cluster_name -- Cluster Name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az managed-cassandra datacenter list", locals())


def show(cluster_name, data_center_name, resource_group):
    '''
    Get a Managed Cassandra DataCenter Resource.

    Required Parameters:
    - cluster_name -- Cluster Name
    - data_center_name -- Datacenter Name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az managed-cassandra datacenter show", locals())


def delete(cluster_name, data_center_name, resource_group, no_wait=None, yes=None):
    '''
    Deletes a Managed Cassandra Datacenter.

    Required Parameters:
    - cluster_name -- Cluster Name
    - data_center_name -- Datacenter Name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az managed-cassandra datacenter delete", locals())

