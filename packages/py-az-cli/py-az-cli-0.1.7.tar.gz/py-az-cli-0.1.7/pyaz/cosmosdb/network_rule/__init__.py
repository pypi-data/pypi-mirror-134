from ... pyaz_utils import _call_az

def list(name, resource_group):
    '''
    

    Required Parameters:
    - name -- Name of the Cosmos DB database account
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb network-rule list", locals())


def add(name, resource_group, subnet, ignore_missing_endpoint=None, vnet_name=None):
    '''
    

    Required Parameters:
    - name -- Name of the Cosmos DB database account
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - subnet -- Name or ID of the subnet

    Optional Parameters:
    - ignore_missing_endpoint -- Create firewall rule before the virtual network has vnet service endpoint enabled.
    - vnet_name -- The name of the VNET, which must be provided in conjunction with the name of the subnet
    '''
    return _call_az("az cosmosdb network-rule add", locals())


def remove(name, resource_group, subnet, vnet_name=None):
    '''
    

    Required Parameters:
    - name -- Name of the Cosmos DB database account
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - subnet -- Name or ID of the subnet

    Optional Parameters:
    - vnet_name -- The name of the VNET, which must be provided in conjunction with the name of the subnet
    '''
    return _call_az("az cosmosdb network-rule remove", locals())

