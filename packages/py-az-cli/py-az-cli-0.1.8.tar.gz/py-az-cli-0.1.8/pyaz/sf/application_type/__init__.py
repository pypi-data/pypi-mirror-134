from ... pyaz_utils import _call_az
from . import version


def list(cluster_name, resource_group):
    '''
    List application types of a given cluster.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sf application-type list", locals())


def delete(cluster_name, name, resource_group):
    '''
    Delete an application type.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - name -- Specify the application type name.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sf application-type delete", locals())


def show(cluster_name, name, resource_group):
    '''
    Show the properties of an application type on an Azure Service Fabric cluster.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - name -- Specify the application type name.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sf application-type show", locals())


def create(cluster_name, name, resource_group):
    '''
    Create a new application type on an Azure Service Fabric cluster.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - name -- Specify the application type name.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sf application-type create", locals())

