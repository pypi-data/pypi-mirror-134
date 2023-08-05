'''
Manage applications running on an Azure Service Fabric cluster. Only support ARM deployed applications.
'''
from ... pyaz_utils import _call_az
from . import certificate


def list(cluster_name, resource_group):
    '''
    List applications of a given cluster.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sf application list", locals())


def delete(cluster_name, name, resource_group):
    '''
    Delete an application.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - name -- Specify the application name.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sf application delete", locals())


def show(cluster_name, name, resource_group):
    '''
    Show the properties of an application on an Azure Service Fabric cluster.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - name -- Specify the application name.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sf application show", locals())


def create(cluster_name, name, resource_group, type_name, version, max_nodes=None, min_nodes=None, package_url=None, parameters=None):
    '''
    Create a new application on an Azure Service Fabric cluster.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - name -- Specify the application name.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    - type_name -- Specify the application type name.
    - version -- Specify the application type version.

    Optional Parameters:
    - max_nodes -- Specify the maximum number of nodes on which to place an application. The value of this parameter must be a non-negative integer. The default value is 0, which indicates the application can be placed on any number of nodes in the cluster.
    - min_nodes -- Specify the minimum number of nodes where Service Fabric will reserve capacity for this application, this does not mean that the application is guaranteed to have replicas on all those nodes. The value of this parameter must be a non-negative integer. Default value for this is zero, which means no capacity is reserved for the application.
    - package_url -- Specify the url of the application package sfpkg file.
    - parameters -- Specify the application parameters as key/value pairs. These parameters must exist in the application manifest. for example: --application-parameters param1=value1 param2=value2
    '''
    return _call_az("az sf application create", locals())


def update(cluster_name, name, resource_group, failure_action=None, force_restart=None, hc_retry_timeout=None, hc_stable_duration=None, hc_wait_duration=None, max_nodes=None, max_porcent_unhealthy_apps=None, max_porcent_unhealthy_partitions=None, max_porcent_unhealthy_replicas=None, max_porcent_unhealthy_services=None, min_nodes=None, parameters=None, service_type_health_policy_map=None, ud_timeout=None, upgrade_replica_set_check_timeout=None, upgrade_timeout=None, version=None, warning_as_error=None):
    '''
    Update a Azure Service Fabric application. This allows updating the application parameters and/or upgrade the application type version which will trigger an application upgrade.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - name -- Specify the application name.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - failure_action -- Specify the action to take if the monitored upgrade fails. The acceptable values for this parameter are Rollback or Manual.
    - force_restart -- Indicates that the service host restarts even if the upgrade is a configuration-only change.
    - hc_retry_timeout -- Specify the duration, in seconds, after which Service Fabric retries the health check if the previous health check fails.
    - hc_stable_duration -- Specify the duration, in seconds, that Service Fabric waits in order to verify that the application is stable before moving to the next upgrade domain or completing the upgrade. This wait duration prevents undetected changes of health right after the health check is performed.
    - hc_wait_duration -- Specify the duration, in seconds, that Service Fabric waits before it performs the initial health check after it finishes the upgrade on the upgrade domain.
    - max_nodes -- Specify the maximum number of nodes on which to place an application. The value of this parameter must be a non-negative integer. The default value is 0, which indicates the application can be placed on any number of nodes in the cluster.
    - max_porcent_unhealthy_apps -- Specify the maximum percentage of the application instances deployed on the nodes in the cluster that have a health state of error before the application health state for the cluster is error. Allowed values are form 0 to 100.
    - max_porcent_unhealthy_partitions -- Specify the maximum percent of unhelthy partitions per service allowed by the health policy for the default service type to use for the monitored upgrade. Allowed values are form 0 to 100.
    - max_porcent_unhealthy_replicas -- Specify the maximum percent of unhelthy replicas per service allowed by the health policy for the default service type to use for the monitored upgrade. Allowed values are form 0 to 100.
    - max_porcent_unhealthy_services -- Specify the maximum percent of unhelthy services allowed by the health policy for the default service type to use for the monitored upgrade. Allowed values are form 0 to 100.
    - min_nodes -- Specify the minimum number of nodes where Service Fabric will reserve capacity for this application, this does not mean that the application is guaranteed to have replicas on all those nodes. The value of this parameter must be a non-negative integer. Default value for this is zero, which means no capacity is reserved for the application.
    - parameters -- Specify the application parameters as key/value pairs. These parameters must exist in the application manifest. for example: --application-parameters param1=value1 param2=value2
    - service_type_health_policy_map -- Specify the map of the health policy to use for different service types as a hash table in the following format: {"ServiceTypeName" : "MaxPercentUnhealthyPartitionsPerService,MaxPercentUnhealthyReplicasPerPartition,MaxPercentUnhealthyServices"}. For example: @{ "ServiceTypeName01" = "5,10,5"; "ServiceTypeName02" = "5,5,5" }
    - ud_timeout -- Specify the maximum time, in seconds, that Service Fabric takes to upgrade a single upgrade domain. After this period, the upgrade fails.
    - upgrade_replica_set_check_timeout -- Specify the maximum time, in seconds, that Service Fabric waits for a service to reconfigure into a safe state, if not already in a safe state, before Service Fabric proceeds with the upgrade.
    - upgrade_timeout -- Specify the maximum time, in seconds, that Service Fabric takes for the entire upgrade. After this period, the upgrade fails.
    - version -- Specify the application type version.
    - warning_as_error -- Indicates whether to treat a warning health event as an error event during health evaluation.
    '''
    return _call_az("az sf application update", locals())

