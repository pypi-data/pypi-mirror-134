from ..... pyaz_utils import _call_az

def add(connection_monitor, endpoint_dest_name, endpoint_source_name, location, name, test_config_name, disable=None, endpoint_dest_address=None, endpoint_dest_resource_id=None, endpoint_source_address=None, endpoint_source_resource_id=None, frequency=None, http_method=None, http_path=None, http_port=None, http_valid_status_codes=None, https_prefer=None, icmp_disable_trace_route=None, preferred_ip_version=None, protocol=None, tcp_disable_trace_route=None, tcp_port=None, threshold_failed_percent=None, threshold_round_trip_time=None):
    '''
    Add a test group along with new-added/existing endpoint and test configuration to a connection monitor

    Required Parameters:
    - connection_monitor -- Connection monitor name.
    - endpoint_dest_name -- The name of the destination of connection monitor endpoint. If you are creating a V2 Connection Monitor, it's required
    - endpoint_source_name -- The name of the source of connection monitor endpoint. If you are creating a V2 Connection Monitor, it's required
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- The name of the connection monitor test group
    - test_config_name -- The name of the connection monitor test configuration. If you are creating a V2 Connection Monitor, it's required

    Optional Parameters:
    - disable -- Value indicating whether test group is disabled. false is default.
    - endpoint_dest_address -- Address of the destination of connection monitor endpoint (IP or domain name)
    - endpoint_dest_resource_id -- Resource ID of the destination of connection monitor endpoint
    - endpoint_source_address -- Address of the source of connection monitor endpoint (IP or domain name)
    - endpoint_source_resource_id -- Resource ID of the source of connection monitor endpoint. If endpoint is intended to used as source, this option is required.
    - frequency -- The frequency of test evaluation, in seconds
    - http_method -- The HTTP method to use
    - http_path -- The path component of the URI. For instance, "/dir1/dir2"
    - http_port -- The port to connect to
    - http_valid_status_codes -- Space-separated list of HTTP status codes to consider successful. For instance, "2xx 301-304 418"
    - https_prefer -- Value indicating whether HTTPS is preferred over HTTP in cases where the choice is not explicit
    - icmp_disable_trace_route -- Value indicating whether path evaluation with trace route should be disabled. false is default.
    - preferred_ip_version -- The preferred IP version to use in test evaluation. The connection monitor may choose to use a different version depending on other parameters
    - protocol -- The protocol to use in test evaluation
    - tcp_disable_trace_route -- Value indicating whether path evaluation with trace route should be disabled. false is default.
    - tcp_port -- The port to connect to
    - threshold_failed_percent -- The maximum percentage of failed checks permitted for a test to evaluate as successful
    - threshold_round_trip_time -- The maximum round-trip time in milliseconds permitted for a test to evaluate as successful
    '''
    return _call_az("az network watcher connection-monitor test-group add", locals())


def remove(connection_monitor, location, name):
    '''
    Remove test group from a connection monitor

    Required Parameters:
    - connection_monitor -- Connection monitor name.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- The name of the connection monitor test group
    '''
    return _call_az("az network watcher connection-monitor test-group remove", locals())


def show(connection_monitor, location, name):
    '''
    Show a test group of a connection monitor

    Required Parameters:
    - connection_monitor -- Connection monitor name.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- The name of the connection monitor test group
    '''
    return _call_az("az network watcher connection-monitor test-group show", locals())


def list(connection_monitor, location):
    '''
    List all test groups of a connection monitor

    Required Parameters:
    - connection_monitor -- Connection monitor name.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    '''
    return _call_az("az network watcher connection-monitor test-group list", locals())

