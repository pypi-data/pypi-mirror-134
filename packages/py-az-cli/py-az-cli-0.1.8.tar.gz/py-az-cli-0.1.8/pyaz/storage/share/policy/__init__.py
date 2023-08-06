'''
Manage shared access policies of a storage file share.
'''
from .... pyaz_utils import _call_az

def create(name, share_name, account_key=None, account_name=None, connection_string=None, expiry=None, permissions=None, sas_token=None, start=None):
    '''
    

    Required Parameters:
    - name -- The stored access policy name.
    - share_name -- The file share name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - expiry -- expiration UTC datetime in (Y-m-d'T'H:M:S'Z')
    - permissions -- Allowed values: (d)elete (l)ist (r)ead (w)rite (d)elete (l)ist (r)ead (w)rite. Can be combined
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - start -- start UTC datetime (Y-m-d'T'H:M:S'Z'). Defaults to time of request.
    '''
    return _call_az("az storage share policy create", locals())


def delete(name, share_name, account_key=None, account_name=None, connection_string=None, sas_token=None):
    '''
    

    Required Parameters:
    - name -- The stored access policy name.
    - share_name -- The file share name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    '''
    return _call_az("az storage share policy delete", locals())


def show(name, share_name, account_key=None, account_name=None, connection_string=None, sas_token=None):
    '''
    

    Required Parameters:
    - name -- The stored access policy name.
    - share_name -- The file share name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    '''
    return _call_az("az storage share policy show", locals())


def list(share_name, account_key=None, account_name=None, connection_string=None, sas_token=None):
    '''
    

    Required Parameters:
    - share_name -- The file share name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    '''
    return _call_az("az storage share policy list", locals())


def update(name, share_name, account_key=None, account_name=None, connection_string=None, expiry=None, permissions=None, sas_token=None, start=None):
    '''
    

    Required Parameters:
    - name -- The stored access policy name.
    - share_name -- The file share name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - expiry -- expiration UTC datetime in (Y-m-d'T'H:M:S'Z')
    - permissions -- Allowed values: (d)elete (l)ist (r)ead (w)rite (d)elete (l)ist (r)ead (w)rite. Can be combined
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - start -- start UTC datetime (Y-m-d'T'H:M:S'Z'). Defaults to time of request.
    '''
    return _call_az("az storage share policy update", locals())

