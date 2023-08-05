'''
Manage Azure Cosmos DB Gremlin graphs.
'''
from .... pyaz_utils import _call_az
from . import throughput


def create(account_name, database_name, name, partition_key_path, resource_group, conflict_resolution_policy=None, idx=None, max_throughput=None, throughput=None, ttl=None):
    '''
    Create an Gremlin graph under an Azure Cosmos DB Gremlin database.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - database_name -- Database name.
    - name -- Graph name
    - partition_key_path -- Partition Key Path, e.g., '/address/zipcode'
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - conflict_resolution_policy -- Conflict Resolution Policy, you can enter it as a string or as a file, e.g., --conflict-resolution-policy @policy-file.json or --conflict-resolution-policy "{\"mode\": \"lastWriterWins\", \"conflictResolutionPath\": \"/path\"}"

    - idx -- Indexing Policy, you can enter it as a string or as a file, e.g., --idx @policy-file.json or --idx "{\"indexingMode\": \"consistent\", \"automatic\": true, \"includedPaths\": [{\"path\": \"/*\"}], \"excludedPaths\": [{ \"path\": \"/headquarters/employees/?\"}, { \"path\": \"/\\"_etag\\"/?\"}]}"

    - max_throughput -- The maximum throughput resource can scale to (RU/s). Provided when the resource is autoscale enabled. The minimum value can be 4000 (RU/s)
    - throughput -- The throughput of Gremlin graph (RU/s). Default value is 400. Omit this parameter if the database has shared throughput unless the graph should have dedicated throughput.
    - ttl -- Default TTL. If the value is missing or set to "-1", items don’t expire. If the value is set to "n", items will expire "n" seconds after last modified time.
    '''
    return _call_az("az cosmosdb gremlin graph create", locals())


def update(account_name, database_name, name, resource_group, idx=None, ttl=None):
    '''
    Update an Gremlin graph under an Azure Cosmos DB Gremlin database.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - database_name -- Database name.
    - name -- Graph name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - idx -- Indexing Policy, you can enter it as a string or as a file, e.g., --idx @policy-file.json or --idx "{\"indexingMode\": \"consistent\", \"automatic\": true, \"includedPaths\": [{\"path\": \"/*\"}], \"excludedPaths\": [{ \"path\": \"/headquarters/employees/?\"}, { \"path\": \"/\\"_etag\\"/?\"}]}"

    - ttl -- Default TTL. If the value is missing or set to "-1", items don’t expire. If the value is set to "n", items will expire "n" seconds after last modified time.
    '''
    return _call_az("az cosmosdb gremlin graph update", locals())


def exists(account_name, database_name, name, resource_group):
    '''
    

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - database_name -- Database name.
    - name -- Graph name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb gremlin graph exists", locals())


def list(account_name, database_name, resource_group):
    '''
    List the Gremlin graphs under an Azure Cosmos DB Gremlin database.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - database_name -- Database name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb gremlin graph list", locals())


def show(account_name, database_name, name, resource_group):
    '''
    Show the details of a Gremlin graph under an Azure Cosmos DB Gremlin database.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - database_name -- Database name.
    - name -- Graph name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb gremlin graph show", locals())


def delete(account_name, database_name, name, resource_group, yes=None):
    '''
    Delete the Gremlin graph under an Azure Cosmos DB Gremlin database.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - database_name -- Database name.
    - name -- Graph name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az cosmosdb gremlin graph delete", locals())

