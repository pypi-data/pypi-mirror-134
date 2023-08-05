from ..... pyaz_utils import _call_az

def add(inbound_nat_rule, ip_config_name, nic_name, resource_group, lb_name=None):
    '''
    Add an inbound NAT rule to an IP configuration.

    Required Parameters:
    - inbound_nat_rule -- The name or ID of an existing inbound NAT rule.
    - ip_config_name -- The name of the IP configuration.
    - nic_name -- The network interface (NIC).
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - lb_name -- The name of the load balancer associated with the NAT rule (Omit if suppying a NAT rule ID).
    '''
    return _call_az("az network nic ip-config inbound-nat-rule add", locals())


def remove(inbound_nat_rule, ip_config_name, nic_name, resource_group, lb_name=None):
    '''
    Remove an inbound NAT rule of an IP configuration.

    Required Parameters:
    - inbound_nat_rule -- The name or ID of an existing inbound NAT rule.
    - ip_config_name -- The name of the IP configuration.
    - nic_name -- The network interface (NIC).
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - lb_name -- The name of the load balancer associated with the NAT rule (Omit if suppying a NAT rule ID).
    '''
    return _call_az("az network nic ip-config inbound-nat-rule remove", locals())

