'''
Manage Azure subscription information.
'''
from .. pyaz_utils import _call_az
from . import lock, management_group


def list(all=None, refresh=None):
    '''
    Get a list of subscriptions for the logged in account. By default, only 'Enabled' subscriptions from the current cloud is shown.

    Optional Parameters:
    - all -- List all subscriptions from all clouds, rather than just 'Enabled' ones
    - refresh -- retrieve up-to-date subscriptions from server
    '''
    return _call_az("az account list", locals())


def set(subscription):
    '''
    Set a subscription to be the current active subscription.

    Required Parameters:
    - subscription -- Name or ID of subscription.
    '''
    return _call_az("az account set", locals())


def show(sdk_auth=None, subscription=None):
    '''
    Get the details of a subscription.

    Optional Parameters:
    - sdk_auth -- Output result to a file compatible with Azure SDK auth. Only applicable when authenticating with a Service Principal.
    - subscription -- Name or ID of subscription.
    '''
    return _call_az("az account show", locals())


def clear():
    '''
    Clear all subscriptions from the CLI's local cache.
    '''
    return _call_az("az account clear", locals())


def list_locations():
    '''
    List supported regions for the current subscription.
    '''
    return _call_az("az account list-locations", locals())


def get_access_token(resource=None, resource_type=None, scope=None, subscription=None, tenant=None):
    '''
    Get a token for utilities to access Azure.

    Optional Parameters:
    - resource -- Azure resource endpoints in AAD v1.0.
    - resource_type -- Type of well-known resource.
    - scope -- Space-separated AAD scopes in AAD v2.0. Default to Azure Resource Manager.
    - subscription -- Name or ID of subscription.
    - tenant -- Tenant ID for which the token is acquired. Only available for user and service principal account, not for MSI or Cloud Shell account
    '''
    return _call_az("az account get-access-token", locals())

