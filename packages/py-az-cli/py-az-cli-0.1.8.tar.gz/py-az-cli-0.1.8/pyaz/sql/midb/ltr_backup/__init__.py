from .... pyaz_utils import _call_az

def show(backup_id=None, database=None, location=None, managed_instance=None, name=None):
    '''
    Get a long term retention backup for a managed database.

    Optional Parameters:
    - backup_id -- The resource id of the backups. Use 'az sql midb ltr-backup show' or 'az sql midb ltr-backup list' for backup id. If provided, other arguments are not required. 
    - database -- The name of the Azure SQL Managed Database.
    - location -- The location of the desired backup(s).
    - managed_instance -- Name of the Azure SQL managed instance.
    - name -- The name of the LTR backup. Use 'az sql midb ltr-backup show' or 'az sql midb ltr-backup list' for backup name.
    '''
    return _call_az("az sql midb ltr-backup show", locals())


def list(location, database=None, database_state=None, managed_instance=None, only_latest_per_database=None, resource_group=None):
    '''
    List the long term retention backups for a location, instance or database.

    Required Parameters:
    - location -- The location of the desired backup(s).

    Optional Parameters:
    - database -- The name of the Azure SQL Managed Database. If specified (along with instance name), retrieves all requested backups under this database.
    - database_state -- 'All', 'Live', or 'Deleted'. Will fetch backups only from databases of specified state. If no state provied, defaults to 'All'.
    - managed_instance -- Name of the Azure SQL managed instance. If specified, retrieves all requested backups under this managed instance.
    - only_latest_per_database -- If true, will only return the latest backup for each database
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql midb ltr-backup list", locals())


def delete(backup_id=None, database=None, location=None, managed_instance=None, name=None, yes=None):
    '''
    Delete a long term retention backup.

    Optional Parameters:
    - backup_id -- The resource id of the backups. Use 'az sql midb ltr-backup show' or 'az sql midb ltr-backup list' for backup id. If provided, other arguments are not required. 
    - database -- The name of the Azure SQL Managed Database.
    - location -- The location of the desired backup(s).
    - managed_instance -- Name of the Azure SQL managed instance.
    - name -- The name of the LTR backup. Use 'az sql midb ltr-backup show' or 'az sql midb ltr-backup list' for backup name.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az sql midb ltr-backup delete", locals())


def restore(backup_id, dest_database, dest_mi, dest_resource_group, no_wait=None):
    '''
    Restore a long term retention backup to a new database.

    Required Parameters:
    - backup_id -- The resource id of the long term retention backup to be restored. Use 'az sql midb ltr-backup show' or 'az sql midb ltr-backup list' for backup id.
    - dest_database -- Name of the managed database that will be created as the restore destination.
    - dest_mi -- Name of the managed instance to restore managed database to.
    - dest_resource_group -- Name of the resource group of the managed instance to restore managed database to.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az sql midb ltr-backup restore", locals())


def wait(database, managed_instance, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the managed database is met.

    Required Parameters:
    - database -- The name of the Azure SQL Managed Database.
    - managed_instance -- Name of the Azure SQL managed instance.
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
    return _call_az("az sql midb ltr-backup wait", locals())

