from .... pyaz_utils import _call_az
from . import event_grid, event_hub, iot_hub


def list(database_name, kusto_pool_name, resource_group, workspace_name):
    '''
    Returns the list of data connections of the given Kusto pool database.

    Required Parameters:
    - database_name -- The name of the database in the Kusto pool.
    - kusto_pool_name -- The name of the Kusto pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace
    '''
    return _call_az("az synapse kusto data-connection list", locals())


def show(data_connection_name, database_name, kusto_pool_name, resource_group, workspace_name):
    '''
    Returns a data connection.

    Required Parameters:
    - data_connection_name -- The name of the data connection.
    - database_name -- The name of the database in the Kusto pool.
    - kusto_pool_name -- The name of the Kusto pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace
    '''
    return _call_az("az synapse kusto data-connection show", locals())


def delete(data_connection_name, database_name, kusto_pool_name, resource_group, workspace_name, no_wait=None, yes=None):
    '''
    Deletes the data connection with the given name.

    Required Parameters:
    - data_connection_name -- The name of the data connection.
    - database_name -- The name of the database in the Kusto pool.
    - kusto_pool_name -- The name of the Kusto pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az synapse kusto data-connection delete", locals())


def wait(data_connection_name, database_name, kusto_pool_name, resource_group, workspace_name, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the synapse kusto data-connection is met.

    Required Parameters:
    - data_connection_name -- The name of the data connection.
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
    return _call_az("az synapse kusto data-connection wait", locals())

