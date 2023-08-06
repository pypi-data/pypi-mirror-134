from .... pyaz_utils import _call_az

def add(name, resource_group, ip_address=None, subnet=None, vnet_name=None):
    '''
    Add a network rule.

    Required Parameters:
    - name -- cognitive service account name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - ip_address -- IPv4 address or CIDR range.
    - subnet -- Name or ID of subnet. If name is supplied, `--vnet-name` must be supplied.
    - vnet_name -- Name of a virtual network.
    '''
    return _call_az("az cognitiveservices account network-rule add", locals())


def list(name, resource_group):
    '''
    List network rules.

    Required Parameters:
    - name -- cognitive service account name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cognitiveservices account network-rule list", locals())


def remove(name, resource_group, ip_address=None, subnet=None, vnet_name=None):
    '''
    Remove a network rule.

    Required Parameters:
    - name -- cognitive service account name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - ip_address -- IPv4 address or CIDR range.
    - subnet -- Name or ID of subnet. If name is supplied, `--vnet-name` must be supplied.
    - vnet_name -- Name of a virtual network.
    '''
    return _call_az("az cognitiveservices account network-rule remove", locals())

