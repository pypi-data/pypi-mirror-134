'''
Manage object storage for unstructured data (blobs).
'''
from ... pyaz_utils import _call_az
from . import copy, immutability_policy, incremental_copy, lease, metadata, service_properties


def show(container_name, name, account_key=None, account_name=None, auth_mode=None, connection_string=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None, lease_id=None, sas_token=None, snapshot=None, tags_condition=None, timeout=None):
    '''
    Get the details of a blob.

    Required Parameters:
    - container_name -- The container name.
    - name -- The blob name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - if_match -- An ETag value, or the wildcard character (*). Specify this header to perform the operation only if the resource's ETag matches the value specified.
    - if_modified_since -- Commence only if modified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - if_none_match -- An ETag value, or the wildcard character (*). Specify this header to perform the operation only if the resource's ETag does not match the value specified. Specify the wildcard character (*) to perform the operation only if the resource does not exist, and fail the operation if it does exist.
    - if_unmodified_since -- Commence only if unmodified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - lease_id -- Required if the blob has an active lease.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - snapshot -- The snapshot parameter is an opaque DateTime value that, when present, specifies the blob snapshot to retrieve.
    - tags_condition -- Specify a SQL where clause on blob tags to operate only on blobs with a matching value.
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage blob show", locals())


def set_tier(container_name, name, tier, account_key=None, account_name=None, auth_mode=None, connection_string=None, rehydrate_priority=None, sas_token=None, timeout=None, type=None):
    '''
    Set the block or page tiers on the blob.

    Required Parameters:
    - container_name -- The container name.
    - name -- The blob name.
    - tier -- None

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - rehydrate_priority -- Indicate the priority with which to rehydrate an archived blob. The priority can be set on a blob only once, default value is Standard.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    - type -- None
    '''
    return _call_az("az storage blob set-tier", locals())


def list(container_name, account_key=None, account_name=None, auth_mode=None, connection_string=None, delimiter=None, include=None, marker=None, num_results=None, prefix=None, sas_token=None, show_next_marker=None, timeout=None):
    '''
    List blobs in a given container.

    Required Parameters:
    - container_name -- The container name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - delimiter -- When the request includes this parameter, the operation returns a BlobPrefix element in the result list that acts as a placeholder for all blobs whose names begin with the same substring up to the appearance of the delimiter character. The delimiter may be a single character or a string.
    - include -- Specify one or more additional datasets to include in the response. Options include: (c)opy, (d)eleted, (m)etadata, (s)napshots, (v)ersions, (t)ags, (i)mmutabilitypolicy, (l)egalhold, (d)eletedwithversions. Can be combined.
    - marker -- A string value that identifies the portion of the list of containers to be returned with the next listing operation. The operation returns the NextMarker value within the response body if the listing operation did not return all containers remaining to be listed with the current page. If specified, this generator will begin returning results from the point where the previous generator stopped.
    - num_results -- Specify the maximum number to return. If the request does not specify num_results, or specifies a value greater than 5000, the server will return up to 5000 items. Note that if the listing operation crosses a partition boundary, then the service will return a continuation token for retrieving the remaining of the results. Provide "*" to return all.
    - prefix -- Filter the results to return only blobs whose name begins with the specified prefix.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - show_next_marker -- Show nextMarker in result when specified.
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage blob list", locals())


