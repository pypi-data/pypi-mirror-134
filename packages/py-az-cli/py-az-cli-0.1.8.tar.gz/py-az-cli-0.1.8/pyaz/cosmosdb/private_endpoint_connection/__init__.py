from ... pyaz_utils import _call_az

def approve(account_name=None, description=None, id=None, name=None, resource_group=None):
    '''
    Approve the specified private endpoint connection associated with Azure Cosmos DB.

    Optional Parameters:
    - account_name -- Name of the Cosmos DB database account. Required if --connection-id is not specified
    - description -- Comments for the approve operation.
    - id -- The ID of the private endpoint connection associated with Azure Cosmos DB. If specified --account-name --resource-group/-g and --name/-n, this should be omitted.
    - name -- The name of the private endpoint connection associated with Azure Cosmos DB. Required if --connection-id is not specified
    - resource_group -- The resource group name of specified Cosmos DB account. Required if --connection-id is not specified
    '''
    return _call_az("az cosmosdb private-endpoint-connection approve", locals())


def reject(account_name=None, description=None, id=None, name=None, resource_group=None):
    '''
    Reject the specified private endpoint connection associated with Azure Cosmos DB.

    Optional Parameters:
    - account_name -- Name of the Cosmos DB database account. Required if --connection-id is not specified
    - description -- Comments for the reject operation.
    - id -- The ID of the private endpoint connection associated with Azure Cosmos DB. If specified --account-name --resource-group/-g and --name/-n, this should be omitted.
    - name -- The name of the private endpoint connection associated with Azure Cosmos DB. Required if --connection-id is not specified
    - resource_group -- The resource group name of specified Cosmos DB account. Required if --connection-id is not specified
    '''
    return _call_az("az cosmosdb private-endpoint-connection reject", locals())


def delete(account_name=None, id=None, name=None, resource_group=None):
    '''
    Delete the specified private endpoint connection associated with Azure Cosmos DB.

    Optional Parameters:
    - account_name -- Name of the Cosmos DB database account. Required if --connection-id is not specified
    - id -- The ID of the private endpoint connection associated with Azure Cosmos DB. If specified --account-name --resource-group/-g and --name/-n, this should be omitted.
    - name -- The name of the private endpoint connection associated with Azure Cosmos DB. Required if --connection-id is not specified
    - resource_group -- The resource group name of specified Cosmos DB account. Required if --connection-id is not specified
    '''
    return _call_az("az cosmosdb private-endpoint-connection delete", locals())


def show(account_name=None, id=None, name=None, resource_group=None):
    '''
    Show details of a private endpoint connection associated with Azure Cosmos DB.

    Optional Parameters:
    - account_name -- Name of the Cosmos DB database account. Required if --connection-id is not specified
    - id -- The ID of the private endpoint connection associated with Azure Cosmos DB. If specified --account-name --resource-group/-g and --name/-n, this should be omitted.
    - name -- The name of the private endpoint connection associated with Azure Cosmos DB. Required if --connection-id is not specified
    - resource_group -- The resource group name of specified Cosmos DB account. Required if --connection-id is not specified
    '''
    return _call_az("az cosmosdb private-endpoint-connection show", locals())

