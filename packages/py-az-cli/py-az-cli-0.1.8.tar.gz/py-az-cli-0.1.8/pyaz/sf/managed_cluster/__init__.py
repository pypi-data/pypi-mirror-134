from ... pyaz_utils import _call_az
from . import client_certificate


def list(resource_group=None):
    '''
    List managed clusters.

    Optional Parameters:
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sf managed-cluster list", locals())


def delete(cluster_name, resource_group):
    '''
    Delete a managed cluster.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sf managed-cluster delete", locals())


def show(cluster_name, resource_group):
    '''
    Show the properties of an Azure Service Fabric managed cluster.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sf managed-cluster show", locals())


def create(admin_password, cluster_name, resource_group, admin_user_name=None, client_cert_common_name=None, client_cert_is_admin=None, client_cert_issuer_thumbprint=None, client_cert_thumbprint=None, client_connection_port=None, cluster_code_version=None, cluster_upgrade_cadence=None, cluster_upgrade_mode=None, dns_name=None, gateway_connection_port=None, location=None, sku=None, tags=None):
    '''
    Delete a managed cluster.

    Required Parameters:
    - admin_password -- Admin password used for the virtual machines.
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - admin_user_name -- Admin user used for the virtual machines.
    - client_cert_common_name -- Client certificate common name.
    - client_cert_is_admin -- Client authentication type.
    - client_cert_issuer_thumbprint -- Space-separated list of issuer thumbprints.
    - client_cert_thumbprint -- Client certificate thumbprint.
    - client_connection_port -- Port used for client connections to the cluster.
    - cluster_code_version -- Cluster service fabric code version. Only use if upgrade mode is Manual.
    - cluster_upgrade_cadence -- The upgrade mode of the cluster when new Service Fabric runtime version is available Wave0: Cluster upgrade starts immediately after a new version is rolled out. Recommended for Test/Dev clusters.Wave1: Cluster upgrade starts 7 days after a new version is rolled out. Recommended for Pre-prod clusters.Wave2: Cluster upgrade starts 14 days after a new version is rolled out. Recommended for Production clusters.
    - cluster_upgrade_mode -- The upgrade mode of the cluster when new Service Fabric runtime version is available Automatic: The cluster will be automatically upgraded to the latest Service Fabric runtime version, upgrade_cadence will determine when the upgrade starts after the new version becomes available.Manual: The cluster will not be automatically upgraded to the latest Service Fabric runtime version. The cluster is upgraded by setting the code_version property in the cluster resource.
    - dns_name -- Cluster's dns name.
    - gateway_connection_port -- Port used for http connections to the cluster.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - sku -- Cluster's Sku, the options are Basic: it will have a minimum of 3 seed nodes and only allows 1 node type and Standard: it will have a minimum of 5 seed nodes and allows multiple node types.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az sf managed-cluster create", locals())


def update(cluster_name, resource_group, client_connection_port=None, dns_name=None, gateway_connection_port=None, tags=None):
    '''
    Update a managed cluster.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - client_connection_port -- Port used for client connections to the cluster.
    - dns_name -- Cluster's dns name
    - gateway_connection_port -- Port used for http connections to the cluster.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az sf managed-cluster update", locals())

