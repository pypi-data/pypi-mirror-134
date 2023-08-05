'''
Manage Azure Cosmos DB MongoDB collections.
'''
from .... pyaz_utils import _call_az
from . import throughput


def create(account_name, database_name, name, resource_group, analytical_storage_ttl=None, idx=None, max_throughput=None, shard=None, throughput=None):
    '''
    Create an MongoDB collection under an Azure Cosmos DB MongoDB database.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - database_name -- Database name.
    - name -- Collection name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - analytical_storage_ttl -- Analytical TTL, when analytical storage is enabled.
    - idx -- Indexes, you can enter it as a string or as a file, e.g., --idx @indexes-file.json or --idx "[{\"key\": {\"keys\": [\"_ts\"]},\"options\": {\"expireAfterSeconds\": 1000}}, {\"key\": {\"keys\": [\"user_id\", \"user_address\"]}, \"options\": {\"unique\": \"true\"}}]"

    - max_throughput -- The maximum throughput resource can scale to (RU/s). Provided when the resource is autoscale enabled. The minimum value can be 4000 (RU/s)
    - shard -- Sharding key path.
    - throughput -- The throughput of MongoDB collection (RU/s). Default value is 400. Omit this parameter if the database has shared throughput unless the collection should have dedicated throughput.
    '''
    return _call_az("az cosmosdb mongodb collection create", locals())


def update(account_name, database_name, name, resource_group, analytical_storage_ttl=None, idx=None):
    '''
    Update an MongoDB collection under an Azure Cosmos DB MongoDB database.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - database_name -- Database name.
    - name -- Collection name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - analytical_storage_ttl -- Analytical TTL, when analytical storage is enabled.
    - idx -- Indexes, you can enter it as a string or as a file, e.g., --idx @indexes-file.json or --idx "[{\"key\": {\"keys\": [\"_ts\"]},\"options\": {\"expireAfterSeconds\": 1000}}, {\"key\": {\"keys\": [\"user_id\", \"user_address\"]}, \"options\": {\"unique\": \"true\"}}]"

    '''
    return _call_az("az cosmosdb mongodb collection update", locals())


def exists(account_name, database_name, name, resource_group):
    '''
    

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - database_name -- Database name.
    - name -- Collection name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb mongodb collection exists", locals())


def list(account_name, database_name, resource_group):
    '''
    List the MongoDB collections under an Azure Cosmos DB MongoDB database.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - database_name -- Database name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb mongodb collection list", locals())


def show(account_name, database_name, name, resource_group):
    '''
    Show the details of a MongoDB collection under an Azure Cosmos DB MongoDB database.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - database_name -- Database name.
    - name -- Collection name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb mongodb collection show", locals())


def delete(account_name, database_name, name, resource_group, yes=None):
    '''
    Delete the MongoDB collection under an Azure Cosmos DB MongoDB database.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - database_name -- Database name.
    - name -- Collection name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az cosmosdb mongodb collection delete", locals())

