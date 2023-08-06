'''
Manage file copy operations.
'''
from .... pyaz_utils import _call_az

def start(destination_path, destination_share, account_key=None, account_name=None, connection_string=None, file_snapshot=None, metadata=None, sas_token=None, source_account_key=None, source_account_name=None, source_blob=None, source_container=None, source_path=None, source_sas=None, source_share=None, source_snapshot=None, source_uri=None, timeout=None):
    '''
    Copy a file asynchronously.

    Required Parameters:
    - destination_path -- The path to the file within the file share.
    - destination_share -- Name of the destination share. The share must exist.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - file_snapshot -- The file snapshot for the source storage account.
    - metadata -- Metadata in space-separated key=value pairs. This overwrites any existing metadata.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - source_account_key -- The storage account key of the source blob.
    - source_account_name -- The storage account name of the source blob.
    - source_blob -- The blob name for the source storage account.
    - source_container -- The container name for the source storage account.
    - source_path -- The file path for the source storage account.
    - source_sas -- The shared access signature for the source storage account.
    - source_share -- The share name for the source storage account.
    - source_snapshot -- The blob snapshot for the source storage account.
    - source_uri --  A URL of up to 2 KB in length that specifies an Azure file or blob. The value should be URL-encoded as it would appear in a request URI. If the source is in another account, the source must either be public or must be authenticated via a shared access signature. If the source is public, no authentication is required. Examples: https://myaccount.file.core.windows.net/myshare/mydir/myfile https://otheraccount.file.core.windows.net/myshare/mydir/myfile?sastoken
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage file copy start", locals())


def cancel(copy_id, destination_path, destination_share, account_key=None, account_name=None, connection_string=None, sas_token=None, timeout=None):
    '''
    

    Required Parameters:
    - copy_id --  Copy identifier provided in the copy.id of the original copy_file operation.
    - destination_path -- The path to the file within the file share.
    - destination_share -- Name of the destination share. The share must exist.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage file copy cancel", locals())


def start_batch(account_key=None, account_name=None, connection_string=None, destination_path=None, destination_share=None, dryrun=None, metadata=None, pattern=None, sas_token=None, source_account_key=None, source_account_name=None, source_client=None, source_container=None, source_sas=None, source_share=None, source_uri=None, timeout=None):
    '''
    Copy multiple files or blobs to a file share.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - destination_path -- None
    - destination_share -- None
    - dryrun -- None
    - metadata -- Metadata in space-separated key=value pairs. This overwrites any existing metadata.
    - pattern -- None
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - source_account_key -- None
    - source_account_name -- None
    - source_client -- ==SUPPRESS==
    - source_container -- None
    - source_sas -- None
    - source_share -- None
    - source_uri -- None
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage file copy start-batch", locals())

