'''
Manage helm chart repositories for Azure Container Registries.
'''
from .... pyaz_utils import _call_az

def add(name, password=None, repository=None, resource_group=None, suffix=None, username=None):
    '''
    Add a helm chart repository from an Azure Container Registry through the Helm CLI.

    Required Parameters:
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - password -- The password used to log into a container registry
    - repository -- ==SUPPRESS==
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - suffix -- The tenant suffix in registry login server. You may specify '--suffix tenant' if your registry login server is in the format 'registry-tenant.azurecr.io'. Applicable if you're accessing the registry from a different subscription or you have permission to access images but not the permission to manage the registry resource.
    - username -- The username used to log into a container registry
    '''
    return _call_az("az acr helm repo add", locals())