def query(container_name, name, query_expression, account_key=None, account_name=None, auth_mode=None, connection_string=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None, in_column_separator=None, in_escape_char=None, in_has_header=None, in_line_separator=None, in_quote_char=None, in_record_separator=None, input_format=None, lease_id=None, out_column_separator=None, out_escape_char=None, out_has_header=None, out_line_separator=None, out_quote_char=None, out_record_separator=None, output_format=None, result_file=None, sas_token=None, tags_condition=None, timeout=None):
    '''
    Enable users to select/project on blob or blob snapshot data by providing simple query expressions.

    Required Parameters:
    - container_name -- The container name.
    - name -- The blob name.
    - query_expression -- The query expression in SQL. The maximum size of the query expression is 256KiB. For more information about the expression syntax, please see https://docs.microsoft.com/azure/storage/blobs/query-acceleration-sql-reference

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - if_match -- An ETag value, or the wildcard character (*). Specify this header to perform the operation only if the resource's ETag matches the value specified.
    - if_modified_since -- Commence only if modified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - if_none_match -- An ETag value, or the wildcard character (*). Specify this header to perform the operation only if the resource's ETag does not match the value specified. Specify the wildcard character (*) to perform the operation only if the resource does not exist, and fail the operation if it does exist.
    - if_unmodified_since -- Commence only if unmodified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - in_column_separator -- The string used to separate columns.
    - in_escape_char -- The string used as an escape character. Default to empty.
    - in_has_header -- Whether the blob data includes headers in the first line. The default value is False, meaning that the data will be returned inclusive of the first line. If set to True, the data will be returned exclusive of the first line.
    - in_line_separator -- The string used to separate records.
    - in_quote_char -- The string used to quote a specific field.
    - in_record_separator -- The string used to separate records.
    - input_format -- Serialization type of the data currently stored in the blob. The default is to treat the blob data as CSV data formatted in the default dialect.The blob data will be reformatted according to that profile when blob format is specified. If you choose `json`, please specify `Output Json Text Configuration Arguments` accordingly; If you choose `csv`, please specify `Output Delimited Text Configuration Arguments`.
    - lease_id -- Required if the blob has an active lease.
    - out_column_separator -- The string used to separate columns.
    - out_escape_char -- The string used as an escape character. Default to empty.
    - out_has_header -- Whether the blob data includes headers in the first line. The default value is False, meaning that the data will be returned inclusive of the first line. If set to True, the data will be returned exclusive of the first line.
    - out_line_separator -- The string used to separate records.
    - out_quote_char -- The string used to quote a specific field.
    - out_record_separator -- The string used to separate records.
    - output_format -- Output serialization type for the data stream. By default the data will be returned as it is represented in the blob. By providing an output format, the blob data will be reformatted according to that profile. If you choose `json`, please specify `Output Json Text Configuration Arguments` accordingly; If you choose `csv`, please specify `Output Delimited Text Configuration Arguments`.
    - result_file -- Specify the file path to save result.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - tags_condition -- Specify a SQL where clause on blob tags to operate only on blobs with a matching value.
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage blob query", locals())


def rewrite(container_name, name, source_uri, account_key=None, account_name=None, auth_mode=None, connection_string=None, encryption_scope=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None, lease_id=None, sas_token=None, tags_condition=None, tier=None, timeout=None):
    '''
    Create a new Block Blob where the content of the blob is read from a given URL.

    Required Parameters:
    - container_name -- The container name.
    - name -- The blob name.
    - source_uri -- A URL of up to 2 KB in length that specifies a file or blob. The value should be URL-encoded as it would appear in a request URI. If the source is in another account, the source must either be public or must be authenticated via a shared access signature. If the source is public, no authentication is required.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - encryption_scope -- A predefined encryption scope used to encrypt the data on the service. An encryption scope can be created using the Management API and referenced here by name. If a default encryption scope has been defined at the container, this value will override it if the container-level scope is configured to allow overrides. Otherwise an error will be raised.
    - if_match -- An ETag value, or the wildcard character (*). Specify this header to perform the operation only if the resource's ETag matches the value specified.
    - if_modified_since -- Commence only if modified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - if_none_match -- An ETag value, or the wildcard character (*). Specify this header to perform the operation only if the resource's ETag does not match the value specified. Specify the wildcard character (*) to perform the operation only if the resource does not exist, and fail the operation if it does exist.
    - if_unmodified_since -- Commence only if unmodified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - lease_id -- Required if the blob has an active lease. Value can be a BlobLeaseClient object or the lease ID as a string.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - tags_condition -- Specify a SQL where clause on blob tags to operate only on blobs with a matching value.
    - tier -- A standard blob tier value to set the blob to. For this version of the library, this is only applicable to block blobs on standard storage accounts.
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage blob rewrite", locals())


