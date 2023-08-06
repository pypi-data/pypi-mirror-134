from .... pyaz_utils import _call_az

def show(name, resource_group, server):
    '''
    

    Required Parameters:
    - name -- Name of the DNS alias.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql server dns-alias show", locals())


def list(resource_group, server):
    '''
    

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql server dns-alias list", locals())


def create(name, resource_group, server):
    '''
    

    Required Parameters:
    - name -- Name of the DNS alias.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql server dns-alias create", locals())


def delete(name, resource_group, server):
    '''
    

    Required Parameters:
    - name -- Name of the DNS alias.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql server dns-alias delete", locals())


def set(name, original_server, resource_group, server, original_resource_group=None, original_subscription_id=None):
    '''
    Sets a server to which DNS alias should point

    Required Parameters:
    - name -- Name of the DNS alias.
    - original_server -- The name of the server to which alias is currently pointing
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`

    Optional Parameters:
    - original_resource_group -- Name of the original resource group.
    - original_subscription_id -- ID of the original subscription.
    '''
    return _call_az("az sql server dns-alias set", locals())

