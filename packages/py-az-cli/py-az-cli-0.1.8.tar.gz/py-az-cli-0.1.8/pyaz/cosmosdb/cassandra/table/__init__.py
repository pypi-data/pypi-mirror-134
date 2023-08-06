'''
Manage Azure Cosmos DB Cassandra tables.
'''
from .... pyaz_utils import _call_az
from . import throughput


def create(account_name, keyspace_name, name, resource_group, schema, analytical_storage_ttl=None, max_throughput=None, throughput=None, ttl=None):
    '''
    Create an Cassandra table under an Azure Cosmos DB Cassandra keyspace.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - keyspace_name -- Keyspace name
    - name -- Table name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - schema -- Schema, you can enter it as a string or as a file, e.g., --schema @schema-file.json or --schema "{\"columns\": [{\"name\": \"columnA\",\"type\": \"uuid\"}, {\"name\": \"columnB\",\"type\": \"Ascii\"}],\"partitionKeys\": [{\"name\": \"columnA\"}]}"


    Optional Parameters:
    - analytical_storage_ttl -- Analytical TTL, when analytical storage is enabled.
    - max_throughput -- The maximum throughput resource can scale to (RU/s). Provided when the resource is autoscale enabled. The minimum value can be 4000 (RU/s)
    - throughput -- The throughput of Cassandra table (RU/s). Default value is 400. Omit this parameter if the keyspace has shared throughput unless the table should have dedicated throughput.
    - ttl -- Default TTL. If the value is missing or set to "-1", items don’t expire. If the value is set to "n", items will expire "n" seconds after last modified time.
    '''
    return _call_az("az cosmosdb cassandra table create", locals())


def update(account_name, keyspace_name, name, resource_group, analytical_storage_ttl=None, schema=None, ttl=None):
    '''
    Update an Cassandra table under an Azure Cosmos DB Cassandra keyspace.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - keyspace_name -- Keyspace name
    - name -- Table name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - analytical_storage_ttl -- Analytical TTL, when analytical storage is enabled.
    - schema -- Schema, you can enter it as a string or as a file, e.g., --schema @schema-file.json or --schema "{\"columns\": [{\"name\": \"columnA\",\"type\": \"uuid\"}, {\"name\": \"columnB\",\"type\": \"Ascii\"}],\"partitionKeys\": [{\"name\": \"columnA\"}]}"

    - ttl -- Default TTL. If the value is missing or set to "-1", items don’t expire. If the value is set to "n", items will expire "n" seconds after last modified time.
    '''
    return _call_az("az cosmosdb cassandra table update", locals())


def exists(account_name, keyspace_name, name, resource_group):
    '''
    

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - keyspace_name -- Keyspace name
    - name -- Table name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb cassandra table exists", locals())


def list(account_name, keyspace_name, resource_group):
    '''
    List the Cassandra tables under an Azure Cosmos DB Cassandra keyspace.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - keyspace_name -- Keyspace name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb cassandra table list", locals())


def show(account_name, keyspace_name, name, resource_group):
    '''
    Show the details of a Cassandra table under an Azure Cosmos DB Cassandra keyspace.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - keyspace_name -- Keyspace name
    - name -- Table name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb cassandra table show", locals())


def delete(account_name, keyspace_name, name, resource_group, yes=None):
    '''
    Delete the Cassandra table under an Azure Cosmos DB Cassandra keyspace.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - keyspace_name -- Keyspace name
    - name -- Table name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az cosmosdb cassandra table delete", locals())

