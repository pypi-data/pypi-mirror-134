from ... pyaz_utils import _call_az

def add(name, ip_address=None, no_wait=None, resource_group=None, subnet=None, vnet_name=None):
    '''
    

    Required Parameters:
    - name -- Name of the Vault.

    Optional Parameters:
    - ip_address -- IPv4 address or CIDR range. Can supply a list: --ip-address ip1 [ip2]...
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- Proceed only if Key Vault belongs to the specified resource group.
    - subnet -- Name or ID of subnet. If name is supplied, `--vnet-name` must be supplied.
    - vnet_name -- Name of a virtual network.
    '''
    return _call_az("az keyvault network-rule add", locals())


def remove(name, ip_address=None, no_wait=None, resource_group=None, subnet=None, vnet_name=None):
    '''
    

    Required Parameters:
    - name -- Name of the Vault.

    Optional Parameters:
    - ip_address -- IPv4 address or CIDR range.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- Proceed only if Key Vault belongs to the specified resource group.
    - subnet -- Name or ID of subnet. If name is supplied, `--vnet-name` must be supplied.
    - vnet_name -- Name of a virtual network.
    '''
    return _call_az("az keyvault network-rule remove", locals())


def list(name, resource_group=None):
    '''
    

    Required Parameters:
    - name -- Name of the Vault.

    Optional Parameters:
    - resource_group -- Proceed only if Key Vault belongs to the specified resource group.
    '''
    return _call_az("az keyvault network-rule list", locals())


def wait(name, created=None, custom=None, deleted=None, exists=None, interval=None, resource_group=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the vault is met.

    Required Parameters:
    - name -- Name of the Vault.

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - resource_group -- Proceed only if Key Vault belongs to the specified resource group.
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az keyvault network-rule wait", locals())

