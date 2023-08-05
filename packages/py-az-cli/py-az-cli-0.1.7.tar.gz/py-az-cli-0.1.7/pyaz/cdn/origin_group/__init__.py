from ... pyaz_utils import _call_az

def show(endpoint_name, name, profile_name, resource_group):
    '''
    

    Required Parameters:
    - endpoint_name -- Name of the CDN endpoint.
    - name -- Name of the origin group.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cdn origin-group show", locals())


def list(endpoint_name, profile_name, resource_group):
    '''
    

    Required Parameters:
    - endpoint_name -- Name of the CDN endpoint.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cdn origin-group list", locals())


def create(endpoint_name, name, profile_name, resource_group, origins=None, probe_interval=None, probe_method=None, probe_path=None, probe_protocol=None):
    '''
    Create an origin group.

    Required Parameters:
    - endpoint_name -- Name of the CDN endpoint.
    - name -- Name of the origin group.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - origins -- None
    - probe_interval -- None
    - probe_method -- None
    - probe_path -- None
    - probe_protocol -- None
    '''
    return _call_az("az cdn origin-group create", locals())


def update(endpoint_name, name, profile_name, resource_group, origins=None, probe_interval=None, probe_method=None, probe_path=None, probe_protocol=None):
    '''
    Update an origin group.

    Required Parameters:
    - endpoint_name -- Name of the CDN endpoint.
    - name -- Name of the origin group.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - origins -- None
    - probe_interval -- None
    - probe_method -- None
    - probe_path -- None
    - probe_protocol -- None
    '''
    return _call_az("az cdn origin-group update", locals())


def delete(endpoint_name, name, profile_name, resource_group, yes=None):
    '''
    

    Required Parameters:
    - endpoint_name -- Name of the CDN endpoint.
    - name -- Name of the origin group.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az cdn origin-group delete", locals())

