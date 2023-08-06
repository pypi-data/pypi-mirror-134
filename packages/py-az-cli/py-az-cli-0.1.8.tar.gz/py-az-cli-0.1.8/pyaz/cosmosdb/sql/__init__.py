'''
Manage SQL resources of Azure Cosmos DB account.
'''
from ... pyaz_utils import _call_az
from . import container, database, restorable_container, restorable_database, restorable_resource, stored_procedure, trigger, user_defined_function


def retrieve_latest_backup_time(account_name, container_name, database_name, location, resource_group):
    '''
    Retrieves latest restorable timestamp for the given sql container in given region.

    Required Parameters:
    - account_name -- Name of the CosmosDB database account
    - container_name -- Name of the CosmosDB Sql container name
    - database_name -- Name of the CosmosDB Sql database name
    - location -- Location of the account
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb sql retrieve-latest-backup-time", locals())

