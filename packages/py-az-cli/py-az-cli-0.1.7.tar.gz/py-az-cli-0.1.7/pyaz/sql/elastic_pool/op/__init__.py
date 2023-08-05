from .... pyaz_utils import _call_az

def list(elastic_pool, resource_group, server):
    '''
    

    Required Parameters:
    - elastic_pool -- Name of the Azure SQL Elastic Pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql elastic-pool op list", locals())


def cancel(elastic_pool, name, resource_group, server):
    '''
    

    Required Parameters:
    - elastic_pool -- Name of the Azure SQL Elastic Pool.
    - name -- The unique name of the operation to cancel.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql elastic-pool op cancel", locals())

