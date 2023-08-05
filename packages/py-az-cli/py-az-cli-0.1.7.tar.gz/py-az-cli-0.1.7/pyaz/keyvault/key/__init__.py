'''
Manage keys.
'''
from ... pyaz_utils import _call_az
from . import rotation_policy


def list(hsm_name=None, id=None, include_managed=None, maxresults=None, vault_name=None):
    '''
    List keys in the specified Vault or HSM.

    Optional Parameters:
    - hsm_name -- Name of the HSM. (--hsm-name and --vault-name are mutually exclusive, please specify just one of them)
    - id -- Full URI of the Vault or HSM. If specified all other 'Id' arguments should be omitted.
    - include_managed -- Include managed keys. Default: false
    - maxresults -- Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    - vault_name -- Name of the Vault.
    '''
    return _call_az("az keyvault key list", locals())


def list_versions(hsm_name=None, id=None, maxresults=None, name=None, vault_name=None):
    '''
    

    Optional Parameters:
    - hsm_name -- Name of the HSM. (--hsm-name and --vault-name are mutually exclusive, please specify just one of them)
    - id -- Id of the key. If specified all other 'Id' arguments should be omitted.
    - maxresults -- Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    - name -- Name of the key. Required if --id is not specified.
    - vault_name -- Name of the Vault.
    '''
    return _call_az("az keyvault key list-versions", locals())


def list_deleted(hsm_name=None, id=None, maxresults=None, vault_name=None):
    '''
    List the deleted keys in the specified Vault or HSM.

    Optional Parameters:
    - hsm_name -- Name of the HSM. (--hsm-name and --vault-name are mutually exclusive, please specify just one of them)
    - id -- Full URI of the Vault or HSM. If specified all other 'Id' arguments should be omitted.
    - maxresults -- Maximum number of results to return in a page. If not specified the service will return up to 25 results.
    - vault_name -- Name of the Vault.
    '''
    return _call_az("az keyvault key list-deleted", locals())


def show_deleted(hsm_name=None, id=None, name=None, vault_name=None):
    '''
    Get the public part of a deleted key.

    Optional Parameters:
    - hsm_name -- Name of the HSM. (--hsm-name and --vault-name are mutually exclusive, please specify just one of them)
    - id -- The recovery id of the key. If specified all other 'Id' arguments should be omitted.
    - name -- Name of the key. Required if --id is not specified.
    - vault_name -- Name of the Vault.
    '''
    return _call_az("az keyvault key show-deleted", locals())


def delete(hsm_name=None, id=None, name=None, vault_name=None):
    '''
    Delete a key of any type from storage in Vault or HSM.

    Optional Parameters:
    - hsm_name -- Name of the HSM. (--hsm-name and --vault-name are mutually exclusive, please specify just one of them)
    - id -- Id of the key. If specified all other 'Id' arguments should be omitted.
    - name -- Name of the key. Required if --id is not specified.
    - vault_name -- Name of the Vault.
    '''
    return _call_az("az keyvault key delete", locals())


def purge(hsm_name=None, id=None, name=None, vault_name=None):
    '''
    Permanently delete the specified key.

    Optional Parameters:
    - hsm_name -- Name of the HSM. (--hsm-name and --vault-name are mutually exclusive, please specify just one of them)
    - id -- The recovery id of the key. If specified all other 'Id' arguments should be omitted.
    - name -- Name of the key. Required if --id is not specified.
    - vault_name -- Name of the Vault.
    '''
    return _call_az("az keyvault key purge", locals())


def recover(hsm_name=None, id=None, name=None, vault_name=None):
    '''
    Recover the deleted key to its latest version.

    Optional Parameters:
    - hsm_name -- Name of the HSM. (--hsm-name and --vault-name are mutually exclusive, please specify just one of them)
    - id -- The recovery id of the key. If specified all other 'Id' arguments should be omitted.
    - name -- Name of the key. Required if --id is not specified.
    - vault_name -- Name of the Vault.
    '''
    return _call_az("az keyvault key recover", locals())


def backup(file, hsm_name=None, id=None, name=None, vault_name=None):
    '''
    Request that a backup of the specified key be downloaded to the client.

    Required Parameters:
    - file -- Local file path in which to store key backup.

    Optional Parameters:
    - hsm_name -- Name of the HSM. (--hsm-name and --vault-name are mutually exclusive, please specify just one of them)
    - id -- Id of the key. If specified all other 'Id' arguments should be omitted.
    - name -- Name of the key. Required if --id is not specified.
    - vault_name -- Name of the Vault.
    '''
    return _call_az("az keyvault key backup", locals())