def set_legal_hold(container_name, legal_hold, name, account_key=None, account_name=None, auth_mode=None, connection_string=None, sas_token=None, timeout=None):
    '''
    Set blob legal hold.

    Required Parameters:
    - container_name -- The container name.
    - legal_hold -- Specified if a legal hold should be set on the blob.
    - name -- The blob name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage blob set-legal-hold", locals())


def download(container_name, file, name, account_key=None, account_name=None, auth_mode=None, connection_string=None, end_range=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None, lease_id=None, max_connections=None, no_progress=None, open_mode=None, sas_token=None, snapshot=None, socket_timeout=None, start_range=None, timeout=None, validate_content=None):
    '''
    

    Required Parameters:
    - container_name -- The container name.
    - file --  Path of file to write out to.
    - name -- The blob name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - end_range --  End of byte range to use for downloading a section of the blob. If end_range is given, start_range must be provided. The start_range and end_range params are inclusive. Ex: start_range=0, end_range=511 will download first 512 bytes of blob.
    - if_match --  An ETag value, or the wildcard character (*). Specify this header to perform the operation only if the resource's ETag matches the value specified.
    - if_modified_since -- Commence only if modified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - if_none_match --  An ETag value, or the wildcard character (*). Specify this header to perform the operation only if the resource's ETag does not match the value specified. Specify the wildcard character (*) to perform the operation only if the resource does not exist, and fail the operation if it does exist.
    - if_unmodified_since -- Commence only if unmodified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - lease_id --  Required if the blob has an active lease.
    - max_connections --  If set to 2 or greater, an initial get will be done for the first self.MAX_SINGLE_GET_SIZE bytes of the blob. If this is the entire blob, the method returns at this point. If it is not, it will download the remaining data parallel using the number of threads equal to max_connections. Each chunk will be of size self.MAX_CHUNK_GET_SIZE. If set to 1, a single large get request will be done. This is not generally recommended but available if very few threads should be used, network requests are very expensive, or a non-seekable stream prevents parallel download. This may also be useful if many blobs are expected to be empty as an extra request is required for empty blobs if max_connections is greater than 1.
    - no_progress -- Include this flag to disable progress reporting for the command.
    - open_mode --  Mode to use when opening the file. Note that specifying append only open_mode prevents parallel download. So, max_connections must be set to 1 if this open_mode is used.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - snapshot --  The snapshot parameter is an opaque DateTime value that, when present, specifies the blob snapshot to retrieve.
    - socket_timeout -- The socket timeout(secs), used by the service to regulate data flow.
    - start_range --  Start of byte range to use for downloading a section of the blob. If no end_range is given, all bytes after the start_range will be downloaded. The start_range and end_range params are inclusive. Ex: start_range=0, end_range=511 will download first 512 bytes of blob.
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    - validate_content --  If set to true, validates an MD5 hash for each retrieved portion of the blob. This is primarily valuable for detecting bitflips on the wire if using http instead of https as https (the default) will already validate. Note that the service will only return transactional MD5s for chunks 4MB or less so the first get request will be of size self.MAX_CHUNK_GET_SIZE instead of self.MAX_SINGLE_GET_SIZE. If self.MAX_CHUNK_GET_SIZE was set to greater than 4MB an error will be thrown. As computing the MD5 takes processing time and more requests will need to be done due to the reduced chunk size there may be some increase in latency.
    '''
    return _call_az("az storage blob download", locals())


def generate_sas(container_name, name, account_key=None, account_name=None, as_user=None, auth_mode=None, cache_control=None, connection_string=None, content_disposition=None, content_encoding=None, content_language=None, content_type=None, expiry=None, full_uri=None, https_only=None, ip=None, permissions=None, policy_name=None, start=None):
    '''
    Generate a shared access signature for the blob.

    Required Parameters:
    - container_name -- The container name.
    - name -- The blob name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - as_user -- Indicates that this command return the SAS signed with the user delegation key. The expiry parameter and '--auth-mode login' are required if this argument is specified. 
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - cache_control -- Response header value for Cache-Control when resource is accessed using this shared access signature.
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - content_disposition -- Response header value for Content-Disposition when resource is accessed using this shared access signature.
    - content_encoding -- Response header value for Content-Encoding when resource is accessed using this shared access signature.
    - content_language -- Response header value for Content-Language when resource is accessed using this shared access signature.
    - content_type -- Response header value for Content-Type when resource is accessed using this shared access signature.
    - expiry -- Specifies the UTC datetime (Y-m-d'T'H:M'Z') at which the SAS becomes invalid. Do not use if a stored access policy is referenced with --id that specifies this value.
    - full_uri -- Indicates that this command return the full blob URI and the shared access signature token.
    - https_only -- Only permit requests made with the HTTPS protocol. If omitted, requests from both the HTTP and HTTPS protocol are permitted.
    - ip -- Specifies the IP address or range of IP addresses from which to accept requests. Supports only IPv4 style addresses.
    - permissions -- The permissions the SAS grants. Allowed values: (a)dd (c)reate (d)elete (r)ead (w)rite (a)dd (c)reate (d)elete (r)ead (w)rite. Do not use if a stored access policy is referenced with --id that specifies this value. Can be combined.
    - policy_name -- The name of a stored access policy within the container's ACL.
    - start -- Specifies the UTC datetime (Y-m-d'T'H:M'Z') at which the SAS becomes valid. Do not use if a stored access policy is referenced with --id that specifies this value. Defaults to the time of the request.
    '''
    return _call_az("az storage blob generate-sas", locals())


def url(container_name, name, account_key=None, account_name=None, auth_mode=None, connection_string=None, protocol=None, sas_token=None, snapshot=None):
    '''
    Create the url to access a blob.

    Required Parameters:
    - container_name -- The container name.
    - name -- The blob name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - protocol -- Protocol to use.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - snapshot -- An string value that uniquely identifies the snapshot. The value of this query parameter indicates the snapshot version.
    '''
    return _call_az("az storage blob url", locals())


def snapshot(container_name, name, account_key=None, account_name=None, auth_mode=None, connection_string=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None, lease_id=None, metadata=None, sas_token=None, timeout=None):
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
    return _call_az("az storage blob snapshot", locals())


def update(container_name, name, account_key=None, account_name=None, auth_mode=None, clear_content_settings=None, connection_string=None, content_cache_control=None, content_disposition=None, content_encoding=None, content_language=None, content_md5=None, content_type=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None, lease_id=None, sas_token=None, timeout=None):
    '''
    

    Required Parameters:
    - container_name -- The container name.
    - name -- The blob name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - clear_content_settings -- If this flag is set, then if any one or more of the following properties (--content-cache-control, --content-disposition, --content-encoding, --content-language, --content-md5, --content-type) is set, then all of these properties are set together. If a value is not provided for a given property when at least one of the properties listed below is set, then that property will be cleared.
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - content_cache_control -- The cache control string.
    - content_disposition -- Conveys additional information about how to process the response payload, and can also be used to attach additional metadata.
    - content_encoding -- The content encoding type.
    - content_language -- The content language.
    - content_md5 -- The content's MD5 hash.
    - content_type -- The content MIME type.
    - if_match --  An ETag value, or the wildcard character (*). Specify this header to perform the operation only if the resource's ETag matches the value specified.
    - if_modified_since -- Commence only if modified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - if_none_match --  An ETag value, or the wildcard character (*). Specify this header to perform the operation only if the resource's ETag does not match the value specified. Specify the wildcard character (*) to perform the operation only if the resource does not exist, and fail the operation if it does exist.
    - if_unmodified_since -- Commence only if unmodified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - lease_id --  Required if the blob has an active lease.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage blob update", locals())


