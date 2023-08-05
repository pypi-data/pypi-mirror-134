from .... pyaz_utils import _call_az

def create(outbound_rule_fqdn, resource_group, server):
    '''
    Create a new outbound firewall rule.

    Required Parameters:
    - outbound_rule_fqdn -- The allowed FQDN for the outbound firewall rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql server outbound-firewall-rule create", locals())


def delete(outbound_rule_fqdn, resource_group, server):
    '''
    Delete the outbound firewall rule.

    Required Parameters:
    - outbound_rule_fqdn -- The allowed FQDN for the outbound firewall rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql server outbound-firewall-rule delete", locals())


def show(outbound_rule_fqdn, resource_group, server):
    '''
    Show the details for an outbound firewall rule.

    Required Parameters:
    - outbound_rule_fqdn -- The allowed FQDN for the outbound firewall rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql server outbound-firewall-rule show", locals())


def list(resource_group, server):
    '''
    List a server's outbound firewall rules.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql server outbound-firewall-rule list", locals())

