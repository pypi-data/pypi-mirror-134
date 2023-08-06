'''
Manage sensitivity classification recommendations.
'''
from ...... pyaz_utils import _call_az

def list(name, resource_group, workspace_name, filter=None, included_disabled=None, skip_token=None):
    '''
    List the recommended sensitivity classifications of a given SQL pool.

    Required Parameters:
    - name -- The SQL pool name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.

    Optional Parameters:
    - filter -- An OData filter expression that filters elements in the collection.
    - included_disabled -- Indicates whether the result should include disabled recommendations
    - skip_token -- An OData query option to indicate how many elements to skip in the collection.
    '''
    return _call_az("az synapse sql pool classification recommendation list", locals())


def enable(column, name, resource_group, schema, table, workspace_name):
    '''
    Enable sensitivity recommendations for a given column(recommendations are enabled by default on all columns).

    Required Parameters:
    - column -- The name of column.
    - name -- The SQL pool name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - schema -- The name of schema.
    - table -- The name of table.
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse sql pool classification recommendation enable", locals())


def disable(column, name, resource_group, schema, table, workspace_name):
    '''
    Disable sensitivity recommendations for a given column(recommendations are enabled by default on all columns).

    Required Parameters:
    - column -- The name of column.
    - name -- The SQL pool name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - schema -- The name of schema.
    - table -- The name of table.
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse sql pool classification recommendation disable", locals())

