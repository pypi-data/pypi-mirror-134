'''
Manage Azure Cosmos DB SQL triggers.
'''
from .... pyaz_utils import _call_az

def create(account_name, body, container_name, database_name, name, resource_group, operation=None, type=None):
    '''
    Create an SQL trigger under an Azure Cosmos DB SQL container.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - body -- Trigger body, you can enter it as a string or as a file, e.g., --body @triggerbody-file.json
    - container_name -- Container name.
    - database_name -- Database name.
    - name -- Trigger name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - operation -- The operation of the trigger.
    - type -- Trigger type
    '''
    return _call_az("az cosmosdb sql trigger create", locals())


def update(account_name, container_name, database_name, name, resource_group, body=None, operation=None, type=None):
    '''
    

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - container_name -- Container name.
    - database_name -- Database name.
    - name -- Trigger name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - body -- Trigger body, you can enter it as a string or as a file, e.g., --body @triggerbody-file.json
    - operation -- The operation of the trigger.
    - type -- Trigger type
    '''
    return _call_az("az cosmosdb sql trigger update", locals())


def list(account_name, container_name, database_name, resource_group):
    '''
    List the SQL triggers under an Azure Cosmos DB SQL container.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - container_name -- Container name.
    - database_name -- Database name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb sql trigger list", locals())


def show(account_name, container_name, database_name, name, resource_group):
    '''
    Show the details of a SQL trigger under an Azure Cosmos DB SQL container.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - container_name -- Container name.
    - database_name -- Database name.
    - name -- Trigger name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb sql trigger show", locals())


def delete(account_name, container_name, database_name, name, resource_group, yes=None):
    '''
    Delete the SQL trigger under an Azure Cosmos DB SQL container.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - container_name -- Container name.
    - database_name -- Database name.
    - name -- Trigger name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az cosmosdb sql trigger delete", locals())

