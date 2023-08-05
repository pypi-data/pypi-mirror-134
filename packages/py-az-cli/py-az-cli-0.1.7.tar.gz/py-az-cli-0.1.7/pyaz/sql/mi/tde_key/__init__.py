from .... pyaz_utils import _call_az

def show(managed_instance, resource_group):
    '''
    

    Required Parameters:
    - managed_instance -- Name of the Azure SQL managed instance.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql mi tde-key show", locals())


def set(managed_instance, resource_group, server_key_type, auto_rotation_enabled=None, kid=None):
    '''
    Sets the SQL Instance's encryption protector.

    Required Parameters:
    - managed_instance -- Name of the Azure SQL managed instance.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_key_type -- The type of the server key

    Optional Parameters:
    - auto_rotation_enabled -- The key auto rotation opt in status. Can be either true or false.
    - kid -- The Azure Key Vault key identifier of the server key. An example key identifier is "https://YourVaultName.vault.azure.net/keys/YourKeyName/01234567890123456789012345678901"
    '''
    return _call_az("az sql mi tde-key set", locals())

