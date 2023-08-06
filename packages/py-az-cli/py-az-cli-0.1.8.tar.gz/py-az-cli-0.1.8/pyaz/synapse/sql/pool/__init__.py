'''
Manage SQL pools.
'''
from .... pyaz_utils import _call_az
from . import audit_policy, classification, tde, threat_policy


def show(name, resource_group, workspace_name):
    '''
    Get a SQL pool.

    Required Parameters:
    - name -- The SQL pool name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse sql pool show", locals())


def list(resource_group, workspace_name):
    '''
    List all SQL pools.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse sql pool list", locals())


def create(name, performance_level, resource_group, workspace_name, no_wait=None, tags=None):
    '''
    Create a SQL pool.

    Required Parameters:
    - name -- The SQL pool name.
    - performance_level -- The performance level.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az synapse sql pool create", locals())


def delete(name, resource_group, workspace_name, no_wait=None, yes=None):
    '''
    Delete a SQL pool.

    Required Parameters:
    - name -- The SQL pool name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az synapse sql pool delete", locals())


def update(name, resource_group, workspace_name, performance_level=None, tags=None):
    '''
    Update a SQL pool.

    Required Parameters:
    - name -- The SQL pool name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.

    Optional Parameters:
    - performance_level -- The performance level.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az synapse sql pool update", locals())


def pause(name, resource_group, workspace_name):
    '''
    Pause a SQL pool.

    Required Parameters:
    - name -- The SQL pool name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse sql pool pause", locals())


def resume(name, resource_group, workspace_name):
    '''
    Resume a SQL pool.

    Required Parameters:
    - name -- The SQL pool name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse sql pool resume", locals())


def restore(dest_name, name, resource_group, workspace_name, deleted_time=None, performance_level=None, time=None):
    '''
    Create a new SQL pool by restoring from a backup.

    Required Parameters:
    - dest_name -- Name of the sql pool that will be created as the restore destination.
    - name -- The SQL pool name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.

    Optional Parameters:
    - deleted_time -- If specified, restore from a deleted database instead of from an existing database. Must match the deleted time of a deleted database in the same server. Either --time or --deleted-time (or both) must be specified. Time should be in following format: "YYYY-MM-DDTHH:MM:SS".
    - performance_level -- The performance level.
    - time -- The point in time of the source database that will be restored to create the new database. Must be greater than or equal to the source database's earliestRestoreDate value. Either --time or --deleted-time (or both) must be specified. Time should be in following format: "YYYY-MM-DDTHH:MM:SS".
    '''
    return _call_az("az synapse sql pool restore", locals())


def show_connection_string(client, auth_type=None, name=None, workspace_name=None):
    '''
    Generate a connection string to a SQL pool.

    Required Parameters:
    - client -- Type of client connection provider.

    Optional Parameters:
    - auth_type -- Type of authentication.
    - name -- The SQL pool name.
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse sql pool show-connection-string", locals())


def wait(resource_group, sql_pool_name, workspace_name, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of a SQL pool is met.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sql_pool_name -- SQL pool name.
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
    return _call_az("az synapse sql pool wait", locals())


def list_deleted(resource_group, workspace_name):
    '''
    List all deleted SQL pools.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse sql pool list-deleted", locals())

