'''
Manage CDN endpoints.
'''
from ... pyaz_utils import _call_az
from . import rule


def start(name, profile_name, resource_group, no_wait=None):
    '''
    Start a CDN endpoint.

    Required Parameters:
    - name -- Name of the CDN endpoint.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az cdn endpoint start", locals())


def stop(name, profile_name, resource_group, no_wait=None):
    '''
    Stop a CDN endpoint.

    Required Parameters:
    - name -- Name of the CDN endpoint.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az cdn endpoint stop", locals())


def delete(name, profile_name, resource_group, no_wait=None):
    '''
    Delete a CDN endpoint.

    Required Parameters:
    - name -- Name of the CDN endpoint.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az cdn endpoint delete", locals())


def show(name, profile_name, resource_group):
    '''
    

    Required Parameters:
    - name -- Name of the CDN endpoint.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cdn endpoint show", locals())


def list(profile_name, resource_group):
    '''
    List available endpoints for a CDN.

    Required Parameters:
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cdn endpoint list", locals())


def load(content_paths, name, profile_name, resource_group, no_wait=None):
    '''
    Pre-load content for a CDN endpoint.

    Required Parameters:
    - content_paths -- None
    - name -- Name of the CDN endpoint.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az cdn endpoint load", locals())


def purge(content_paths, name, profile_name, resource_group, no_wait=None):
    '''
    Purge pre-loaded content for a CDN endpoint.

    Required Parameters:
    - content_paths -- None
    - name -- Name of the CDN endpoint.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az cdn endpoint purge", locals())


def validate_custom_domain(host_name, name, profile_name, resource_group):
    '''
    Validates the custom domain mapping to ensure it maps to the correct CDN endpoint in DNS.

    Required Parameters:
    - host_name -- None
    - name -- Name of the CDN endpoint.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cdn endpoint validate-custom-domain", locals())


def create(name, origin, profile_name, resource_group, content_types_to_compress=None, enable_compression=None, location=None, no_http=None, no_https=None, no_wait=None, origin_host_header=None, origin_path=None, query_string_caching_behavior=None, tags=None):
    '''
    Create a named endpoint to connect to a CDN.

    Required Parameters:
    - name -- Name of the CDN endpoint.
    - origin -- Endpoint origin specified by the following space-delimited 6 tuple: `www.example.com http_port https_port private_link_resource_id private_link_location private_link_approval_message`. The HTTP and HTTPS ports and the private link resource ID and location are optional. The HTTP and HTTPS ports default to 80 and 443, respectively. Private link fields are only valid for the sku Standard_Microsoft, and private_link_location is required if private_link_resource_id is set.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - content_types_to_compress -- List of content types on which compression applies. The value should be a valid MIME type.
    - enable_compression -- If compression is enabled, content will be served as compressed if user requests for a compressed version. Content won't be compressed on CDN when requested content is smaller than 1 byte or larger than 1 MB.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - no_http -- Indicates whether HTTP traffic is not allowed on the endpoint. Default is to allow HTTP traffic.
    - no_https -- Indicates whether HTTPS traffic is not allowed on the endpoint. Default is to allow HTTPS traffic.
    - no_wait -- Do not wait for the long-running operation to finish.
    - origin_host_header -- The host header value sent to the origin with each request. This property at Endpoint is only allowed when endpoint uses single origin and can be overridden by the same property specified at origin.If you leave this blank, the request hostname determines this value. Azure CDN origins, such as Web Apps, Blob Storage, and Cloud Services require this host header value to match the origin hostname by default.
    - origin_path -- A directory path on the origin that CDN can use to retrieve content from, e.g. contoso.cloudapp.net/originpath.
    - query_string_caching_behavior -- Defines how CDN caches requests that include query strings. You can ignore any query strings when caching, bypass caching to prevent requests that contain query strings from being cached, or cache every request with a unique URL. Possible values include: "IgnoreQueryString", "BypassCaching", "UseQueryString", "NotSet".
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az cdn endpoint create", locals())


def update(name, profile_name, resource_group, add=None, content_types_to_compress=None, default_origin_group=None, enable_compression=None, force_string=None, no_http=None, no_https=None, no_wait=None, origin_host_header=None, origin_path=None, query_string_caching=None, remove=None, set=None, tags=None):
    '''
    Update a CDN endpoint to manage how content is delivered.

    Required Parameters:
    - name -- Name of the CDN endpoint.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - content_types_to_compress -- List of content types on which compression applies. The value should be a valid MIME type.
    - default_origin_group -- A reference to the origin group.
    - enable_compression -- If compression is enabled, content will be served as compressed if user requests for a compressed version. Content won't be compressed on CDN when requested content is smaller than 1 byte or larger than 1 MB.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - no_http -- Indicates whether HTTP traffic is not allowed on the endpoint. Default is to allow HTTP traffic.
    - no_https -- Indicates whether HTTPS traffic is not allowed on the endpoint. Default is to allow HTTPS traffic.
    - no_wait -- Do not wait for the long-running operation to finish.
    - origin_host_header -- The host header value sent to the origin with each request. This property at Endpoint is only allowed when endpoint uses single origin and can be overridden by the same property specified at origin.If you leave this blank, the request hostname determines this value. Azure CDN origins, such as Web Apps, Blob Storage, and Cloud Services require this host header value to match the origin hostname by default.
    - origin_path -- A directory path on the origin that CDN can use to retrieve content from, e.g. contoso.cloudapp.net/originpath.
    - query_string_caching -- Defines how CDN caches requests that include query strings. You can ignore any query strings when caching, bypass caching to prevent requests that contain query strings from being cached, or cache every request with a unique URL. Possible values include: "IgnoreQueryString", "BypassCaching", "UseQueryString", "NotSet".
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az cdn endpoint update", locals())

