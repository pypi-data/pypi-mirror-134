from ..... pyaz_utils import _call_az

def add(connection_monitor, location, type, workspace_id=None):
    '''
    Add an output to a connection monitor

    Required Parameters:
    - connection_monitor -- Connection monitor name.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - type -- Connection monitor output destination type. Currently, only "Workspace" is supported

    Optional Parameters:
    - workspace_id -- The id of log analytics workspace
    '''
    return _call_az("az network watcher connection-monitor output add", locals())


def remove(connection_monitor, location):
    '''
    Remove all outputs from a connection monitor

    Required Parameters:
    - connection_monitor -- Connection monitor name.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    '''
    return _call_az("az network watcher connection-monitor output remove", locals())


def list(connection_monitor, location):
    '''
    List all output from a connection monitor

    Required Parameters:
    - connection_monitor -- Connection monitor name.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    '''
    return _call_az("az network watcher connection-monitor output list", locals())

