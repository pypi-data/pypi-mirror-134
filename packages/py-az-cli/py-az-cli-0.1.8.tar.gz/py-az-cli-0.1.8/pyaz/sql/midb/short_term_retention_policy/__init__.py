from .... pyaz_utils import _call_az

def set(managed_instance, name, resource_group, retention_days, deleted_time=None, no_wait=None):
    '''
    Update short term retention for automated backups on a single database.

    Required Parameters:
    - managed_instance -- Name of the Azure SQL managed instance.
    - name -- The name of the Azure SQL Managed Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - retention_days -- New backup short term retention policy in days.Valid policy for live database is 7-35 days, valid policy for dropped databases is 0-35 days.

    Optional Parameters:
    - deleted_time -- If specified, updates retention days for a deleted database, instead of an existing database.Must match the deleted time of a deleted database on the source Managed Instance.
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az sql midb short-term-retention-policy set", locals())


def show(managed_instance, name, resource_group, deleted_time=None):
    '''
    Show short term retention for automated backups on a single database.

    Required Parameters:
    - managed_instance -- Name of the Azure SQL managed instance.
    - name -- The name of the Azure SQL Managed Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - deleted_time -- If specified, shows retention days for a deleted database, instead of an existing database.Must match the deleted time of a deleted database on the source Managed Instance.
    '''
    return _call_az("az sql midb short-term-retention-policy show", locals())

