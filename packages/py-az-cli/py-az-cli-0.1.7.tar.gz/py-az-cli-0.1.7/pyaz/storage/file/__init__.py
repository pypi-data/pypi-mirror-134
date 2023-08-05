'''
Manage file shares that use the SMB 3.0 protocol.
'''
from ... pyaz_utils import _call_az
from . import copy, metadata


def list(share_name, account_key=None, account_name=None, connection_string=None, exclude_dir=None, marker=None, num_results=None, path=None, sas_token=None, snapshot=None, timeout=None):
    '''
    List files and directories in a share.

    Required Parameters:
    - share_name -- The file share name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - exclude_dir -- None
    - marker --  An opaque continuation token. This value can be retrieved from the next_marker field of a previous generator object if num_results was specified and that generator has finished enumerating results. If specified, this generator will begin returning results from the point where the previous generator stopped.
    - num_results -- Specify the maximum number to return. If the request does not specify num_results, or specifies a value greater than 5000, the server will return up to 5000 items. Note that if the listing operation crosses a partition boundary, then the service will return a continuation token for retrieving the remaining of the results. Provide "*" to return all.
    - path -- The directory path within the file share.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - snapshot --  A string that represents the snapshot version, if applicable.
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage file list", locals())


def delete(path, share_name, account_key=None, account_name=None, connection_string=None, sas_token=None, timeout=None):
    '''
    

    Required Parameters:
    - path -- The path to the file within the file share.
    - share_name -- The file share name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage file delete", locals())


def resize(path, share_name, size, account_key=None, account_name=None, connection_string=None, sas_token=None, timeout=None):
    '''
    

    Required Parameters:
    - path -- The path to the file within the file share.
    - share_name -- The file share name.
    - size --  The length to resize the file to.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage file resize", locals())


def url(path, share_name, account_key=None, account_name=None, connection_string=None, protocol=None, sas_token=None):
    '''
    Create the url to access a file.

    Required Parameters:
    - path -- The path to the file within the file share.
    - share_name -- The file share name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - protocol -- Protocol to use.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    '''
    return _call_az("az storage file url", locals())


def generate_sas(path, share_name, account_key=None, account_name=None, cache_control=None, connection_string=None, content_disposition=None, content_encoding=None, content_language=None, content_type=None, expiry=None, https_only=None, ip=None, permissions=None, policy_name=None, start=None):
    '''
    

    Required Parameters:
    - path -- The path to the file within the file share.
    - share_name -- The file share name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - cache_control --  Response header value for Cache-Control when resource is accessed using this shared access signature.
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - content_disposition --  Response header value for Content-Disposition when resource is accessed using this shared access signature.
    - content_encoding --  Response header value for Content-Encoding when resource is accessed using this shared access signature.
    - content_language --  Response header value for Content-Language when resource is accessed using this shared access signature.
    - content_type --  Response header value for Content-Type when resource is accessed using this shared access signature.
    - expiry -- Specifies the UTC datetime (Y-m-d'T'H:M'Z') at which the SAS becomes invalid. Do not use if a stored access policy is referenced with --id that specifies this value.
    - https_only -- Only permit requests made with the HTTPS protocol. If omitted, requests from both the HTTP and HTTPS protocol are permitted.
    - ip -- Specifies the IP address or range of IP addresses from which to accept requests. Supports only IPv4 style addresses.
    - permissions -- The permissions the SAS grants. Allowed values: (c)reate (d)elete (r)ead (w)rite (c)reate (d)elete (r)ead (w)rite. Do not use if a stored access policy is referenced with --id that specifies this value. Can be combined.
    - policy_name -- The name of a stored access policy within the container's ACL.
    - start -- Specifies the UTC datetime (Y-m-d'T'H:M'Z') at which the SAS becomes valid. Do not use if a stored access policy is referenced with --id that specifies this value. Defaults to the time of the request.
    '''
    return _call_az("az storage file generate-sas", locals())


def show(path, share_name, account_key=None, account_name=None, connection_string=None, sas_token=None, snapshot=None, timeout=None):
    '''
    

    Required Parameters:
    - path -- The path to the file within the file share.
    - share_name -- The file share name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - snapshot --  A string that represents the snapshot version, if applicable.
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage file show", locals())


def update(path, share_name, account_key=None, account_name=None, clear_content_settings=None, connection_string=None, content_cache_control=None, content_disposition=None, content_encoding=None, content_language=None, content_md5=None, content_type=None, sas_token=None, timeout=None):
    '''
    

    Required Parameters:
    - path -- The path to the file within the file share.
    - share_name -- The file share name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - clear_content_settings -- If this flag is set, then if any one or more of the following properties (--content-cache-control, --content-disposition, --content-encoding, --content-language, --content-md5, --content-type) is set, then all of these properties are set together. If a value is not provided for a given property when at least one of the properties listed below is set, then that property will be cleared.
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - content_cache_control -- The cache control string.
    - content_disposition -- Conveys additional information about how to process the response payload, and can also be used to attach additional metadata.
    - content_encoding -- The content encoding type.
    - content_language -- The content language.
    - content_md5 -- The content's MD5 hash.
    - content_type -- The content MIME type.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage file update", locals())


def exists(path, share_name, account_key=None, account_name=None, connection_string=None, sas_token=None, snapshot=None, timeout=None):
    '''
    Check for the existence of a file.

    Required Parameters:
    - path -- The path to the file within the file share.
    - share_name -- The file share name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - snapshot --  A string that represents the snapshot version, if applicable.
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage file exists", locals())


