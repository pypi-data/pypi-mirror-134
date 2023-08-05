'''
Manage kusto pool database with synapse
'''
from .... pyaz_utils import _call_az

def list(kusto_pool_name, resource_group, workspace_name):
    '''
    Returns the list of databases of the given Kusto pool.

    Required Parameters:
    - kusto_pool_name -- The name of the Kusto pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace
    '''
    return _call_az("az synapse kusto database list", locals())


def show(database_name, kusto_pool_name, resource_group, workspace_name):
    '''
    Returns a database.

    Required Parameters:
    - database_name -- The name of the database in the Kusto pool.
    - kusto_pool_name -- The name of the Kusto pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace
    '''
    return _call_az("az synapse kusto database show", locals())


def create(database_name, kusto_pool_name, resource_group, workspace_name, no_wait=None, read_write_database=None):
    '''
    Create a database.

    Required Parameters:
    - database_name -- The name of the database in the Kusto pool.
    - kusto_pool_name -- The name of the Kusto pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - read_write_database -- Class representing a read write database.
    '''
    return _call_az("az synapse kusto database create", locals())


def update(database_name, kusto_pool_name, resource_group, workspace_name, no_wait=None, read_write_database=None):
    '''
    Updates a database.

    Required Parameters:
    - database_name -- The name of the database in the Kusto pool.
    - kusto_pool_name -- The name of the Kusto pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - read_write_database -- Class representing a read write database.
    '''
    return _call_az("az synapse kusto database update", locals())


def delete(database_name, kusto_pool_name, resource_group, workspace_name, no_wait=None, yes=None):
    '''
    Deletes the database with the given name.

    Required Parameters:
    - database_name -- The name of the database in the Kusto pool.
    - kusto_pool_name -- The name of the Kusto pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az synapse kusto database delete", locals())


def wait(database_name, kusto_pool_name, resource_group, workspace_name, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the synapse kusto database is met.

    Required Parameters:
    - database_name -- The name of the database in the Kusto pool.
    - kusto_pool_name -- The name of the Kusto pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az synapse kusto database wait", locals())

