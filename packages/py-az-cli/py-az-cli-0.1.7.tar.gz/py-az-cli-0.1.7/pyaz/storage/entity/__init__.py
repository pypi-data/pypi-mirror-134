'''
Manage table storage entities.
'''
from ... pyaz_utils import _call_az

def query(table_name, accept=None, account_key=None, account_name=None, connection_string=None, filter=None, marker=None, num_results=None, sas_token=None, select=None, timeout=None):
    '''
    List entities which satisfy a query.

    Required Parameters:
    - table_name --  The name of the table to query.

    Optional Parameters:
    - accept -- Specifies how much metadata to include in the response payload.
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - filter --  Returns only entities that satisfy the specified filter. Note that no more than 15 discrete comparisons are permitted within a $filter string. See http://msdn.microsoft.com/en-us/library/windowsazure/dd894031.aspx for more information on constructing filters.
    - marker --  An opaque continuation object. This value can be retrieved from the next_marker field of a previous generator object if max_results was specified and that generator has finished enumerating results. If specified, this generator will begin returning results from the point where the previous generator stopped.
    - num_results --  The maximum number of entities to return.
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - select -- Space-separated list of properties to return for each entity.
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage entity query", locals())


def replace(entity, table_name, account_key=None, account_name=None, connection_string=None, if_match=None, sas_token=None, timeout=None):
    '''
    

    Required Parameters:
    - entity --  The entity to update. Could be a dict or an entity object. Must contain a PartitionKey and a RowKey.
    - table_name --  The name of the table containing the entity to update.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - if_match --  The client may specify the ETag for the entity on the request in order to compare to the ETag maintained by the service for the purpose of optimistic concurrency. The update operation will be performed only if the ETag sent by the client matches the value maintained by the server, indicating that the entity has not been modified since it was retrieved by the client. To force an unconditional update, set If-Match to the wildcard character (*).
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage entity replace", locals())


def merge(entity, table_name, account_key=None, account_name=None, connection_string=None, if_match=None, sas_token=None, timeout=None):
    '''
    

    Required Parameters:
    - entity --  The entity to merge. Could be a dict or an entity object. Must contain a PartitionKey and a RowKey.
    - table_name --  The name of the table containing the entity to merge.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - if_match --  The client may specify the ETag for the entity on the request in order to compare to the ETag maintained by the service for the purpose of optimistic concurrency. The merge operation will be performed only if the ETag sent by the client matches the value maintained by the server, indicating that the entity has not been modified since it was retrieved by the client. To force an unconditional merge, set If-Match to the wildcard character (*).
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage entity merge", locals())


def delete(partition_key, row_key, table_name, account_key=None, account_name=None, connection_string=None, if_match=None, sas_token=None, timeout=None):
    '''
    

    Required Parameters:
    - partition_key --  The PartitionKey of the entity.
    - row_key --  The RowKey of the entity.
    - table_name --  The name of the table containing the entity to delete.

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - if_match --  The client may specify the ETag for the entity on the request in order to compare to the ETag maintained by the service for the purpose of optimistic concurrency. The delete operation will be performed only if the ETag sent by the client matches the value maintained by the server, indicating that the entity has not been modified since it was retrieved by the client. To force an unconditional delete, set If-Match to the wildcard character (*).
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage entity delete", locals())


def show(partition_key, row_key, table_name, accept=None, account_key=None, account_name=None, connection_string=None, sas_token=None, select=None, timeout=None):
    '''
    

    Required Parameters:
    - partition_key --  The PartitionKey of the entity.
    - row_key --  The RowKey of the entity.
    - table_name --  The name of the table to get the entity from.

    Optional Parameters:
    - accept --  Specifies the accepted content type of the response payload. See :class:`~azure.storage.table.models.TablePayloadFormat` for possible values.
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - select -- Space-separated list of properties to return for each entity.
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage entity show", locals())


def insert(entity, table_name, account_key=None, account_name=None, connection_string=None, if_exists=None, sas_token=None, timeout=None):
    '''
    Insert an entity into a table.

    Required Parameters:
    - entity -- None
    - table_name -- None

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT. Must be used in conjunction with either storage account key or a SAS token. If neither are present, the command will try to query the storage account key using the authenticated Azure account. If a large number of storage commands are executed the API quota may be hit
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - if_exists -- None
    - sas_token -- A Shared Access Signature (SAS). Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_SAS_TOKEN
    - timeout -- Request timeout in seconds. Applies to each call to the service.
    '''
    return _call_az("az storage entity insert", locals())

