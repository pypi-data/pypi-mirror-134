from .... pyaz_utils import _call_az

def add(dh_group, gateway_name, ike_encryption, ike_integrity, ipsec_encryption, ipsec_integrity, pfs_group, resource_group, sa_lifetime, sa_max_size, no_wait=None):
    '''
    Add a virtual network gateway IPSec policy.

    Required Parameters:
    - dh_group -- The DH Groups used for initial SA.
    - gateway_name -- Virtual network gateway name
    - ike_encryption -- The IKE encryption algorithm.
    - ike_integrity -- The IKE integrity algorithm.
    - ipsec_encryption -- The IPSec encryption algorithm.
    - ipsec_integrity -- The IPSec integrity algorithm.
    - pfs_group -- The Pfs Groups used for new child SA.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sa_lifetime -- The lifetime in seconds for P2S client.
    - sa_max_size -- The payload size in KB for P2S client.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network vnet-gateway ipsec-policy add", locals())


def list(gateway_name, resource_group):
    '''
    List IPSec policies associated with a virtual network gateway.

    Required Parameters:
    - gateway_name -- Virtual network gateway name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network vnet-gateway ipsec-policy list", locals())


def clear(gateway_name, resource_group, no_wait=None):
    '''
    Delete all IPsec policies on a virtual network gateway.

    Required Parameters:
    - gateway_name -- Virtual network gateway name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network vnet-gateway ipsec-policy clear", locals())

