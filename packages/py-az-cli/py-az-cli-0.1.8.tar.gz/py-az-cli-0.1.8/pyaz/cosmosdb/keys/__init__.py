'''
Manage Azure Cosmos DB keys.
'''
from ... pyaz_utils import _call_az

def list(name, resource_group, type=None):
    '''
    List the access keys or connection strings for a Azure Cosmos DB database account.

    Required Parameters:
    - name -- Cosmosdb account name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - type -- The type of account key.
    '''
    return _call_az("az cosmosdb keys list", locals())


def regenerate(key_kind, name, resource_group):
    '''
    Regenerate an access key for a Azure Cosmos DB database account.

    Required Parameters:
    - key_kind -- The access key to regenerate.
    - name -- Name of the Cosmos DB database account
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb keys regenerate", locals())

