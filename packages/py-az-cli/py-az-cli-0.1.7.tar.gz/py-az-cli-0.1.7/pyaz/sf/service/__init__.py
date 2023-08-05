'''
Manage services running on an Azure Service Fabric cluster. Only support ARM deployed services.
'''
from ... pyaz_utils import _call_az

def list(application_name, cluster_name, resource_group):
    '''
    List services of a given application.

    Required Parameters:
    - application_name -- The name of the application resource.
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sf service list", locals())


def delete(application_name, cluster_name, name, resource_group):
    '''
    Delete a service.

    Required Parameters:
    - application_name -- The name of the application resource.
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - name -- Specify the name of the service. The application name must be a prefix of the service name, for example: appName~serviceName
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sf service delete", locals())


def show(application_name, cluster_name, name, resource_group):
    '''
    Get a service.

    Required Parameters:
    - application_name -- The name of the application resource.
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - name -- Specify the name of the service. The application name must be a prefix of the service name, for example: appName~serviceName
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sf service show", locals())


def create(application, cluster_name, name, resource_group, service_type, state, default_move_cost=None, instance_count=None, min_replica_set_size=None, partition_scheme=None, target_replica_set_size=None):
    '''
    Create a new service on an Azure Service Fabric cluster.

    Required Parameters:
    - application -- Specify the name of the service. The application name must be a prefix of the service name, for example: appName~serviceName
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - name -- Specify the name of the service. The application name must be a prefix of the service name, for example: appName~serviceName
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    - service_type -- Specify the service type name of the application, it should exist in the application manifest.
    - state -- Specify if the service is stateless or stateful.

    Optional Parameters:
    - default_move_cost -- Specify the default cost for a move. Higher costs make it less likely that the Cluster Resource Manager will move the replica when trying to balance the cluster.
    - instance_count -- Specify the instance count for the stateless service. If -1 is used, it means it will run on all the nodes.
    - min_replica_set_size -- Specify the min replica set size for the stateful service.
    - partition_scheme -- Specify what partition scheme to use. Singleton partitions are typically used when the service does not require any additional routing. UniformInt64 means that each partition owns a range of int64 keys. Named is usually for services with data that can be bucketed, within a bounded set. Some common examples of data fields used as named partition keys would be regions, postal codes, customer groups, or other business boundaries.
    - target_replica_set_size -- Specify the target replica set size for the stateful service.
    '''
    return _call_az("az sf service create", locals())

