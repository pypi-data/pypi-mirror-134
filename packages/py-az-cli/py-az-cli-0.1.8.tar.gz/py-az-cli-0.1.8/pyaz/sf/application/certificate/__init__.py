'''
Manage the certificate of an application.
'''
from .... pyaz_utils import _call_az

def add(cluster_name, resource_group, certificate_file=None, certificate_output_folder=None, certificate_password=None, certificate_subject_name=None, secret_identifier=None, vault_name=None, vault_rg=None):
    '''
    Add a new certificate to the Virtual Machine Scale Sets that make up the cluster to be used by hosted applications.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - certificate_file -- The existing certificate file path for the primary cluster certificate.
    - certificate_output_folder -- The folder of the new certificate file to be created.
    - certificate_password -- The password of the certificate file.
    - certificate_subject_name -- The subject name of the certificate to be created.
    - secret_identifier -- The existing Azure key vault secret URL
    - vault_name -- Azure key vault name, it not given it will be the cluster resource group name
    - vault_rg -- Key vault resource group name, if not given it will be cluster resource group name
    '''
    return _call_az("az sf application certificate add", locals())

