'''
Manage taskruns using Azure Container Registries.
'''
from ... pyaz_utils import _call_az

def list(registry, resource_group=None):
    '''
    List the taskruns for an Azure Container Registry.

    Required Parameters:
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr taskrun list", locals())


def delete(name, registry, resource_group=None, yes=None):
    '''
    Delete a taskrun from an Azure Container Registry.

    Required Parameters:
    - name -- The name of the taskrun.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az acr taskrun delete", locals())


def show(name, registry, resource_group=None):
    '''
    Get the properties of a named taskrun for an Azure Container Registry.

    Required Parameters:
    - name -- The name of the taskrun.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr taskrun show", locals())


def logs(name, registry, resource_group=None):
    '''
    Show run logs for a particular taskrun.

    Required Parameters:
    - name -- The name of the taskrun.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr taskrun logs", locals())

