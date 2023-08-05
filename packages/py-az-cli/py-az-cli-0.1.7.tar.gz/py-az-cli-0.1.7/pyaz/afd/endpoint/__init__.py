'''
Manage AFD endpoints within the specified profile.
'''
from ... pyaz_utils import _call_az

def show(endpoint_name, profile_name, resource_group):
    '''
    Show details of an endpoint within the specified profile.

    Required Parameters:
    - endpoint_name -- Name of the endpoint under the profile which is unique globally.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az afd endpoint show", locals())


def list(profile_name, resource_group):
    '''
    List all the endpoints within the specified profile.

    Required Parameters:
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az afd endpoint list", locals())


def purge(content_paths, endpoint_name, profile_name, resource_group, domains=None, no_wait=None):
    '''
    Removes cached contents from Azure Front Door.

    Required Parameters:
    - content_paths -- The path to the content to be purged. Can describe a file path or a wildcard directory.
    - endpoint_name -- Name of the endpoint under the profile which is unique globally.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - domains -- List of domains.
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az afd endpoint purge", locals())


def delete(endpoint_name, profile_name, resource_group, yes=None):
    '''
    Delete an endpoint within the specified profile.

    Required Parameters:
    - endpoint_name -- Name of the endpoint under the profile which is unique globally.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az afd endpoint delete", locals())


def update(endpoint_name, profile_name, resource_group, enabled_state=None, origin_response_timeout_seconds=None, tags=None):
    '''
    Update an endpoint within the specified profile.

    Required Parameters:
    - endpoint_name -- Name of the endpoint under the profile which is unique globally.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - enabled_state -- Whether to enable this endpoint.
    - origin_response_timeout_seconds -- Send and receive timeout on forwarding request to the origin. When timeout is reached, the request fails and returns.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az afd endpoint update", locals())


def create(enabled_state, endpoint_name, origin_response_timeout_seconds, profile_name, resource_group, tags=None):
    '''
    Creates an endpoint within the specified profile.

    Required Parameters:
    - enabled_state -- Whether to enable this endpoint.
    - endpoint_name -- Name of the endpoint under the profile which is unique globally.
    - origin_response_timeout_seconds -- Send and receive timeout on forwarding request to the origin. When timeout is reached, the request fails and returns.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az afd endpoint create", locals())

