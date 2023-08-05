'''
Manage Azure API Management API Operations.
'''
from .... pyaz_utils import _call_az

def list(api_id, resource_group, service_name):
    '''
    List a collection of the operations for the specified API.

    Required Parameters:
    - api_id -- API identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the API Management service instance.
    '''
    return _call_az("az apim api operation list", locals())


def show(api_id, operation_id, resource_group, service_name):
    '''
    Gets the details of the API Operation specified by its identifier.

    Required Parameters:
    - api_id -- API identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    - operation_id -- Operation identifier within an API. Must be unique in the current API Management service instance.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the API Management service instance.
    '''
    return _call_az("az apim api operation show", locals())


def create(api_id, display_name, method, resource_group, service_name, url_template, description=None, if_match=None, operation_id=None, template_parameters=None):
    '''
    Creates a new operation in the API

    Required Parameters:
    - api_id -- API identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    - display_name -- Required. Operation Name.
    - method -- Required. A Valid HTTP Operation Method. Typical Http Methods like GET, PUT, POST but not limited by only them.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the API Management service instance.
    - url_template -- Relative URL template identifying the target resource for this operation. May include parameters.

    Optional Parameters:
    - description -- Description of the operation. May include HTML formatting tags.
    - if_match -- ETag of the Entity.
    - operation_id -- Operation identifier within an API. Must be unique in the current API Management service instance.
    - template_parameters -- Collection of URL template parameters.
    '''
    return _call_az("az apim api operation create", locals())


def update(api_id, operation_id, resource_group, service_name, add=None, description=None, display_name=None, force_string=None, if_match=None, method=None, remove=None, set=None, url_template=None):
    '''
    Updates the details of the operation in the API specified by its identifier.

    Required Parameters:
    - api_id -- API identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    - operation_id -- Operation identifier within an API. Must be unique in the current API Management service instance.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the API Management service instance.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - description -- Description of the operation. May include HTML formatting tags.
    - display_name -- Required. Operation Name.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - if_match -- ETag of the Entity.
    - method -- Required. A Valid HTTP Operation Method. Typical Http Methods like GET, PUT, POST but not limited by only them.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - url_template -- Relative URL template identifying the target resource for this operation. May include parameters.
    '''
    return _call_az("az apim api operation update", locals())


def delete(api_id, operation_id, resource_group, service_name, if_match=None):
    '''
    Deletes the specified operation in the API.

    Required Parameters:
    - api_id -- API identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    - operation_id -- Operation identifier within an API. Must be unique in the current API Management service instance.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the API Management service instance.

    Optional Parameters:
    - if_match -- ETag of the Entity.
    '''
    return _call_az("az apim api operation delete", locals())

