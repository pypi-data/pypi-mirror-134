'''
Manage storage service metrics.
'''
from ... pyaz_utils import _call_az

def update(retention, services, account_key=None, account_name=None, api=None, connection_string=None, hour=None, minute=None, sas_token=None, timeout=None):
    '''
    Update metrics settings for a storage account.

    Required Parameters:
    - retention -- None
    - services -- None

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - api -- None
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - hour -- None
    - minute -- None
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage metrics update", locals())


def show(account_key=None, account_name=None, connection_string=None, interval=None, sas_token=None, services=None, timeout=None):
    '''
    Show metrics settings for a storage account.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - interval -- None
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - services -- None
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage metrics show", locals())

