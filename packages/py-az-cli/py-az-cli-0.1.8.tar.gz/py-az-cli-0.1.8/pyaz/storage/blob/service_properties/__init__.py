from .... pyaz_utils import _call_az
from . import delete_policy


def show(account_key=None, account_name=None, auth_mode=None, connection_string=None, sas_token=None, timeout=None):
    '''
    

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage blob service-properties show", locals())


def update(_404_document=None, account_key=None, account_name=None, add=None, auth_mode=None, connection_string=None, delete_retention=None, delete_retention_period=None, force_string=None, index_document=None, remove=None, sas_token=None, set=None, static_website=None, timeout=None):
    '''
    Update storage blob service properties.

    Optional Parameters:
    - 404_document -- Represents the path to the error document that should be shown when an error 404 is issued, in other words, when a browser requests a page that does not exist.
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - delete_retention -- Enables soft-delete.
    - delete_retention_period -- Number of days that soft-deleted blob will be retained. Must be in range [1,365].
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - index_document -- Represents the name of the index document. This is commonly "index.html".
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - static_website -- Enables static-website.
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage blob service-properties update", locals())

