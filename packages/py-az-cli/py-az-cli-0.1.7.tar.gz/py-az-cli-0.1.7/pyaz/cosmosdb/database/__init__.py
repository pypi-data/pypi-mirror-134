'''
Manage Azure Cosmos DB databases.
'''
from ... pyaz_utils import _call_az

def show(db_name, key=None, name=None, resource_group_name=None, url_connection=None):
    '''
    Shows an Azure Cosmos DB database

    Required Parameters:
    - db_name -- Database Name

    Optional Parameters:
    - key -- Cosmos DB account key. Must be used in conjunction with cosmosdb account name or url-connection.
    - name -- Cosmos DB account name. Must be used in conjunction with either name of the resource group or cosmosdb account key.
    - resource_group_name -- name of the resource group. Must be used in conjunction with cosmosdb account name.
    - url_connection -- Cosmos DB account url connection. Must be used in conjunction with cosmosdb account key.
    '''
    return _call_az("az cosmosdb database show", locals())


def list(key=None, name=None, resource_group_name=None, url_connection=None):
    '''
    Lists all Azure Cosmos DB databases

    Optional Parameters:
    - key -- Cosmos DB account key. Must be used in conjunction with cosmosdb account name or url-connection.
    - name -- Cosmos DB account name. Must be used in conjunction with either name of the resource group or cosmosdb account key.
    - resource_group_name -- name of the resource group. Must be used in conjunction with cosmosdb account name.
    - url_connection -- Cosmos DB account url connection. Must be used in conjunction with cosmosdb account key.
    '''
    return _call_az("az cosmosdb database list", locals())


def exists(db_name, key=None, name=None, resource_group_name=None, url_connection=None):
    '''
    Returns a boolean indicating whether the database exists

    Required Parameters:
    - db_name -- Database Name

    Optional Parameters:
    - key -- Cosmos DB account key. Must be used in conjunction with cosmosdb account name or url-connection.
    - name -- Cosmos DB account name. Must be used in conjunction with either name of the resource group or cosmosdb account key.
    - resource_group_name -- name of the resource group. Must be used in conjunction with cosmosdb account name.
    - url_connection -- Cosmos DB account url connection. Must be used in conjunction with cosmosdb account key.
    '''
    return _call_az("az cosmosdb database exists", locals())


def create(db_name, key=None, name=None, resource_group_name=None, throughput=None, url_connection=None):
    '''
    Creates an Azure Cosmos DB database

    Required Parameters:
    - db_name -- Database Name

    Optional Parameters:
    - key -- Cosmos DB account key. Must be used in conjunction with cosmosdb account name or url-connection.
    - name -- Cosmos DB account name. Must be used in conjunction with either name of the resource group or cosmosdb account key.
    - resource_group_name -- name of the resource group. Must be used in conjunction with cosmosdb account name.
    - throughput -- Offer Throughput (RU/s)
    - url_connection -- Cosmos DB account url connection. Must be used in conjunction with cosmosdb account key.
    '''
    return _call_az("az cosmosdb database create", locals())


def delete(db_name, key=None, name=None, resource_group_name=None, url_connection=None, yes=None):
    '''
    Deletes an Azure Cosmos DB database

    Required Parameters:
    - db_name -- Database Name

    Optional Parameters:
    - key -- Cosmos DB account key. Must be used in conjunction with cosmosdb account name or url-connection.
    - name -- Cosmos DB account name. Must be used in conjunction with either name of the resource group or cosmosdb account key.
    - resource_group_name -- name of the resource group. Must be used in conjunction with cosmosdb account name.
    - url_connection -- Cosmos DB account url connection. Must be used in conjunction with cosmosdb account key.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az cosmosdb database delete", locals())

