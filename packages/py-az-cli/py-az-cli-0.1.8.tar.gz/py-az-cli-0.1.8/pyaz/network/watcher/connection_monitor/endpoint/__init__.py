from ..... pyaz_utils import _call_az

def add(connection_monitor, location, name, address=None, address_exclude=None, address_include=None, coverage_level=None, dest_test_groups=None, filter_item=None, filter_type=None, resource_id=None, source_test_groups=None, type=None):
    '''
    Add an endpoint to a connection monitor

    Required Parameters:
    - connection_monitor -- Connection monitor name.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- The name of the connection monitor endpoint

    Optional Parameters:
    - address -- Address of the connection monitor endpoint (IP or domain name)
    - address_exclude -- List of address of the endpoint item which needs to be included to the endpoint scope
    - address_include -- List of address of the endpoint item which needs to be included to the endpoint scope
    - coverage_level -- Test coverage for the endpoint
    - dest_test_groups -- Space-separated list of names for test group to reference as destination
    - filter_item -- List of property=value pairs to define filter items. Property currently include: type, address. Property value of type supports 'AgentAddress' only now.
    - filter_type -- The behavior of the endpoint filter. Currently only 'Include' is supported.
    - resource_id -- Resource ID of the connection monitor endpoint
    - source_test_groups -- Space-separated list of names for test group to reference as source
    - type -- The endpoint type
    '''
    return _call_az("az network watcher connection-monitor endpoint add", locals())


def remove(connection_monitor, location, name, test_groups=None):
    '''
    Remove an endpoint from a connection monitor

    Required Parameters:
    - connection_monitor -- Connection monitor name.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- The name of the connection monitor endpoint

    Optional Parameters:
    - test_groups -- Space-separated list of names of test group which only need to be affected if specified
    '''
    return _call_az("az network watcher connection-monitor endpoint remove", locals())


def show(connection_monitor, location, name):
    '''
    Show an endpoint from a connection monitor

    Required Parameters:
    - connection_monitor -- Connection monitor name.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- The name of the connection monitor endpoint
    '''
    return _call_az("az network watcher connection-monitor endpoint show", locals())


def list(connection_monitor, location):
    '''
    List all endpoints form a connection monitor

    Required Parameters:
    - connection_monitor -- Connection monitor name.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    '''
    return _call_az("az network watcher connection-monitor endpoint list", locals())

