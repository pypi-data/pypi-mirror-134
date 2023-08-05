'''
Manage file shares.
'''
from ... pyaz_utils import _call_az
from . import metadata, policy


def list(account_key=None, account_name=None, connection_string=None, include_metadata=None, include_snapshots=None, marker=None, num_results=None, prefix=None, sas_token=None, timeout=None):
    '''
    List the file shares in a storage account.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - include_metadata --  Specifies that share metadata be returned in the response.
    - include_snapshots --  Specifies that share snapshots be returned in the response.
    - marker --  An opaque continuation token. This value can be retrieved from the next_marker field of a previous generator object if num_results was specified and that generator has finished enumerating results. If specified, this generator will begin returning results from the point where the previous generator stopped.
    - num_results -- Specify the maximum number to return. If the request does not specify num_results, or specifies a value greater than 5000, the server will return up to 5000 items. Note that if the listing operation crosses a partition boundary, then the service will return a continuation token for retrieving the remaining of the results. Provide "*" to return all.
    - prefix --  Filters the results to return only shares whose names begin with the specified prefix.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage share list", locals())


def create(name, account_key=None, account_name=None, connection_string=None, fail_on_exist=None, metadata=None, quota=None, sas_token=None, timeout=None):
    '''
    Creates a new share under the specified account.

    Required Parameters:
    - name -- The file share name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - fail_on_exist --  Specify whether to throw an exception when the share exists. False by default.
    - metadata -- Metadata in space-separated key=value pairs. This overwrites any existing metadata.
    - quota --  Specifies the maximum size of the share, in gigabytes. Must be greater than 0, and less than or equal to 5TB (5120).
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage share create", locals())


def delete(name, account_key=None, account_name=None, connection_string=None, delete_snapshots=None, fail_not_exist=None, sas_token=None, snapshot=None, timeout=None):
    '''
    

    Required Parameters:
    - name -- The file share name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - delete_snapshots -- Specify the deletion strategy when the share has snapshots.
    - fail_not_exist --  Specify whether to throw an exception when the share doesn't exist. False by default.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - snapshot --  A string that represents the snapshot version, if applicable. Specify this argument to delete a specific snapshot only. delete_snapshots must be None if this is specified.
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage share delete", locals())


def generate_sas(name, account_key=None, account_name=None, cache_control=None, connection_string=None, content_disposition=None, content_encoding=None, content_language=None, content_type=None, expiry=None, https_only=None, ip=None, permissions=None, policy_name=None, start=None):
    '''
    

    Required Parameters:
    - name -- The file share name.

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
    - permissions -- The permissions the SAS grants. Allowed values: (d)elete (l)ist (r)ead (w)rite (d)elete (l)ist (r)ead (w)rite. Do not use if a stored access policy is referenced with --id that specifies this value. Can be combined.
    - policy_name -- The name of a stored access policy within the share's ACL.
    - start -- Specifies the UTC datetime (Y-m-d'T'H:M'Z') at which the SAS becomes valid. Do not use if a stored access policy is referenced with --id that specifies this value. Defaults to the time of the request.
    '''
    return _call_az("az storage share generate-sas", locals())


def stats(name, account_key=None, account_name=None, connection_string=None, sas_token=None, timeout=None):
    '''
    

    Required Parameters:
    - name -- The file share name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage share stats", locals())


def show(name, account_key=None, account_name=None, connection_string=None, sas_token=None, snapshot=None, timeout=None):
    '''
    

    Required Parameters:
    - name -- The file share name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - snapshot --  A string that represents the snapshot version, if applicable.
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage share show", locals())


def update(name, quota, account_key=None, account_name=None, connection_string=None, sas_token=None, timeout=None):
    '''
    

    Required Parameters:
    - name -- The file share name.
    - quota --  Specifies the maximum size of the share, in gigabytes. Must be greater than 0, and less than or equal to 5 TB (5120 GB).

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage share update", locals())


def snapshot(name, account_key=None, account_name=None, connection_string=None, metadata=None, quota=None, sas_token=None, timeout=None):
    '''
    

    Required Parameters:
    - name -- The file share name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - metadata -- Metadata in space-separated key=value pairs. This overwrites any existing metadata.
    - quota --  Specifies the maximum size of the share, in gigabytes. Must be greater than 0, and less than or equal to 5TB (5120).
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage share snapshot", locals())


def exists(name, account_key=None, account_name=None, connection_string=None, sas_token=None, snapshot=None, timeout=None):
    '''
    Check for the existence of a file share.

    Required Parameters:
    - name -- The file share name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - snapshot --  A string that represents the snapshot version, if applicable.
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage share exists", locals())


def url(name, account_key=None, account_name=None, connection_string=None, protocol=None, sas_token=None, unc=None):
    '''
    Create a URI to access a file share.

    Required Parameters:
    - name -- The file share name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - protocol -- Protocol to use.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - unc -- Output UNC network path.
    '''
    return _call_az("az storage share url", locals())


def list_handle(name, account_key=None, account_name=None, connection_string=None, marker=None, max_results=None, path=None, recursive=None, sas_token=None, snapshot=None, timeout=None):
    '''
    List file handles of a file share.

    Required Parameters:
    - name -- The file share name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - marker --  An opaque continuation token. This value can be retrieved from the next_marker field of a previous generator object if max_results was specified and that generator has finished enumerating results. If specified, this generator will begin returning results from the point where the previous generator stopped.
    - max_results --  Specifies the maximum number of handles taken on files and/or directories to return. If the request does not specify max_results or specifies a value greater than 5,000, the server will return up to 5,000 items. Setting max_results to a value less than or equal to zero results in error response code 400 (Bad Request).
    - path -- The path to the file within the file share.
    - recursive --  Boolean that specifies if operation should apply to the directory specified in the URI, its files, its subdirectories and their files.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - snapshot --  A string that represents the snapshot version, if applicable.
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage share list-handle", locals())


def close_handle(name, account_key=None, account_name=None, close_all=None, connection_string=None, handle_id=None, marker=None, path=None, recursive=None, sas_token=None, snapshot=None, timeout=None):
    '''
    Close file handles of a file share.

    Required Parameters:
    - name -- The file share name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - close_all -- Whether or not to close all the file handles. Specify close-all or a specific handle-id.
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - handle_id -- Specifies handle ID opened on the file or directory to be closed. Astrix (‘*’) is a wildcard that specifies all handles.
    - marker -- An opaque continuation token. This value can be retrieved from the next_marker field of a previous generator object if it has not finished closing handles. If specified, this generator will begin closing handles from the point where the previous generator stopped.
    - path -- The path to the file within the file share.
    - recursive -- Boolean that specifies if operation should apply to the directory specified in the URI, its files, its subdirectories and their files.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - snapshot -- A string that represents the snapshot version, if applicable.
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage share close-handle", locals())

