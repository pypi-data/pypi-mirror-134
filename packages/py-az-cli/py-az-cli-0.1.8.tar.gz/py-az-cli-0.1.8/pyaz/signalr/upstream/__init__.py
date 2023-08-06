'''
Manage upstream settings.
'''
from ... pyaz_utils import _call_az

def list(name, resource_group):
    '''
    List upstream settings of an existing SignalR Service.

    Required Parameters:
    - name -- Name of signalr service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az signalr upstream list", locals())


def update(name, resource_group, template):
    '''
    Update order sensitive upstream settings for an existing SignalR Service.

    Required Parameters:
    - name -- Name of signalr service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - template -- Template item for upstream settings. Use key=value pattern to set properties. Supported keys are "url-template", "hub-pattern", "event-pattern", "category-pattern".
    '''
    return _call_az("az signalr upstream update", locals())


def clear(name, resource_group):
    '''
    List upstream settings of an existing SignalR Service.

    Required Parameters:
    - name -- Name of signalr service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az signalr upstream clear", locals())

