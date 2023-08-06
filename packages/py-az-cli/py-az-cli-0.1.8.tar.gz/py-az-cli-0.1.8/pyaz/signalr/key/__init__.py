'''
Manage keys for Azure SignalR Service.
'''
from ... pyaz_utils import _call_az

def list(name, resource_group):
    '''
    List the access keys for a SignalR Service.

    Required Parameters:
    - name -- Name of signalr service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az signalr key list", locals())


def renew(key_type, name, resource_group):
    '''
    Regenerate the access key for a SignalR Service.

    Required Parameters:
    - key_type -- The name of access key to regenerate
    - name -- Name of signalr service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az signalr key renew", locals())

