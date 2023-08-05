'''
Manage blob metadata.
'''
from .... pyaz_utils import _call_az

def show(container_name, name, account_key=None, account_name=None, auth_mode=None, connection_string=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None, lease_id=None, sas_token=None, snapshot=None, timeout=None):
    '''
    

    Required Parameters:
    - container_name -- The container name.
    - name -- The blob name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - if_match --  An ETag value, or the wildcard character (*). Specify this header to perform the operation only if the resource's ETag matches the value specified.
    - if_modified_since -- Commence only if modified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - if_none_match --  An ETag value, or the wildcard character (*). Specify this header to perform the operation only if the resource's ETag does not match the value specified. Specify the wildcard character (*) to perform the operation only if the resource does not exist, and fail the operation if it does exist.
    - if_unmodified_since -- Commence only if unmodified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - lease_id --  Required if the blob has an active lease.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - snapshot --  The snapshot parameter is an opaque value that, when present, specifies the blob snapshot to retrieve.
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage blob metadata show", locals())


def update(container_name, name, account_key=None, account_name=None, auth_mode=None, connection_string=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None, lease_id=None, metadata=None, sas_token=None, timeout=None):
    '''
    

    Required Parameters:
    - container_name -- The container name.
    - name -- The blob name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - if_match --  An ETag value, or the wildcard character (*). Specify this header to perform the operation only if the resource's ETag matches the value specified.
    - if_modified_since -- Commence only if modified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - if_none_match --  An ETag value, or the wildcard character (*). Specify this header to perform the operation only if the resource's ETag does not match the value specified. Specify the wildcard character (*) to perform the operation only if the resource does not exist, and fail the operation if it does exist.
    - if_unmodified_since -- Commence only if unmodified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - lease_id --  Required if the blob has an active lease.
    - metadata -- Metadata in space-separated key=value pairs. This overwrites any existing metadata.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage blob metadata update", locals())

