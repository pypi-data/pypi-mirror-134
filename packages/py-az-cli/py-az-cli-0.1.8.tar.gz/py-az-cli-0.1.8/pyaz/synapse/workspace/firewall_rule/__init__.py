from .... pyaz_utils import _call_az

def list(resource_group, workspace_name):
    '''
    List all firewall rules.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse workspace firewall-rule list", locals())


def show(name, resource_group, workspace_name):
    '''
    Get a firewall rule.

    Required Parameters:
    - name -- The IP firewall rule name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse workspace firewall-rule show", locals())


def create(end_ip_address, name, resource_group, start_ip_address, workspace_name, no_wait=None):
    '''
    Create a firewall rule.

    Required Parameters:
    - end_ip_address -- The end IP address of the firewall rule. Must be IPv4 format. Must be greater than or equal to startIpAddress.
    - name -- The IP firewall rule name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - start_ip_address -- The start IP address of the firewall rule. Must be IPv4 format.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az synapse workspace firewall-rule create", locals())


def update(name, resource_group, workspace_name, end_ip_address=None, no_wait=None, start_ip_address=None):
    '''
    Update a firewall rule.

    Required Parameters:
    - name -- The IP firewall rule name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.

    Optional Parameters:
    - end_ip_address -- The end IP address of the firewall rule. Must be IPv4 format. Must be greater than or equal to startIpAddress.
    - no_wait -- Do not wait for the long-running operation to finish.
    - start_ip_address -- The start IP address of the firewall rule. Must be IPv4 format.
    '''
    return _call_az("az synapse workspace firewall-rule update", locals())


def delete(name, resource_group, workspace_name, no_wait=None, yes=None):
    '''
    Delete a firewall rule.

    Required Parameters:
    - name -- The IP firewall rule name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az synapse workspace firewall-rule delete", locals())


def wait(resource_group, rule_name, workspace_name, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of a firewall rule is met.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_name -- The IP firewall rule name.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az synapse workspace firewall-rule wait", locals())

