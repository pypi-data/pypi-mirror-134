'''
Manage an application's OAuth2 permissions.
'''
from .... pyaz_utils import _call_az

def grant(api, id, consent_type=None, expires=None, principal_id=None, scope=None):
    '''
    Grant the app an API Delegated permissions

    Required Parameters:
    - api -- Specify `RequiredResourceAccess.resourceAppId` - The unique identifier for the resource that the application requires access to. This should be equal to the appId declared on the target resource application.
    - id -- identifier uri, application id, or object id

    Optional Parameters:
    - consent_type -- Indicates if consent was provided by the administrator (on behalf of the organization) or by an individual.
    - expires -- Expiry date for the permissions in years. e.g. 1, 2 or "never"
    - principal_id -- If --consent-type is "Principal", this argument specifies the object of the user that granted consent and applies only for that user.
    - scope -- Specifies the value of the scope claim that the resource application should expect in the OAuth 2.0 access token, e.g. User.Read
    '''
    return _call_az("az ad app permission grant", locals())


def list(id):
    '''
    List API permissions the application has requested

    Required Parameters:
    - id -- identifier uri, application id, or object id of the associated application
    '''
    return _call_az("az ad app permission list", locals())


def add(api, api_permissions, id):
    '''
    Add an API permission

    Required Parameters:
    - api -- Specify `RequiredResourceAccess.resourceAppId` - The unique identifier for the resource that the application requires access to. This should be equal to the appId declared on the target resource application.
    - api_permissions -- Specify `ResourceAccess.id` - The unique identifier for one of the OAuth2Permission or AppRole instances that the resource application exposes. Space-separated list of `<resource-access-id>=<type>`.
    - id -- identifier uri, application id, or object id
    '''
    return _call_az("az ad app permission add", locals())


def delete(api, id, api_permissions=None):
    '''
    Remove an API permission

    Required Parameters:
    - api -- Specify `RequiredResourceAccess.resourceAppId` - The unique identifier for the resource that the application requires access to. This should be equal to the appId declared on the target resource application.
    - id -- identifier uri, application id, or object id

    Optional Parameters:
    - api_permissions -- Specify `ResourceAccess.id` - The unique identifier for one of the OAuth2Permission or AppRole instances that the resource application exposes. Space-separated list of `<resource-access-id>`.
    '''
    return _call_az("az ad app permission delete", locals())


def list_grants(filter=None, id=None, show_resource_name=None):
    '''
    List Oauth2 permission grants

    Optional Parameters:
    - filter -- OData filter, e.g. --filter "displayname eq 'test' and servicePrincipalType eq 'Application'"
    - id -- identifier uri, application id, or object id
    - show_resource_name -- show resource's display name
    '''
    return _call_az("az ad app permission list-grants", locals())


def admin_consent(id):
    '''
    Grant Application & Delegated permissions through admin-consent.

    Required Parameters:
    - id -- identifier uri, application id, or object id
    '''
    return _call_az("az ad app permission admin-consent", locals())

