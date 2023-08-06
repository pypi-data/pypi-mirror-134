from .... pyaz_utils import _call_az

def show(registry, resource_group=None):
    '''
    Show the configured content-trust policy for an Azure Container Registry.

    Required Parameters:
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr config content-trust show", locals())


def update(registry, resource_group=None, status=None):
    '''
    Update content-trust policy for an Azure Container Registry.

    Required Parameters:
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - status -- Indicates whether content-trust is enabled.
    '''
    return _call_az("az acr config content-trust update", locals())

