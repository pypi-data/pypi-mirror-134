from .... pyaz_utils import _call_az
from . import endpoint, output, test_configuration, test_group


def create(name, dest_address=None, dest_port=None, dest_resource=None, do_not_start=None, endpoint_dest_address=None, endpoint_dest_coverage_level=None, endpoint_dest_name=None, endpoint_dest_resource_id=None, endpoint_dest_type=None, endpoint_source_address=None, endpoint_source_coverage_level=None, endpoint_source_name=None, endpoint_source_resource_id=None, endpoint_source_type=None, frequency=None, http_method=None, http_path=None, http_port=None, http_valid_status_codes=None, https_prefer=None, icmp_disable_trace_route=None, location=None, monitoring_interval=None, notes=None, output_type=None, preferred_ip_version=None, protocol=None, resource_group=None, source_port=None, source_resource=None, tags=None, tcp_disable_trace_route=None, tcp_port=None, tcp_port_behavior=None, test_config_name=None, test_group_disable=None, test_group_name=None, threshold_failed_percent=None, threshold_round_trip_time=None, workspace_ids=None):
    '''
    Create a connection monitor.

    Required Parameters:
    - name -- Connection monitor name.

    Optional Parameters:
    - dest_address -- The IP address or URI at which to receive traffic.
    - dest_port -- Port number on which to receive traffic.
    - dest_resource -- Name of ID of the resource to receive traffic. Currently only Virtual Machines are supported.
    - do_not_start -- Create the connection monitor but do not start it immediately.
    - endpoint_dest_address -- Address of the destination of connection monitor endpoint (IP or domain name)
    - endpoint_dest_coverage_level -- Test coverage for the endpoint
    - endpoint_dest_name -- The name of the destination of connection monitor endpoint. If you are creating a V2 Connection Monitor, it's required
    - endpoint_dest_resource_id -- Resource ID of the destination of connection monitor endpoint
    - endpoint_dest_type -- The endpoint type
    - endpoint_source_address -- Address of the source of connection monitor endpoint (IP or domain name)
    - endpoint_source_coverage_level -- Test coverage for the endpoint
    - endpoint_source_name -- The name of the source of connection monitor endpoint. If you are creating a V2 Connection Monitor, it's required
    - endpoint_source_resource_id -- Resource ID of the source of connection monitor endpoint. If endpoint is intended to used as source, this option is required.
    - endpoint_source_type -- The endpoint type
    - frequency -- The frequency of test evaluation, in seconds
    - http_method -- The HTTP method to use
    - http_path -- The path component of the URI. For instance, "/dir1/dir2"
    - http_port -- The port to connect to
    - http_valid_status_codes -- Space-separated list of HTTP status codes to consider successful. For instance, "2xx 301-304 418"
    - https_prefer -- Value indicating whether HTTPS is preferred over HTTP in cases where the choice is not explicit
    - icmp_disable_trace_route -- Value indicating whether path evaluation with trace route should be disabled. false is default.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - monitoring_interval -- Monitoring interval in seconds.
    - notes -- Optional notes to be associated with the connection monitor
    - output_type -- Connection monitor output destination type. Currently, only "Workspace" is supported
    - preferred_ip_version -- The preferred IP version to use in test evaluation. The connection monitor may choose to use a different version depending on other parameters
    - protocol -- The protocol to use in test evaluation
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - source_port -- Port number from which to originate traffic.
    - source_resource -- Name or ID of the resource from which to originate traffic. Currently only Virtual Machines are supported.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - tcp_disable_trace_route -- Value indicating whether path evaluation with trace route should be disabled. false is default.
    - tcp_port -- The port to connect to
    - tcp_port_behavior -- Destination port behavior
    - test_config_name -- The name of the connection monitor test configuration. If you are creating a V2 Connection Monitor, it's required
    - test_group_disable -- Value indicating whether test group is disabled. false is default.
    - test_group_name -- The name of the connection monitor test group
    - threshold_failed_percent -- The maximum percentage of failed checks permitted for a test to evaluate as successful
    - threshold_round_trip_time -- The maximum round-trip time in milliseconds permitted for a test to evaluate as successful
    - workspace_ids -- Space-separated list of ids of log analytics workspace
    '''
    return _call_az("az network watcher connection-monitor create", locals())


def delete(location, name, resource_group=None):
    '''
    Delete a connection monitor for the given region.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- Connection monitor name.

    Optional Parameters:
    - resource_group -- ==SUPPRESS==
    '''
    return _call_az("az network watcher connection-monitor delete", locals())


def show(location, name, resource_group=None):
    '''
    Shows a connection monitor by name.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- Connection monitor name.

    Optional Parameters:
    - resource_group -- ==SUPPRESS==
    '''
    return _call_az("az network watcher connection-monitor show", locals())


def stop(location, name, resource_group=None):
    '''
    Stop the specified connection monitor.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- Connection monitor name.

    Optional Parameters:
    - resource_group -- ==SUPPRESS==
    '''
    return _call_az("az network watcher connection-monitor stop", locals())


def start(location, name, resource_group=None):
    '''
    Start the specified connection monitor.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- Connection monitor name.

    Optional Parameters:
    - resource_group -- ==SUPPRESS==
    '''
    return _call_az("az network watcher connection-monitor start", locals())


def query(location, name, resource_group=None):
    '''
    Query a snapshot of the most recent connection state of a connection monitor.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- Connection monitor name.

    Optional Parameters:
    - resource_group -- ==SUPPRESS==
    '''
    return _call_az("az network watcher connection-monitor query", locals())


def list(location, resource_group=None):
    '''
    List connection monitors for the given region.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.

    Optional Parameters:
    - resource_group -- ==SUPPRESS==
    '''
    return _call_az("az network watcher connection-monitor list", locals())

