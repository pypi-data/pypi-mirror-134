'''
Manage helm charts for Azure Container Registries.
'''
from ... pyaz_utils import _call_az
from . import repo


def list(name, password=None, repository=None, resource_group=None, suffix=None, username=None):
    '''
    List all helm charts in an Azure Container Registry.

    Required Parameters:
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - password -- The password used to log into a container registry
    - repository -- ==SUPPRESS==
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - suffix -- The tenant suffix in registry login server. You may specify '--suffix tenant' if your registry login server is in the format 'registry-tenant.azurecr.io'. Applicable if you're accessing the registry from a different subscription or you have permission to access images but not the permission to manage the registry resource.
    - username -- The username used to log into a container registry
    '''
    return _call_az("az acr helm list", locals())


def show(name, password=None, repository=None, resource_group=None, suffix=None, username=None, version=None):
    '''
    Describe a helm chart in an Azure Container Registry.

    Required Parameters:
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - password -- The password used to log into a container registry
    - repository -- ==SUPPRESS==
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - suffix -- The tenant suffix in registry login server. You may specify '--suffix tenant' if your registry login server is in the format 'registry-tenant.azurecr.io'. Applicable if you're accessing the registry from a different subscription or you have permission to access images but not the permission to manage the registry resource.
    - username -- The username used to log into a container registry
    - version -- The helm chart version.
    '''
    return _call_az("az acr helm show", locals())


def delete(name, password=None, prov=None, repository=None, resource_group=None, suffix=None, username=None, version=None, yes=None):
    '''
    Delete a helm chart version in an Azure Container Registry.

    Required Parameters:
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - password -- The password used to log into a container registry
    - prov -- Only delete the provenance file.
    - repository -- ==SUPPRESS==
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - suffix -- The tenant suffix in registry login server. You may specify '--suffix tenant' if your registry login server is in the format 'registry-tenant.azurecr.io'. Applicable if you're accessing the registry from a different subscription or you have permission to access images but not the permission to manage the registry resource.
    - username -- The username used to log into a container registry
    - version -- The helm chart version.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az acr helm delete", locals())


def push(name, force=None, password=None, repository=None, resource_group=None, suffix=None, username=None):
    '''
    Push a helm chart package to an Azure Container Registry.

    Required Parameters:
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - force -- Overwrite the existing chart package.
    - password -- The password used to log into a container registry
    - repository -- ==SUPPRESS==
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - suffix -- The tenant suffix in registry login server. You may specify '--suffix tenant' if your registry login server is in the format 'registry-tenant.azurecr.io'. Applicable if you're accessing the registry from a different subscription or you have permission to access images but not the permission to manage the registry resource.
    - username -- The username used to log into a container registry
    '''
    return _call_az("az acr helm push", locals())


def install_cli(client_version=None, install_location=None, yes=None):
    '''
    Download and install Helm command-line tool.

    Optional Parameters:
    - client_version -- The target Helm CLI version. (Attention: Currently, Helm 3 does not work with "az acr helm" commands) 
    - install_location -- Path at which to install Helm CLI (Existing one at the same path will be overwritten)
    - yes -- Agree to the license of Helm, and do not prompt for confirmation.
    '''
    return _call_az("az acr helm install-cli", locals())

