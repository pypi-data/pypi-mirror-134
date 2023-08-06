'''
Manage files in Azure Data Lake Storage Gen2 account.
'''
from .... pyaz_utils import _call_az
from . import metadata


def create(account_key=None, account_name=None, auth_mode=None, connection_string=None, content_cache_control=None, content_disposition=None, content_encoding=None, content_language=None, content_md5=None, content_type=None, metadata=None, permissions=None, sas_token=None, timeout=None, umask=None):
    '''
    Create a new file in ADLS Gen2 file system.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - content_cache_control -- The cache control string.
    - content_disposition -- Conveys additional information about how to process the response payload, and can also be used to attach additional metadata.
    - content_encoding -- The content encoding type.
    - content_language -- The content language.
    - content_md5 -- The content's MD5 hash.
    - content_type -- The content MIME type.
    - metadata -- Metadata in space-separated key=value pairs. This overwrites any existing metadata.
    - permissions -- POSIX access permissions for the file owner, the file owning group, and others. Each class may be granted read, write, or execute permission. The sticky bit is also supported. Both symbolic (rwxrw-rw-) and 4-digit octal notation (e.g. 0766) are supported. For more information, please refer to https://docs.microsoft.com/azure/storage/blobs/data-lake-storage-access-control#levels-of-permission.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    - umask -- When creating a file or directory and the parent folder does not have a default ACL, the umask restricts the permissions of the file or directory to be created. The resulting permission is given by p & ^u, where p is the permission and u is the umask. For more information, please refer to https://docs.microsoft.com/azure/storage/blobs/data-lake-storage-access-control#umask.
    '''
    return _call_az("az storage fs file create", locals())


def upload(source, account_key=None, account_name=None, auth_mode=None, connection_string=None, content_cache_control=None, content_disposition=None, content_encoding=None, content_language=None, content_md5=None, content_type=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None, metadata=None, overwrite=None, permissions=None, sas_token=None, timeout=None, umask=None):
    '''
    Upload a file to a file path in ADLS Gen2 file system.

    Required Parameters:
    - source -- Path of the local file to upload as the file content.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - content_cache_control -- The cache control string.
    - content_disposition -- Conveys additional information about how to process the response payload, and can also be used to attach additional metadata.
    - content_encoding -- The content encoding type.
    - content_language -- The content language.
    - content_md5 -- The content's MD5 hash.
    - content_type -- The content MIME type.
    - if_match -- An ETag value, or the wildcard character (*). Specify this header to perform the operation only if the resource's ETag matches the value specified.
    - if_modified_since -- A Commence only if modified since supplied UTC datetime (Y-m-d'T'H:M'Z').
    - if_none_match -- An ETag value, or the wildcard character (*). Specify this header to perform the operation only if the resource's ETag does not match the value specified.
    - if_unmodified_since -- A Commence only if unmodified since supplied UTC datetime (Y-m-d'T'H:M'Z').
    - metadata -- Metadata in space-separated key=value pairs. This overwrites any existing metadata.
    - overwrite -- Overwrite an existing file when specified.
    - permissions -- POSIX access permissions for the file owner, the file owning group, and others. Each class may be granted read, write, or execute permission. The sticky bit is also supported. Both symbolic (rwxrw-rw-) and 4-digit octal notation (e.g. 0766) are supported. For more information, please refer to https://docs.microsoft.com/azure/storage/blobs/data-lake-storage-access-control#levels-of-permission.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    - umask -- When creating a file or directory and the parent folder does not have a default ACL, the umask restricts the permissions of the file or directory to be created. The resulting permission is given by p & ^u, where p is the permission and u is the umask. For more information, please refer to https://docs.microsoft.com/azure/storage/blobs/data-lake-storage-access-control#umask.
    '''
    return _call_az("az storage fs file upload", locals())


def exists(account_key=None, account_name=None, auth_mode=None, connection_string=None, sas_token=None, timeout=None):
    '''
    Check for the existence of a file in ADLS Gen2 file system.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage fs file exists", locals())


def append(content, account_key=None, account_name=None, auth_mode=None, connection_string=None, sas_token=None, timeout=None):
    '''
    Append content to a file in ADLS Gen2 file system.

    Required Parameters:
    - content -- Content to be appended to file.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage fs file append", locals())


def download(account_key=None, account_name=None, auth_mode=None, connection_string=None, destination=None, overwrite=None, sas_token=None, timeout=None):
    '''
    Download a file from the specified path in ADLS Gen2 file system.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - destination -- The local file where the file or folder will be downloaded to. The source filename will be used if not specified.
    - overwrite -- Overwrite an existing file when specified. Default value is false.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage fs file download", locals())


def show(account_key=None, account_name=None, auth_mode=None, connection_string=None, sas_token=None, timeout=None):
    '''
    Show properties of file in ADLS Gen2 file system.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage fs file show", locals())


def list(account_key=None, account_name=None, auth_mode=None, connection_string=None, exclude_dir=None, marker=None, num_results=None, path=None, recursive=None, sas_token=None, show_next_marker=None, timeout=None):
    '''
    List files and directories in ADLS Gen2 file system.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - exclude_dir -- List only files in the given file system.
    - marker -- An opaque continuation token. This value can be retrieved from the next_marker field of a previous generator object. If specified, this generator will begin returning results from this point.
    - num_results -- Specify the maximum number of results to return. If the request does not specify num_results or specifies a value greater than 5,000, the server will return up to 5,000 items.
    - path -- Filter the results to return only paths under the specified path.
    - recursive -- Look into sub-directories recursively when set to true.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - show_next_marker -- Show nextMarker in result when specified.
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage fs file list", locals())


def move(new_path, account_key=None, account_name=None, auth_mode=None, connection_string=None, content_cache_control=None, content_disposition=None, content_encoding=None, content_language=None, content_md5=None, content_type=None, sas_token=None):
    '''
    Move a file in ADLS Gen2 Account.

    Required Parameters:
    - new_path -- The new path the users want to move to. The value must have the following format: "{filesystem}/{directory}/{subdirectory}/{file}".

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - content_cache_control -- The cache control string.
    - content_disposition -- Conveys additional information about how to process the response payload, and can also be used to attach additional metadata.
    - content_encoding -- The content encoding type.
    - content_language -- The content language.
    - content_md5 -- The content's MD5 hash.
    - content_type -- The content MIME type.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    '''
    return _call_az("az storage fs file move", locals())


def delete(account_key=None, account_name=None, auth_mode=None, connection_string=None, sas_token=None, timeout=None, yes=None):
    '''
    Delete a file in ADLS Gen2 file system.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az storage fs file delete", locals())

