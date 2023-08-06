'''
Manage file systems in Azure Data Lake Storage Gen2 account.
'''
from ... pyaz_utils import _call_az
from . import access, directory, file, metadata


def create(name, account_key=None, account_name=None, auth_mode=None, connection_string=None, metadata=None, public_access=None, sas_token=None, timeout=None):
    '''
    Create file system for Azure Data Lake Storage Gen2 account.

    Required Parameters:
    - name -- File system name (i.e. container name).

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - metadata -- Metadata in space-separated key=value pairs. This overwrites any existing metadata.
    - public_access -- Specify whether data in the file system may be accessed publicly and the level of access.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage fs create", locals())


def list(account_key=None, account_name=None, auth_mode=None, connection_string=None, include_metadata=None, prefix=None, sas_token=None):
    '''
    List file systems in ADLS Gen2 account.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - include_metadata -- Specify that file system metadata be returned in the response. The default value is "False".
    - prefix -- Filter the results to return only file systems whose names begin with the specified prefix.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    '''
    return _call_az("az storage fs list", locals())


def show(name, account_key=None, account_name=None, auth_mode=None, connection_string=None, sas_token=None, timeout=None):
    '''
    Show properties of file system in ADLS Gen2 account.

    Required Parameters:
    - name -- File system name (i.e. container name).

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage fs show", locals())


def delete(name, account_key=None, account_name=None, auth_mode=None, connection_string=None, sas_token=None, timeout=None, yes=None):
    '''
    Delete a file system in ADLS Gen2 account.

    Required Parameters:
    - name -- File system name (i.e. container name).

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az storage fs delete", locals())


def exists(name, account_key=None, account_name=None, auth_mode=None, connection_string=None, sas_token=None, timeout=None):
    '''
    Check for the existence of a file system in ADLS Gen2 account.

    Required Parameters:
    - name -- File system name (i.e. container name).

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage fs exists", locals())


def generate_sas(name, account_key=None, account_name=None, as_user=None, auth_mode=None, cache_control=None, connection_string=None, content_disposition=None, content_encoding=None, content_language=None, content_type=None, expiry=None, full_uri=None, https_only=None, ip=None, permissions=None, policy_name=None, start=None):
    '''
    Generate a SAS token for file system in ADLS Gen2 account.

    Required Parameters:
    - name -- File system name (i.e. container name).

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - as_user -- Indicates that this command return the SAS signed with the user delegation key. The expiry parameter and '--auth-mode login' are required if this argument is specified. 
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - cache_control -- Response header value for Cache-Control when resource is accessedusing this shared access signature.
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - content_disposition -- Response header value for Content-Disposition when resource is accessedusing this shared access signature.
    - content_encoding -- Response header value for Content-Encoding when resource is accessedusing this shared access signature.
    - content_language -- Response header value for Content-Language when resource is accessedusing this shared access signature.
    - content_type -- Response header value for Content-Type when resource is accessedusing this shared access signature.
    - expiry -- Specifies the UTC datetime (Y-m-d'T'H:M'Z') at which the SAS becomes invalid. Do not use if a stored access policy is referenced with --id that specifies this value.
    - full_uri -- Indicate that this command return the full blob URI and the shared access signature token.
    - https_only -- Only permit requests made with the HTTPS protocol. If omitted, requests from both the HTTP and HTTPS protocol are permitted.
    - ip -- Specifies the IP address or range of IP addresses from which to accept requests. Supports only IPv4 style addresses.
    - permissions -- The permissions the SAS grants. Allowed values: (d)elete (e)xecute (l)ist (p)ermissions (o)wnership (m)ove (r)ead (w)rite. Do not use if a stored access policy is referenced with --id that specifies this value. Can be combined.
    - policy_name -- The name of a stored access policy.
    - start -- Specifies the UTC datetime (Y-m-d'T'H:M'Z') at which the SAS becomes valid. Do not use if a stored access policy is referenced with --id that specifies this value. Defaults to the time of the request.
    '''
    return _call_az("az storage fs generate-sas", locals())

