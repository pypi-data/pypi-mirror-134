from .... pyaz_utils import _call_az

def start(destination_blob, destination_container, account_key=None, account_name=None, auth_mode=None, connection_string=None, destination_if_match=None, destination_if_modified_since=None, destination_if_none_match=None, destination_if_unmodified_since=None, destination_lease_id=None, metadata=None, sas_token=None, source_account_key=None, source_account_name=None, source_blob=None, source_container=None, source_lease_id=None, source_sas=None, source_snapshot=None, source_uri=None, timeout=None):
    '''
    Copies an incremental copy of a blob asynchronously.

    Required Parameters:
    - destination_blob -- Name of the destination blob. If the exists, it will be overwritten.
    - destination_container -- The container name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - destination_if_match --  An ETag value, or the wildcard character (*). Specify an ETag value for this conditional header to copy the blob only if the specified ETag value matches the ETag value for an existing destination blob. If the ETag for the destination blob does not match the ETag specified for If-Match, the Blob service returns status code 412 (Precondition Failed).
    - destination_if_modified_since -- Commence only if modified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - destination_if_none_match --  An ETag value, or the wildcard character (*). Specify an ETag value for this conditional header to copy the blob only if the specified ETag value does not match the ETag value for the destination blob. Specify the wildcard character (*) to perform the operation only if the destination blob does not exist. If the specified condition isn't met, the Blob service returns status code 412 (Precondition Failed).
    - destination_if_unmodified_since -- Commence only if unmodified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - destination_lease_id --  The lease ID specified for this header must match the lease ID of the destination blob. If the request does not include the lease ID or it is not valid, the operation fails with status code 412 (Precondition Failed).
    - metadata -- Metadata in space-separated key=value pairs. This overwrites any existing metadata.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - source_account_key -- The storage account key of the source blob.
    - source_account_name -- The storage account name of the source blob.
    - source_blob -- The blob name for the source storage account.
    - source_container -- The container name for the source storage account.
    - source_lease_id --  Specify this to perform the Copy Blob operation only if the lease ID given matches the active lease ID of the source blob.
    - source_sas -- The shared access signature for the source storage account.
    - source_snapshot -- The blob snapshot for the source storage account.
    - source_uri --  A URL of up to 2 KB in length that specifies an Azure page blob. The value should be URL-encoded as it would appear in a request URI. The copy source must be a snapshot and include a valid SAS token or be public. Example: https://myaccount.blob.core.windows.net/mycontainer/myblob?snapshot=<DateTime>&sastoken
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage blob incremental-copy start", locals())


def cancel(container_name, copy_id, name, account_key=None, account_name=None, auth_mode=None, connection_string=None, lease_id=None, sas_token=None, timeout=None):
    '''
    

    Required Parameters:
    - container_name -- The container name.
    - copy_id --  Copy identifier provided in the copy.id of the original copy_blob operation.
    - name -- The blob name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - lease_id --  Required if the destination blob has an active infinite lease.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage blob incremental-copy cancel", locals())

