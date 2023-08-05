'''
Manage login credentials for Azure Container Registries.
'''
from ... pyaz_utils import _call_az

def show(name, resource_group=None):
    '''
    Get the login credentials for an Azure Container Registry.

    Required Parameters:
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr credential show", locals())


def renew(name, password_name, resource_group=None):
    '''
    Regenerate login credentials for an Azure Container Registry.

    Required Parameters:
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`
    - password_name -- The name of password to regenerate

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr credential renew", locals())

