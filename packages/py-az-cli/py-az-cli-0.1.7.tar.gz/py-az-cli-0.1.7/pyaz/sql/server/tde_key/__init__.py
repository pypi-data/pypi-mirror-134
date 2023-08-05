from .... pyaz_utils import _call_az

def show(resource_group, server):
    '''
    

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql server tde-key show", locals())


def set(resource_group, server, server_key_type, auto_rotation_enabled=None, kid=None):
    '''
    Sets the server's encryption protector.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    - server_key_type -- The type of the server key

    Optional Parameters:
    - auto_rotation_enabled -- The key auto rotation opt in status. Can be either true or false.
    - kid -- The Azure Key Vault key identifier of the server key. An example key identifier is "https://YourVaultName.vault.azure.net/keys/YourKeyName/01234567890123456789012345678901"
    '''
    return _call_az("az sql server tde-key set", locals())

