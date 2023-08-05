from ..... pyaz_utils import _call_az

def set(dh_group, ike_encryption, ike_integrity, ipsec_encryption, ipsec_integrity, name, pfs_group, resource_group, sa_lifetime, sa_max_size, no_wait=None):
    '''
    Set the VPN client connection ipsec policy per P2S client connection of the virtual network gateway.

    Required Parameters:
    - dh_group -- The DH Groups used for initial SA.
    - ike_encryption -- The IKE encryption algorithm.
    - ike_integrity -- The IKE integrity algorithm.
    - ipsec_encryption -- The IPSec encryption algorithm.
    - ipsec_integrity -- The IPSec integrity algorithm.
    - name -- Name of the VNet gateway.
    - pfs_group -- The Pfs Groups used for new child SA.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sa_lifetime -- The lifetime in seconds for P2S client.
    - sa_max_size -- The payload size in KB for P2S client.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network vnet-gateway vpn-client ipsec-policy set", locals())


def show(name, resource_group):
    '''
    Get the VPN client connection ipsec policy per P2S client connection of the virtual network gateway.

    Required Parameters:
    - name -- Name of the VNet gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network vnet-gateway vpn-client ipsec-policy show", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the vnet gateway vpn client ipsec policy is met.

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
    return _call_az("az network vnet-gateway vpn-client ipsec-policy wait", locals())

