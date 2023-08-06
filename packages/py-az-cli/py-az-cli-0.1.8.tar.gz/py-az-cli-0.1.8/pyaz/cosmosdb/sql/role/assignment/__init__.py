'''
Manage Azure Cosmos DB SQL role assignments.
'''
from ..... pyaz_utils import _call_az

def create(account_name, principal_id, resource_group, scope, no_wait=None, role_assignment_id=None, role_definition_id=None, role_definition_name=None):
    '''
    Create a SQL role assignment under an Azure Cosmos DB account.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - principal_id -- AAD Object ID of the principal to which this Role Assignment is being granted.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - scope -- Data plane resource path at which this Role Assignment is being granted.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - role_assignment_id -- Optional for Create. Unique ID for the Role Assignment. If not provided, a new GUID will be used.
    - role_definition_id -- Unique ID of the Role Definition that this Role Assignment refers to.
    - role_definition_name -- Unique Name of the Role Definition that this Role Assignment refers to. Eg. 'Contoso Reader Role'.
    '''
    return _call_az("az cosmosdb sql role assignment create", locals())


def update(account_name, resource_group, role_assignment_id, no_wait=None, principal_id=None, role_definition_id=None, role_definition_name=None, scope=None):
    '''
    Update a SQL role assignment under an Azure Cosmos DB account.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - role_assignment_id -- Optional for Create. Unique ID for the Role Assignment. If not provided, a new GUID will be used.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - principal_id -- AAD Object ID of the principal to which this Role Assignment is being granted.
    - role_definition_id -- Unique ID of the Role Definition that this Role Assignment refers to.
    - role_definition_name -- Unique Name of the Role Definition that this Role Assignment refers to. Eg. 'Contoso Reader Role'.
    - scope -- Data plane resource path at which this Role Assignment is being granted.
    '''
    return _call_az("az cosmosdb sql role assignment update", locals())


def exists(account_name, resource_group, role_assignment_id):
    '''
    Check if an Azure Cosmos DB role assignment exists.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - role_assignment_id -- Optional for Create. Unique ID for the Role Assignment. If not provided, a new GUID will be used.
    '''
    return _call_az("az cosmosdb sql role assignment exists", locals())


def list(account_name, resource_group):
    '''
    List all SQL role assignments under an Azure Cosmos DB account.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb sql role assignment list", locals())


def show(account_name, resource_group, role_assignment_id):
    '''
    Show the properties of a SQL role assignment under an Azure Cosmos DB account.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - role_assignment_id -- Optional for Create. Unique ID for the Role Assignment. If not provided, a new GUID will be used.
    '''
    return _call_az("az cosmosdb sql role assignment show", locals())


def delete(account_name, resource_group, role_assignment_id, no_wait=None, yes=None):
    '''
    Delete a SQL role assignment under an Azure Cosmos DB account.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - role_assignment_id -- Optional for Create. Unique ID for the Role Assignment. If not provided, a new GUID will be used.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az cosmosdb sql role assignment delete", locals())


def wait(account_name, resource_group, role_assignment_id, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Poll on a SQL role assignment until a specific condition is met.

    Required Parameters:
    - account_name -- Cosmosdb account name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - role_assignment_id -- Optional for Create. Unique ID for the Role Assignment. If not provided, a new GUID will be used.

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az cosmosdb sql role assignment wait", locals())

