'''
Manage MongoDB resources of Azure Cosmos DB account.
'''
from ... pyaz_utils import _call_az
from . import collection, database, restorable_collection, restorable_database, restorable_resource


def retrieve_latest_backup_time(account_name, collection_name, database_name, location, resource_group):
    '''
    Retrieves latest restorable timestamp for the given mongodb collection in given region.

    Required Parameters:
    - account_name -- Name of the CosmosDB database account
    - collection_name -- Name of the CosmosDB MongoDB collection name
    - database_name -- Name of the CosmosDB MongoDB database name
    - location -- Location of the account
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb mongodb retrieve-latest-backup-time", locals())

