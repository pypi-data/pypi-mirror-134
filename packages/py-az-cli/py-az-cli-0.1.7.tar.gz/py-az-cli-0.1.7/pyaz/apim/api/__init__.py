'''
Manage Azure API Management API's.
'''
from ... pyaz_utils import _call_az
from . import operation, release, revision, versionset


def import_(path, resource_group, service_name, specification_format, api_id=None, api_revision=None, api_type=None, api_version=None, api_version_set_id=None, description=None, display_name=None, no_wait=None, protocols=None, service_url=None, soap_api_type=None, specification_path=None, specification_url=None, subscription_key_header_name=None, subscription_key_query_param_name=None, subscription_required=None, wsdl_endpoint_name=None, wsdl_service_name=None):
    '''
    Import an API Management API.

    Required Parameters:
    - path -- Required. Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the api management service instance
    - specification_format -- Specify the format of the imported API.

    Optional Parameters:
    - api_id -- API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    - api_revision -- Describes the Revision of the Api. If no value is provided, default revision 1 is created.
    - api_type -- The type of the API.
    - api_version -- Describes the Version of the Api. If you add a version to a non-versioned API, an Original version will be automatically created and will respond on the default URL
    - api_version_set_id -- Describes the Version Set to be used with the API
    - description -- Description of the API. May include HTML formatting tags.
    - display_name -- Display name of this API.
    - no_wait -- Do not wait for the long-running operation to finish.
    - protocols -- Describes on which protocols(one or more) the operations in this API can be invoked.
    - service_url -- Absolute URL of the backend service implementing this API. Cannot be more than 2000 characters long.
    - soap_api_type -- The type of API when file format is WSDL.
    - specification_path -- File path specified to import the API.
    - specification_url -- Url specified to import the API.
    - subscription_key_header_name -- Specifies the subscription key header name.
    - subscription_key_query_param_name -- Specifies the subscription key query string parameter name.
    - subscription_required -- If true, the API requires a subscription key on requests.
    - wsdl_endpoint_name -- Local name of WSDL Endpoint (port) to be imported.
    - wsdl_service_name -- Local name of WSDL Service to be imported.
    '''
    return _call_az("az apim api import", locals())


def create(api_id, display_name, path, resource_group, service_name, api_type=None, authorization_scope=None, authorization_server_id=None, bearer_token_sending_methods=None, description=None, no_wait=None, open_id_provider_id=None, protocols=None, service_url=None, subscription_key_header_name=None, subscription_key_query_param_name=None, subscription_key_required=None, subscription_required=None):
    '''
    Create an API Management API.

    Required Parameters:
    - api_id -- API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    - display_name -- API name. Must be 1 to 300 characters long.
    - path -- Required. Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the API Management service instance.

    Optional Parameters:
    - api_type -- The type of the API.
    - authorization_scope -- Specifies the OAuth operations scope.
    - authorization_server_id -- Specifies the OAuth authorization server ID.
    - bearer_token_sending_methods -- Specifies the sending methods for bearer token.
    - description -- Description of the API. May include HTML formatting tags.
    - no_wait -- Do not wait for the long-running operation to finish.
    - open_id_provider_id -- Specifies the openid in the authentication setting.
    - protocols -- Describes on which protocols the operations in this API can be invoked.
    - service_url -- Absolute URL of the backend service implementing this API. Cannot be more than 2000 characters long.
    - subscription_key_header_name -- Specifies the subscription key header name.
    - subscription_key_query_param_name -- Specifies the subscription key query string parameter name.
    - subscription_key_required -- Specifies whether subscription key is required during call to this API, true - API is included into closed products only, false - API is included into open products alone, null - there is a mix of products.
    - subscription_required -- If true, the API requires a subscription key on requests.
    '''
    return _call_az("az apim api create", locals())


def show(api_id, resource_group, service_name):
    '''
    Show details of an API Management API.

    Required Parameters:
    - api_id -- API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the API Management service instance.
    '''
    return _call_az("az apim api show", locals())


def list(resource_group, service_name, filter_display_name=None, skip=None, top=None):
    '''
    List API Management API's.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the API Management service instance.

    Optional Parameters:
    - filter_display_name -- Filter of APIs by displayName.
    - skip -- Number of records to skip.
    - top -- Number of records to return.
    '''
    return _call_az("az apim api list", locals())


def delete(api_id, resource_group, service_name, delete_revisions=None, if_match=None, no_wait=None, yes=None):
    '''
    Delete an API Management API.

    Required Parameters:
    - api_id -- API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the API Management service instance.

    Optional Parameters:
    - delete_revisions -- Delete all revisions of the Api.
    - if_match -- ETag of the Entity.
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az apim api delete", locals())


def update(api_id, resource_group, service_name, add=None, api_type=None, description=None, display_name=None, force_string=None, if_match=None, no_wait=None, path=None, protocols=None, remove=None, service_url=None, set=None, subscription_key_header_name=None, subscription_key_query_param_name=None, subscription_required=None, tags=None):
    '''
    Update an API Management API.

    Required Parameters:
    - api_id -- API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_name -- The name of the API Management service instance.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - api_type -- The type of the API.
    - description -- Description of the API. May include HTML formatting tags.
    - display_name -- API name. Must be 1 to 300 characters long.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - if_match -- ETag of the Entity. Not required when creating an entity, but required when updating an entity.
    - no_wait -- Do not wait for the long-running operation to finish.
    - path -- Required. Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance.
    - protocols -- Describes on which protocols the operations in this API can be invoked.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - service_url -- Absolute URL of the backend service implementing this API. Cannot be more than 2000 characters long.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - subscription_key_header_name -- Specifies the subscription key header name.
    - subscription_key_query_param_name -- Specifies the subscription key query string parameter name.
    - subscription_required -- If true, the API requires a subscription key on requests.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az apim api update", locals())


def wait(api_id, name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of an apim api is met.

    Required Parameters:
    - api_id -- API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    - name -- The name of the api management service instance
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
    return _call_az("az apim api wait", locals())

