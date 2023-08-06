'''
List or show existing origins related to CDN endpoints.
'''
from ... pyaz_utils import _call_az

def show(endpoint_name, name, profile_name, resource_group):
    '''
    

    Required Parameters:
    - endpoint_name -- Name of the CDN endpoint.
    - name -- Name of the origin.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cdn origin show", locals())


def list(endpoint_name, profile_name, resource_group):
    '''
    

    Required Parameters:
    - endpoint_name -- Name of the CDN endpoint.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cdn origin list", locals())


def create(endpoint_name, host_name, name, profile_name, resource_group, disabled=None, http_port=None, https_port=None, origin_host_header=None, priority=None, private_link_approval_message=None, private_link_location=None, private_link_resource_id=None, weight=None):
    '''
    Create an origin.

    Required Parameters:
    - endpoint_name -- Name of the CDN endpoint.
    - host_name -- None
    - name -- Name of the origin.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - disabled -- None
    - http_port -- None
    - https_port -- None
    - origin_host_header -- None
    - priority -- None
    - private_link_approval_message -- None
    - private_link_location -- None
    - private_link_resource_id -- None
    - weight -- None
    '''
    return _call_az("az cdn origin create", locals())


def update(endpoint_name, name, profile_name, resource_group, disabled=None, host_name=None, http_port=None, https_port=None, origin_host_header=None, priority=None, private_link_approval_message=None, private_link_location=None, private_link_resource_id=None, weight=None):
    '''
    Update an origin.

    Required Parameters:
    - endpoint_name -- Name of the CDN endpoint.
    - name -- Name of the origin.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - disabled -- None
    - host_name -- None
    - http_port -- None
    - https_port -- None
    - origin_host_header -- None
    - priority -- None
    - private_link_approval_message -- None
    - private_link_location -- None
    - private_link_resource_id -- None
    - weight -- None
    '''
    return _call_az("az cdn origin update", locals())


def delete(endpoint_name, name, profile_name, resource_group, yes=None):
    '''
    

    Required Parameters:
    - endpoint_name -- Name of the CDN endpoint.
    - name -- Name of the origin.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az cdn origin delete", locals())

