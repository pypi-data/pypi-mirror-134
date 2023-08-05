from .... pyaz_utils import _call_az

def create(application, cluster_name, metric_name, name, resource_group, default_load=None, primary_default_load=None, secondary_default_load=None, weight=None):
    '''
    Create a new managed service load metric on an Azure Service Fabric managed cluster.

    Required Parameters:
    - application -- Specify the name of the service.
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - metric_name -- Specify the name of the metric.
    - name -- Specify the name of the service.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - default_load -- Specify the default amount of load, as a number, that this service creates for this metric. Used only for Stateless services.
    - primary_default_load -- Specify the default amount of load, as a number, that this service creates for this metric when it is a Primary replica. Used only for Stateful services.
    - secondary_default_load -- Specify the default amount of load, as a number, that this service creates for this metric when it is a Secondary replica. Used only for Stateful services.
    - weight -- Specify the service load metric relative weight, compared to other metrics configured for this service, as a number.
    '''
    return _call_az("az sf managed-service load-metrics create", locals())


def update(application, cluster_name, metric_name, name, resource_group, default_load=None, primary_default_load=None, secondary_default_load=None, weight=None):
    '''
    Update a managed service.

    Required Parameters:
    - application -- Specify the name of the service.
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - metric_name -- Specify the name of the metric.
    - name -- Specify the name of the service.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - default_load -- Specify the default amount of load, as a number, that this service creates for this metric. Used only for Stateless services.
    - primary_default_load -- Specify the default amount of load, as a number, that this service creates for this metric when it is a Primary replica. Used only for Stateful services.
    - secondary_default_load -- Specify the default amount of load, as a number, that this service creates for this metric when it is a Secondary replica. Used only for Stateful services.
    - weight -- Specify the service load metric relative weight, compared to other metrics configured for this service, as a number.
    '''
    return _call_az("az sf managed-service load-metrics update", locals())


def delete(application, cluster_name, metric_name, name, resource_group):
    '''
    Delete a managed service.

    Required Parameters:
    - application -- Specify the name of the service.
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - metric_name -- Specify the name of the metric.
    - name -- Specify the name of the service.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sf managed-service load-metrics delete", locals())

