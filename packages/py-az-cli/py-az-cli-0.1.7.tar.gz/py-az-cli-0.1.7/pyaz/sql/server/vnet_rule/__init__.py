from .... pyaz_utils import _call_az

def create(name, resource_group, server, subnet, ignore_missing_endpoint=None, vnet_name=None):
    '''
    Create a virtual network rule to allows access to an Azure SQL server.

    Required Parameters:
    - name -- The name of the virtual network rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    - subnet -- Name or ID of the subnet that allows access to an Azure Sql Server. If subnet name is provided, --vnet-name must be provided.

    Optional Parameters:
    - ignore_missing_endpoint -- Create firewall rule before the virtual network has vnet service endpoint enabled
    - vnet_name -- The virtual network name
    '''
    return _call_az("az sql server vnet-rule create", locals())


def show(name, resource_group, server):
    '''
    

    Required Parameters:
    - name -- The name of the virtual network rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql server vnet-rule show", locals())


def list(resource_group, server):
    '''
    

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql server vnet-rule list", locals())


def delete(name, resource_group, server):
    '''
    

    Required Parameters:
    - name -- The name of the virtual network rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql server vnet-rule delete", locals())


def update(name, resource_group, server, subnet, ignore_missing_endpoint=None):
    '''
    Update a virtual network rule.

    Required Parameters:
    - name -- The name of the virtual network rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    - subnet -- Name or ID of the subnet that allows access to an Azure Sql Server. If subnet name is provided, --vnet-name must be provided.

    Optional Parameters:
    - ignore_missing_endpoint -- Create firewall rule before the virtual network has vnet service endpoint enabled
    '''
    return _call_az("az sql server vnet-rule update", locals())