def download(path, share_name, account_key=None, account_name=None, connection_string=None, dest=None, end_range=None, max_connections=None, no_progress=None, open_mode=None, sas_token=None, snapshot=None, start_range=None, timeout=None, validate_content=None):
    '''
    

    Required Parameters:
    - path -- The path to the file within the file share.
    - share_name -- The file share name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - dest -- Path of the file to write to. The source filename will be used if not specified.
    - end_range --  End of byte range to use for downloading a section of the file. If end_range is given, start_range must be provided. The start_range and end_range params are inclusive. Ex: start_range=0, end_range=511 will download first 512 bytes of file.
    - max_connections --  If set to 2 or greater, an initial get will be done for the first self.MAX_SINGLE_GET_SIZE bytes of the file. If this is the entire file, the method returns at this point. If it is not, it will download the remaining data parallel using the number of threads equal to max_connections. Each chunk will be of size self.MAX_CHUNK_GET_SIZE. If set to 1, a single large get request will be done. This is not generally recommended but available if very few threads should be used, network requests are very expensive, or a non-seekable stream prevents parallel download. This may also be valuable if the file is being concurrently modified to enforce atomicity or if many files are expected to be empty as an extra request is required for empty files if max_connections is greater than 1.
    - no_progress -- Include this flag to disable progress reporting for the command.
    - open_mode --  Mode to use when opening the file. Note that specifying append only open_mode prevents parallel download. So, max_connections must be set to 1 if this open_mode is used.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - snapshot --  A string that represents the snapshot version, if applicable.
    - start_range --  Start of byte range to use for downloading a section of the file. If no end_range is given, all bytes after the start_range will be downloaded. The start_range and end_range params are inclusive. Ex: start_range=0, end_range=511 will download first 512 bytes of file.
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    - validate_content --  If set to true, validates an MD5 hash for each retrieved portion of the file. This is primarily valuable for detecting bitflips on the wire if using http instead of https as https (the default) will already validate. Note that the service will only return transactional MD5s for chunks 4MB or less so the first get request will be of size self.MAX_CHUNK_GET_SIZE instead of self.MAX_SINGLE_GET_SIZE. If self.MAX_CHUNK_GET_SIZE was set to greater than 4MB an error will be thrown. As computing the MD5 takes processing time and more requests will need to be done due to the reduced chunk size there may be some increase in latency.
    '''
    return _call_az("az storage file download", locals())


def upload(share_name, source, account_key=None, account_name=None, connection_string=None, content_cache_control=None, content_disposition=None, content_encoding=None, content_language=None, content_md5=None, content_type=None, max_connections=None, metadata=None, no_progress=None, path=None, sas_token=None, timeout=None, validate_content=None):
    '''
    Upload a file to a share that uses the SMB 3.0 protocol.

    Required Parameters:
    - share_name -- The file share name.
    - source --  Path of the local file to upload as the file content.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - content_cache_control -- The cache control string.
    - content_disposition -- Conveys additional information about how to process the response payload, and can also be used to attach additional metadata.
    - content_encoding -- The content encoding type.
    - content_language -- The content language.
    - content_md5 -- The content's MD5 hash.
    - content_type -- The content MIME type.
    - max_connections --  Maximum number of parallel connections to use.
    - metadata -- Metadata in space-separated key=value pairs. This overwrites any existing metadata.
    - no_progress -- Include this flag to disable progress reporting for the command.
    - path -- The path to the file within the file share. If the file name is omitted, the source file name will be used.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    - validate_content --  If true, calculates an MD5 hash for each range of the file. The storage service checks the hash of the content that has arrived with the hash that was sent. This is primarily valuable for detecting bitflips on the wire if using http instead of https as https (the default) will already validate. Note that this MD5 hash is not stored with the file.
    '''
    return _call_az("az storage file upload", locals())


def upload_batch(destination, source, account_key=None, account_name=None, connection_string=None, content_cache_control=None, content_disposition=None, content_encoding=None, content_language=None, content_md5=None, content_type=None, destination_path=None, dryrun=None, max_connections=None, metadata=None, no_progress=None, pattern=None, sas_token=None, validate_content=None):
    '''
    Upload files from a local directory to an Azure Storage File Share in a batch operation.

    Required Parameters:
    - destination -- None
    - source -- None

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - content_cache_control -- The cache control string.
    - content_disposition -- Conveys additional information about how to process the response payload, and can also be used to attach additional metadata.
    - content_encoding -- The content encoding type.
    - content_language -- The content language.
    - content_md5 -- The content's MD5 hash.
    - content_type -- The content MIME type.
    - destination_path -- None
    - dryrun -- None
    - max_connections -- None
    - metadata -- Metadata in space-separated key=value pairs. This overwrites any existing metadata.
    - no_progress -- Include this flag to disable progress reporting for the command.
    - pattern -- None
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - validate_content -- None
    '''
    return _call_az("az storage file upload-batch", locals())


def download_batch(destination, source, account_key=None, account_name=None, connection_string=None, dryrun=None, max_connections=None, no_progress=None, pattern=None, sas_token=None, snapshot=None, validate_content=None):
    '''
    Download files from an Azure Storage File Share to a local directory in a batch operation.

    Required Parameters:
    - destination -- None
    - source -- None

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - dryrun -- None
    - max_connections -- None
    - no_progress -- Include this flag to disable progress reporting for the command.
    - pattern -- None
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - snapshot -- None
    - validate_content -- None
    '''
    return _call_az("az storage file download-batch", locals())


def delete_batch(source, account_key=None, account_name=None, connection_string=None, dryrun=None, pattern=None, sas_token=None, timeout=None):
    '''
    Delete files from an Azure Storage File Share.

    Required Parameters:
    - source -- None

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - dryrun -- None
    - pattern -- None
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage file delete-batch", locals())

