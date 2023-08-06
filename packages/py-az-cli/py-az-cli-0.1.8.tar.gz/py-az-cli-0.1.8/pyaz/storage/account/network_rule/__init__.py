from .... pyaz_utils import _call_az

def add(account_name, action=None, ip_address=None, resource_group=None, resource_id=None, subnet=None, tenant_id=None, vnet_name=None):
    '''
    Add a network rule.

    Required Parameters:
    - account_name -- The storage account name.

    Optional Parameters:
    - action -- The action of virtual network rule. Possible value is Allow.
    - ip_address -- IPv4 address or CIDR range.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_id -- The resource id to add in network rule.
    - subnet -- Name or ID of subnet. If name is supplied, `--vnet-name` must be supplied.
    - tenant_id -- The tenant id to add in network rule.
    - vnet_name -- Name of a virtual network.
    '''
    return _call_az("az storage account network-rule add", locals())


def list(account_name, resource_group=None):
    '''
    List network rules.

    Required Parameters:
    - account_name -- The storage account name.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage account network-rule list", locals())


def remove(account_name, ip_address=None, resource_group=None, resource_id=None, subnet=None, tenant_id=None, vnet_name=None):
    '''
    Remove a network rule.

    Required Parameters:
    - account_name -- The storage account name.

    Optional Parameters:
    - ip_address -- IPv4 address or CIDR range.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_id -- The resource id to add in network rule.
    - subnet -- Name or ID of subnet. If name is supplied, `--vnet-name` must be supplied.
    - tenant_id -- The tenant id to add in network rule.
    - vnet_name -- Name of a virtual network.
    '''
    return _call_az("az storage account network-rule remove", locals())

