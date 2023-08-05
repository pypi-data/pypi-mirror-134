'''
Manage container stored access policies.
'''
from .... pyaz_utils import _call_az

def create(container_name, name, account_key=None, account_name=None, auth_mode=None, connection_string=None, expiry=None, lease_id=None, permissions=None, sas_token=None, start=None):
    '''
    

    Required Parameters:
    - container_name -- The container name.
    - name -- The stored access policy name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - expiry -- expiration UTC datetime in (Y-m-d'T'H:M:S'Z')
    - lease_id -- The container lease ID.
    - permissions -- Allowed values: (a)dd (c)reate (d)elete (l)ist (r)ead (w)rite (a)dd (c)reate (d)elete (l)ist (r)ead (w)rite. Can be combined
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - start -- start UTC datetime (Y-m-d'T'H:M:S'Z'). Defaults to time of request.
    '''
    return _call_az("az storage container policy create", locals())


def delete(container_name, name, account_key=None, account_name=None, auth_mode=None, connection_string=None, lease_id=None, sas_token=None):
    '''
    

    Required Parameters:
    - container_name -- The container name.
    - name -- The stored access policy name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - lease_id -- The container lease ID.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    '''
    return _call_az("az storage container policy delete", locals())


def update(container_name, name, account_key=None, account_name=None, auth_mode=None, connection_string=None, expiry=None, lease_id=None, permissions=None, sas_token=None, start=None):
    '''
    

    Required Parameters:
    - container_name -- The container name.
    - name -- The stored access policy name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - expiry -- expiration UTC datetime in (Y-m-d'T'H:M:S'Z')
    - lease_id -- The container lease ID.
    - permissions -- Allowed values: (a)dd (c)reate (d)elete (l)ist (r)ead (w)rite (a)dd (c)reate (d)elete (l)ist (r)ead (w)rite. Can be combined
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - start -- start UTC datetime (Y-m-d'T'H:M:S'Z'). Defaults to time of request.
    '''
    return _call_az("az storage container policy update", locals())


def show(container_name, name, account_key=None, account_name=None, auth_mode=None, connection_string=None, lease_id=None, sas_token=None):
    '''
    

    Required Parameters:
    - container_name -- The container name.
    - name -- The stored access policy name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - lease_id -- The container lease ID.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    '''
    return _call_az("az storage container policy show", locals())


def list(container_name, account_key=None, account_name=None, auth_mode=None, connection_string=None, lease_id=None, sas_token=None):
    '''
    

    Required Parameters:
    - container_name -- The container name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - lease_id -- The container lease ID.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    '''
    return _call_az("az storage container policy list", locals())

