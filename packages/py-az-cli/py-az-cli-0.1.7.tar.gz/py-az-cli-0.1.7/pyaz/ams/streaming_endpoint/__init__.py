from ... pyaz_utils import _call_az
from . import akamai


def list(account_name, resource_group):
    '''
    List all the streaming endpoints within an Azure Media Services account.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams streaming-endpoint list", locals())


def start(account_name, name, resource_group, no_wait=None):
    '''
    Start a streaming endpoint.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the streaming endpoint.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az ams streaming-endpoint start", locals())


def stop(account_name, name, resource_group, no_wait=None):
    '''
    Stop a streaming endpoint.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the streaming endpoint.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az ams streaming-endpoint stop", locals())


def create(account_name, name, resource_group, scale_units, auto_start=None, availability_set_name=None, cdn_profile=None, cdn_provider=None, client_access_policy=None, cross_domain_policy=None, custom_host_names=None, description=None, ips=None, max_cache_age=None, no_wait=None, tags=None):
    '''
    Create a streaming endpoint.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the streaming endpoint.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - scale_units -- The number of scale units for Premium StreamingEndpoints. For Standard StreamingEndpoints, set this value to 0. Use the Scale operation to adjust this value for Premium StreamingEndpoints.

    Optional Parameters:
    - auto_start -- The flag indicates if the resource should be automatically started on creation.
    - availability_set_name -- The name of the AvailabilitySet used with this StreamingEndpoint for high availability streaming. This value can only be set at creation time.
    - cdn_profile -- The CDN profile name.
    - cdn_provider -- The CDN provider name. Allowed values: StandardVerizon, PremiumVerizon, StandardAkamai.
    - client_access_policy -- The XML representing the clientaccesspolicy data used by Microsoft Silverlight and Adobe Flash. Use @{file} to load from a file. For further information about the XML structure please refer to documentation on https://docs.microsoft.com/rest/api/media/operations/crosssiteaccesspolicies
    - cross_domain_policy -- The XML representing the crossdomain data used by Silverlight. Use @{file} to load from a file. For further information about the XML structure please refer to documentation on https://docs.microsoft.com/rest/api/media/operations/crosssiteaccesspolicies
    - custom_host_names -- Space-separated list of custom host names for the streaming endpoint. Use "" to clear existing list.
    - description -- The streaming endpoint description.
    - ips -- Space-separated IP addresses for access control. Allowed IP addresses can be specified as either a single IP address (e.g. "10.0.0.1") or as an IP range using an IP address and a CIDR subnet mask (e.g. "10.0.0.1/22"). Use "" to clear existing list. If no IP addresses are specified any IP address will be allowed.
    - max_cache_age -- Max cache age.
    - no_wait -- Do not wait for the long-running operation to finish.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az ams streaming-endpoint create", locals())


def scale(account_name, name, resource_group, scale_units):
    '''
    Set the scale of a streaming endpoint.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the streaming endpoint.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - scale_units -- The number of scale units for Premium StreamingEndpoints. For Standard StreamingEndpoints, set this value to 0. Use the Scale operation to adjust this value for Premium StreamingEndpoints.
    '''
    return _call_az("az ams streaming-endpoint scale", locals())


def update(account_name, name, resource_group, add=None, cdn_profile=None, cdn_provider=None, client_access_policy=None, cross_domain_policy=None, custom_host_names=None, description=None, disable_cdn=None, force_string=None, ips=None, max_cache_age=None, no_wait=None, remove=None, set=None, tags=None):
    '''
    Update the details of a streaming endpoint.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the streaming endpoint.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - cdn_profile -- The CDN profile name.
    - cdn_provider -- The CDN provider name. Allowed values: StandardVerizon, PremiumVerizon, StandardAkamai.
    - client_access_policy -- The XML representing the clientaccesspolicy data used by Microsoft Silverlight and Adobe Flash. Use @{file} to load from a file. For further information about the XML structure please refer to documentation on https://docs.microsoft.com/rest/api/media/operations/crosssiteaccesspolicies
    - cross_domain_policy -- The XML representing the crossdomain data used by Silverlight. Use @{file} to load from a file. For further information about the XML structure please refer to documentation on https://docs.microsoft.com/rest/api/media/operations/crosssiteaccesspolicies
    - custom_host_names -- Space-separated list of custom host names for the streaming endpoint. Use "" to clear existing list.
    - description -- The streaming endpoint description.
    - disable_cdn -- Use this flag to disable CDN for the streaming endpoint.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - ips -- Space-separated IP addresses for access control. Allowed IP addresses can be specified as either a single IP address (e.g. "10.0.0.1") or as an IP range using an IP address and a CIDR subnet mask (e.g. "10.0.0.1/22"). Use "" to clear existing list. If no IP addresses are specified any IP address will be allowed.
    - max_cache_age -- Max cache age.
    - no_wait -- Do not wait for the long-running operation to finish.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az ams streaming-endpoint update", locals())


def show(account_name, name, resource_group):
    '''
    Show the details of a streaming endpoint.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the streaming endpoint.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams streaming-endpoint show", locals())


def delete(account_name, name, resource_group):
    '''
    Delete a streaming endpoint.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the streaming endpoint.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams streaming-endpoint delete", locals())


def wait(account_name, name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the streaming endpoint is met.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the streaming endpoint.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az ams streaming-endpoint wait", locals())

