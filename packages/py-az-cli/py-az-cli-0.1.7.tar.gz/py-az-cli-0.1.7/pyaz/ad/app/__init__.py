'''
Manage applications with AAD Graph.
'''
from ... pyaz_utils import _call_az
from . import credential, owner, permission


def create(display_name, app_roles=None, available_to_other_tenants=None, credential_description=None, end_date=None, homepage=None, identifier_uris=None, key_type=None, key_usage=None, key_value=None, native_app=None, oauth2_allow_implicit_flow=None, optional_claims=None, password=None, reply_urls=None, required_resource_accesses=None, start_date=None):
    '''
    Create a web application, web API or native application

    Required Parameters:
    - display_name -- the display name of the application

    Optional Parameters:
    - app_roles -- declare the roles you want to associate with your application. Should be in manifest json format. See examples below for details
    - available_to_other_tenants -- the application can be used from any Azure AD tenants
    - credential_description -- the description of the password
    - end_date -- Date or datetime after which credentials expire(e.g. '2017-12-31T11:59:59+00:00' or '2017-12-31'). Default value is one year after current time
    - homepage -- the url where users can sign in and use your app.
    - identifier_uris -- space-separated unique URIs that Azure AD can use for this app.
    - key_type -- the type of the key credentials associated with the application
    - key_usage -- the usage of the key credentials associated with the application.
    - key_value -- the value for the key credentials associated with the application
    - native_app -- an application which can be installed on a user's device or computer
    - oauth2_allow_implicit_flow -- whether to allow implicit grant flow for OAuth2
    - optional_claims -- declare the optional claims for the application. Should be in manifest json format. See examples below for details. Please reference https://docs.microsoft.com/azure/active-directory/develop/active-directory-optional-claims#optionalclaim-type for optional claim properties.
    - password -- app password, aka 'client secret'
    - reply_urls -- space-separated URIs to which Azure AD will redirect in response to an OAuth 2.0 request. The value does not need to be a physical endpoint, but must be a valid URI.
    - required_resource_accesses -- resource scopes and roles the application requires access to. Should be in manifest json format. See examples below for details
    - start_date -- Date or datetime at which credentials become valid(e.g. '2017-01-01T01:00:00+00:00' or '2017-01-01'). Default value is current time
    '''
    return _call_az("az ad app create", locals())


def delete(id):
    '''
    Delete an application.

    Required Parameters:
    - id -- identifier uri, application id, or object id
    '''
    return _call_az("az ad app delete", locals())


def list(all=None, app_id=None, display_name=None, filter=None, identifier_uri=None, show_mine=None):
    '''
    List applications.

    Optional Parameters:
    - all -- list all entities, expect long delay if under a big organization
    - app_id -- application id
    - display_name -- the display name of the application
    - filter -- OData filter, e.g. --filter "displayname eq 'test' and servicePrincipalType eq 'Application'"
    - identifier_uri -- graph application identifier, must be in uri format
    - show_mine -- list entities owned by the current user
    '''
    return _call_az("az ad app list", locals())


def show(id):
    '''
    Get the details of an application.

    Required Parameters:
    - id -- identifier uri, application id, or object id
    '''
    return _call_az("az ad app show", locals())


def update(id, add=None, app_roles=None, available_to_other_tenants=None, credential_description=None, display_name=None, end_date=None, force_string=None, homepage=None, identifier_uris=None, key_type=None, key_usage=None, key_value=None, oauth2_allow_implicit_flow=None, optional_claims=None, password=None, remove=None, reply_urls=None, required_resource_accesses=None, set=None, start_date=None):
    '''
    Update an application.

    Required Parameters:
    - id -- identifier uri, application id, or object id

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - app_roles -- declare the roles you want to associate with your application. Should be in manifest json format. See examples below for details
    - available_to_other_tenants -- the application can be used from any Azure AD tenants
    - credential_description -- the description of the password
    - display_name -- the display name of the application
    - end_date -- Date or datetime after which credentials expire(e.g. '2017-12-31T11:59:59+00:00' or '2017-12-31'). Default value is one year after current time
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - homepage -- the url where users can sign in and use your app.
    - identifier_uris -- space-separated unique URIs that Azure AD can use for this app.
    - key_type -- the type of the key credentials associated with the application
    - key_usage -- the usage of the key credentials associated with the application.
    - key_value -- the value for the key credentials associated with the application
    - oauth2_allow_implicit_flow -- whether to allow implicit grant flow for OAuth2
    - optional_claims -- declare the optional claims for the application. Should be in manifest json format. See examples below for details. Please reference https://docs.microsoft.com/azure/active-directory/develop/active-directory-optional-claims#optionalclaim-type for optional claim properties.
    - password -- app password, aka 'client secret'
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - reply_urls -- space-separated URIs to which Azure AD will redirect in response to an OAuth 2.0 request. The value does not need to be a physical endpoint, but must be a valid URI.
    - required_resource_accesses -- resource scopes and roles the application requires access to. Should be in manifest json format. See examples below for details
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - start_date -- Date or datetime at which credentials become valid(e.g. '2017-01-01T01:00:00+00:00' or '2017-01-01'). Default value is current time
    '''
    return _call_az("az ad app update", locals())

