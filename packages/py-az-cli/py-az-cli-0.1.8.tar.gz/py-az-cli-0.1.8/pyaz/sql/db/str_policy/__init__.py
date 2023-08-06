from .... pyaz_utils import _call_az

def set(diffbackup_hours, name, resource_group, retention_days, server, no_wait=None):
    '''
    Update short term retention settings for a live database.

    Required Parameters:
    - diffbackup_hours -- New backup short term retention policy differential backup interval in hours.Valid differential backup interval for live database can be 12 or 24 hours.
    - name -- Name of the Azure SQL Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - retention_days -- New backup short term retention policy retention in days.Valid retention days for live database of (DTU) Basic can be 1-7 days; Rest models can be 1-35 days.
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az sql db str-policy set", locals())


def show(name, resource_group, server):
    '''
    Show the short term retention policy for a live database.

    Required Parameters:
    - name -- Name of the Azure SQL Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql db str-policy show", locals())


def wait(name, policy_name, resource_group, server, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until the policy is set.

    Required Parameters:
    - name -- Name of the Azure SQL Database.
    - policy_name -- The policy name. Should always be "default".
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az sql db str-policy wait", locals())