def exists(container_name, name, account_key=None, account_name=None, auth_mode=None, connection_string=None, sas_token=None, snapshot=None, timeout=None):
    '''
    Check for the existence of a blob in a container.

    Required Parameters:
    - container_name -- The container name.
    - name -- The blob name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - snapshot --  The snapshot parameter is an opaque DateTime value that, when present, specifies the snapshot.
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage blob exists", locals())


def delete(container_name, name, account_key=None, account_name=None, auth_mode=None, connection_string=None, delete_snapshots=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None, lease_id=None, sas_token=None, snapshot=None, timeout=None):
    '''
    Mark a blob or snapshot for deletion.

    Required Parameters:
    - container_name -- The container name.
    - name -- The blob name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - delete_snapshots --  Required if the blob has associated snapshots.
    - if_match --  An ETag value, or the wildcard character (*). Specify this header to perform the operation only if the resource's ETag matches the value specified.
    - if_modified_since -- Commence only if modified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - if_none_match --  An ETag value, or the wildcard character (*). Specify this header to perform the operation only if the resource's ETag does not match the value specified. Specify the wildcard character (*) to perform the operation only if the resource does not exist, and fail the operation if it does exist.
    - if_unmodified_since -- Commence only if unmodified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - lease_id --  Required if the blob has an active lease.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - snapshot --  The snapshot parameter is an opaque DateTime value that, when present, specifies the blob snapshot to delete.
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage blob delete", locals())


