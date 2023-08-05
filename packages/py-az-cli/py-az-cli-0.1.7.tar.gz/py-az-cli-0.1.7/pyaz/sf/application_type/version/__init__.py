from .... pyaz_utils import _call_az

def list(cluster_name, name, resource_group):
    '''
    List version of a given application type.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - name -- Specify the application type name.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sf application-type version list", locals())


def delete(cluster_name, name, resource_group, version):
    '''
    Delete an application type version.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - name -- Specify the application type name.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    - version -- Specify the application type version.
    '''
    return _call_az("az sf application-type version delete", locals())


def show(cluster_name, name, resource_group, version):
    '''
    Show the properties of an application type version on an Azure Service Fabric cluster.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - name -- Specify the application type name.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    - version -- Specify the application type version.
    '''
    return _call_az("az sf application-type version show", locals())


def create(cluster_name, name, package_url, resource_group, version):
    '''
    Create a new application type on an Azure Service Fabric cluster.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - name -- Specify the application type name.
    - package_url -- Specify the url of the application package sfpkg file.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    - version -- Specify the application type version.
    '''
    return _call_az("az sf application-type version create", locals())

