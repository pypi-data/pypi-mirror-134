'''
Manage queue storage messages.
'''
from ... pyaz_utils import _call_az

def put(content, queue_name, account_key=None, account_name=None, auth_mode=None, connection_string=None, sas_token=None, time_to_live=None, timeout=None, visibility_timeout=None):
    '''
    

    Required Parameters:
    - content -- Message content, up to 64KB in size.
    - queue_name -- The queue name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - time_to_live --  Specifies the time-to-live interval for the message, in seconds. The time-to-live may be any positive number or -1 for infinity. If this parameter is omitted, the default time-to-live is 7 days.
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    - visibility_timeout --  If not specified, the default value is 0. Specifies the new visibility timeout value, in seconds, relative to server time. The value must be larger than or equal to 0, and cannot be larger than 7 days. The visibility timeout of a message cannot be set to a value later than the expiry time. visibility_timeout should be set to a value smaller than the time-to-live value.
    '''
    return _call_az("az storage message put", locals())


def get(queue_name, account_key=None, account_name=None, auth_mode=None, connection_string=None, num_messages=None, sas_token=None, timeout=None, visibility_timeout=None):
    '''
    

    Required Parameters:
    - queue_name -- The queue name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - num_messages --  A nonzero integer value that specifies the number of messages to retrieve from the queue, up to a maximum of 32. If fewer are visible, the visible messages are returned. By default, a single message is retrieved from the queue with this operation.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    - visibility_timeout --  Specifies the new visibility timeout value, in seconds, relative to server time. The new value must be larger than or equal to 1 second, and cannot be larger than 7 days. The visibility timeout of a message can be set to a value later than the expiry time.
    '''
    return _call_az("az storage message get", locals())


def peek(queue_name, account_key=None, account_name=None, auth_mode=None, connection_string=None, num_messages=None, sas_token=None, timeout=None):
    '''
    

    Required Parameters:
    - queue_name -- The queue name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - num_messages --  A nonzero integer value that specifies the number of messages to peek from the queue, up to a maximum of 32. By default, a single message is peeked from the queue with this operation.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage message peek", locals())


def delete(id, pop_receipt, queue_name, account_key=None, account_name=None, auth_mode=None, connection_string=None, sas_token=None, timeout=None):
    '''
    

    Required Parameters:
    - id --  The message id identifying the message to delete.
    - pop_receipt --  A valid pop receipt value returned from an earlier call to the :func:`~get_messages` or :func:`~update_message`.
    - queue_name -- The queue name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage message delete", locals())


def clear(queue_name, account_key=None, account_name=None, auth_mode=None, connection_string=None, sas_token=None, timeout=None):
    '''
    

    Required Parameters:
    - queue_name -- The queue name.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage message clear", locals())


def update(id, pop_receipt, queue_name, visibility_timeout, account_key=None, account_name=None, auth_mode=None, connection_string=None, content=None, sas_token=None, timeout=None):
    '''
    

    Required Parameters:
    - id --  The message id identifying the message to update.
    - pop_receipt --  A valid pop receipt value returned from an earlier call to the :func:`~get_messages` or :func:`~update_message` operation.
    - queue_name -- The queue name.
    - visibility_timeout --  Specifies the new visibility timeout value, in seconds, relative to server time. The new value must be larger than or equal to 0, and cannot be larger than 7 days. The visibility timeout of a message cannot be set to a value later than the expiry time. A message can be updated until it has been deleted or has expired.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - content -- Message content, up to 64KB in size.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage message update", locals())

