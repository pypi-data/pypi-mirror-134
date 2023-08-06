'''
Manage Azure Maps accounts.
'''
from ... pyaz_utils import _call_az
from . import keys


def show(name, resource_group):
    '''
    Show the details of a maps account.

    Required Parameters:
    - name -- The name of the maps account
    - resource_group -- Resource group name
    '''
    return _call_az("az maps account show", locals())


def list(resource_group=None):
    '''
    Show all maps accounts in a subscription or in a resource group.

    Optional Parameters:
    - resource_group -- Resource group name
    '''
    return _call_az("az maps account list", locals())


def create(name, resource_group, sku, accept_tos=None, disable_local_auth=None, kind=None, linked_resources=None, tags=None, type=None, user_identities=None):
    '''
    Create a Maps Account. A Maps Account holds the keys which allow access to the Maps REST APIs.

    Required Parameters:
    - name -- The name of the maps account
    - resource_group -- Resource group name
    - sku -- The name of the SKU, in standard format (such as S0).

    Optional Parameters:
    - accept_tos -- You must agree to the License and Privacy Statement to create an account.
    - disable_local_auth -- Allows toggle functionality on Azure Policy to disable Azure Maps local authentication support. This will disable Shared Keys authentication from any usage.
    - kind -- Get or Set Kind property.
    - linked_resources -- Sets the resources to be used for Managed Identities based operations for the Map account resource.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - type -- The identity type.
    - user_identities -- The list of user identities associated with the resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'. Expected value: json-string/@json-file.
    '''
    return _call_az("az maps account create", locals())


def delete(name, resource_group):
    '''
    Delete a Maps Account.

    Required Parameters:
    - name -- The name of the maps account
    - resource_group -- Resource group name
    '''
    return _call_az("az maps account delete", locals())


def update(name, resource_group, sku, disable_local_auth=None, kind=None, linked_resources=None, tags=None, type=None, user_identities=None):
    '''
    Updates a Maps Account. Only a subset of the parameters may be updated after creation, such as Sku, Tags, Properties.

    Required Parameters:
    - name -- The name of the maps account
    - resource_group -- Resource group name
    - sku -- The name of the SKU, in standard format (such as S0).

    Optional Parameters:
    - disable_local_auth -- Allows toggle functionality on Azure Policy to disable Azure Maps local authentication support. This will disable Shared Keys authentication from any usage.
    - kind -- Get or Set Kind property.
    - linked_resources -- Sets the resources to be used for Managed Identities based operations for the Map account resource.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - type -- The identity type.
    - user_identities -- The list of user identities associated with the resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'. Expected value: json-string/@json-file.
    '''
    return _call_az("az maps account update", locals())

