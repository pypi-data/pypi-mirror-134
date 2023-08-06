from ..... pyaz_utils import _call_az

def add(connection_monitor, location, name, protocol, test_groups, frequency=None, http_method=None, http_path=None, http_port=None, http_prefer_https=None, http_request_header=None, http_valid_status_codes=None, icmp_disable_trace_route=None, preferred_ip_version=None, tcp_disable_trace_route=None, tcp_port=None, tcp_port_behavior=None, threshold_failed_percent=None, threshold_round_trip_time=None):
    '''
    Add a test configuration to a connection monitor

    Required Parameters:
    - connection_monitor -- Connection monitor name
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- The name of the connection monitor test configuration
    - protocol -- The protocol to use in test evaluation
    - test_groups -- Space-separated list of names of test group which only need to be affected if specified

    Optional Parameters:
    - frequency -- The frequency of test evaluation, in seconds
    - http_method -- The HTTP method to use
    - http_path -- The path component of the URI. For instance, "/dir1/dir2"
    - http_port -- The port to connect to
    - http_prefer_https -- Value indicating whether HTTPS is preferred over HTTP in cases where the choice is not explicit
    - http_request_header -- The HTTP headers to transmit with the request. List of property=value pairs to define HTTP headers.
    - http_valid_status_codes -- Space-separated list of HTTP status codes to consider successful. For instance, "2xx 301-304 418"
    - icmp_disable_trace_route -- Value indicating whether path evaluation with trace route should be disabled. false is default.
    - preferred_ip_version -- The preferred IP version to use in test evaluation. The connection monitor may choose to use a different version depending on other parameters
    - tcp_disable_trace_route -- Value indicating whether path evaluation with trace route should be disabled. false is default.
    - tcp_port -- The port to connect to
    - tcp_port_behavior -- Destination port behavior
    - threshold_failed_percent -- The maximum percentage of failed checks permitted for a test to evaluate as successful
    - threshold_round_trip_time -- The maximum round-trip time in milliseconds permitted for a test to evaluate as successful
    '''
    return _call_az("az network watcher connection-monitor test-configuration add", locals())


def remove(connection_monitor, location, name, test_groups=None):
    '''
    Remove a test configuration from a connection monitor

    Required Parameters:
    - connection_monitor -- Connection monitor name
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- The name of the connection monitor test configuration

    Optional Parameters:
    - test_groups -- Space-separated list of names of test group which only need to be affected if specified
    '''
    return _call_az("az network watcher connection-monitor test-configuration remove", locals())


def show(connection_monitor, location, name):
    '''
    Show a test configuration from a connection monitor

    Required Parameters:
    - connection_monitor -- Connection monitor name
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- The name of the connection monitor test configuration
    '''
    return _call_az("az network watcher connection-monitor test-configuration show", locals())


def list(connection_monitor, location):
    '''
    List all test configurations of a connection monitor

    Required Parameters:
    - connection_monitor -- Connection monitor name
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    '''
    return _call_az("az network watcher connection-monitor test-configuration list", locals())

