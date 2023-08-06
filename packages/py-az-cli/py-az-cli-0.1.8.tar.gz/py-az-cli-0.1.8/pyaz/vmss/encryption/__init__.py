'''
Manage encryption of VMSS.
'''
from ... pyaz_utils import _call_az

def enable(disk_encryption_keyvault, name, resource_group, force=None, key_encryption_algorithm=None, key_encryption_key=None, key_encryption_keyvault=None, volume_type=None):
    '''
    Encrypt a VMSS with managed disks.

    Required Parameters:
    - disk_encryption_keyvault -- Name or ID of the key vault where the generated encryption key will be placed.
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - force -- continue by ignoring client side validation errors
    - key_encryption_algorithm -- None
    - key_encryption_key -- Key vault key name or URL used to encrypt the disk encryption key.
    - key_encryption_keyvault -- Name or ID of the key vault containing the key encryption key used to encrypt the disk encryption key. If missing, CLI will use `--disk-encryption-keyvault`.
    - volume_type -- Type of volume that the encryption operation is performed on
    '''
    return _call_az("az vmss encryption enable", locals())


def disable(name, resource_group, force=None, volume_type=None):
    '''
    Disable the encryption on a VMSS with managed disks.

    Required Parameters:
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - force -- continue by ignoring client side validation errors
    - volume_type -- Type of volume that the encryption operation is performed on
    '''
    return _call_az("az vmss encryption disable", locals())


def show(name, resource_group):
    '''
    Show encryption status.

    Required Parameters:
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vmss encryption show", locals())

