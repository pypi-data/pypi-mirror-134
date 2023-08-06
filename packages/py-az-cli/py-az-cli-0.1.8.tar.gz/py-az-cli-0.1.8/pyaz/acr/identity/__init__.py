'''
Manage service (managed) identities for a container registry
'''
from ... pyaz_utils import _call_az

def show(name, resource_group=None):
    '''
    Show the container registry's identity details

    Required Parameters:
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr identity show", locals())


def assign(identities, name, resource_group=None):
    '''
    Assign a managed identity to a container registry

    Required Parameters:
    - identities -- Space-separated identities. Use '[system]' to refer to the system assigned identity
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr identity assign", locals())


def remove(identities, name, resource_group=None):
    '''
    Remove a managed identity from a container registry

    Required Parameters:
    - identities -- Space-separated identities. Use '[system]' to refer to the system assigned identity
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr identity remove", locals())

