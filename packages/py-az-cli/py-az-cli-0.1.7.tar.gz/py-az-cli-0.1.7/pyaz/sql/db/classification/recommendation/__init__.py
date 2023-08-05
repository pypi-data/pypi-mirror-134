'''
Manage sensitivity classification recommendations.
'''
from ..... pyaz_utils import _call_az

def list(name, resource_group, server, filter=None, include_disabled_recommendations=None):
    '''
    List the recommended sensitivity classifications of a given database.

    Required Parameters:
    - name -- Name of the Azure SQL Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`

    Optional Parameters:
    - filter -- An OData filter expression that filters elements in the collection.
    - include_disabled_recommendations -- Specifies whether to include disabled recommendations or not.
    '''
    return _call_az("az sql db classification recommendation list", locals())


def enable(column, name, resource_group, schema, server, table):
    '''
    Enable sensitivity recommendations for a given column (recommendations are enabled by default on all columns).

    Required Parameters:
    - column -- The name of the column.
    - name -- Name of the Azure SQL Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - schema -- The name of the schema.
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    - table -- The name of the table.
    '''
    return _call_az("az sql db classification recommendation enable", locals())


def disable(column, name, resource_group, schema, server, table):
    '''
    Disable sensitivity recommendations for a given column (recommendations are enabled by default on all columns).

    Required Parameters:
    - column -- The name of the column.
    - name -- Name of the Azure SQL Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - schema -- The name of the schema.
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    - table -- The name of the table.
    '''
    return _call_az("az sql db classification recommendation disable", locals())

