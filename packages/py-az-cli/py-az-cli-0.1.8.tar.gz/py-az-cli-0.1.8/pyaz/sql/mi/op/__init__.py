'''
Manage operations on a managed instance.
'''
from .... pyaz_utils import _call_az

def list(managed_instance, resource_group):
    '''
    

    Required Parameters:
    - managed_instance -- Name of the Azure SQL Managed Instance.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql mi op list", locals())


def show(managed_instance, name, resource_group):
    '''
    

    Required Parameters:
    - managed_instance -- Name of the Azure SQL Managed Instance.
    - name -- The unique name of the operation to show.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql mi op show", locals())


def cancel(managed_instance, name, resource_group):
    '''
    

    Required Parameters:
    - managed_instance -- Name of the Azure SQL Managed Instance.
    - name -- The unique name of the operation to cancel.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql mi op cancel", locals())

