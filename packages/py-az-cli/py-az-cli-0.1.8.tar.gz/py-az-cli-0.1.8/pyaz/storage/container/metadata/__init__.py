'''
Manage container metadata.
'''
from .... pyaz_utils import _call_az

def update(name, account_key=None, account_name=None, auth_mode=None, connection_string=None, if_modified_since=None, lease_id=None, metadata=None, sas_token=None, timeout=None):
    '''
    

    Required Parameters:
    - name -- The container name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - if_modified_since -- Commence only if modified since supplied UTC datetime (Y-m-d'T'H:M'Z')
    - lease_id --  If specified, set_container_metadata only succeeds if the container's lease is active and matches this ID.
    - metadata -- Metadata in space-separated key=value pairs. This overwrites any existing metadata.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage container metadata update", locals())


def show(name, account_key=None, account_name=None, auth_mode=None, connection_string=None, lease_id=None, sas_token=None, timeout=None):
    '''
    

    Required Parameters:
    - name -- The container name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - lease_id --  If specified, get_container_metadata only succeeds if the container's lease is active and matches this ID.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage container metadata show", locals())