def undelete(container_name, name, account_key=None, account_name=None, auth_mode=None, connection_string=None, sas_token=None, timeout=None):
    '''
    

    Required Parameters:
    - container_name -- The container name.
    - name -- The blob name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage blob undelete", locals())


def upload(container_name, file, account_key=None, account_name=None, auth_mode=None, connection_string=None, content_cache_control=None, content_disposition=None, content_encoding=None, content_language=None, content_md5=None, content_type=None, encryption_scope=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None, lease_id=None, max_connections=None, maxsize_condition=None, metadata=None, name=None, no_progress=None, sas_token=None, socket_timeout=None, tier=None, timeout=None, type=None, validate_content=None):
    '''
    Upload a file to a storage blob.

    Required Parameters:
    - container_name -- The container name.
    - file --  Path of the file to upload as the blob content.

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
    - encryption_scope -- A predefined encryption scope used to encrypt the data on the service.
    - if_match --  An ETag value, or the wildcard character (*). Specify this header to perform the operation only if the resource's ETag matches the value specified.
    - if_modified_since -- Commence only if modified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - if_none_match --  An ETag value, or the wildcard character (*). Specify this header to perform the operation only if the resource's ETag does not match the value specified. Specify the wildcard character (*) to perform the operation only if the resource does not exist, and fail the operation if it does exist.
    - if_unmodified_since -- Commence only if unmodified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - lease_id --  Required if the blob has an active lease.
    - max_connections --  Maximum number of parallel connections to use when the blob size exceeds 64MB.
    - maxsize_condition -- None
    - metadata -- Metadata in space-separated key=value pairs. This overwrites any existing metadata.
    - name -- The blob name.
    - no_progress -- Include this flag to disable progress reporting for the command.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - socket_timeout -- The socket timeout(secs), used by the service to regulate data flow.
    - tier -- None
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    - type -- None
    - validate_content --  If true, calculates an MD5 hash for each chunk of the blob. The storage service checks the hash of the content that has arrived with the hash that was sent. This is primarily valuable for detecting bitflips on the wire if using http instead of https as https (the default) will already validate. Note that this MD5 hash is not stored with the blob. Also note that if enabled, the memory-efficient upload algorithm will not be used, because computing the MD5 hash requires buffering entire blocks, and doing so defeats the purpose of the memory-efficient algorithm.
    '''
    return _call_az("az storage blob upload", locals())


def upload_batch(destination, source, account_key=None, account_name=None, auth_mode=None, connection_string=None, content_cache_control=None, content_disposition=None, content_encoding=None, content_language=None, content_md5=None, content_type=None, destination_path=None, dryrun=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None, lease_id=None, max_connections=None, maxsize_condition=None, metadata=None, no_progress=None, pattern=None, sas_token=None, socket_timeout=None, timeout=None, type=None, validate_content=None):
    '''
    Upload files from a local directory to a blob container.

    Required Parameters:
    - destination -- None
    - source -- None

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
    - destination_path -- The destination path that will be prepended to the blob name.
    - dryrun -- None
    - if_match -- None
    - if_modified_since -- Commence only if modified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - if_none_match -- None
    - if_unmodified_since -- Commence only if unmodified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - lease_id -- None
    - max_connections -- Maximum number of parallel connections to use when the blob size exceeds 64MB.
    - maxsize_condition -- None
    - metadata -- Metadata in space-separated key=value pairs. This overwrites any existing metadata.
    - no_progress -- Include this flag to disable progress reporting for the command.
    - pattern -- None
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - socket_timeout -- The socket timeout(secs), used by the service to regulate data flow.
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    - type -- None
    - validate_content -- None
    '''
    return _call_az("az storage blob upload-batch", locals())


def download_batch(destination, source, account_key=None, account_name=None, auth_mode=None, connection_string=None, dryrun=None, max_connections=None, no_progress=None, pattern=None, sas_token=None, socket_timeout=None):
    '''
    Download blobs from a blob container recursively.

    Required Parameters:
    - destination -- None
    - source -- None

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - dryrun -- None
    - max_connections -- Maximum number of parallel connections to use when the blob size exceeds 64MB.
    - no_progress -- Include this flag to disable progress reporting for the command.
    - pattern -- None
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - socket_timeout -- The socket timeout(secs), used by the service to regulate data flow.
    '''
    return _call_az("az storage blob download-batch", locals())


def delete_batch(source, account_key=None, account_name=None, auth_mode=None, connection_string=None, delete_snapshots=None, dryrun=None, if_match=None, if_modified_since=None, if_none_match=None, if_unmodified_since=None, lease_id=None, pattern=None, sas_token=None, timeout=None):
    '''
    Delete blobs from a blob container recursively.

    Required Parameters:
    - source -- None

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - delete_snapshots -- Required if the blob has associated snapshots.
    - dryrun -- None
    - if_match -- None
    - if_modified_since -- Commence only if modified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - if_none_match -- None
    - if_unmodified_since -- Commence only if unmodified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - lease_id -- The active lease id for the blob.
    - pattern -- None
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage blob delete-batch", locals())


