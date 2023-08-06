'''
Manage origins within the specified origin group.
'''
from ... pyaz_utils import _call_az

def show(origin_group_name, origin_name, profile_name, resource_group):
    '''
    

    Required Parameters:
    - origin_group_name -- Name of the origin group which is unique within the endpoint.
    - origin_name -- Name of the origin.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az afd origin show", locals())


def list(origin_group_name, profile_name, resource_group):
    '''
    

    Required Parameters:
    - origin_group_name -- Name of the origin group which is unique within the endpoint.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az afd origin list", locals())


def create(enabled_state, host_name, origin_group_name, origin_name, profile_name, resource_group, enable_private_link=None, http_port=None, https_port=None, origin_host_header=None, priority=None, private_link_location=None, private_link_request_message=None, private_link_resource=None, private_link_sub_resource_type=None, weight=None):
    '''
    Create an AFD origin.

    Required Parameters:
    - enabled_state -- Whether to enable this origin.
    - host_name -- The address of the origin. Domain names, IPv4 addresses, and IPv6 addresses are supported.This should be unique across all origins in a origin group.
    - origin_group_name -- Name of the origin group which is unique within the endpoint.
    - origin_name -- Name of the origin.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - enable_private_link -- Indicates whether private link is enanbled on that origin.
    - http_port -- The port used for http requests to the origin.
    - https_port -- The port used for https requests to the origin.
    - origin_host_header -- The Host header to send for requests to this origin. If you leave this blank, the request hostname determines this value. Azure CDN origins, such as Web Apps, Blob Storage, and Cloud Services require this host header value to match the origin hostname by default.
    - priority -- Priority of origin in given origin group for load balancing. Higher priorities will not be used for load balancing if any lower priority origin is healthy. Must be between 1 and 5.
    - private_link_location -- The location of origin that will be connected to using the private link.
    - private_link_request_message -- The message that is shown to the approver of the private link request.
    - private_link_resource -- The resource ID of the origin that will be connected to using the private link.
    - private_link_sub_resource_type -- The sub-resource type of the origin that will be connected to using the private link.You can use "az network private-link-resource list" to obtain the supported sub-resource types.
    - weight -- Weight of the origin in given origin group for load balancing. Must be between 1 and 1000.
    '''
    return _call_az("az afd origin create", locals())


def update(origin_group_name, origin_name, profile_name, resource_group, enable_private_link=None, enabled_state=None, host_name=None, http_port=None, https_port=None, origin_host_header=None, priority=None, private_link_location=None, private_link_request_message=None, private_link_resource=None, private_link_sub_resource_type=None, weight=None):
    '''
    Update the settings of the specified AFD origin.

    Required Parameters:
    - origin_group_name -- Name of the origin group which is unique within the endpoint.
    - origin_name -- Name of the origin.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - enable_private_link -- Indicates whether private link is enanbled on that origin.
    - enabled_state -- Whether to enable this origin.
    - host_name -- The address of the origin. Domain names, IPv4 addresses, and IPv6 addresses are supported.This should be unique across all origins in a origin group.
    - http_port -- The port used for http requests to the origin.
    - https_port -- The port used for https requests to the origin.
    - origin_host_header -- The Host header to send for requests to this origin. If you leave this blank, the request hostname determines this value. Azure CDN origins, such as Web Apps, Blob Storage, and Cloud Services require this host header value to match the origin hostname by default.
    - priority -- Priority of origin in given origin group for load balancing. Higher priorities will not be used for load balancing if any lower priority origin is healthy. Must be between 1 and 5.
    - private_link_location -- The location of origin that will be connected to using the private link.
    - private_link_request_message -- The message that is shown to the approver of the private link request.
    - private_link_resource -- The resource ID of the origin that will be connected to using the private link.
    - private_link_sub_resource_type -- The sub-resource type of the origin that will be connected to using the private link.You can use "az network private-link-resource list" to obtain the supported sub-resource types.
    - weight -- Weight of the origin in given origin group for load balancing. Must be between 1 and 1000.
    '''
    return _call_az("az afd origin update", locals())


def delete(origin_group_name, origin_name, profile_name, resource_group, yes=None):
    '''
    

    Required Parameters:
    - origin_group_name -- Name of the origin group which is unique within the endpoint.
    - origin_name -- Name of the origin.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az afd origin delete", locals())

