from .... pyaz_utils import _call_az

def create(name, resource_group, server, end_ip_address=None, start_ip_address=None):
    '''
    Create a firewall rule.

    Required Parameters:
    - name -- The name of the firewall rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`

    Optional Parameters:
    - end_ip_address -- The end IP address of the firewall rule. Must be IPv4 format. Use value '0.0.0.0' to represent all Azure-internal IP addresses.
    - start_ip_address -- The start IP address of the firewall rule. Must be IPv4 format. Use value '0.0.0.0' to represent all Azure-internal IP addresses.
    '''
    return _call_az("az sql server firewall-rule create", locals())


def update(name, resource_group, server, end_ip_address=None, start_ip_address=None):
    '''
    Update a firewall rule.

    Required Parameters:
    - name -- The name of the firewall rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`

    Optional Parameters:
    - end_ip_address -- The end IP address of the firewall rule. Must be IPv4 format. Use value '0.0.0.0' to represent all Azure-internal IP addresses.
    - start_ip_address -- The start IP address of the firewall rule. Must be IPv4 format. Use value '0.0.0.0' to represent all Azure-internal IP addresses.
    '''
    return _call_az("az sql server firewall-rule update", locals())


def delete(name, resource_group, server):
    '''
    

    Required Parameters:
    - name -- The name of the firewall rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql server firewall-rule delete", locals())


def show(name, resource_group, server):
    '''
    Shows the details for a firewall rule.

    Required Parameters:
    - name -- The name of the firewall rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql server firewall-rule show", locals())


def list(resource_group, server):
    '''
    List a server's firewall rules.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql server firewall-rule list", locals())

