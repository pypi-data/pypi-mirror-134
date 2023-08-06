'''
Manage sensitivity classifications.
'''
from ..... pyaz_utils import _call_az
from . import recommendation


def show(column, name, resource_group, schema, table, workspace_name):
    '''
    Get the sensitivity classification of a given column.

    Required Parameters:
    - column -- The name of column.
    - name -- The SQL pool name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - schema -- The name of schema.
    - table -- The name of table.
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse sql pool classification show", locals())


def list(name, resource_group, workspace_name, filter=None):
    '''
    Get the sensitivity classifications of a given SQL pool.

    Required Parameters:
    - name -- The SQL pool name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.

    Optional Parameters:
    - filter -- An OData filter expression that filters elements in the collection.
    '''
    return _call_az("az synapse sql pool classification list", locals())


def create(column, information_type, label, name, resource_group, schema, table, workspace_name):
    '''
    Create a column's sensitivity classification.

    Required Parameters:
    - column -- The name of column.
    - information_type -- The information type.
    - label -- The label name.
    - name -- The SQL pool name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - schema -- The name of schema.
    - table -- The name of table.
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse sql pool classification create", locals())


def delete(column, name, resource_group, schema, table, workspace_name):
    '''
    Delete the sensitivity classification of a given column.

    Required Parameters:
    - column -- The name of column.
    - name -- The SQL pool name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - schema -- The name of schema.
    - table -- The name of table.
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse sql pool classification delete", locals())


def update(column, name, resource_group, schema, table, workspace_name, information_type=None, label=None):
    '''
    Update a column's sensitivity classification.

    Required Parameters:
    - column -- The name of column.
    - name -- The SQL pool name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - schema -- The name of schema.
    - table -- The name of table.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - information_type -- The information type.
    - label -- The label name.
    '''
    return _call_az("az synapse sql pool classification update", locals())

