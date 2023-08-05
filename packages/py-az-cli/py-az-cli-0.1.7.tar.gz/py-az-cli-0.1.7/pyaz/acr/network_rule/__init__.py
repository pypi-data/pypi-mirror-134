from ... pyaz_utils import _call_az

def list(name, resource_group=None):
    '''
    List network rules.

    Required Parameters:
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr network-rule list", locals())


def add(name, ip_address=None, resource_group=None, subnet=None, vnet_name=None):
    '''
    Add a network rule.

    Required Parameters:
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - ip_address -- IPv4 address or CIDR range.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - subnet -- Name or ID of subnet. If name is supplied, `--vnet-name` must be supplied.
    - vnet_name -- Name of a virtual network.
    '''
    return _call_az("az acr network-rule add", locals())


def remove(name, ip_address=None, resource_group=None, subnet=None, vnet_name=None):
    '''
    Remove a network rule.

    Required Parameters:
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - ip_address -- IPv4 address or CIDR range.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - subnet -- Name or ID of subnet. If name is supplied, `--vnet-name` must be supplied.
    - vnet_name -- Name of a virtual network.
    '''
    return _call_az("az acr network-rule remove", locals())

