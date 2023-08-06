from ... pyaz_utils import _call_az

def list(account_name, resource_group):
    '''
    List the private link resources supported for Azure Cosmos DB.

    Required Parameters:
    - account_name -- Cosmosdb account name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb private-link-resource list", locals())

