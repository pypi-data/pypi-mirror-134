'''
Manage throughput of SQL database under an Azure Cosmos DB account.
'''
from ..... pyaz_utils import _call_az

def show(account_name, name, resource_group):
    '''
    Get the throughput of the SQL database under an Azure Cosmos DB account.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - name -- Database name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb sql database throughput show", locals())


def migrate(account_name, name, resource_group, throughput_type):
    '''
    Migrate the throughput of the SQL database between autoscale and manually provisioned.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - name -- Database name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - throughput_type -- The type of throughput to migrate to.
    '''
    return _call_az("az cosmosdb sql database throughput migrate", locals())


def update(account_name, name, resource_group, max_throughput=None, throughput=None):
    '''
    Update the throughput of the SQL database under an Azure Cosmos DB account.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - name -- Database name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - max_throughput -- The maximum throughput resource can scale to (RU/s). Provided when the resource is autoscale enabled. The minimum value can be 4000 (RU/s)
    - throughput -- The throughput of SQL database (RU/s).
    '''
    return _call_az("az cosmosdb sql database throughput update", locals())

