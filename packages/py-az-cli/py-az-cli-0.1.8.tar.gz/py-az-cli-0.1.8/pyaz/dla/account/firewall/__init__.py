'''
Manage Data Lake Analytics account firewall rules.
'''
from .... pyaz_utils import _call_az

def create(account, end_ip_address, firewall_rule_name, start_ip_address, resource_group=None):
    '''
    Create a firewall rule in a Data Lake Analytics account.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - end_ip_address -- None
    - firewall_rule_name -- None
    - start_ip_address -- None

    Optional Parameters:
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Analytics account.
    '''
    return _call_az("az dla account firewall create", locals())


def update(account, firewall_rule_name, end_ip_address=None, resource_group=None, start_ip_address=None):
    '''
    Update a firewall rule in a Data Lake Analytics account.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - firewall_rule_name -- The name of the firewall rule to update.

    Optional Parameters:
    - end_ip_address -- the end IP address for the firewall rule. This can be either ipv4 or ipv6. Start and End should be in the same protocol.
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Analytics account.
    - start_ip_address -- the start IP address for the firewall rule. This can be either ipv4 or ipv6. Start and End should be in the same protocol.
    '''
    return _call_az("az dla account firewall update", locals())


def list(account, resource_group=None):
    '''
    List firewall rules in a Data Lake Analytics account.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.

    Optional Parameters:
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Analytics account.
    '''
    return _call_az("az dla account firewall list", locals())


def show(account, firewall_rule_name, resource_group=None):
    '''
    Retrieve a firewall rule in a Data Lake Analytics account.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - firewall_rule_name -- The name of the firewall rule to retrieve.

    Optional Parameters:
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Analytics account.
    '''
    return _call_az("az dla account firewall show", locals())


def delete(account, firewall_rule_name, resource_group=None):
    '''
    Delete a firewall rule in a Data Lake Analytics account.

    Required Parameters:
    - account -- Name of the Data Lake Analytics account.
    - firewall_rule_name -- The name of the firewall rule to delete.

    Optional Parameters:
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Analytics account.
    '''
    return _call_az("az dla account firewall delete", locals())

