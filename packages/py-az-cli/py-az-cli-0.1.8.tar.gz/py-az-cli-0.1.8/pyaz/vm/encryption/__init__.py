'''
Manage encryption of VM disks.
'''
from ... pyaz_utils import _call_az

def enable(disk_encryption_keyvault, name, resource_group, aad_client_cert_thumbprint=None, aad_client_id=None, aad_client_secret=None, encrypt_format_all=None, force=None, key_encryption_algorithm=None, key_encryption_key=None, key_encryption_keyvault=None, volume_type=None):
    '''
    Enable disk encryption on the OS disk and/or data disks. Encrypt mounted disks.

    Required Parameters:
    - disk_encryption_keyvault -- Name or ID of the key vault where the generated encryption key will be placed.
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - aad_client_cert_thumbprint -- None
    - aad_client_id -- None
    - aad_client_secret -- None
    - encrypt_format_all -- Encrypts-formats data disks instead of encrypting them. Encrypt-formatting is a lot faster than in-place encryption but wipes out the partition getting encrypt-formatted.
    - force -- continue by ignoring client side validation errors
    - key_encryption_algorithm -- None
    - key_encryption_key -- Key vault key name or URL used to encrypt the disk encryption key.
    - key_encryption_keyvault -- Name or ID of the key vault containing the key encryption key used to encrypt the disk encryption key. If missing, CLI will use `--disk-encryption-keyvault`.
    - volume_type -- Type of volume that the encryption operation is performed on
    '''
    return _call_az("az vm encryption enable", locals())


def disable(name, resource_group, force=None, volume_type=None):
    '''
    Disable disk encryption on the OS disk and/or data disks. Decrypt mounted disks.

    Required Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - force -- continue by ignoring client side validation errors
    - volume_type -- Type of volume that the encryption operation is performed on
    '''
    return _call_az("az vm encryption disable", locals())


def show(name, resource_group):
    '''
    Show encryption status.

    Required Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vm encryption show", locals())

