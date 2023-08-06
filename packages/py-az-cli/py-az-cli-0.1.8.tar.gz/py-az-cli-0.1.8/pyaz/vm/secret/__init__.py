'''
Manage VM secrets.
'''
from ... pyaz_utils import _call_az

def format(secrets, certificate_store=None, keyvault=None, resource_group=None):
    '''
    Transform secrets into a form that can be used by VMs and VMSSes.

    Required Parameters:
    - secrets -- Space-separated list of key vault secret URIs. Perhaps, produced by 'az keyvault secret list-versions --vault-name vaultname -n cert1 --query "[?attributes.enabled].id" -o tsv'

    Optional Parameters:
    - certificate_store -- Windows certificate store names. Default: My
    - keyvault -- Name or ID of the key vault.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vm secret format", locals())


def add(certificate, keyvault, name, resource_group, certificate_store=None):
    '''
    Add a secret to a VM.

    Required Parameters:
    - certificate -- key vault certificate name or its full secret URL
    - keyvault -- Name or ID of the key vault.
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - certificate_store -- Windows certificate store names. Default: My
    '''
    return _call_az("az vm secret add", locals())


def list(name, resource_group):
    '''
    List secrets on a VM.

    Required Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vm secret list", locals())


def remove(keyvault, name, resource_group, certificate=None):
    '''
    Remove a secret from a VM.

    Required Parameters:
    - keyvault -- Name or ID of the key vault.
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - certificate -- key vault certificate name or its full secret URL
    '''
    return _call_az("az vm secret remove", locals())