def restore(backup_folder=None, blob_container_name=None, file=None, hsm_name=None, id=None, name=None, no_wait=None, storage_account_name=None, storage_container_SAS_token=None, storage_resource_uri=None, vault_name=None):
    '''
    Restore a backed up key to a Vault or HSM.

    Optional Parameters:
    - backup_folder -- Name of the blob container which contains the backup
    - blob_container_name -- Name of Blob Container.
    - file -- Local key backup from which to restore key.
    - hsm_name -- Name of the HSM. (--hsm-name and --vault-name are mutually exclusive, please specify just one of them)
    - id -- Full URI of the Vault or HSM. If specified all other 'Id' arguments should be omitted.
    - name -- Name of the key. (Only for restoring from storage account)
    - no_wait -- Do not wait for the long-running operation to finish.
    - storage_account_name -- Name of Azure Storage Account.
    - storage_container_SAS_token -- The SAS token pointing to an Azure Blob storage container
    - storage_resource_uri -- Azure Blob storage container Uri. If specified, all other 'Storage Id' arguments should be omitted
    - vault_name -- Name of the Vault.
    '''
    return _call_az("az keyvault key restore", locals())


def download(file, encoding=None, hsm_name=None, id=None, name=None, vault_name=None, version=None):
    '''
    Download the public part of a stored key.

    Required Parameters:
    - file -- File to receive the key contents.

    Optional Parameters:
    - encoding -- Encoding of the key, default: PEM
    - hsm_name -- Name of the HSM. (--hsm-name and --vault-name are mutually exclusive, please specify just one of them)
    - id -- Id of the key. If specified all other 'Id' arguments should be omitted.
    - name -- Name of the key. Required if --id is not specified.
    - vault_name -- Name of the Vault.
    - version -- The key version. If omitted, uses the latest version.
    '''
    return _call_az("az keyvault key download", locals())


def create(curve=None, disabled=None, expires=None, exportable=None, hsm_name=None, id=None, kty=None, name=None, not_before=None, ops=None, policy=None, protection=None, size=None, tags=None, vault_name=None):
    '''
    Create a new key, stores it, then returns key parameters and attributes to the client.

    Optional Parameters:
    - curve -- Elliptic curve name. For valid values, see: https://docs.microsoft.com/rest/api/keyvault/createkey/createkey#jsonwebkeycurvename
    - disabled -- Create key in disabled state.
    - expires -- Expiration UTC datetime  (Y-m-d'T'H:M:S'Z').
    - exportable -- Whether the private key can be exported. To create key with release policy, "exportable" must be true and caller must have "export" permission.
    - hsm_name -- Name of the HSM. (--hsm-name and --vault-name are mutually exclusive, please specify just one of them)
    - id -- Id of the key. If specified all other 'Id' arguments should be omitted.
    - kty -- The type of key to create. For valid values, see: https://docs.microsoft.com/rest/api/keyvault/createkey/createkey#jsonwebkeytype
    - name -- Name of the key. Required if --id is not specified.
    - not_before -- Key not usable before the provided UTC datetime  (Y-m-d'T'H:M:S'Z').
    - ops -- Space-separated list of permitted JSON web key operations.
    - policy -- The policy rules under which the key can be exported. Policy definition as JSON, or a path to a file containing JSON policy definition.
    - protection -- Specifies the type of key protection.
    - size -- The key size in bits. For example: 2048, 3072, or 4096 for RSA. 128, 192, or 256 for oct.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - vault_name -- Name of the Vault.
    '''
    return _call_az("az keyvault key create", locals())


def set_attributes(enabled=None, expires=None, hsm_name=None, id=None, name=None, not_before=None, ops=None, policy=None, tags=None, vault_name=None, version=None):
    '''
    The update key operation changes specified attributes of a stored key and can be applied to any key type and key version stored in Vault or HSM.

    Optional Parameters:
    - enabled -- Enable the key.
    - expires -- Expiration UTC datetime  (Y-m-d'T'H:M:S'Z').
    - hsm_name -- Name of the HSM. (--hsm-name and --vault-name are mutually exclusive, please specify just one of them)
    - id -- Id of the key. If specified all other 'Id' arguments should be omitted.
    - name -- Name of the key. Required if --id is not specified.
    - not_before -- Key not usable before the provided UTC datetime  (Y-m-d'T'H:M:S'Z').
    - ops -- Space-separated list of permitted JSON web key operations.
    - policy -- The policy rules under which the key can be exported. Policy definition as JSON, or a path to a file containing JSON policy definition.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - vault_name -- Name of the Vault.
    - version -- The key version. If omitted, uses the latest version.
    '''
    return _call_az("az keyvault key set-attributes", locals())


def show(hsm_name=None, id=None, name=None, vault_name=None, version=None):
    '''
    

    Optional Parameters:
    - hsm_name -- Name of the HSM. (--hsm-name and --vault-name are mutually exclusive, please specify just one of them)
    - id -- Id of the key. If specified all other 'Id' arguments should be omitted.
    - name -- Name of the key. Required if --id is not specified.
    - vault_name -- Name of the Vault.
    - version -- The key version. If omitted, uses the latest version.
    '''
    return _call_az("az keyvault key show", locals())


