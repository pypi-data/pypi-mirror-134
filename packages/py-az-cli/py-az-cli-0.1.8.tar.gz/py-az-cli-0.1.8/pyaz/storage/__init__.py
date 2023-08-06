'''
Manage Azure Cloud Storage resources.
'''
from .. pyaz_utils import _call_az
from . import account, blob, container, container_rm, cors, directory, entity, file, fs, logging, message, metrics, queue, share, share_rm, table


def remove(account_key=None, account_name=None, connection_string=None, container_name=None, exclude_path=None, exclude_pattern=None, include_path=None, include_pattern=None, name=None, path=None, recursive=None, sas_token=None, share_name=None):
    '''
    Delete blobs or files from Azure Storage.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - container_name -- The container name.
    - exclude_path -- Exclude these paths. This option does not support wildcard characters (*). Checks relative path prefix. For example: myFolder;myFolder/subDirName/file.pdf.
    - exclude_pattern -- Exclude these files where the name matches the pattern list. For example: *.jpg;*.pdf;exactName. This option supports wildcard characters (*)
    - include_path -- Include only these paths. This option does not support wildcard characters (*). Checks relative path prefix. For example:myFolder;myFolder/subDirName/file.pdf
    - include_pattern -- Include only these files where the name matches the pattern list. For example: *.jpg;*.pdf;exactName. This option supports wildcard characters (*)
    - name -- The blob name.
    - path -- The path to the file within the file share.
    - recursive -- Look into sub-directories recursively.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - share_name -- The file share name.
    '''
    return _call_az("az storage remove", locals())


def copy(account_key=None, account_name=None, blob_type=None, cap_mbps=None, connection_string=None, content_type=None, destination=None, destination_blob=None, destination_container=None, destination_file_path=None, destination_share=None, exclude_path=None, exclude_pattern=None, follow_symlinks=None, include_path=None, include_pattern=None, preserve_s2s_access_tier=None, put_md5=None, recursive=None, sas_token=None, source=None, source_account_key=None, source_account_name=None, source_blob=None, source_connection_string=None, source_container=None, source_file_path=None, source_sas=None, source_share=None):
    '''
    Copy files or directories to or from Azure storage.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name of copy destination
    - blob_type -- The type of blob at the destination.
    - cap_mbps -- Caps the transfer rate, in megabits per second. Moment-by-moment throughput might vary slightly from the cap. If this option is set to zero, or it is omitted, the throughput isn't capped. 
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - content_type -- Specify content type of the file. 
    - destination -- The path/url of copy destination. It can be a local path, an url to azure storage server. If you provide destination parameter here, you do not need to provide arguments in copy destination arguments group and copy destination arguments will be deprecated in future.
    - destination_blob -- Blob name in blob container of copy destination storage account
    - destination_container -- Container name of copy destination storage account
    - destination_file_path -- File path in file share of copy destination storage account
    - destination_share -- File share name of copy destination storage account
    - exclude_path -- Exclude these paths. This option does not support wildcard characters (*). Checks relative path prefix. For example: myFolder;myFolder/subDirName/file.pdf.
    - exclude_pattern -- Exclude these files where the name matches the pattern list. For example: *.jpg;*.pdf;exactName. This option supports wildcard characters (*)
    - follow_symlinks -- Follow symbolic links when uploading from local file system.
    - include_path -- Include only these paths. This option does not support wildcard characters (*). Checks relative path prefix. For example:myFolder;myFolder/subDirName/file.pdf
    - include_pattern -- Include only these files where the name matches the pattern list. For example: *.jpg;*.pdf;exactName. This option supports wildcard characters (*)
    - preserve_s2s_access_tier -- Preserve access tier during service to service copy. Please refer to https://docs.microsoft.com/azure/storage/blobs/storage-blob-storage-tiers to ensure destination storage account support setting access tier. In the cases that setting access tier is not supported, please use `--preserve-s2s-access-tier false` to bypass copying access tier. (Default true)
    - put_md5 -- Create an MD5 hash of each file, and save the hash as the Content-MD5 property of the destination blob/file.Only available when uploading.
    - recursive -- Look into sub-directories recursively.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - source -- The path/url of copy source. It can be a local path, an url to azure storage server or AWS S3 buckets. If you provide source parameter here, you do not need to provide arguments in copy source arguments group and copy source arguments will be deprecated in future.
    - source_account_key -- Account key of copy source storage account. Must be used in conjunction with source storage account name.
    - source_account_name -- Account name of copy source storage account.
    - source_blob -- Blob name in blob container of copy source storage account
    - source_connection_string -- Connection string of source storage account.
    - source_container -- Container name of copy source storage account
    - source_file_path -- File path in file share of copy source storage account
    - source_sas -- Shared Access Signature (SAS) token of copy source. Must be used in conjunction with source storage account name.
    - source_share -- File share name of copy source storage account
    '''
    return _call_az("az storage copy", locals())

