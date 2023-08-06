from ..... pyaz_utils import _call_az

def create(data_connection_name, database_name, kusto_pool_name, resource_group, workspace_name, blob_storage_event_type=None, consumer_group=None, data_format=None, event_hub_resource_id=None, ignore_first_record=None, location=None, mapping_rule_name=None, no_wait=None, storage_account_resource_id=None, table_name=None):
    '''
    Create a data connection.

    Required Parameters:
    - data_connection_name -- The name of the data connection.
    - database_name -- The name of the database in the Kusto pool.
    - kusto_pool_name -- The name of the Kusto pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace

    Optional Parameters:
    - blob_storage_event_type -- The name of blob storage event type to process.
    - consumer_group -- The event hub consumer group.
    - data_format -- The data format of the message. Optionally the data format can be added to each message.
    - event_hub_resource_id -- The resource ID where the event grid is configured to send events.
    - ignore_first_record -- A Boolean value that, if set to true, indicates that ingestion should ignore the first record of every file
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - mapping_rule_name -- The mapping rule to be used to ingest the data. Optionally the mapping information can be added to each message.
    - no_wait -- Do not wait for the long-running operation to finish.
    - storage_account_resource_id -- The resource ID of the storage account where the data resides.
    - table_name -- The table where the data should be ingested. Optionally the table information can be added to each message.
    '''
    return _call_az("az synapse kusto data-connection event-grid create", locals())


def update(data_connection_name, database_name, kusto_pool_name, resource_group, workspace_name, blob_storage_event_type=None, consumer_group=None, data_format=None, event_hub_resource_id=None, ignore_first_record=None, location=None, mapping_rule_name=None, no_wait=None, storage_account_resource_id=None, table_name=None):
    '''
    Updates a data connection.

    Required Parameters:
    - data_connection_name -- The name of the data connection.
    - database_name -- The name of the database in the Kusto pool.
    - kusto_pool_name -- The name of the Kusto pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace

    Optional Parameters:
    - blob_storage_event_type -- The name of blob storage event type to process.
    - consumer_group -- The event hub consumer group.
    - data_format -- The data format of the message. Optionally the data format can be added to each message.
    - event_hub_resource_id -- The resource ID where the event grid is configured to send events.
    - ignore_first_record -- A Boolean value that, if set to true, indicates that ingestion should ignore the first record of every file
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - mapping_rule_name -- The mapping rule to be used to ingest the data. Optionally the mapping information can be added to each message.
    - no_wait -- Do not wait for the long-running operation to finish.
    - storage_account_resource_id -- The resource ID of the storage account where the data resides.
    - table_name -- The table where the data should be ingested. Optionally the table information can be added to each message.
    '''
    return _call_az("az synapse kusto data-connection event-grid update", locals())

