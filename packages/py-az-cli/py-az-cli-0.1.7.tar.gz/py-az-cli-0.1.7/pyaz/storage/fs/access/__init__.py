'''
Manage file system access and permissions for Azure Data Lake Storage Gen2 account.
'''
from .... pyaz_utils import _call_az

def set(account_key=None, account_name=None, acl=None, auth_mode=None, connection_string=None, group=None, owner=None, permissions=None, sas_token=None):
    '''
    Set the access control properties of a path(directory or file) in Azure Data Lake Storage Gen2 account.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - acl --  Sets POSIX access control rights on files and directories. The value is a comma-separated list of access control entries. Each access control entry (ACE) consists of a scope, a type, a user or group identifier, and permissions in the format "[scope:][type]:[id]:[permissions]". permissions and acl are mutually exclusive.
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - group --  Optional. The owning group of the file or directory.
    - owner --  Optional. The owner of the file or directory.
    - permissions --  Optional and only valid if Hierarchical Namespace is enabled for the account. Sets POSIX access permissions for the file owner, the file owning group, and others. Each class may be granted read, write, or execute permission.  The sticky bit is also supported. Both symbolic (rwxrw-rw-) and 4-digit octal notation (e.g. 0766) are supported. permissions and acl are mutually exclusive.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    '''
    return _call_az("az storage fs access set", locals())


def show(account_key=None, account_name=None, auth_mode=None, connection_string=None, sas_token=None):
    '''
    Show the access control properties of a path (directory or file) in Azure Data Lake Storage Gen2 account.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    '''
    return _call_az("az storage fs access show", locals())


def set_recursive(acl, account_key=None, account_name=None, auth_mode=None, batch_size=None, connection_string=None, continuation=None, continue_on_failure=None, max_batches=None, sas_token=None, timeout=None):
    '''
    Set the Access Control on a path and sub-paths in Azure Data Lake Storage Gen2 account.

    Required Parameters:
    - acl -- The value is a comma-separated list of access control entries. Each access control entry (ACE) consists of a scope, a type, a user or group identifier, and permissions in the format "[scope:][type]:[id]:[permissions]".  For more information, please refer to https://docs.microsoft.com/azure/storage/blobs/data-lake-storage-access-control.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - batch_size -- Optional. If data set size exceeds batch size then operation will be split into multiple requests so that progress can be tracked. Batch size should be between 1 and 2000. The default when unspecified is 2000.
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - continuation -- Optional continuation token that can be used to resume previously stopped operation.
    - continue_on_failure -- If set to False, the operation will terminate quickly on encountering user errors (4XX). If True, the operation will ignore user errors and proceed with the operation on other sub-entities of the directory. Continuation token will only be returned when --continue-on-failure is True in case of user errors. If not set the default value is False for this.
    - max_batches -- Optional. Define maximum number of batches that single change Access Control operation can execute. If maximum is reached before all sub-paths are processed, then continuation token can be used to resume operation. Empty value indicates that maximum number of batches in unbound and operation continues till end.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage fs access set-recursive", locals())


def update_recursive(acl, account_key=None, account_name=None, auth_mode=None, batch_size=None, connection_string=None, continuation=None, continue_on_failure=None, max_batches=None, sas_token=None, timeout=None):
    '''
    Modify the Access Control on a path and sub-paths in Azure Data Lake Storage Gen2 account.

    Required Parameters:
    - acl -- The value is a comma-separated list of access control entries. Each access control entry (ACE) consists of a scope, a type, a user or group identifier, and permissions in the format "[scope:][type]:[id]:[permissions]".  For more information, please refer to https://docs.microsoft.com/azure/storage/blobs/data-lake-storage-access-control.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - batch_size -- Optional. If data set size exceeds batch size then operation will be split into multiple requests so that progress can be tracked. Batch size should be between 1 and 2000. The default when unspecified is 2000.
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - continuation -- Optional continuation token that can be used to resume previously stopped operation.
    - continue_on_failure -- If set to False, the operation will terminate quickly on encountering user errors (4XX). If True, the operation will ignore user errors and proceed with the operation on other sub-entities of the directory. Continuation token will only be returned when --continue-on-failure is True in case of user errors. If not set the default value is False for this.
    - max_batches -- Optional. Define maximum number of batches that single change Access Control operation can execute. If maximum is reached before all sub-paths are processed, then continuation token can be used to resume operation. Empty value indicates that maximum number of batches in unbound and operation continues till end.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage fs access update-recursive", locals())


def remove_recursive(acl, account_key=None, account_name=None, auth_mode=None, batch_size=None, connection_string=None, continuation=None, continue_on_failure=None, max_batches=None, sas_token=None, timeout=None):
    '''
    Remove the Access Control on a path and sub-paths in Azure Data Lake Storage Gen2 account.

    Required Parameters:
    - acl -- The value is a comma-separated list of access control entries. Each access control entry (ACE) consists of a scope, a type, a user or group identifier, and permissions in the format "[scope:][type]:[id]:[permissions]".  For more information, please refer to https://docs.microsoft.com/azure/storage/blobs/data-lake-storage-access-control.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - auth_mode -- The mode in which to run the command. "login" mode will directly use your login credentials for the authentication. The legacy "key" mode will attempt to query for an account key if no authentication parameters for the account are provided. Environment variable: AZURE_STORAGE_AUTH_MODE
    - batch_size -- Optional. If data set size exceeds batch size then operation will be split into multiple requests so that progress can be tracked. Batch size should be between 1 and 2000. The default when unspecified is 2000.
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - continuation -- Optional continuation token that can be used to resume previously stopped operation.
    - continue_on_failure -- If set to False, the operation will terminate quickly on encountering user errors (4XX). If True, the operation will ignore user errors and proceed with the operation on other sub-entities of the directory. Continuation token will only be returned when --continue-on-failure is True in case of user errors. If not set the default value is False for this.
    - max_batches -- Optional. Define maximum number of batches that single change Access Control operation can execute. If maximum is reached before all sub-paths are processed, then continuation token can be used to resume operation. Empty value indicates that maximum number of batches in unbound and operation continues till end.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage fs access remove-recursive", locals())

