'''
Encryption details of a Recovery Services Vault.
'''
from .... pyaz_utils import _call_az

def update(encryption_key_id, name, resource_group, infrastructure_encryption=None, mi_system_assigned=None, mi_user_assigned=None):
    '''
    Update encryption properties of a Recovery Services Vault.

    Required Parameters:
    - encryption_key_id -- The encryption key id you want to use for encryption
    - name -- Name of the Recovery services vault.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - infrastructure_encryption -- Use this parameter to enable/disable infrastructure encryption. This must be set when configuring encryption of the vault for the first time. Once enabled/disabled, infrastructure encryption setting cannot be changed. Default value: Disabled. Allowed values: Enabled, Disabled
    - mi_system_assigned -- Provide this flag to use system assigned identity for encryption.
    - mi_user_assigned -- UserAssigned Identity Id to be used for CMK encryption, this will be applicable for encryption using userassigned identity
    '''
    return _call_az("az backup vault encryption update", locals())


def show(name, resource_group):
    '''
    Show details of encryption properties of a Recovery Services Vault.

    Required Parameters:
    - name -- Name of the Recovery services vault.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az backup vault encryption show", locals())

