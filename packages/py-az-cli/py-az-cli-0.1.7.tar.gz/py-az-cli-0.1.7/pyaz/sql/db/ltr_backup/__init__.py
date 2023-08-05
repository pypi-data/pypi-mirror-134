from .... pyaz_utils import _call_az

def show(database, location, name, server):
    '''
    Get a long term retention backup for a database.

    Required Parameters:
    - database -- Name of the Azure SQL Database. If specified (along with server name), retrieves all requested backups under this database.
    - location -- The location of the desired backups.
    - name -- The name of the LTR backup. Use 'az sql db ltr-backup show' or 'az sql db ltr-backup list' for backup name.
    - server -- Name of the Azure SQL Server. If specified, retrieves all requested backups under this server.
    '''
    return _call_az("az sql db ltr-backup show", locals())


def list(location, database=None, database_state=None, only_latest_per_database=None, resource_group=None, server=None):
    '''
    List the long term retention backups for a location, server or database.

    Required Parameters:
    - location -- The location of the desired backups.

    Optional Parameters:
    - database -- Name of the Azure SQL Database. If specified (along with server name), retrieves all requested backups under this database.
    - database_state -- 'All', 'Live', or 'Deleted'. Will fetch backups only from databases of specified state. If no state provied, defaults to 'All'.
    - only_latest_per_database -- If true, will only return the latest backup for each database
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL Server. If specified, retrieves all requested backups under this server.
    '''
    return _call_az("az sql db ltr-backup list", locals())


def delete(database, location, name, server, yes=None):
    '''
    Delete a long term retention backup.

    Required Parameters:
    - database -- Name of the Azure SQL Database. If specified (along with server name), retrieves all requested backups under this database.
    - location -- The location of the desired backups.
    - name -- The name of the LTR backup. Use 'az sql db ltr-backup show' or 'az sql db ltr-backup list' for backup name.
    - server -- Name of the Azure SQL Server. If specified, retrieves all requested backups under this server.

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az sql db ltr-backup delete", locals())


def restore(backup_id, dest_database, dest_resource_group, dest_server, backup_storage_redundancy=None, no_wait=None):
    '''
    Restore a long term retention backup to a new database.

    Required Parameters:
    - backup_id -- The resource id of the long term retention backup to be restored. Use 'az sql db ltr-backup show' or 'az sql db ltr-backup list' for backup id.
    - dest_database -- Name of the database that will be created as the restore destination.
    - dest_resource_group -- Name of the resource group of the server to restore database to.
    - dest_server -- Name of the server to restore database to.

    Optional Parameters:
    - backup_storage_redundancy -- Backup storage redundancy used to store backups. Allowed values include: Local, Zone, Geo.
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az sql db ltr-backup restore", locals())


def wait(name, resource_group, server, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the database is met.

    Required Parameters:
    - name -- Name of the Azure SQL Database.
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
    return _call_az("az sql db ltr-backup wait", locals())

