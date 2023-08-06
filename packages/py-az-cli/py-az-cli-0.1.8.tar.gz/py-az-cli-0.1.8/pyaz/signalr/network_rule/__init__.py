from ... pyaz_utils import _call_az

def list(name, resource_group):
    '''
    Get the Network access control of SignalR Service.

    Required Parameters:
    - name -- Name of signalr service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az signalr network-rule list", locals())


def update(name, resource_group, allow=None, connection_name=None, deny=None, public_network=None):
    '''
    Update the Network access control of SignalR Service.

    Required Parameters:
    - name -- Name of signalr service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - allow -- The allowed virtual network rule. Space-separeted list of scope to assign. Allowed values: ClientConnection, ServerConnection, RESTAPI
    - connection_name -- Space-separeted list of private endpoint connection name.
    - deny -- The denied virtual network rule. Space-separeted list of scope to assign. Allowed values: ClientConnection, ServerConnection, RESTAPI
    - public_network -- Set rules for public network.
    '''
    return _call_az("az signalr network-rule update", locals())

