'''
Manage a database's transparent data encryption.
'''
from .... pyaz_utils import _call_az

def set(database, resource_group, server, status):
    '''
    Sets a database's transparent data encryption configuration.

    Required Parameters:
    - database -- Name of the Azure SQL Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    - status -- Status of the transparent data encryption.
    '''
    return _call_az("az sql db tde set", locals())


def show(database, resource_group, server):
    '''
    

    Required Parameters:
    - database -- Name of the Azure SQL Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql db tde show", locals())


def list_activity(database, resource_group, server):
    '''
    

    Required Parameters:
    - database -- Name of the Azure SQL Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql db tde list-activity", locals())

