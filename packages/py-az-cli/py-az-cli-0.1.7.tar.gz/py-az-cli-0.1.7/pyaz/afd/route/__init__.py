'''
Manage routes under an AFD endpoint.
'''
from ... pyaz_utils import _call_az

def show(endpoint_name, profile_name, resource_group, route_name):
    '''
    Show route details.

    Required Parameters:
    - endpoint_name -- Name of the endpoint.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - route_name -- Name of the route.
    '''
    return _call_az("az afd route show", locals())


def list(endpoint_name, profile_name, resource_group):
    '''
    List all the routes within the specified endpoint.

    Required Parameters:
    - endpoint_name -- Name of the endpoint.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az afd route list", locals())


def create(endpoint_name, forwarding_protocol, https_redirect, origin_group, profile_name, resource_group, route_name, supported_protocols, content_types_to_compress=None, custom_domains=None, enable_compression=None, link_to_default_domain=None, origin_path=None, patterns_to_match=None, query_string_caching_behavior=None, rule_sets=None):
    '''
    Creates a new route within the specified endpoint.

    Required Parameters:
    - endpoint_name -- Name of the endpoint.
    - forwarding_protocol -- Protocol this rule will use when forwarding traffic to backends.
    - https_redirect -- Whether to automatically redirect HTTP traffic to HTTPS traffic.
    - origin_group -- Name or ID of the origin group to be associated with.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - route_name -- Name of the route.
    - supported_protocols -- List of supported protocols for this route.

    Optional Parameters:
    - content_types_to_compress -- List of content types on which compression applies. The value should be a valid MIME type.
    - custom_domains -- Custom domains referenced by this endpoint.
    - enable_compression -- Indicates whether content compression is enabled on AzureFrontDoor. Default value is false. If compression is enabled, content will be served as compressed if user requests for a compressed version. Content won't be compressed on AzureFrontDoor when requested content is smaller than 1 byte or larger than 1 MB.
    - link_to_default_domain -- Whether this route will be linked to the default endpoint domain.
    - origin_path -- A directory path on the origin that AFD can use to retrieve content from. E.g, "/img/*"
    - patterns_to_match -- The route patterns of the rule.
    - query_string_caching_behavior -- Defines how CDN caches requests that include query strings. You can ignore any query strings when caching, bypass caching to prevent requests that contain query strings from being cached, or cache every request with a unique URL.
    - rule_sets -- Collection of ID or name of rule set referenced by the route.
    '''
    return _call_az("az afd route create", locals())


def update(endpoint_name, profile_name, resource_group, route_name, content_types_to_compress=None, custom_domains=None, enable_compression=None, forwarding_protocol=None, https_redirect=None, link_to_default_domain=None, origin_group=None, origin_path=None, patterns_to_match=None, query_string_caching_behavior=None, rule_sets=None, supported_protocols=None):
    '''
    Update an existing route within the specified endpoint.

    Required Parameters:
    - endpoint_name -- Name of the endpoint.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - route_name -- Name of the route.

    Optional Parameters:
    - content_types_to_compress -- List of content types on which compression applies. The value should be a valid MIME type.
    - custom_domains -- Custom domains referenced by this endpoint.
    - enable_compression -- Indicates whether content compression is enabled on AzureFrontDoor. Default value is false. If compression is enabled, content will be served as compressed if user requests for a compressed version. Content won't be compressed on AzureFrontDoor when requested content is smaller than 1 byte or larger than 1 MB.
    - forwarding_protocol -- Protocol this rule will use when forwarding traffic to backends.
    - https_redirect -- Whether to automatically redirect HTTP traffic to HTTPS traffic.
    - link_to_default_domain -- Whether this route will be linked to the default endpoint domain.
    - origin_group -- Name or ID of the origin group to be associated with.
    - origin_path -- A directory path on the origin that AFD can use to retrieve content from. E.g, "/img/*"
    - patterns_to_match -- The route patterns of the rule.
    - query_string_caching_behavior -- Defines how CDN caches requests that include query strings. You can ignore any query strings when caching, bypass caching to prevent requests that contain query strings from being cached, or cache every request with a unique URL.
    - rule_sets -- Collection of ID or name of rule set referenced by the route.
    - supported_protocols -- List of supported protocols for this route.
    '''
    return _call_az("az afd route update", locals())


def delete(endpoint_name, profile_name, resource_group, route_name, yes=None):
    '''
    Delete an existing route within the specified endpoint.

    Required Parameters:
    - endpoint_name -- Name of the endpoint.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - route_name -- Name of the route.

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az afd route delete", locals())

