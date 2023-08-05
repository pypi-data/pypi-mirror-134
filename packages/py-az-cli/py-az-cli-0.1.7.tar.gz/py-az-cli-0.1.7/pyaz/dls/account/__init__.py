'''
Manage Data Lake Store accounts.
'''
from ... pyaz_utils import _call_az
from . import firewall, network_rule, trusted_provider


def create(account, default_group=None, disable_encryption=None, encryption_type=None, key_name=None, key_vault_id=None, key_version=None, location=None, resource_group=None, tags=None, tier=None):
    '''
    Creates a Data Lake Store account.

    Required Parameters:
    - account -- Name of the Data Lake Store account.

    Optional Parameters:
    - default_group -- Name of the default group to give permissions to for freshly created files and folders in the Data Lake Store account.
    - disable_encryption -- Indicates that the account will not have any form of encryption applied to it.
    - encryption_type -- Indicates what type of encryption to provision the account with. By default, encryption is ServiceManaged. If no encryption is desired, it must be explicitly set with the --disable-encryption flag.
    - key_name -- None
    - key_vault_id -- None
    - key_version -- Key version for the user-assigned encryption type.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - tier -- The desired commitment tier for this account to use.
    '''
    return _call_az("az dls account create", locals())


def update(account, allow_azure_ips=None, default_group=None, firewall_state=None, key_version=None, resource_group=None, tags=None, tier=None, trusted_id_provider_state=None):
    '''
    Updates a Data Lake Store account.

    Required Parameters:
    - account -- Name of the Data Lake Store account.

    Optional Parameters:
    - allow_azure_ips -- Allow/block Azure originating IPs through the firewall
    - default_group -- Name of the default group to give permissions to for freshly created files and folders in the Data Lake Store account.
    - firewall_state -- Enable/disable existing firewall rules.
    - key_version -- Key version for the user-assigned encryption type.
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Store account.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - tier -- The desired commitment tier for this account to use.
    - trusted_id_provider_state -- Enable/disable the existing trusted ID providers.
    '''
    return _call_az("az dls account update", locals())


def list(resource_group=None):
    '''
    Lists available Data Lake Store accounts.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az dls account list", locals())


def delete(account, resource_group=None):
    '''
    Delete a Data Lake Store account.

    Required Parameters:
    - account -- Name of the Data Lake Store account.

    Optional Parameters:
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Store account.
    '''
    return _call_az("az dls account delete", locals())


def show(account, resource_group=None):
    '''
    Get the details of a Data Lake Store account.

    Required Parameters:
    - account -- Name of the Data Lake Store account.

    Optional Parameters:
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Store account.
    '''
    return _call_az("az dls account show", locals())


def enable_key_vault(account, resource_group=None):
    '''
    Enable the use of Azure Key Vault for encryption of a Data Lake Store account.

    Required Parameters:
    - account -- Name of the Data Lake Store account.

    Optional Parameters:
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Store account.
    '''
    return _call_az("az dls account enable-key-vault", locals())

