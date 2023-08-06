from .... pyaz_utils import _call_az

def create(account_name, body, container_name, database_name, name, resource_group):
    '''
    Create an SQL stored procedure under an Azure Cosmos DB SQL container.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - body -- StoredProcedure body, you can enter it as a string or as a file, e.g., --body @sprocbody-file.json
    - container_name -- Container name.
    - database_name -- Database name.
    - name -- StoredProcedure name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb sql stored-procedure create", locals())


def update(account_name, body, container_name, database_name, name, resource_group):
    '''
    

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - body -- StoredProcedure body, you can enter it as a string or as a file, e.g., --body @sprocbody-file.json
    - container_name -- Container name.
    - database_name -- Database name.
    - name -- StoredProcedure name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb sql stored-procedure update", locals())


def list(account_name, container_name, database_name, resource_group):
    '''
    List the SQL stored procedures under an Azure Cosmos DB SQL container.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - container_name -- Container name.
    - database_name -- Database name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb sql stored-procedure list", locals())


def show(account_name, container_name, database_name, name, resource_group):
    '''
    Show the details of a SQL stored procedure under an Azure Cosmos DB SQL container.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - container_name -- Container name.
    - database_name -- Database name.
    - name -- StoredProcedure name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb sql stored-procedure show", locals())


def delete(account_name, container_name, database_name, name, resource_group, yes=None):
    '''
    Delete the SQL stored procedure under an Azure Cosmos DB SQL container.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - container_name -- Container name.
    - database_name -- Database name.
    - name -- StoredProcedure name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az cosmosdb sql stored-procedure delete", locals())

