'''
Manage SQL managed instance databases.
'''
from ... pyaz_utils import _call_az
from . import log_replay, ltr_backup, ltr_policy, short_term_retention_policy


def list_deleted(managed_instance, resource_group):
    '''
    List restorable deleted managed databases.

    Required Parameters:
    - managed_instance -- Name of the Azure SQL managed instance.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql midb list-deleted", locals())


def create(managed_instance, name, resource_group, collation=None, no_wait=None):
    '''
    Create a managed database.

    Required Parameters:
    - managed_instance -- Name of the Azure SQL managed instance.
    - name -- The name of the Azure SQL Managed Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - collation -- The collation of the Azure SQL Managed Database collation to use, e.g.: SQL_Latin1_General_CP1_CI_AS or Latin1_General_100_CS_AS_SC
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az sql midb create", locals())


def restore(dest_name, managed_instance, name, resource_group, time, deleted_time=None, dest_mi=None, dest_resource_group=None, no_wait=None):
    '''
    Restore a managed database.

    Required Parameters:
    - dest_name -- Name of the managed database that will be created as the restore destination.
    - managed_instance -- Name of the Azure SQL managed instance.
    - name -- The name of the Azure SQL Managed Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - time -- The point in time of the source database that will be restored to create the new database. Must be greater than or equal to the source database's earliestRestoreDate value. Time should be in following format: "YYYY-MM-DDTHH:MM:SS".

    Optional Parameters:
    - deleted_time -- If specified, restore from a deleted database instead of from an existing database. Must match the deleted time of a deleted database on the source Managed Instance.
    - dest_mi -- Name of the managed instance to restore managed database to. This can be same managed instance, or another managed instance on same subscription. When not specified it defaults to source managed instance.
    - dest_resource_group -- Name of the resource group of the managed instance to restore managed database to. When not specified it defaults to source resource group.
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az sql midb restore", locals())


def show(managed_instance, name, resource_group):
    '''
    Get the details for a managed database.

    Required Parameters:
    - managed_instance -- Name of the Azure SQL managed instance.
    - name -- The name of the Azure SQL Managed Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql midb show", locals())


def list(managed_instance, resource_group):
    '''
    List managed databases on a managed instance.

    Required Parameters:
    - managed_instance -- Name of the Azure SQL managed instance.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql midb list", locals())


def delete(managed_instance, name, resource_group, no_wait=None, yes=None):
    '''
    Delete a managed database.

    Required Parameters:
    - managed_instance -- Name of the Azure SQL managed instance.
    - name -- The name of the Azure SQL Managed Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az sql midb delete", locals())

