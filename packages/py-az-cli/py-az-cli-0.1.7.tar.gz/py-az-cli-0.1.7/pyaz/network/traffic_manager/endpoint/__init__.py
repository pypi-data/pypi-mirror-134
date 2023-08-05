from .... pyaz_utils import _call_az

def show(name, profile_name, resource_group, type):
    '''
    Get the details of a traffic manager endpoint.

    Required Parameters:
    - name -- Endpoint name.
    - profile_name -- Name of parent profile.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - type -- Endpoint type.
    '''
    return _call_az("az network traffic-manager endpoint show", locals())


def delete(name, profile_name, resource_group, type):
    '''
    Delete a traffic manager endpoint.

    Required Parameters:
    - name -- Endpoint name.
    - profile_name -- Name of parent profile.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - type -- Endpoint type.
    '''
    return _call_az("az network traffic-manager endpoint delete", locals())


def create(name, profile_name, resource_group, type, custom_headers=None, endpoint_location=None, endpoint_monitor_status=None, endpoint_status=None, geo_mapping=None, min_child_endpoints=None, priority=None, subnets=None, target=None, target_resource_id=None, weight=None):
    '''
    Create a traffic manager endpoint.

    Required Parameters:
    - name -- Endpoint name.
    - profile_name -- Name of parent profile.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - type -- Endpoint type.

    Optional Parameters:
    - custom_headers -- Space-separated list of custom headers in KEY=VALUE format.
    - endpoint_location -- Location of the external or nested endpoints when using the 'Performance' routing method.
    - endpoint_monitor_status -- The monitoring status of the endpoint.
    - endpoint_status -- The status of the endpoint. If enabled the endpoint is probed for endpoint health and included in the traffic routing method.
    - geo_mapping -- Space-separated list of country/region codes mapped to this endpoint when using the 'Geographic' routing method.
    - min_child_endpoints -- The minimum number of endpoints that must be available in the child profile for the parent profile to be considered available. Only applicable to an endpoint of type 'NestedEndpoints'.
    - priority -- Priority of the endpoint when using the 'Priority' traffic routing method. Values range from 1 to 1000, with lower values representing higher priority.
    - subnets -- Space-separated list of subnet CIDR prefixes (10.0.0.0/24) or subnet ranges (10.0.0.0-11.0.0.0).
    - target -- Fully-qualified DNS name of the endpoint.
    - target_resource_id -- The Azure Resource URI of the endpoint. Not applicable for endpoints of type 'ExternalEndpoints'.
    - weight -- Weight of the endpoint when using the 'Weighted' traffic routing method. Values range from 1 to 1000.
    '''
    return _call_az("az network traffic-manager endpoint create", locals())


def list(profile_name, resource_group, type=None):
    '''
    List traffic manager endpoints.

    Required Parameters:
    - profile_name -- Name of parent profile.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - type -- Endpoint type.
    '''
    return _call_az("az network traffic-manager endpoint list", locals())


def update(name, profile_name, resource_group, add=None, custom_headers=None, endpoint_location=None, endpoint_monitor_status=None, endpoint_status=None, force_string=None, geo_mapping=None, min_child_endpoints=None, priority=None, remove=None, set=None, subnets=None, target=None, target_resource_id=None, type=None, weight=None):
    '''
    Update a traffic manager endpoint.

    Required Parameters:
    - name -- Endpoint name.
    - profile_name -- Name of parent profile.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - custom_headers -- Space-separated list of custom headers in KEY=VALUE format.
    - endpoint_location -- Location of the external or nested endpoints when using the 'Performance' routing method.
    - endpoint_monitor_status -- The monitoring status of the endpoint.
    - endpoint_status -- The status of the endpoint. If enabled the endpoint is probed for endpoint health and included in the traffic routing method.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - geo_mapping -- Space-separated list of country/region codes mapped to this endpoint when using the 'Geographic' routing method.
    - min_child_endpoints -- The minimum number of endpoints that must be available in the child profile for the parent profile to be considered available. Only applicable to an endpoint of type 'NestedEndpoints'.
    - priority -- Priority of the endpoint when using the 'Priority' traffic routing method. Values range from 1 to 1000, with lower values representing higher priority.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - subnets -- Space-separated list of subnet CIDR prefixes (10.0.0.0/24) or subnet ranges (10.0.0.0-11.0.0.0).
    - target -- Fully-qualified DNS name of the endpoint.
    - target_resource_id -- The Azure Resource URI of the endpoint. Not applicable for endpoints of type 'ExternalEndpoints'.
    - type -- Endpoint type.
    - weight -- Weight of the endpoint when using the 'Weighted' traffic routing method. Values range from 1 to 1000.
    '''
    return _call_az("az network traffic-manager endpoint update", locals())


def show_geographic_hierarchy():
    '''
    Get the default geographic hierarchy used by the geographic traffic routing method.
    '''
    return _call_az("az network traffic-manager endpoint show-geographic-hierarchy", locals())

