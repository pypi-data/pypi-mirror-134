from .... pyaz_utils import _call_az

def list(cluster_name, name, resource_group):
    '''
    List versions of a given managed application type.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - name -- Specify the application type name.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sf managed-application-type version list", locals())


def delete(cluster_name, name, resource_group, version):
    '''
    Delete a managed application type version.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - name -- Specify the application type name.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    - version -- Specify the application type version.
    '''
    return _call_az("az sf managed-application-type version delete", locals())


def show(cluster_name, name, resource_group, version):
    '''
    Show the properties of a managed application type version on an Azure Service Fabric managed cluster.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - name -- Specify the application type name.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    - version -- Specify the application type version.
    '''
    return _call_az("az sf managed-application-type version show", locals())


def create(cluster_name, name, package_url, resource_group, version, tags=None):
    '''
    Create a new managed application type on an Azure Service Fabric managed cluster.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - name -- Specify the application type name.
    - package_url -- Specify the url of the application package sfpkg file.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    - version -- Specify the application type version.

    Optional Parameters:
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az sf managed-application-type version create", locals())


def update(cluster_name, name, resource_group, version, package_url=None, tags=None):
    '''
    Update a managed application type version.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - name -- Specify the application type name.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    - version -- Specify the application type version.

    Optional Parameters:
    - package_url -- Specify the url of the application package sfpkg file.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az sf managed-application-type version update", locals())

