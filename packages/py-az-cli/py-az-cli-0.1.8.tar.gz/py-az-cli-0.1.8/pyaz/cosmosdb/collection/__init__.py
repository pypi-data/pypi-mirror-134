'''
Manage Azure Cosmos DB collections.
'''
from ... pyaz_utils import _call_az

def show(collection_name, db_name, key=None, name=None, resource_group_name=None, url_connection=None):
    '''
    

    Required Parameters:
    - collection_name -- Collection Name
    - db_name -- Database Name

    Optional Parameters:
    - key -- Cosmos DB account key. Must be used in conjunction with cosmosdb account name or url-connection.
    - name -- Cosmos DB account name. Must be used in conjunction with either name of the resource group or cosmosdb account key.
    - resource_group_name -- name of the resource group. Must be used in conjunction with cosmosdb account name.
    - url_connection -- Cosmos DB account url connection. Must be used in conjunction with cosmosdb account key.
    '''
    return _call_az("az cosmosdb collection show", locals())


def list(db_name, key=None, name=None, resource_group_name=None, url_connection=None):
    '''
    

    Required Parameters:
    - db_name -- Database Name

    Optional Parameters:
    - key -- Cosmos DB account key. Must be used in conjunction with cosmosdb account name or url-connection.
    - name -- Cosmos DB account name. Must be used in conjunction with either name of the resource group or cosmosdb account key.
    - resource_group_name -- name of the resource group. Must be used in conjunction with cosmosdb account name.
    - url_connection -- Cosmos DB account url connection. Must be used in conjunction with cosmosdb account key.
    '''
    return _call_az("az cosmosdb collection list", locals())


def exists(collection_name, db_name, key=None, name=None, resource_group_name=None, url_connection=None):
    '''
    

    Required Parameters:
    - collection_name -- Collection Name
    - db_name -- Database Name

    Optional Parameters:
    - key -- Cosmos DB account key. Must be used in conjunction with cosmosdb account name or url-connection.
    - name -- Cosmos DB account name. Must be used in conjunction with either name of the resource group or cosmosdb account key.
    - resource_group_name -- name of the resource group. Must be used in conjunction with cosmosdb account name.
    - url_connection -- Cosmos DB account url connection. Must be used in conjunction with cosmosdb account key.
    '''
    return _call_az("az cosmosdb collection exists", locals())


def create(collection_name, db_name, default_ttl=None, indexing_policy=None, key=None, name=None, partition_key_path=None, resource_group_name=None, throughput=None, url_connection=None):
    '''
    

    Required Parameters:
    - collection_name -- Collection Name
    - db_name -- Database Name

    Optional Parameters:
    - default_ttl -- Default TTL. Provide 0 to disable.
    - indexing_policy -- Indexing Policy, you can enter it as a string or as a file, e.g., --indexing-policy @policy-file.json)
    - key -- Cosmos DB account key. Must be used in conjunction with cosmosdb account name or url-connection.
    - name -- Cosmos DB account name. Must be used in conjunction with either name of the resource group or cosmosdb account key.
    - partition_key_path -- Partition Key Path, e.g., '/properties/name'
    - resource_group_name -- name of the resource group. Must be used in conjunction with cosmosdb account name.
    - throughput -- Offer Throughput (RU/s)
    - url_connection -- Cosmos DB account url connection. Must be used in conjunction with cosmosdb account key.
    '''
    return _call_az("az cosmosdb collection create", locals())


def delete(collection_name, db_name, key=None, name=None, resource_group_name=None, url_connection=None, yes=None):
    '''
    

    Required Parameters:
    - collection_name -- Collection Name
    - db_name -- Database Name

    Optional Parameters:
    - key -- Cosmos DB account key. Must be used in conjunction with cosmosdb account name or url-connection.
    - name -- Cosmos DB account name. Must be used in conjunction with either name of the resource group or cosmosdb account key.
    - resource_group_name -- name of the resource group. Must be used in conjunction with cosmosdb account name.
    - url_connection -- Cosmos DB account url connection. Must be used in conjunction with cosmosdb account key.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az cosmosdb collection delete", locals())


def update(collection_name, db_name, default_ttl=None, indexing_policy=None, key=None, name=None, resource_group_name=None, throughput=None, url_connection=None):
    '''
    

    Required Parameters:
    - collection_name -- Collection Name
    - db_name -- Database Name

    Optional Parameters:
    - default_ttl -- Default TTL. Provide 0 to disable.
    - indexing_policy -- Indexing Policy, you can enter it as a string or as a file, e.g., --indexing-policy @policy-file.json)
    - key -- Cosmos DB account key. Must be used in conjunction with cosmosdb account name or url-connection.
    - name -- Cosmos DB account name. Must be used in conjunction with either name of the resource group or cosmosdb account key.
    - resource_group_name -- name of the resource group. Must be used in conjunction with cosmosdb account name.
    - throughput -- Offer Throughput (RU/s)
    - url_connection -- Cosmos DB account url connection. Must be used in conjunction with cosmosdb account key.
    '''
    return _call_az("az cosmosdb collection update", locals())

