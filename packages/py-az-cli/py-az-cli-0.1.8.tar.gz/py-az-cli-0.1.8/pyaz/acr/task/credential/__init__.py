'''
Manage credentials for a task. Please see https://aka.ms/acr/tasks/cross-registry-authentication for more information.
'''
from .... pyaz_utils import _call_az

def add(login_server, name, registry, password=None, resource_group=None, use_identity=None, username=None):
    '''
    Add a custom registry login credential to the task

    Required Parameters:
    - login_server -- The login server of the custom registry. For instance, 'myregistry.azurecr.io'.
    - name -- The name of the task.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - password -- The password to login to the custom registry. This can be plain text or a key vault secret URI.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - use_identity -- The task managed identity used for the credential. Use '[system]' to refer to the system-assigned identity or a client id to refer to a user-assigned identity. Please see https://aka.ms/acr/tasks/cross-registry-authentication for more information.
    - username -- The username to login to the custom registry. This can be plain text or a key vault secret URI.
    '''
    return _call_az("az acr task credential add", locals())


def update(login_server, name, registry, password=None, resource_group=None, use_identity=None, username=None):
    '''
    Update the registry login credential for a task.

    Required Parameters:
    - login_server -- The login server of the custom registry. For instance, 'myregistry.azurecr.io'.
    - name -- The name of the task.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - password -- The password to login to the custom registry. This can be plain text or a key vault secret URI.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - use_identity -- The task managed identity used for the credential. Use '[system]' to refer to the system-assigned identity or a client id to refer to a user-assigned identity. Please see https://aka.ms/acr/tasks/cross-registry-authentication for more information.
    - username -- The username to login to the custom registry. This can be plain text or a key vault secret URI.
    '''
    return _call_az("az acr task credential update", locals())


def remove(login_server, name, registry, resource_group=None):
    '''
    Remove credential for a task.

    Required Parameters:
    - login_server -- The login server of the custom registry. For instance, 'myregistry.azurecr.io'.
    - name -- The name of the task.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr task credential remove", locals())


def list(name, registry, resource_group=None):
    '''
    List all the custom registry credentials for task.

    Required Parameters:
    - name -- The name of the task.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr task credential list", locals())

