'''
Manage managed identity settings.
'''
from ... pyaz_utils import _call_az

def assign(identity, name, resource_group):
    '''
    Assign managed identity for SignalR Service.

    Required Parameters:
    - identity -- Assigns managed identities to the service. Use '[system]' to refer to the system-assigned identity or a resource ID to refer to a user-assigned identity. You can only assign either on of them.
    - name -- Name of signalr service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az signalr identity assign", locals())


def remove(name, resource_group):
    '''
    Remove managed identity for SignalR Service.

    Required Parameters:
    - name -- Name of signalr service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az signalr identity remove", locals())


def show(name, resource_group):
    '''
    Show managed identity for SignalR Service.

    Required Parameters:
    - name -- Name of signalr service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az signalr identity show", locals())

