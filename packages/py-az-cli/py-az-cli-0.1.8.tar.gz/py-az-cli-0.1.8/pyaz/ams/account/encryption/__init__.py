'''
Manage encryption for an Azure Media Services account.
'''
from .... pyaz_utils import _call_az

def show(account_name, resource_group):
    '''
    Show the details of encryption settings for an Azure Media Services account.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams account encryption show", locals())


def set(account_name, key_type, resource_group, current_key_id=None, key_identifier=None):
    '''
    Set the encryption settings for an Azure Media Services account.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - key_type -- The encryption key source (provider). Allowed values: SystemKey, CustomerKey.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - current_key_id -- The current key used to encrypt the Media Services account, including the key version.
    - key_identifier -- The URL of the Key Vault key used to encrypt the account. The key may either be versioned (for example https://vault/keys/mykey/version1) or reference a key without a version (for example https://vault/keys/mykey).
    '''
    return _call_az("az ams account encryption set", locals())

