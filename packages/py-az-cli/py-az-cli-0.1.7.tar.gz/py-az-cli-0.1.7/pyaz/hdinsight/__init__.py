'''
Manage HDInsight resources.
'''
from .. pyaz_utils import _call_az
from . import application, autoscale, azure_monitor, host, monitor, script_action


def create(name, resource_group, type, assign_identity=None, autoscale_max_workernode_count=None, autoscale_min_workernode_count=None, autoscale_type=None, autoscale_workernode_count=None, cluster_admin_account=None, cluster_admin_password=None, cluster_configurations=None, cluster_tier=None, cluster_users_group_dns=None, component_version=None, days=None, domain=None, edgenode_size=None, enable_compute_isolation=None, enable_private_link=None, encryption_algorithm=None, encryption_at_host=None, encryption_in_transit=None, encryption_key_name=None, encryption_key_version=None, encryption_vault_uri=None, esp=None, headnode_size=None, host_sku=None, http_password=None, http_user=None, idbroker=None, kafka_client_group_id=None, kafka_client_group_name=None, kafka_management_node_count=None, kafka_management_node_size=None, ldaps_urls=None, location=None, minimal_tls_version=None, no_validation_timeout=None, no_wait=None, private_link_config=None, resource_provider_connection=None, ssh_password=None, ssh_public_key=None, ssh_user=None, storage_account=None, storage_account_key=None, storage_account_managed_identity=None, storage_container=None, storage_filesystem=None, subnet=None, tags=None, time=None, timezone=None, version=None, vnet_name=None, workernode_count=None, workernode_data_disk_size=None, workernode_data_disk_storage_account_type=None, workernode_data_disks_per_node=None, workernode_size=None, zones=None, zookeepernode_size=None):
    '''
    Create a new cluster.

    Required Parameters:
    - name -- The name of the cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - type -- Type of HDInsight cluster, like: hadoop, interactivehive, hbase, kafka, storm, spark, rserver, mlservices. See also: https://docs.microsoft.com/azure/hdinsight/hdinsight-hadoop-provision-linux-clusters#cluster-types

    Optional Parameters:
    - assign_identity -- The name or ID of user assigned identity.
    - autoscale_max_workernode_count -- The max workernode count for Load-based atuoscale.
    - autoscale_min_workernode_count -- The minimal workernode count for Load-based atuoscale.
    - autoscale_type -- The autoscale type.
    - autoscale_workernode_count -- The scheduled workernode count.
    - cluster_admin_account -- The domain user account that will have admin privileges on the cluster. Required only when create cluster with Enterprise Security Package.
    - cluster_admin_password -- The domain admin password. Required only when create cluster with Enterprise Security Package.
    - cluster_configurations -- Extra configurations of various components. Configurations may be supplied from a file using the `@{path}` syntax or a JSON string. See also: https://docs.microsoft.com/azure/hdinsight/hdinsight-hadoop-customize-cluster-bootstrap
    - cluster_tier -- The tier of the cluster
    - cluster_users_group_dns -- A space-delimited list of Distinguished Names for cluster user groups. Required only when create cluster with Enterprise Security Package. 
    - component_version -- The versions of various Hadoop components, in space-separated versions in 'component=version' format. Example: Spark=2.0 Hadoop=2.7.3 See also: https://docs.microsoft.com/azure/hdinsight/hdinsight-component-versioning#hadoop-components-available-with-different-hdinsight-versions
    - days -- A space-delimited list of schedule day.
    - domain -- The name or resource ID of the user's Azure Active Directory Domain Service. Required only when create cluster with Enterprise Security Package.
    - edgenode_size -- The size of the node. See also: https://docs.microsoft.com/azure/hdinsight/hdinsight-hadoop-provision-linux-clusters#configure-cluster-size
    - enable_compute_isolation -- Indicate whether enable compute isolation or not.
    - enable_private_link -- Indicate whether enable the private link or not.
    - encryption_algorithm -- Algorithm identifier for encryption.
    - encryption_at_host -- Indicates whether enable encryption at host or not.
    - encryption_in_transit -- Indicates whether enable encryption in transit.
    - encryption_key_name -- Key name that is used for enabling disk encryption.
    - encryption_key_version -- Key version that is used for enabling disk encryption.
    - encryption_vault_uri -- Base key vault URI where the customers key is located eg. https://myvault.vault.azure.net
    - esp -- Specify to create cluster with Enterprise Security Package. If omitted, creating cluster with Enterprise Security Package will not not allowed.
    - headnode_size -- The size of the node. See also: https://docs.microsoft.com/azure/hdinsight/hdinsight-hadoop-provision-linux-clusters#configure-cluster-size
    - host_sku -- The dedicated host sku of compute isolation.
    - http_password -- HTTP password for the cluster. Will prompt if not given.
    - http_user -- HTTP username for the cluster.  Default: admin.
    - idbroker -- Specify to create ESP cluster with HDInsight ID Broker. If omitted, creating ESP cluster with HDInsight ID Broker will not not allowed.
    - kafka_client_group_id -- The client AAD security group id for Kafka Rest Proxy
    - kafka_client_group_name -- The client AAD security group name for Kafka Rest Proxy
    - kafka_management_node_count -- The number of kafka management node in the cluster
    - kafka_management_node_size -- The size of the node. See also: https://docs.microsoft.com/azure/hdinsight/hdinsight-hadoop-provision-linux-clusters#configure-cluster-size
    - ldaps_urls -- A space-delimited list of LDAPS protocol URLs to communicate with the Active Directory. Required only when create cluster with Enterprise Security Package.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - minimal_tls_version -- The minimal supported TLS version.
    - no_validation_timeout -- Permit timeout error during argument validation phase. If omitted, validation timeout error will be permitted.
    - no_wait -- Do not wait for the long-running operation to finish.
    - private_link_config -- The private link configurations when creating cluster. Private Link Configurations may be supplied from a file using the `@{path}` syntax or a JSON string. Please see https://github.com/Azure/azure-cli/blob/dev/src/azure-cli/azure/cli/command_modules/hdinsight/tests/latest/privatelinkconfigurations.json
    - resource_provider_connection -- The resource provider connection type
    - ssh_password -- SSH password for the cluster nodes. If none specified, uses the HTTP password.
    - ssh_public_key -- SSH public key for the cluster nodes.
    - ssh_user -- SSH username for the cluster nodes.
    - storage_account -- The name or ID of the storage account.
    - storage_account_key -- The storage account key. A key can be retrieved automatically if the user has access to the storage account.
    - storage_account_managed_identity -- User-assigned managed identity with access to the storage account filesystem. Only required when storage account type is Azure Data Lake Storage Gen2.
    - storage_container -- The storage container the cluster will use. Uses the cluster name if none was specified. (WASB only)
    - storage_filesystem -- The storage filesystem the cluster will use. Uses the cluster name if none was specified. (DFS only)
    - subnet -- The name or ID of subnet. If name is supplied, `--vnet-name` must be supplied.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - time -- The 24-hour time in the form of xx:xx in days.
    - timezone -- The timezone for schedule autoscale type. Values from `az hdinsight autoscale list-timezones`
    - version -- The HDInsight cluster version. See also: https://docs.microsoft.com/azure/hdinsight/hdinsight-component-versioning#supported-hdinsight-versions
    - vnet_name -- The name of a virtual network.
    - workernode_count -- The number of worker nodes in the cluster.
    - workernode_data_disk_size -- The size of the data disk in GB, e.g. 1023.
    - workernode_data_disk_storage_account_type -- The type of storage account that will be used for the data disks: standard_lrs or premium_lrs
    - workernode_data_disks_per_node -- The number of data disks to use per worker node.
    - workernode_size -- The size of the node. See also: https://docs.microsoft.com/azure/hdinsight/hdinsight-hadoop-provision-linux-clusters#configure-cluster-size
    - zones -- A space-delimited list of availability zones where cluster will be created.
    - zookeepernode_size -- The size of the node. See also: https://docs.microsoft.com/azure/hdinsight/hdinsight-hadoop-provision-linux-clusters#configure-cluster-size
    '''
    return _call_az("az hdinsight create", locals())


