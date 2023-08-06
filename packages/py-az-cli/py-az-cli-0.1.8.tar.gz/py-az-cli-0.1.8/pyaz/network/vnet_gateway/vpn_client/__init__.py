from .... pyaz_utils import _call_az
from . import ipsec_policy


def generate(name, resource_group, authentication_method=None, client_root_certificates=None, processor_architecture=None, radius_server_auth_certificate=None, use_legacy=None):
    '''
    Generate VPN client configuration.

    Required Parameters:
    - name -- Name of the VNet gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - authentication_method -- Method used to authenticate with the generated client.
    - client_root_certificates -- Space-separated list of client root certificate public certificate data in Base-64 format. Optional for external Radius-based auth with EAPTLS
    - processor_architecture -- Processor architecture of the target system.
    - radius_server_auth_certificate -- Public certificate data for the Radius server auth certificate in Base-64 format. Required only if external Radius auth has been configured with EAPTLS auth.
    - use_legacy -- Generate VPN client package using legacy implementation.
    '''
    return _call_az("az network vnet-gateway vpn-client generate", locals())


def show_url(name, resource_group):
    '''
    Retrieve a pre-generated VPN client configuration.

    Required Parameters:
    - name -- Name of the VNet gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network vnet-gateway vpn-client show-url", locals())


def show_health(name, resource_group):
    '''
    Get the VPN client connection health detail per P2S client connection of the virtual network gateway.

    Required Parameters:
    - name -- Name of the VNet gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network vnet-gateway vpn-client show-health", locals())

