from .... pyaz_utils import _call_az

def show(resource_group, server):
    '''
    Gets a server's secure connection policy.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql server conn-policy show", locals())


def update(connection_type, resource_group, server):
    '''
    Updates a server's secure connection policy.

    Required Parameters:
    - connection_type -- The required parameters for updating a secure connection policy. The value is default
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql server conn-policy update", locals())

