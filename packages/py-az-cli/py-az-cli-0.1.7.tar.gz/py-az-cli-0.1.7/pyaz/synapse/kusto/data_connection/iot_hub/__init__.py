from ..... pyaz_utils import _call_az

def create(data_connection_name, database_name, kusto_pool_name, resource_group, workspace_name, consumer_group=None, data_format=None, event_system_properties=None, iot_hub_resource_id=None, location=None, mapping_rule_name=None, no_wait=None, shared_access_policy_name=None, table_name=None):
    '''
    Create a data connection.

    Required Parameters:
    - data_connection_name -- The name of the data connection.
    - database_name -- The name of the database in the Kusto pool.
    - kusto_pool_name -- The name of the Kusto pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace

    Optional Parameters:
    - consumer_group -- The iot hub consumer group.
    - data_format -- The data format of the message. Optionally the data format can be added to each message.
    - event_system_properties -- System properties of the iot hub
    - iot_hub_resource_id -- The resource ID of the Iot hub to be used to create a data connection.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - mapping_rule_name -- The mapping rule to be used to ingest the data. Optionally the mapping information can be added to each message.
    - no_wait -- Do not wait for the long-running operation to finish.
    - shared_access_policy_name -- The name of the share access policy
    - table_name -- The table where the data should be ingested. Optionally the table information can be added to each message.
    '''
    return _call_az("az synapse kusto data-connection iot-hub create", locals())


def update(data_connection_name, database_name, kusto_pool_name, resource_group, workspace_name, consumer_group=None, data_format=None, event_system_properties=None, iot_hub_resource_id=None, location=None, mapping_rule_name=None, no_wait=None, shared_access_policy_name=None, table_name=None):
    '''
    Updates a data connection.

    Required Parameters:
    - data_connection_name -- The name of the data connection.
    - database_name -- The name of the database in the Kusto pool.
    - kusto_pool_name -- The name of the Kusto pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace

    Optional Parameters:
    - consumer_group -- The iot hub consumer group.
    - data_format -- The data format of the message. Optionally the data format can be added to each message.
    - event_system_properties -- System properties of the iot hub
    - iot_hub_resource_id -- The resource ID of the Iot hub to be used to create a data connection.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - mapping_rule_name -- The mapping rule to be used to ingest the data. Optionally the mapping information can be added to each message.
    - no_wait -- Do not wait for the long-running operation to finish.
    - shared_access_policy_name -- The name of the share access policy
    - table_name -- The table where the data should be ingested. Optionally the table information can be added to each message.
    '''
    return _call_az("az synapse kusto data-connection iot-hub update", locals())

