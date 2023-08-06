'''
Manage Azure Cosmos DB managed service identities.
'''
from ... pyaz_utils import _call_az

def show(name, resource_group):
    '''
    Show the identities for a Azure Cosmos DB database account.

    Required Parameters:
    - name -- Name of the Cosmos DB database account
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb identity show", locals())


def assign(name, resource_group, identities=None):
    '''
    Assign SystemAssigned identity for a Azure Cosmos DB database account.

    Required Parameters:
    - name -- Name of the Cosmos DB database account
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - identities -- Space-separated identities to assign. Use '[system]' to refer to the system assigned identity. Default: '[system]'
    '''
    return _call_az("az cosmosdb identity assign", locals())


def remove(name, resource_group, identities=None):
    '''
    Remove SystemAssigned identity for a Azure Cosmos DB database account.

    Required Parameters:
    - name -- Name of the Cosmos DB database account
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - identities -- Space-separated identities to remove. Use '[system]' to refer to the system assigned identity. Default: '[system]'
    '''
    return _call_az("az cosmosdb identity remove", locals())

