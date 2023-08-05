from .... pyaz_utils import _call_az

def create(application, cluster_name, correlated_service_name, name, resource_group, scheme):
    '''
    Create a new managed service correlation scheme on an Azure Service Fabric managed cluster.

    Required Parameters:
    - application -- Specify the name of the service.
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - correlated_service_name -- Specify the Arm Resource ID of the service that the correlation relationship is established with.
    - name -- Specify the name of the service.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    - scheme -- Specify the ServiceCorrelationScheme which describes the relationship between this service and the service specified via correlated_service_name.
    '''
    return _call_az("az sf managed-service correlation-scheme create", locals())


def update(application, cluster_name, correlated_service_name, name, resource_group, scheme):
    '''
    Update a managed service correlation scheme.

    Required Parameters:
    - application -- Specify the name of the service.
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - correlated_service_name -- Specify the Arm Resource ID of the service that the correlation relationship is established with.
    - name -- Specify the name of the service.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    - scheme -- Specify the ServiceCorrelationScheme which describes the relationship between this service and the service specified via correlated_service_name.
    '''
    return _call_az("az sf managed-service correlation-scheme update", locals())


def delete(application, cluster_name, correlated_service_name, name, resource_group):
    '''
    Delete a managed service correlation scheme.

    Required Parameters:
    - application -- Specify the name of the service.
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - correlated_service_name -- Specify the Arm Resource ID of the service that the correlation relationship is established with.
    - name -- Specify the name of the service.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sf managed-service correlation-scheme delete", locals())

