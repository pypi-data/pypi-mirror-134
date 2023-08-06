'''
Manage sensitivity classifications.
'''
from .... pyaz_utils import _call_az
from . import recommendation


def list(name, resource_group, server, count=None, filter=None, skip_token=None):
    '''
    Get the sensitivity classifications of a given database.

    Required Parameters:
    - name -- Name of the Azure SQL Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`

    Optional Parameters:
    - count -- 
    - filter -- An OData filter expression that filters elements in the collection.
    - skip_token -- 
    '''
    return _call_az("az sql db classification list", locals())


def show(column, name, resource_group, schema, server, table):
    '''
    Get the sensitivity classification of a given column.

    Required Parameters:
    - column -- The name of the column.
    - name -- Name of the Azure SQL Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - schema -- The name of the schema.
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    - table -- The name of the table.
    '''
    return _call_az("az sql db classification show", locals())


def delete(column, name, resource_group, schema, server, table):
    '''
    Delete the sensitivity classification of a given column.

    Required Parameters:
    - column -- The name of the column.
    - name -- Name of the Azure SQL Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - schema -- The name of the schema.
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    - table -- The name of the table.
    '''
    return _call_az("az sql db classification delete", locals())


def update(column, name, resource_group, schema, server, table, information_type=None, label=None):
    '''
    Update a columns's sensitivity classification.

    Required Parameters:
    - column -- The name of the column.
    - name -- Name of the Azure SQL Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - schema -- The name of the schema.
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    - table -- The name of the table.

    Optional Parameters:
    - information_type -- The information type.
    - label -- The label name.
    '''
    return _call_az("az sql db classification update", locals())

