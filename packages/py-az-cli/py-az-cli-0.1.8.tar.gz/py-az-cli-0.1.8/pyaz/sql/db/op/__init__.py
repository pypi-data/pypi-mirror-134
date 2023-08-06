'''
Manage operations on a database.
'''
from .... pyaz_utils import _call_az

def list(database, resource_group, server):
    '''
    

    Required Parameters:
    - database -- Name of the Azure SQL Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql db op list", locals())


def cancel(database, name, resource_group, server):
    '''
    

    Required Parameters:
    - database -- Name of the Azure SQL Database.
    - name -- The unique name of the operation to cancel.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql db op cancel", locals())

