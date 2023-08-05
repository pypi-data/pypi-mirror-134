'''
Manage Azure SignalR Service.
'''
from .. pyaz_utils import _call_az
from . import cors, identity, key, network_rule, upstream


def create(name, resource_group, sku, allowed_origins=None, default_action=None, enable_message_logs=None, location=None, service_mode=None, tags=None, unit_count=None):
    '''
    Creates a SignalR Service.

    Required Parameters:
    - name -- Name of signalr service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sku -- The sku name of the signalr service. E.g. Standard_S1

    Optional Parameters:
    - allowed_origins -- space separated origins that should be allowed to make cross-origin calls (for example: http://example.com:12345). To allow all, use "*"
    - default_action -- Default action to apply when no rule matches.
    - enable_message_logs -- The switch for messaging logs which signalr service will generate or not
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - service_mode -- The service mode which signalr service will be working on
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - unit_count -- The number of signalr service unit count
    '''
    return _call_az("az signalr create", locals())


def delete(name, resource_group):
    '''
    Deletes a SignalR Service.

    Required Parameters:
    - name -- Name of signalr service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az signalr delete", locals())


def list(resource_group=None):
    '''
    Lists all the SignalR Service under the current subscription.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az signalr list", locals())


def show(name, resource_group):
    '''
    Get the details of a SignalR Service.

    Required Parameters:
    - name -- Name of signalr service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az signalr show", locals())


def restart(name, resource_group):
    '''
    Restart an existing SignalR Service.

    Required Parameters:
    - name -- Name of signalr service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az signalr restart", locals())


def update(name, resource_group, add=None, allowed_origins=None, default_action=None, enable_message_logs=None, force_string=None, remove=None, service_mode=None, set=None, sku=None, tags=None, unit_count=None):
    '''
    Update an existing SignalR Service.

    Required Parameters:
    - name -- Name of signalr service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - allowed_origins -- space separated origins that should be allowed to make cross-origin calls (for example: http://example.com:12345). To allow all, use "*"
    - default_action -- Default action to apply when no rule matches.
    - enable_message_logs -- The switch for messaging logs which signalr service will generate or not
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - service_mode -- The service mode which signalr service will be working on
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - sku -- The sku name of the signalr service. E.g. Standard_S1
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - unit_count -- The number of signalr service unit count
    '''
    return _call_az("az signalr update", locals())

