'''
Manage a SQL Instance's keys.
'''
from .... pyaz_utils import _call_az

def create(kid, managed_instance, resource_group):
    '''
    Creates a SQL Instance key.

    Required Parameters:
    - kid -- The Azure Key Vault key identifier of the server key. An example key identifier is "https://YourVaultName.vault.azure.net/keys/YourKeyName/01234567890123456789012345678901"
    - managed_instance -- Name of the Azure SQL managed instance.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql mi key create", locals())


def delete(kid, managed_instance, resource_group):
    '''
    Deletes a SQL Instance key.

    Required Parameters:
    - kid -- The Azure Key Vault key identifier of the server key. An example key identifier is "https://YourVaultName.vault.azure.net/keys/YourKeyName/01234567890123456789012345678901"
    - managed_instance -- Name of the Azure SQL managed instance.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql mi key delete", locals())


def show(kid, managed_instance, resource_group):
    '''
    Shows a SQL Instance key.

    Required Parameters:
    - kid -- The Azure Key Vault key identifier of the server key. An example key identifier is "https://YourVaultName.vault.azure.net/keys/YourKeyName/01234567890123456789012345678901"
    - managed_instance -- Name of the Azure SQL managed instance.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql mi key show", locals())


def list(managed_instance, resource_group, filter=None):
    '''
    

    Required Parameters:
    - managed_instance -- Name of the Azure SQL managed instance.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - filter -- An OData filter expression that filters elements in the collection.
    '''
    return _call_az("az sql mi key list", locals())