def import_(byok_file=None, byok_string=None, curve=None, disabled=None, expires=None, exportable=None, hsm_name=None, id=None, kty=None, name=None, not_before=None, ops=None, pem_file=None, pem_password=None, pem_string=None, policy=None, protection=None, tags=None, vault_name=None):
    '''
    

    Optional Parameters:
    - byok_file -- BYOK file containing the key to be imported. Must not be password protected.
    - byok_string -- BYOK string containing the key to be imported. Must not be password protected.
    - curve -- The curve name of the key to import (only for BYOK).
    - disabled -- Create key in disabled state.
    - expires -- Expiration UTC datetime  (Y-m-d'T'H:M:S'Z').
    - exportable -- Whether the private key can be exported. To create key with release policy, "exportable" must be true and caller must have "export" permission.
    - hsm_name -- Name of the HSM. (--hsm-name and --vault-name are mutually exclusive, please specify just one of them)
    - id -- Id of the key. If specified all other 'Id' arguments should be omitted.
    - kty -- The type of key to import (only for BYOK).
    - name -- Name of the key. Required if --id is not specified.
    - not_before -- Key not usable before the provided UTC datetime  (Y-m-d'T'H:M:S'Z').
    - ops -- Space-separated list of permitted JSON web key operations.
    - pem_file -- PEM file containing the key to be imported.
    - pem_password -- Password of PEM file.
    - pem_string -- PEM string containing the key to be imported.
    - policy -- The policy rules under which the key can be exported. Policy definition as JSON, or a path to a file containing JSON policy definition.
    - protection -- Specifies the type of key protection.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - vault_name -- Name of the Vault.
    '''
    return _call_az("az keyvault key import", locals())


def get_policy_template():
    '''
    Return policy template as JSON encoded policy definition.
    '''
    return _call_az("az keyvault key get-policy-template", locals())


def encrypt(algorithm, value, aad=None, data_type=None, hsm_name=None, id=None, iv=None, name=None, vault_name=None, version=None):
    '''
    Encrypt an arbitrary sequence of bytes using an encryption key that is stored in a Vault or HSM.

    Required Parameters:
    - algorithm -- Algorithm identifier
    - value -- The value to be encrypted. Default data type is Base64 encoded string.

    Optional Parameters:
    - aad -- Optional data that is authenticated but not encrypted. For use with AES-GCM encryption.
    - data_type -- The type of the original data.
    - hsm_name -- Name of the HSM. (--hsm-name and --vault-name are mutually exclusive, please specify just one of them)
    - id -- Id of the key. If specified all other 'Id' arguments should be omitted.
    - iv -- Initialization vector. Required for only AES-CBC(PAD) encryption.
    - name -- Name of the key. Required if --id is not specified.
    - vault_name -- Name of the Vault.
    - version -- The key version. If omitted, uses the latest version.
    '''
    return _call_az("az keyvault key encrypt", locals())


def decrypt(algorithm, value, aad=None, data_type=None, hsm_name=None, id=None, iv=None, name=None, tag=None, vault_name=None, version=None):
    '''
    Decrypt a single block of encrypted data.

    Required Parameters:
    - algorithm -- Algorithm identifier
    - value -- The value to be decrypted, which should be the result of "az keyvault encrypt"

    Optional Parameters:
    - aad -- Optional data that is authenticated but not encrypted. For use with AES-GCM decryption.
    - data_type -- The type of the original data.
    - hsm_name -- Name of the HSM. (--hsm-name and --vault-name are mutually exclusive, please specify just one of them)
    - id -- Id of the key. If specified all other 'Id' arguments should be omitted.
    - iv -- The initialization vector used during encryption. Required for AES decryption.
    - name -- Name of the key. Required if --id is not specified.
    - tag -- The authentication tag generated during encryption. Required for only AES-GCM decryption.
    - vault_name -- Name of the Vault.
    - version -- The key version. If omitted, uses the latest version.
    '''
    return _call_az("az keyvault key decrypt", locals())


def random(count, hsm_name=None, id=None):
    '''
    

    Required Parameters:
    - count -- The requested number of random bytes.

    Optional Parameters:
    - hsm_name -- Name of the HSM.
    - id -- Full URI of the HSM.
    '''
    return _call_az("az keyvault key random", locals())


def rotate(hsm_name=None, id=None, name=None, vault_name=None):
    '''
    Rotate the key based on the key policy by generating a new version of the key.

    Optional Parameters:
    - hsm_name -- Name of the HSM. (--hsm-name and --vault-name are mutually exclusive, please specify just one of them)
    - id -- Id of the key. If specified all other 'Id' arguments should be omitted.
    - name -- Name of the key. Required if --id is not specified.
    - vault_name -- Name of the Vault.
    '''
    return _call_az("az keyvault key rotate", locals())

