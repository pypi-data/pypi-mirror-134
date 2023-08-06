from .... pyaz_utils import _call_az

def disable(name, resource_group):
    '''
    Disable Azure Active Directly only Authentication for this Server.

    Required Parameters:
    - name -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql server ad-only-auth disable", locals())


def enable(name, resource_group):
    '''
    Enable Azure Active Directly only Authentication for this Server.

    Required Parameters:
    - name -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql server ad-only-auth enable", locals())


def get(name, resource_group):
    '''
    Get a specific Azure Active Directly only Authentication property.

    Required Parameters:
    - name -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql server ad-only-auth get", locals())