def resize(name, resource_group, workernode_count, no_wait=None):
    '''
    Resize the specified HDInsight cluster to the specified size.

    Required Parameters:
    - name -- The name of the cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workernode_count -- The target worker node instance count for the operation.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az hdinsight resize", locals())


def show(name, resource_group):
    '''
    

    Required Parameters:
    - name -- The name of the cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az hdinsight show", locals())


def list(resource_group=None):
    '''
    List HDInsight clusters in a resource group or subscription.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az hdinsight list", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until an operation is complete.

    Required Parameters:
    - name -- The name of the cluster.
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
    return _call_az("az hdinsight wait", locals())


def delete(name, resource_group, no_wait=None, yes=None):
    '''
    

    Required Parameters:
    - name -- The name of the cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az hdinsight delete", locals())


def rotate_disk_encryption_key(encryption_key_name, encryption_key_version, encryption_vault_uri, name, resource_group, no_wait=None):
    '''
    Rotate the disk encryption key of the specified HDInsight cluster.

    Required Parameters:
    - encryption_key_name -- Key name that is used for enabling disk encryption.
    - encryption_key_version -- Key version that is used for enabling disk encryption.
    - encryption_vault_uri -- Base key vault URI where the customers key is located eg. https://myvault.vault.azure.net
    - name -- The name of the cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az hdinsight rotate-disk-encryption-key", locals())


def update(name, resource_group, no_wait=None, tags=None):
    '''
    Update the tags of the specified HDInsight cluster.

    Required Parameters:
    - name -- The name of the cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az hdinsight update", locals())


def list_usage(location):
    '''
    

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    '''
    return _call_az("az hdinsight list-usage", locals())

