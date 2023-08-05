from .... pyaz_utils import _call_az

def create(name, resource_group, vm, capture_limit=None, capture_size=None, file_path=None, filters=None, storage_account=None, storage_path=None, time_limit=None):
    '''
    Create and start a packet capture session.

    Required Parameters:
    - name -- Name of the packet capture session.
    - resource_group -- Name of the resource group the target VM is in.
    - vm -- Name or ID of the VM to target. If the name of the VM is provided, the --resource-group is required.

    Optional Parameters:
    - capture_limit -- None
    - capture_size -- None
    - file_path -- None
    - filters -- None
    - storage_account -- None
    - storage_path -- None
    - time_limit -- None
    '''
    return _call_az("az network watcher packet-capture create", locals())


def show(location, name, network_watcher_name=None):
    '''
    Show details of a packet capture session.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- The name of the packet capture session.

    Optional Parameters:
    - network_watcher_name -- ==SUPPRESS==
    '''
    return _call_az("az network watcher packet-capture show", locals())


def show_status(location, name, network_watcher_name=None):
    '''
    Show the status of a packet capture session.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- The name given to the packet capture session.

    Optional Parameters:
    - network_watcher_name -- ==SUPPRESS==
    '''
    return _call_az("az network watcher packet-capture show-status", locals())


def delete(location, name, network_watcher_name=None):
    '''
    Delete a packet capture session.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- The name of the packet capture session.

    Optional Parameters:
    - network_watcher_name -- ==SUPPRESS==
    '''
    return _call_az("az network watcher packet-capture delete", locals())


def stop(location, name, network_watcher_name=None):
    '''
    Stop a running packet capture session.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- The name of the packet capture session.

    Optional Parameters:
    - network_watcher_name -- ==SUPPRESS==
    '''
    return _call_az("az network watcher packet-capture stop", locals())


def list(location, network_watcher_name=None):
    '''
    List all packet capture sessions within a resource group.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.

    Optional Parameters:
    - network_watcher_name -- ==SUPPRESS==
    '''
    return _call_az("az network watcher packet-capture list", locals())

