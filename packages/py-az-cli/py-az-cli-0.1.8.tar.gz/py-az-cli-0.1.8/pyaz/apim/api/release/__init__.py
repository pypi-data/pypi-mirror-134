'''
Manage Azure API Management API Release.
'''
from .... pyaz_utils import _call_az

def list(api_id, resource_group, service_name):
    '''
    Lists all releases of an API.

    Required Parameters:
    - api_id -- API identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the API Management service instance.
    '''
    return _call_az("az apim api release list", locals())


def show(api_id, release_id, resource_group, service_name):
    '''
    Returns the details of an API release.

    Required Parameters:
    - api_id -- API identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    - release_id -- Release identifier within an API. Must be unique in the current API Management service instance.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the API Management service instance.
    '''
    return _call_az("az apim api release show", locals())


def create(api_id, api_revision, resource_group, service_name, if_match=None, notes=None, release_id=None):
    '''
    Creates a new Release for the API.

    Required Parameters:
    - api_id -- API identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    - api_revision -- API revision number.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the API Management service instance.

    Optional Parameters:
    - if_match -- ETag of the Entity.
    - notes -- Release Notes.
    - release_id -- Release identifier within an API. Must be unique in the current API Management service instance.
    '''
    return _call_az("az apim api release create", locals())


def update(api_id, release_id, resource_group, service_name, add=None, api_id1=None, force_string=None, if_match=None, notes=None, remove=None, set=None):
    '''
    Updates the details of the release of the API specified by its identifier.

    Required Parameters:
    - api_id -- API identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    - release_id -- Release identifier within an API. Must be unique in the current API Management service instance.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the API Management service instance.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - api_id1 -- Identifier of the API the release belongs to.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - if_match -- ETag of the Entity.
    - notes -- Release Notes.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az apim api release update", locals())


def delete(api_id, release_id, resource_group, service_name, if_match=None):
    '''
    Deletes the specified release in the API.

    Required Parameters:
    - api_id -- API identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    - release_id -- Release identifier within an API. Must be unique in the current API Management service instance.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the API Management service instance.

    Optional Parameters:
    - if_match -- ETag of the Entity.
    '''
    return _call_az("az apim api release delete", locals())

