from .... pyaz_utils import _call_az

def check_dns(name, type=None):
    '''
    Check the availability of a relative DNS name.

    Required Parameters:
    - name -- DNS prefix to verify availability for.

    Optional Parameters:
    - type -- ==SUPPRESS==
    '''
    return _call_az("az network traffic-manager profile check-dns", locals())


def show(name, resource_group):
    '''
    Get the details of a traffic manager profile.

    Required Parameters:
    - name -- The name of the Traffic Manager profile.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network traffic-manager profile show", locals())


def delete(name, resource_group):
    '''
    Delete a traffic manager profile.

    Required Parameters:
    - name -- The name of the Traffic Manager profile to be deleted.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network traffic-manager profile delete", locals())


def list(resource_group=None):
    '''
    List traffic manager profiles.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network traffic-manager profile list", locals())


def create(name, resource_group, routing_method, unique_dns_name, custom_headers=None, interval=None, max_failures=None, max_return=None, path=None, port=None, protocol=None, status=None, status_code_ranges=None, tags=None, timeout=None, ttl=None):
    '''
    Create a traffic manager profile.

    Required Parameters:
    - name -- Traffic manager profile name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - routing_method -- Routing method.
    - unique_dns_name -- Relative DNS name for the traffic manager profile. Resulting FQDN will be `<unique-dns-name>.trafficmanager.net` and must be globally unique.

    Optional Parameters:
    - custom_headers -- Space-separated list of NAME=VALUE pairs.
    - interval -- The interval in seconds at which health checks are conducted.
    - max_failures -- The number of consecutive failed health checks tolerated before an endpoint is considered degraded.
    - max_return -- Maximum number of endpoints to be returned for MultiValue routing type.
    - path -- Path to monitor. Use ""('""' in PowerShell) for none.
    - port -- Port to monitor.
    - protocol -- Monitor protocol.
    - status -- Status of the Traffic Manager profile.
    - status_code_ranges -- Space-separated list of status codes in MIN-MAX or VAL format.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - timeout -- The time in seconds allowed for endpoints to respond to a health check.
    - ttl -- DNS config time-to-live in seconds.
    '''
    return _call_az("az network traffic-manager profile create", locals())


def update(name, resource_group, add=None, custom_headers=None, force_string=None, interval=None, max_failures=None, max_return=None, path=None, port=None, protocol=None, remove=None, routing_method=None, set=None, status=None, status_code_ranges=None, tags=None, timeout=None, ttl=None):
    '''
    Update a traffic manager profile.

    Required Parameters:
    - name -- The name of the Traffic Manager profile.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - custom_headers -- Space-separated list of NAME=VALUE pairs.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - interval -- The interval in seconds at which health checks are conducted.
    - max_failures -- The number of consecutive failed health checks tolerated before an endpoint is considered degraded.
    - max_return -- Maximum number of endpoints to be returned for MultiValue routing type.
    - path -- Path to monitor. Use ""('""' in PowerShell) for none.
    - port -- Port to monitor.
    - protocol -- Monitor protocol.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - routing_method -- Routing method.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - status -- Status of the Traffic Manager profile.
    - status_code_ranges -- Space-separated list of status codes in MIN-MAX or VAL format.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - timeout -- The time in seconds allowed for endpoints to respond to a health check.
    - ttl -- DNS config time-to-live in seconds.
    '''
    return _call_az("az network traffic-manager profile update", locals())

