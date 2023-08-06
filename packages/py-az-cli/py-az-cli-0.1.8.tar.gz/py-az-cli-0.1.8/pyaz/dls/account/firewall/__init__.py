'''
Manage Data Lake Store account firewall rules.
'''
from .... pyaz_utils import _call_az

def create(account, end_ip_address, firewall_rule_name, start_ip_address, resource_group=None):
    '''
    Creates a firewall rule in a Data Lake Store account.

    Required Parameters:
    - account -- Name of the Data Lake Store account.
    - end_ip_address -- None
    - firewall_rule_name -- None
    - start_ip_address -- None

    Optional Parameters:
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Store account.
    '''
    return _call_az("az dls account firewall create", locals())


def update(account, firewall_rule_name, end_ip_address=None, resource_group=None, start_ip_address=None):
    '''
    Updates a firewall rule in a Data Lake Store account.

    Required Parameters:
    - account -- Name of the Data Lake Store account.
    - firewall_rule_name -- The name of the firewall rule to update.

    Optional Parameters:
    - end_ip_address -- The end IP address for the firewall rule. This can be either ipv4 or ipv6. Start and End should be in the same protocol.
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Store account.
    - start_ip_address -- The start IP address for the firewall rule. This can be either ipv4 or ipv6. Start and End should be in the same protocol.
    '''
    return _call_az("az dls account firewall update", locals())


def list(account, resource_group=None):
    '''
    Lists firewall rules in a Data Lake Store account.

    Required Parameters:
    - account -- Name of the Data Lake Store account.

    Optional Parameters:
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Store account.
    '''
    return _call_az("az dls account firewall list", locals())


def show(account, firewall_rule_name, resource_group=None):
    '''
    Get the details of a firewall rule in a Data Lake Store account.

    Required Parameters:
    - account -- Name of the Data Lake Store account.
    - firewall_rule_name -- The name of the firewall rule to retrieve.

    Optional Parameters:
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Store account.
    '''
    return _call_az("az dls account firewall show", locals())


def delete(account, firewall_rule_name, resource_group=None):
    '''
    Deletes a firewall rule in a Data Lake Store account.

    Required Parameters:
    - account -- Name of the Data Lake Store account.
    - firewall_rule_name -- The name of the firewall rule to delete.

    Optional Parameters:
    - resource_group -- If not specified, will attempt to discover the resource group for the specified Data Lake Store account.
    '''
    return _call_az("az dls account firewall delete", locals())

