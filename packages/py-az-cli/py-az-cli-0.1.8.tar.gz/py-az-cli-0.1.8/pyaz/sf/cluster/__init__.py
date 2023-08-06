'''
Manage an Azure Service Fabric cluster.
'''
from ... pyaz_utils import _call_az
from . import client_certificate, durability, node, node_type, reliability, setting, upgrade_type


def show(cluster_name, resource_group):
    '''
    

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sf cluster show", locals())


def list(resource_group=None):
    '''
    List cluster resources.

    Optional Parameters:
    - resource_group -- The resource group name
    '''
    return _call_az("az sf cluster list", locals())


def create(resource_group, certificate_file=None, certificate_output_folder=None, certificate_password=None, certificate_subject_name=None, cluster_name=None, cluster_size=None, location=None, parameter_file=None, secret_identifier=None, template_file=None, vault_name=None, vault_rg=None, vm_os=None, vm_password=None, vm_sku=None, vm_user_name=None):
    '''
    Create a new Azure Service Fabric cluster.

    Required Parameters:
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - certificate_file -- The existing certificate file path for the primary cluster certificate.
    - certificate_output_folder -- The folder of the new certificate file to be created.
    - certificate_password -- The password of the certificate file.
    - certificate_subject_name -- The subject name of the certificate to be created.
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - cluster_size -- The number of nodes in the cluster. Default are 5 nodes
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - parameter_file -- The path to the template parameter file.
    - secret_identifier -- The existing Azure key vault secret URL
    - template_file -- The path to the template file.
    - vault_name -- Azure key vault name, it not given it will be the cluster resource group name
    - vault_rg -- Key vault resource group name, if not given it will be cluster resource group name
    - vm_os -- The Operating System of the VMs that make up the cluster.
    - vm_password -- The password of the Vm
    - vm_sku -- VM Sku
    - vm_user_name -- The user name for logging to Vm. Default will be adminuser
    '''
    return _call_az("az sf cluster create", locals())

