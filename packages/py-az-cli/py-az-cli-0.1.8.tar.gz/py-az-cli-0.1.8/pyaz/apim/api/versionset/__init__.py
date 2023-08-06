'''
Manage Azure API Management API Version Set.
'''
from .... pyaz_utils import _call_az

def list(resource_group, service_name):
    '''
    Lists a collection of API Version Sets in the specified service instance.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the API Management service instance.
    '''
    return _call_az("az apim api versionset list", locals())


def show(resource_group, service_name, version_set_id):
    '''
    Gets the details of the Api Version Set specified by its identifier.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the API Management service instance.
    - version_set_id -- A resource identifier for the related ApiVersionSet.
    '''
    return _call_az("az apim api versionset show", locals())


def create(display_name, resource_group, service_name, versioning_scheme, description=None, if_match=None, version_header_name=None, version_query_name=None, version_set_id=None):
    '''
    Creates a Api Version Set.

    Required Parameters:
    - display_name -- Required. Name of API Version Set
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the API Management service instance.
    - versioning_scheme -- Required. An value that determines where the API Version identifer will be located in a HTTP request. Possible values include: 'Segment', 'Query', 'Header'

    Optional Parameters:
    - description -- Description of API Version Set.
    - if_match -- ETag of the Entity.
    - version_header_name -- Name of HTTP header parameter that indicates the API Version if versioningScheme is set to `header`.
    - version_query_name -- Name of query parameter that indicates the API Version if versioningScheme is set to `query`.
    - version_set_id -- A resource identifier for the related ApiVersionSet.
    '''
    return _call_az("az apim api versionset create", locals())


def update(resource_group, service_name, version_set_id, add=None, description=None, display_name=None, force_string=None, if_match=None, remove=None, set=None, version_header_name=None, version_query_name=None, versioning_scheme=None):
    '''
    Updates the details of the Api VersionSet specified by its identifier.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the API Management service instance.
    - version_set_id -- A resource identifier for the related ApiVersionSet.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - description -- Description of API Version Set.
    - display_name -- Required. Name of API Version Set
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - if_match -- ETag of the Entity.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - version_header_name -- Name of HTTP header parameter that indicates the API Version if versioningScheme is set to `header`.
    - version_query_name -- Name of query parameter that indicates the API Version if versioningScheme is set to `query`.
    - versioning_scheme -- Required. An value that determines where the API Version identifer will be located in a HTTP request. Possible values include: 'Segment', 'Query', 'Header'
    '''
    return _call_az("az apim api versionset update", locals())


def delete(resource_group, service_name, version_set_id, if_match=None):
    '''
    Deletes specific Api Version Set.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the API Management service instance.
    - version_set_id -- A resource identifier for the related ApiVersionSet.

    Optional Parameters:
    - if_match -- ETag of the Entity.
    '''
    return _call_az("az apim api versionset delete", locals())

