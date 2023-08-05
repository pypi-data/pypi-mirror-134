'''
Manage file storage directories.
'''
from ... pyaz_utils import _call_az
from . import metadata


def create(name, share_name, account_key=None, account_name=None, connection_string=None, fail_on_exist=None, metadata=None, sas_token=None, timeout=None):
    '''
    

    Required Parameters:
    - name -- The directory name.
    - share_name -- The file share name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - fail_on_exist --  specify whether to throw an exception when the directory exists. False by default.
    - metadata -- Metadata in space-separated key=value pairs. This overwrites any existing metadata.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage directory create", locals())


def delete(name, share_name, account_key=None, account_name=None, connection_string=None, fail_not_exist=None, sas_token=None, timeout=None):
    '''
    

    Required Parameters:
    - name -- The directory name.
    - share_name -- The file share name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - fail_not_exist --  Specify whether to throw an exception when the directory doesn't exist.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage directory delete", locals())


def show(name, share_name, account_key=None, account_name=None, connection_string=None, sas_token=None, snapshot=None, timeout=None):
    '''
    

    Required Parameters:
    - name -- The directory name.
    - share_name -- The file share name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - snapshot --  A string that represents the snapshot version, if applicable.
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage directory show", locals())


def exists(name, share_name, account_key=None, account_name=None, connection_string=None, sas_token=None, snapshot=None, timeout=None):
    '''
    Check for the existence of a storage directory.

    Required Parameters:
    - name -- The directory name.
    - share_name -- The file share name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - snapshot --  A string that represents the snapshot version, if applicable.
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage directory exists", locals())


def list(share_name, account_key=None, account_name=None, connection_string=None, name=None, sas_token=None, timeout=None):
    '''
    List directories in a share.

    Required Parameters:
    - share_name -- The file share name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - name -- The directory name.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage directory list", locals())

