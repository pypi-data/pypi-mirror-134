'''
Manage resource providers.
'''
from .. pyaz_utils import _call_az
from . import operation, permission


def list(expand=None):
    '''
    

    Optional Parameters:
    - expand -- The properties to include in the results. For example, use &$expand=metadata in the query string to retrieve resource provider metadata. To include property aliases in response, use $expand=resourceTypes/aliases.
    '''
    return _call_az("az provider list", locals())


def show(namespace, expand=None):
    '''
    

    Required Parameters:
    - namespace -- the resource namespace, aka 'provider'

    Optional Parameters:
    - expand -- The $expand query parameter. For example, to include property aliases in response, use $expand=resourceTypes/aliases.
    '''
    return _call_az("az provider show", locals())


def register(namespace, accept_terms=None, consent_to_permissions=None, management_group_id=None, wait=None):
    '''
    Register a provider.

    Required Parameters:
    - namespace -- the resource namespace, aka 'provider'

    Optional Parameters:
    - accept_terms -- Accept market place terms and RP terms for RPaaS. Required when registering RPs from RPaaS, such as 'Microsoft.Confluent' and 'Microsoft.Datadog'.
    - consent_to_permissions -- A value indicating whether authorization is consented or not.
    - management_group_id -- The management group id to register.
    - wait -- wait for the registration to finish
    '''
    return _call_az("az provider register", locals())


def unregister(namespace, wait=None):
    '''
    Unregister a provider.

    Required Parameters:
    - namespace -- the resource namespace, aka 'provider'

    Optional Parameters:
    - wait -- wait for unregistration to finish
    '''
    return _call_az("az provider unregister", locals())

