'''
Manage retention policy for Azure Container Registries.
'''
from .... pyaz_utils import _call_az

def show(registry, resource_group=None):
    '''
    Show the configured retention policy for an Azure Container Registry.

    Required Parameters:
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr config retention show", locals())


def update(registry, type, days=None, resource_group=None, status=None):
    '''
    Update retention policy for an Azure Container Registry.

    Required Parameters:
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`
    - type -- The type of retention policy.

    Optional Parameters:
    - days -- The number of days to retain an untagged manifest after which it gets purged (Range: 0 to 365). Value "0" will delete untagged manifests immediately.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - status -- Indicates whether retention policy is enabled.
    '''
    return _call_az("az acr config retention update", locals())