def restore(account_name, time_to_restore, blob_range=None, no_wait=None, resource_group=None):
    '''
    Restore blobs in the specified blob ranges.

    Required Parameters:
    - account_name -- The storage account name.
    - time_to_restore -- Restore blob to the specified time, which should be UTC datetime in (Y-m-d'T'H:M:S'Z').

    Optional Parameters:
    - blob_range -- Blob ranges to restore. You need to two values to specify start_range and end_range for each blob range, e.g. -r blob1 blob2. Note: Empty means account start as start range value, and means account end for end range.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage blob restore", locals())


def sync(container, source, account_key=None, account_name=None, auth_mode=None, connection_string=None, destination=None, exclude_path=None, exclude_pattern=None, include_pattern=None, sas_token=None):
    '''
    Sync blobs recursively to a storage blob container.

    Required Parameters:
    - container -- The sync destination container.
    - source -- The source file path to sync from.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - destination -- The destination path that will be prepended to the blob name.
    - exclude_path -- Exclude these paths. This option does not support wildcard characters (*). Checks relative path prefix. For example: myFolder;myFolder/subDirName/file.pdf.
    - exclude_pattern -- Exclude these files where the name matches the pattern list. For example: *.jpg;*.pdf;exactName. This option supports wildcard characters (*)
    - include_pattern -- Include only these files where the name matches the pattern list. For example: *.jpg;*.pdf;exactName. This option supports wildcard characters (*)
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    '''
    return _call_az("az storage blob sync", locals())

