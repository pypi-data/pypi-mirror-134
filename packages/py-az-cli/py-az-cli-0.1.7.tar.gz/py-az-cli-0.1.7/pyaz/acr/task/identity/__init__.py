'''
Managed Identities for Task. Please see https://aka.ms/acr/tasks/task-create-managed-identity for more information.
'''
from .... pyaz_utils import _call_az

def assign(name, registry, identities=None, resource_group=None):
    '''
    Update the managed identity for a task.

    Required Parameters:
    - name -- The name of the task.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - identities -- Assigns managed identities to the task. Use '[system]' to refer to the system-assigned identity or a resource ID to refer to a user-assigned identity.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr task identity assign", locals())


def remove(name, registry, identities=None, resource_group=None):
    '''
    Remove managed identities for a task.

    Required Parameters:
    - name -- The name of the task.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - identities -- Assigns managed identities to the task. Use '[system]' to refer to the system-assigned identity or a resource ID to refer to a user-assigned identity.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr task identity remove", locals())


def show(name, registry, resource_group=None):
    '''
    Display the managed identities for task.

    Required Parameters:
    - name -- The name of the task.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr task identity show", locals())

