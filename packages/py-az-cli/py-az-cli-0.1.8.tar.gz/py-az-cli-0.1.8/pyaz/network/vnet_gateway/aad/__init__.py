from .... pyaz_utils import _call_az

def assign(audience, gateway_name, issuer, resource_group, tenant, no_wait=None):
    '''
    Assign/Update AAD(Azure Active Directory) authentication to a virtual network gateway.

    Required Parameters:
    - audience -- The AADAudience ID of the VirtualNetworkGateway.
    - gateway_name -- Virtual network gateway name
    - issuer -- The AADIssuer URI of the VirtualNetworkGateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - tenant -- The AADTenant URI of the VirtualNetworkGateway.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network vnet-gateway aad assign", locals())


def show(gateway_name, resource_group):
    '''
    Show AAD(Azure Active Directory) authentication of a virtual network gateway

    Required Parameters:
    - gateway_name -- Virtual network gateway name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network vnet-gateway aad show", locals())


def remove(gateway_name, resource_group, no_wait=None):
    '''
    Remove AAD(Azure Active Directory) authentication from a virtual network gateway

    Required Parameters:
    - gateway_name -- Virtual network gateway name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network vnet-gateway aad remove", locals())

