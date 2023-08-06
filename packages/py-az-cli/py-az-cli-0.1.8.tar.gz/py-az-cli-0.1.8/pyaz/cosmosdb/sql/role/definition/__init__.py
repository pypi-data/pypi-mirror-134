'''
Manage Azure Cosmos DB SQL role definitions.
'''
from ..... pyaz_utils import _call_az

def create(account_name, body, resource_group, no_wait=None):
    '''
    Create a SQL role definition under an Azure Cosmos DB account.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - body -- Role Definition body with Id (Optional for create), DataActions or Permissions, Type (Default is CustomRole), and AssignableScopes.  You can enter it as a string or as a file, e.g., --body @rdbody-file.json or --body "{ \"Id\": \"be79875a-2cc4-40d5-8958-566017875b39\", \"RoleName\": \"My Read Write Role\", \"Type\": \"CustomRole\", \"AssignableScopes\": [ \"/\" ], \"DataActions\": [ \"Microsoft.DocumentDB/databaseAccounts/sqlDatabases/containers/items/create\", \"Microsoft.DocumentDB/databaseAccounts/sqlDatabases/containers/items/read\" ]}"

    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az cosmosdb sql role definition create", locals())


def update(account_name, body, resource_group, no_wait=None):
    '''
    Update a SQL role definition under an Azure Cosmos DB account.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - body -- Role Definition body with Id (Optional for create), DataActions or Permissions, Type (Default is CustomRole), and AssignableScopes.  You can enter it as a string or as a file, e.g., --body @rdbody-file.json or --body "{ \"Id\": \"be79875a-2cc4-40d5-8958-566017875b39\", \"RoleName\": \"My Read Write Role\", \"Type\": \"CustomRole\", \"AssignableScopes\": [ \"/\" ], \"DataActions\": [ \"Microsoft.DocumentDB/databaseAccounts/sqlDatabases/containers/items/create\", \"Microsoft.DocumentDB/databaseAccounts/sqlDatabases/containers/items/read\" ]}"

    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az cosmosdb sql role definition update", locals())


def exists(account_name, id, resource_group):
    '''
    Check if an Azure Cosmos DB role definition exists.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - id -- Unique ID for the Role Definition.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb sql role definition exists", locals())


def list(account_name, resource_group):
    '''
    List all SQL role definitions under an Azure Cosmos DB account.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb sql role definition list", locals())


def show(account_name, id, resource_group):
    '''
    Show the properties of a SQL role definition under an Azure Cosmos DB account.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - id -- Unique ID for the Role Definition.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb sql role definition show", locals())


def delete(account_name, id, resource_group, no_wait=None, yes=None):
    '''
    Delete a SQL role definition under an Azure Cosmos DB account.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - id -- Unique ID for the Role Definition.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az cosmosdb sql role definition delete", locals())


def wait(account_name, id, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Poll on a SQL role definition until a specific condition is met.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - id -- Unique ID for the Role Definition.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az cosmosdb sql role definition wait", locals())

