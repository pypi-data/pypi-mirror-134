'''
Manage Azure Cosmos DB SQL databases.
'''
from .... pyaz_utils import _call_az
from . import throughput


def create(account_name, name, resource_group, max_throughput=None, throughput=None):
    '''
    Create an SQL database under an Azure Cosmos DB account.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - name -- Database name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - max_throughput -- The maximum throughput resource can scale to (RU/s). Provided when the resource is autoscale enabled. The minimum value can be 4000 (RU/s)
    - throughput -- The throughput of SQL database (RU/s). Default value is 400
    '''
    return _call_az("az cosmosdb sql database create", locals())


def exists(account_name, name, resource_group):
    '''
    

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - name -- Database name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb sql database exists", locals())


def list(account_name, resource_group):
    '''
    List the SQL databases under an Azure Cosmos DB account.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb sql database list", locals())


def show(account_name, name, resource_group):
    '''
    Show the details of a SQL database under an Azure Cosmos DB account.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - name -- Database name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb sql database show", locals())


def delete(account_name, name, resource_group, yes=None):
    '''
    Delete the SQL database under an Azure Cosmos DB account.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - name -- Database name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az cosmosdb sql database delete", locals())

