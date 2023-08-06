'''
Manage blob storage containers.
'''
from ... pyaz_utils import _call_az
from . import immutability_policy, lease, legal_hold, metadata, policy


def list(account_key=None, account_name=None, auth_mode=None, connection_string=None, include_deleted=None, include_metadata=None, marker=None, num_results=None, prefix=None, sas_token=None, show_next_marker=None, timeout=None):
    '''
    List containers in a storage account.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - include_deleted -- Specify that deleted containers to be returned in the response. This is for container restore enabled account. The default value is `False`
    - include_metadata -- Specify that container metadata to be returned in the response.
    - marker -- A string value that identifies the portion of the list of containers to be returned with the next listing operation. The operation returns the NextMarker value within the response body if the listing operation did not return all containers remaining to be listed with the current page. If specified, this generator will begin returning results from the point where the previous generator stopped.
    - num_results -- Specify the maximum number to return. If the request does not specify num_results, or specifies a value greater than 5000, the server will return up to 5000 items. Note that if the listing operation crosses a partition boundary, then the service will return a continuation token for retrieving the remaining of the results. Provide "*" to return all.
    - prefix -- Filter the results to return only blobs whose name begins with the specified prefix.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - show_next_marker -- Show nextMarker in result when specified.
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage container list", locals())


def delete(name, account_key=None, account_name=None, auth_mode=None, bypass_immutability_policy=None, connection_string=None, fail_not_exist=None, if_modified_since=None, if_unmodified_since=None, lease_id=None, sas_token=None, timeout=None):
    '''
    Marks the specified container for deletion.

    Required Parameters:
    - name -- The container name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - bypass_immutability_policy -- Bypasses upcoming service behavior that will block a container from being deleted if it has a immutability-policy. Specifying this will ignore arguments aside from those used to identify the container ("--name", "--account-name").
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - fail_not_exist -- Throw an exception if the container does not exist.
    - if_modified_since -- Commence only if modified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - if_unmodified_since -- Commence only if unmodified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - lease_id -- If specified, delete_container only succeeds if the container's lease is active and matches this ID. Required if the container has an active lease.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage container delete", locals())


def show(name, account_key=None, account_name=None, auth_mode=None, connection_string=None, lease_id=None, sas_token=None, timeout=None):
    '''
    

    Required Parameters:
    - name -- The container name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - lease_id --  If specified, get_container_properties only succeeds if the container's lease is active and matches this ID.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage container show", locals())


def create(name, account_key=None, account_name=None, auth_mode=None, connection_string=None, default_encryption_scope=None, fail_on_exist=None, metadata=None, prevent_encryption_scope_override=None, public_access=None, resource_group=None, sas_token=None, timeout=None):
    '''
    Create a container in a storage account.

    Required Parameters:
    - name -- The container name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT.
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - default_encryption_scope -- Default the container to use specified encryption scope for all writes.
    - fail_on_exist -- Throw an exception if the container already exists.
    - metadata -- Metadata in space-separated key=value pairs. This overwrites any existing metadata.
    - prevent_encryption_scope_override -- Block override of encryption scope from the container default.
    - public_access -- Specifies whether data in the container may be accessed publicly.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage container create", locals())


def generate_sas(name, account_key=None, account_name=None, as_user=None, auth_mode=None, cache_control=None, connection_string=None, content_disposition=None, content_encoding=None, content_language=None, content_type=None, expiry=None, https_only=None, ip=None, permissions=None, policy_name=None, start=None):
    '''
    Generate a SAS token for a storage container.

    Required Parameters:
    - name -- The container name.

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
    - https_only -- Only permit requests made with the HTTPS protocol. If omitted, requests from both the HTTP and HTTPS protocol are permitted.
    - ip -- Specifies the IP address or range of IP addresses from which to accept requests. Supports only IPv4 style addresses.
    - permissions -- The permissions the SAS grants. Allowed values: (a)dd (c)reate (d)elete (l)ist (r)ead (w)rite (a)dd (c)reate (d)elete (l)ist (r)ead (w)rite. Do not use if a stored access policy is referenced with --id that specifies this value. Can be combined.
    - policy_name -- The name of a stored access policy within the container's ACL.
    - start -- Specifies the UTC datetime (Y-m-d'T'H:M'Z') at which the SAS becomes valid. Do not use if a stored access policy is referenced with --id that specifies this value. Defaults to the time of the request.
    '''
    return _call_az("az storage container generate-sas", locals())


def exists(name, account_key=None, account_name=None, auth_mode=None, connection_string=None, sas_token=None, timeout=None):
    '''
    Check for the existence of a storage container.

    Required Parameters:
    - name -- The container name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage container exists", locals())


def set_permission(name, account_key=None, account_name=None, auth_mode=None, connection_string=None, if_modified_since=None, if_unmodified_since=None, lease_id=None, public_access=None, sas_token=None, timeout=None):
    '''
    

    Required Parameters:
    - name -- The container name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - if_modified_since -- Commence only if modified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - if_unmodified_since -- Commence only if unmodified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - lease_id --  If specified, set_container_acl only succeeds if the container's lease is active and matches this ID.
    - public_access -- Specifies whether data in the container may be accessed publicly.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage container set-permission", locals())


def show_permission(name, account_key=None, account_name=None, auth_mode=None, connection_string=None, lease_id=None, sas_token=None, timeout=None):
    '''
    

    Required Parameters:
    - name -- The container name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - lease_id --  If specified, get_container_acl only succeeds if the container's lease is active and matches this ID.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage container show-permission", locals())


def restore(deleted_version, name, account_key=None, account_name=None, auth_mode=None, connection_string=None, sas_token=None, timeout=None):
    '''
    Restore soft-deleted container.

    Required Parameters:
    - deleted_version -- Specify the version of the deleted container to restore.
    - name -- Specify the name of the deleted container to restore.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage container restore", locals())

