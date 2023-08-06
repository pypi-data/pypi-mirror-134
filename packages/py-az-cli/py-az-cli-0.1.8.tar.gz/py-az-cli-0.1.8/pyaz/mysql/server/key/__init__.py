'''
Manage MySQL server keys.
'''
from .... pyaz_utils import _call_az

def create(kid, name, resource_group):
    '''
    Create server key.

    Required Parameters:
    - kid -- The Azure Key Vault key identifier of the server key. An example key identifier is "https://YourVaultName.vault.azure.net/keys/YourKeyName/01234567890123456789012345678901"
    - name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az mysql server key create", locals())


def delete(kid, name, resource_group, yes=None):
    '''
    Delete server key.

    Required Parameters:
    - kid -- The Azure Key Vault key identifier of the server key. An example key identifier is "https://YourVaultName.vault.azure.net/keys/YourKeyName/01234567890123456789012345678901"
    - name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az mysql server key delete", locals())


def show(kid, name, resource_group):
    '''
    Show server key.

    Required Parameters:
    - kid -- The Azure Key Vault key identifier of the server key. An example key identifier is "https://YourVaultName.vault.azure.net/keys/YourKeyName/01234567890123456789012345678901"
    - name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az mysql server key show", locals())


def list(name, resource_group):
    '''
    

    Required Parameters:
    - name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az mysql server key list", locals())

