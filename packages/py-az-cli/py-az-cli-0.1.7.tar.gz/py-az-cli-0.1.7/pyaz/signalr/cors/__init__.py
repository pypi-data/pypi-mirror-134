'''
Manage CORS for Azure SignalR Service.
'''
from ... pyaz_utils import _call_az

def add(allowed_origins, name, resource_group):
    '''
    Add allowed origins to a SignalR Service

    Required Parameters:
    - allowed_origins -- space separated origins that should be allowed to make cross-origin calls (for example: http://example.com:12345). To allow all, use "*"
    - name -- Name of signalr service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az signalr cors add", locals())


def remove(allowed_origins, name, resource_group):
    '''
    Remove allowed origins from a SignalR Service

    Required Parameters:
    - allowed_origins -- space separated origins that should be allowed to make cross-origin calls (for example: http://example.com:12345). To allow all, use "*"
    - name -- Name of signalr service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az signalr cors remove", locals())


def list(name, resource_group):
    '''
    List allowed origins of a SignalR Service

    Required Parameters:
    - name -- Name of signalr service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az signalr cors list", locals())


def update(allowed_origins, name, resource_group):
    '''
    Update allowed origins to a SignalR Service

    Required Parameters:
    - allowed_origins -- space separated origins that should be allowed to make cross-origin calls (for example: http://example.com:12345). To allow all, use "*"
    - name -- Name of signalr service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az signalr cors update", locals())

