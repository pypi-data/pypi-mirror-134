'''
Manage blob copy operations. Use `az storage blob show` to check the status of the blobs.
'''
from .... pyaz_utils import _call_az

def start(destination_blob, destination_container, account_key=None, account_name=None, auth_mode=None, connection_string=None, destination_if_match=None, destination_if_modified_since=None, destination_if_none_match=None, destination_if_unmodified_since=None, destination_lease_id=None, destination_tags_condition=None, metadata=None, rehydrate_priority=None, requires_sync=None, sas_token=None, source_account_key=None, source_account_name=None, source_blob=None, source_container=None, source_if_match=None, source_if_modified_since=None, source_if_none_match=None, source_if_unmodified_since=None, source_lease_id=None, source_path=None, source_sas=None, source_share=None, source_snapshot=None, source_tags_condition=None, source_uri=None, tags=None, tier=None, timeout=None):
    '''
    Copy a blob asynchronously. Use `az storage blob show` to check the status of the blobs.

    Required Parameters:
    - destination_blob -- Name of the destination blob. If the exists, it will be overwritten.
    - destination_container -- The container name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - destination_if_match -- An ETag value, or the wildcard character (*). Specify this header to perform the operation only if the resource's ETag matches the value specified.
    - destination_if_modified_since -- Commence only if modified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - destination_if_none_match -- An ETag value, or the wildcard character (*). Specify this header to perform the operation only if the resource's ETag does not match the value specified. Specify the wildcard character (*) to perform the operation only if the resource does not exist, and fail the operation if it does exist.
    - destination_if_unmodified_since -- Commence only if unmodified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - destination_lease_id -- The lease ID specified for this header must match the lease ID of the estination blob. If the request does not include the lease ID or it is not valid, the operation fails with status code 412 (Precondition Failed).
    - destination_tags_condition -- Specify a SQL where clause on blob tags to operate only on blobs with a matching value.
    - metadata -- Metadata in space-separated key=value pairs. This overwrites any existing metadata.
    - rehydrate_priority -- Indicate the priority with which to rehydrate an archived blob.
    - requires_sync -- Enforce that the service will not return a response until the copy is complete.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - source_account_key -- The storage account key of the source blob.
    - source_account_name -- The storage account name of the source blob.
    - source_blob -- The blob name for the source storage account.
    - source_container -- The container name for the source storage account.
    - source_if_match -- An ETag value, or the wildcard character (*). Specify this header to perform the operation only if the resource's ETag matches the value specified.
    - source_if_modified_since -- Commence only if modified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - source_if_none_match -- An ETag value, or the wildcard character (*). Specify this header to perform the operation only if the resource's ETag does not match the value specified. Specify the wildcard character (*) to perform the operation only if the resource does not exist, and fail the operation if it does exist.
    - source_if_unmodified_since -- Commence only if unmodified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - source_lease_id -- Specify this to perform the Copy Blob operation only if the lease ID given matches the active lease ID of the source blob.
    - source_path -- The file path for the source storage account.
    - source_sas -- The shared access signature for the source storage account.
    - source_share -- The share name for the source storage account.
    - source_snapshot -- The blob snapshot for the source storage account.
    - source_tags_condition -- Specify a SQL where clause on blob tags to operate only on blobs with a matching value.
    - source_uri -- None
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - tier -- The tier value to set the blob to. For page blob, the tier correlates to the size of the blob and number of allowed IOPS. Possible values are P10, P15, P20, P30, P4, P40, P50, P6, P60, P70, P80 and this is only applicable to page blobs on premium storage accounts; For block blob, possible values are Archive, Cool and Hot. This is only applicable to block blobs on standard storage accounts.
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage blob copy start", locals())


def cancel(copy_id, destination_blob, destination_container, account_key=None, account_name=None, auth_mode=None, connection_string=None, lease_id=None, sas_token=None, timeout=None):
    '''
    

    Required Parameters:
    - copy_id --  Copy identifier provided in the copy.id of the original copy_blob operation.
    - destination_blob -- Name of the destination blob. If the exists, it will be overwritten.
    - destination_container -- The container name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - lease_id --  Required if the destination blob has an active infinite lease.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage blob copy cancel", locals())


def start_batch(account_key=None, account_name=None, auth_mode=None, connection_string=None, destination_container=None, destination_path=None, dryrun=None, pattern=None, sas_token=None, source_account_key=None, source_account_name=None, source_client=None, source_container=None, source_sas=None, source_share=None, source_uri=None):
    '''
    Copy multiple blobs to a blob container. Use `az storage blob show` to check the status of the blobs.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - destination_container -- The container name.
    - destination_path -- The destination path that will be prepended to the blob name.
    - dryrun -- None
    - pattern -- None
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - source_account_key -- None
    - source_account_name -- None
    - source_client -- ==SUPPRESS==
    - source_container -- None
    - source_sas -- None
    - source_share -- None
    - source_uri -- None
    '''
    return _call_az("az storage blob copy start-batch", locals())

