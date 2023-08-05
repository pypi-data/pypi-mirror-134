from .... pyaz_utils import _call_az

def add(external_mappings, gateway_name, internal_mappings, name, resource_group, ip_config_id=None, mode=None, no_wait=None, type=None):
    '''
    Add nat rule in a virtual network gateway

    Required Parameters:
    - external_mappings -- The private IP address external mapping for NAT.
    - gateway_name -- Virtual network gateway name
    - internal_mappings -- The private IP address internal mapping for NAT.
    - name -- The name of the resource that is unique within a resource group. This name can be used to access the resource.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - ip_config_id -- The IP Configuration ID this NAT rule applies to.
    - mode -- The Source NAT direction of a VPN NAT.
    - no_wait -- Do not wait for the long-running operation to finish.
    - type -- The type of NAT rule for VPN NAT.
    '''
    return _call_az("az network vnet-gateway nat-rule add", locals())


def list(gateway_name, resource_group):
    '''
    List nat rule for a virtual network gateway

    Required Parameters:
    - gateway_name -- Virtual network gateway name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network vnet-gateway nat-rule list", locals())


def remove(gateway_name, name, resource_group, no_wait=None):
    '''
    Remove nat rule from a virtual network gateway

    Required Parameters:
    - gateway_name -- Virtual network gateway name
    - name -- The name of the resource that is unique within a resource group. This name can be used to access the resource.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network vnet-gateway nat-rule remove", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the vnet gateway nat rule is met.

    Required Parameters:
    - name -- Name of the VNet gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az network vnet-gateway nat-rule wait", locals())

