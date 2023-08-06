from .... pyaz_utils import _call_az

def start(managed_instance, name, resource_group, storage_sas, storage_uri, auto_complete=None, last_backup_name=None, no_wait=None):
    '''
    Start Log Replay service on specified database.

    Required Parameters:
    - managed_instance -- Name of the Azure SQL managed instance.
    - name -- The name of the Azure SQL Managed Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - storage_sas -- The authorization Sas token to access storage container where backups are.
    - storage_uri -- The URI of the storage container where backups are.

    Optional Parameters:
    - auto_complete -- The flag that in usage with last_backup_name automatically completes log replay servise.
    - last_backup_name -- The name of the last backup to restore.
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az sql midb log-replay start", locals())


def stop(managed_instance, name, resource_group, no_wait=None, yes=None):
    '''
    Stop Log Replay service.

    Required Parameters:
    - managed_instance -- Name of the Azure SQL managed instance.
    - name -- The name of the Azure SQL Managed Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az sql midb log-replay stop", locals())


def complete(managed_instance, name, resource_group, last_backup_name=None):
    '''
    Complete Log Replay service on specified database.

    Required Parameters:
    - managed_instance -- Name of the Azure SQL managed instance.
    - name -- The name of the Azure SQL Managed Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - last_backup_name -- The name of the last backup to restore.
    '''
    return _call_az("az sql midb log-replay complete", locals())


def wait(managed_instance, name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the managed database is met.

    Required Parameters:
    - managed_instance -- Name of the Azure SQL managed instance.
    - name -- The name of the Azure SQL Managed Database.
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
    return _call_az("az sql midb log-replay wait", locals())


def show(managed_instance, name, resource_group):
    '''
    Get status of Log Replay service.

    Required Parameters:
    - managed_instance -- Name of the Azure SQL managed instance.
    - name -- The name of the Azure SQL Managed Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql midb log-replay show", locals())

