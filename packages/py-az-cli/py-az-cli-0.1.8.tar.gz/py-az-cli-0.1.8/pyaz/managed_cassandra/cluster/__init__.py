from ... pyaz_utils import _call_az

def create(cluster_name, delegated_management_subnet_id, location, resource_group, authentication_method=None, cassandra_version=None, client_certificates=None, cluster_name_override=None, external_gossip_certificates=None, external_seed_nodes=None, hours_between_backups=None, identity_type=None, initial_cassandra_admin_password=None, no_wait=None, repair_enabled=None, restore_from_backup_id=None, tags=None):
    '''
    Create a Managed Cassandra Cluster.

    Required Parameters:
    - cluster_name -- Cluster Name
    - delegated_management_subnet_id -- The resource id of a subnet where the ip address of the cassandra management server will be allocated. This subnet must have connectivity to the delegated_subnet_id subnet of each data center.
    - location -- Azure Location of the Cluster
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - authentication_method -- Authentication mode can be None or Cassandra. If None, no authentication will be required to connect to the Cassandra API. If Cassandra, then passwords will be used.
    - cassandra_version -- The version of Cassandra chosen.
    - client_certificates -- If specified, enables client certificate authentication to the Cassandra API.
    - cluster_name_override -- If a cluster must have a name that is not a valid azure resource name, this field can be specified to choose the Cassandra cluster name. Otherwise, the resource name will be used as the cluster name.
    - external_gossip_certificates -- A list of certificates that the managed cassandra data center's should accept.
    - external_seed_nodes -- A list of ip addresses of the seed nodes of on-premise data centers.
    - hours_between_backups -- The number of hours between backup attempts.
    - identity_type -- Type of identity used for Customer Managed Disk Key.
    - initial_cassandra_admin_password -- The intial password to be configured when a cluster is created for authentication_method Cassandra.
    - no_wait -- Do not wait for the long-running operation to finish.
    - repair_enabled -- Enables automatic repair.
    - restore_from_backup_id -- The resource id of a backup. If provided on create, the backup will be used to prepopulate the cluster. The cluster data center count and node counts must match the backup.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az managed-cassandra cluster create", locals())


def update(cluster_name, resource_group, authentication_method=None, cassandra_version=None, client_certificates=None, external_gossip_certificates=None, external_seed_nodes=None, hours_between_backups=None, identity_type=None, no_wait=None, repair_enabled=None, tags=None):
    '''
    Update a Managed Cassandra Cluster.

    Required Parameters:
    - cluster_name -- Cluster Name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - authentication_method -- Authentication mode can be None or Cassandra. If None, no authentication will be required to connect to the Cassandra API. If Cassandra, then passwords will be used.
    - cassandra_version -- The version of Cassandra chosen.
    - client_certificates -- If specified, enables client certificate authentication to the Cassandra API.
    - external_gossip_certificates -- A list of certificates that the managed cassandra data center's should accept.
    - external_seed_nodes -- A list of ip addresses of the seed nodes of on-premise data centers.
    - hours_between_backups -- The number of hours between backup attempts.
    - identity_type -- Type of identity used for Customer Managed Disk Key.
    - no_wait -- Do not wait for the long-running operation to finish.
    - repair_enabled -- Enables automatic repair.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az managed-cassandra cluster update", locals())


def deallocate(cluster_name, resource_group, no_wait=None):
    '''
    Deallocate the Managed Cassandra Cluster and Associated Data Centers. Deallocation will deallocate the host virtual machine of this cluster, and reserved the data disk. This won't do anything on an already deallocated cluster. Use Start to restart the cluster.

    Required Parameters:
    - cluster_name -- Cluster Name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az managed-cassandra cluster deallocate", locals())


def invoke_command(cluster_name, command_name, host, resource_group, arguments=None, cassandra_stop_start=None, no_wait=None, readwrite=None):
    '''
    Invoke a command like nodetool for cassandra maintenance.

    Required Parameters:
    - cluster_name -- Cluster Name
    - command_name -- The command which should be run
    - host -- IP address of the cassandra host to run the command on
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - arguments -- The key="value" of arguments for the command.
    - cassandra_stop_start -- If true, stops cassandra before executing the command and then start it again.
    - no_wait -- Do not wait for the long-running operation to finish.
    - readwrite -- If true, allows the command to *write* to the cassandra directory, otherwise read-only.
    '''
    return _call_az("az managed-cassandra cluster invoke-command", locals())


def start(cluster_name, resource_group, no_wait=None):
    '''
    Start the Managed Cassandra Cluster and Associated Data Centers. Start will start the host virtual machine of this cluster with reserved data disk. This won't do anything on an already running cluster. Use Deallocate to deallocate the cluster.

    Required Parameters:
    - cluster_name -- Cluster Name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az managed-cassandra cluster start", locals())


def status(cluster_name, resource_group):
    '''
    Gets the CPU, memory, and disk usage statistics for each Cassandra node in a cluster.

    Required Parameters:
    - cluster_name -- Cluster Name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az managed-cassandra cluster status", locals())


def list(resource_group=None):
    '''
    List the Managed Cassandra Clusters in a ResourceGroup and Subscription. If the ResourceGroup is not specified all the clusters in this Subscription are returned.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az managed-cassandra cluster list", locals())


def show(cluster_name, resource_group):
    '''
    Get a Managed Cassandra Cluster Resource.

    Required Parameters:
    - cluster_name -- Cluster Name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az managed-cassandra cluster show", locals())


def delete(cluster_name, resource_group, no_wait=None, yes=None):
    '''
    Deletes a Managed Cassandra Cluster.

    Required Parameters:
    - cluster_name -- Cluster Name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az managed-cassandra cluster delete", locals())

