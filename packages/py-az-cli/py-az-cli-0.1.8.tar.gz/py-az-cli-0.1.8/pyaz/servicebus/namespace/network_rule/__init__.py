from .... pyaz_utils import _call_az

def add(namespace_name, resource_group, action=None, ignore_missing_endpoint=None, ip_address=None, subnet=None, vnet_name=None):
    '''
    Add a network rule for a namespace.

    Required Parameters:
    - namespace_name -- Name of the Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - action -- Action of the IP rule
    - ignore_missing_endpoint -- A boolean value that indicates whether to ignore missing vnet Service Endpoint
    - ip_address -- IPv4 address or CIDR range.
    - subnet -- Name or ID of subnet. If name is supplied, `--vnet-name` must be supplied.
    - vnet_name -- Name of the Virtual Network
    '''
    return _call_az("az servicebus namespace network-rule add", locals())


def list(namespace_name, resource_group):
    '''
    Show properties of Network rule of the given Namespace.

    Required Parameters:
    - namespace_name -- Name of the Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az servicebus namespace network-rule list", locals())


def remove(namespace_name, resource_group, ip_address=None, subnet=None, vnet_name=None):
    '''
    Remove network rule for a namespace

    Required Parameters:
    - namespace_name -- Name of the Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - ip_address -- IPv4 address or CIDR range.
    - subnet -- Name or ID of subnet. If name is supplied, `--vnet-name` must be supplied.
    - vnet_name -- Name of the Virtual Network
    '''
    return _call_az("az servicebus namespace network-rule remove", locals())

