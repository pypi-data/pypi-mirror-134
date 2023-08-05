'''
Manage NoSQL key-value storage.
'''
from ... pyaz_utils import _call_az
from . import policy


def create(name, account_key=None, account_name=None, connection_string=None, fail_on_exist=None, sas_token=None, timeout=None):
    '''
    

    Required Parameters:
    - name --  The name of the table to create. The table name may contain only alphanumeric characters and cannot begin with a numeric character. It is case-insensitive and must be from 3 to 63 characters long.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - fail_on_exist -- Throw an exception if the table already exists.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage table create", locals())


def delete(name, account_key=None, account_name=None, connection_string=None, fail_not_exist=None, sas_token=None, timeout=None):
    '''
    

    Required Parameters:
    - name --  The name of the table to delete.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - fail_not_exist --  Specifies whether to throw an exception if the table doesn't exist.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage table delete", locals())


def exists(name, account_key=None, account_name=None, connection_string=None, sas_token=None, timeout=None):
    '''
    

    Required Parameters:
    - name --  The name of table to check for existence.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage table exists", locals())


def generate_sas(name, account_key=None, account_name=None, connection_string=None, end_pk=None, end_rk=None, expiry=None, https_only=None, ip=None, permissions=None, policy_name=None, start=None, start_pk=None, start_rk=None):
    '''
    

    Required Parameters:
    - name --  The name of the table to create a SAS token for.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - end_pk --  The maximum partition key accessible with this shared access signature. endpk must accompany endrk. Key values are inclusive. If omitted, there is no upper bound on the table entities that can be accessed.
    - end_rk --  The maximum row key accessible with this shared access signature. endpk must accompany endrk. Key values are inclusive. If omitted, there is no upper bound on the table entities that can be accessed.
    - expiry -- Specifies the UTC datetime (Y-m-d'T'H:M'Z') at which the SAS becomes invalid. Do not use if a stored access policy is referenced with --id that specifies this value.
    - https_only -- Only permit requests made with the HTTPS protocol. If omitted, requests from both the HTTP and HTTPS protocol are permitted.
    - ip -- Specifies the IP address or range of IP addresses from which to accept requests. Supports only IPv4 style addresses.
    - permissions -- The permissions the SAS grants. Allowed values: (r)ead/query (a)dd (u)pdate (d)elete. Do not use if a stored access policy is referenced with --id that specifies this value. Can be combined.
    - policy_name -- The name of a stored access policy within the table's ACL.
    - start -- Specifies the UTC datetime (Y-m-d'T'H:M'Z') at which the SAS becomes valid. Do not use if a stored access policy is referenced with --id that specifies this value. Defaults to the time of the request.
    - start_pk --  The minimum partition key accessible with this shared access signature. startpk must accompany startrk. Key values are inclusive. If omitted, there is no lower bound on the table entities that can be accessed.
    - start_rk --  The minimum row key accessible with this shared access signature. startpk must accompany startrk. Key values are inclusive. If omitted, there is no lower bound on the table entities that can be accessed.
    '''
    return _call_az("az storage table generate-sas", locals())


def list(account_key=None, account_name=None, connection_string=None, marker=None, num_results=None, sas_token=None, timeout=None):
    '''
    List tables in a storage account.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - marker --  An opaque continuation object. This value can be retrieved from the next_marker field of a previous generator object if num_results was specified and that generator has finished enumerating results. If specified, this generator will begin returning results from the point where the previous generator stopped.
    - num_results --  The maximum number of tables to return.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage table list", locals())


def stats(account_key=None, account_name=None, connection_string=None, sas_token=None, timeout=None):
    '''
    

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage table stats", locals())

