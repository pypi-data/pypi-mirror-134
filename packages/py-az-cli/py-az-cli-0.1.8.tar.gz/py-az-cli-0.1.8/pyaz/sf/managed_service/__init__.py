from ... pyaz_utils import _call_az
from . import correlation_scheme, load_metrics


def list(application, cluster_name, resource_group):
    '''
    List managed services of a given managed application.

    Required Parameters:
    - application -- Specify the name of the service.
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sf managed-service list", locals())


def delete(application, cluster_name, name, resource_group):
    '''
    Delete a managed service.

    Required Parameters:
    - application -- Specify the name of the service.
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - name -- Specify the name of the service.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sf managed-service delete", locals())


def show(application, cluster_name, name, resource_group):
    '''
    Get a service.

    Required Parameters:
    - application -- Specify the name of the service.
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - name -- Specify the name of the service.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sf managed-service show", locals())


def create(application, cluster_name, name, resource_group, state, type, default_move_cost=None, has_persisted_state=None, high_key=None, instance_count=None, low_key=None, min_instance_count=None, min_instance_percentage=None, min_replica_set_size=None, partition_count=None, partition_names=None, partition_scheme=None, placement_constraints=None, quorum_loss_wait_duration=None, replica_restart_wait_duration=None, service_package_activation_mode=None, service_placement_time_limit=None, stand_by_replica_keep_duration=None, tags=None, target_replica_set_size=None):
    '''
    Create a new managed service on an Azure Service Fabric managed cluster.

    Required Parameters:
    - application -- Specify the name of the service.
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - name -- Specify the name of the service.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    - state -- Specify if the service is stateless or stateful.
    - type -- Specify the service type name of the application, it should exist in the application manifest.

    Optional Parameters:
    - default_move_cost -- Specify the default cost for a move. Higher costs make it less likely that the Cluster Resource Manager will move the replica when trying to balance the cluster.
    - has_persisted_state -- Determines whether this is a persistent service which stores states on the local disk. If it is then the value of this property is true, if not it is false.
    - high_key -- Specify the upper bound of the partition key range that should be split between the partition ‘Count’ This is only used with UniformInt64 partition scheme.
    - instance_count -- Specify the instance count for the stateless service. If -1 is used, it means it will run on all the nodes.
    - low_key -- Specify the lower bound of the partition key range that should be split between the partition ‘Count’ This is only used with UniformInt64 partition scheme.
    - min_instance_count -- Specify the minimum number of instances that must be up to meet the EnsureAvailability safety check during operations like upgrade or deactivate node. The actual number that is used is max( MinInstanceCount, ceil( MinInstancePercentage/100.0 * InstanceCount) ). Note, if InstanceCount is set to -1, during MinInstanceCount computation -1 is first converted into the number of nodes on which the instances are allowed to be placed according to the placement constraints on the service.
    - min_instance_percentage -- Specify the minimum percentage of InstanceCount that must be up to meet the EnsureAvailability safety check during operations like upgrade or deactivate node. The actual number that is used is max( MinInstanceCount, ceil( MinInstancePercentage/100.0 * InstanceCount) ). Note, if InstanceCount is set to -1, during MinInstancePercentage computation, -1 is first converted into the number of nodes on which the instances are allowed to be placed according to the placement constraints on the service. Allowed values are from 0 to 100.
    - min_replica_set_size -- Specify the min replica set size for the stateful service.
    - partition_count -- Specify the number of partitions. This is only used with UniformInt64 partition scheme.
    - partition_names -- Specify the array for the names of the partitions. This is only used with Named partition scheme.
    - partition_scheme -- Specify what partition scheme to use. Singleton partitions are typically used when the service does not require any additional routing. UniformInt64 means that each partition owns a range of int64 keys. Named is usually for services with data that can be bucketed, within a bounded set. Some common examples of data fields used as named partition keys would be regions, postal codes, customer groups, or other business boundaries.
    - placement_constraints -- Specify the placement constraints as a string. Placement constraints are boolean expressions on node properties and allow for restricting a service to particular nodes based on the service requirements. For example, to place a service on nodes where NodeType is blue specify the following: "NodeColor == blue)".
    - quorum_loss_wait_duration -- Specify the maximum duration for which a partition is allowed to be in a state of quorum loss, represented in ISO 8601 format "hh:mm:ss".
    - replica_restart_wait_duration -- Specify the duration between when a replica goes down and when a new replica is created, represented in ISO 8601 format "hh:mm:ss".
    - service_package_activation_mode -- Specify the activation mode of the service package.
    - service_placement_time_limit -- Specify the duration for which replicas can stay InBuild before reporting that build is stuck, represented in ISO 8601 format "hh:mm:ss".
    - stand_by_replica_keep_duration -- Specify the definition on how long StandBy replicas should be maintained before being removed, represented in ISO 8601 format "hh:mm:ss".
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - target_replica_set_size -- Specify the target replica set size for the stateful service.
    '''
    return _call_az("az sf managed-service create", locals())


def update(application, cluster_name, name, resource_group, default_move_cost=None, instance_count=None, min_instance_count=None, min_instance_percentage=None, min_replica_set_size=None, placement_constraints=None, quorum_loss_wait_duration=None, replica_restart_wait_duration=None, service_placement_time_limit=None, stand_by_replica_keep_duration=None, tags=None, target_replica_set_size=None):
    '''
    Update a managed service.

    Required Parameters:
    - application -- Specify the name of the service.
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - name -- Specify the name of the service.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - default_move_cost -- Specify the default cost for a move. Higher costs make it less likely that the Cluster Resource Manager will move the replica when trying to balance the cluster.
    - instance_count -- Specify the instance count for the stateless service. If -1 is used, it means it will run on all the nodes.
    - min_instance_count -- Specify the minimum number of instances that must be up to meet the EnsureAvailability safety check during operations like upgrade or deactivate node. The actual number that is used is max( MinInstanceCount, ceil( MinInstancePercentage/100.0 * InstanceCount) ). Note, if InstanceCount is set to -1, during MinInstanceCount computation -1 is first converted into the number of nodes on which the instances are allowed to be placed according to the placement constraints on the service.
    - min_instance_percentage -- Specify the minimum percentage of InstanceCount that must be up to meet the EnsureAvailability safety check during operations like upgrade or deactivate node. The actual number that is used is max( MinInstanceCount, ceil( MinInstancePercentage/100.0 * InstanceCount) ). Note, if InstanceCount is set to -1, during MinInstancePercentage computation, -1 is first converted into the number of nodes on which the instances are allowed to be placed according to the placement constraints on the service. Allowed values are from 0 to 100.
    - min_replica_set_size -- Specify the min replica set size for the stateful service.
    - placement_constraints -- Specify the placement constraints as a string. Placement constraints are boolean expressions on node properties and allow for restricting a service to particular nodes based on the service requirements. For example, to place a service on nodes where NodeType is blue specify the following: "NodeColor == blue)".
    - quorum_loss_wait_duration -- Specify the maximum duration for which a partition is allowed to be in a state of quorum loss, represented in ISO 8601 format "hh:mm:ss".
    - replica_restart_wait_duration -- Specify the duration between when a replica goes down and when a new replica is created, represented in ISO 8601 format "hh:mm:ss".
    - service_placement_time_limit -- Specify the duration for which replicas can stay InBuild before reporting that build is stuck, represented in ISO 8601 format "hh:mm:ss".
    - stand_by_replica_keep_duration -- Specify the definition on how long StandBy replicas should be maintained before being removed, represented in ISO 8601 format "hh:mm:ss".
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - target_replica_set_size -- Specify the target replica set size for the stateful service.
    '''
    return _call_az("az sf managed-service update", locals())

