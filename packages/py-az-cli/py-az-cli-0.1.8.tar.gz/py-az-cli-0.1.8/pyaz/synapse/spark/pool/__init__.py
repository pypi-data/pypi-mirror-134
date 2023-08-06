'''
Manage Spark pools.
'''
from .... pyaz_utils import _call_az

def show(name, resource_group, workspace_name):
    '''
    Get a Spark pool.

    Required Parameters:
    - name -- The name of the Spark pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse spark pool show", locals())


def list(resource_group, workspace_name):
    '''
    List all Spark pools.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse spark pool list", locals())


def create(name, node_count, node_size, resource_group, spark_version, workspace_name, delay=None, enable_auto_pause=None, enable_auto_scale=None, max_node_count=None, min_node_count=None, no_wait=None, node_size_family=None, spark_config_file_path=None, spark_events_folder=None, spark_log_folder=None, tags=None):
    '''
    Create a Spark pool.

    Required Parameters:
    - name -- The name of the Spark pool.
    - node_count -- The number of node.
    - node_size -- The node size.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - spark_version -- The supported Spark version is 2.4 now.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - delay -- The delay time whose unit is minute.
    - enable_auto_pause -- The flag of enabling auto pause.
    - enable_auto_scale -- The flag of enabling auto scale.
    - max_node_count -- The max node count.
    - min_node_count -- The min node count.
    - no_wait -- Do not wait for the long-running operation to finish.
    - node_size_family -- The node size family.
    - spark_config_file_path -- Absolute path of Spark pool properties configuration file.
    - spark_events_folder -- The Spark events folder.
    - spark_log_folder -- The default Spark log folder.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az synapse spark pool create", locals())


def update(name, resource_group, workspace_name, delay=None, enable_auto_pause=None, enable_auto_scale=None, force=None, library_requirements=None, max_node_count=None, min_node_count=None, no_wait=None, node_count=None, node_size=None, package=None, package_action=None, spark_config_file_path=None, tags=None):
    '''
    Update the Spark pool.

    Required Parameters:
    - name -- The name of the Spark pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.

    Optional Parameters:
    - delay -- The delay time whose unit is minute.
    - enable_auto_pause -- The flag of enabling auto pause.
    - enable_auto_scale -- The flag of enabling auto scale.
    - force -- The flag of force operation.
    - library_requirements -- The library requirements file.
    - max_node_count -- The max node count.
    - min_node_count -- The min node count.
    - no_wait -- Do not wait for the long-running operation to finish.
    - node_count -- The number of node.
    - node_size -- The node size.
    - package -- List of workspace packages name.
    - package_action -- Package action must be specified when you add or remove a workspace package from a Apache Spark pool.
    - spark_config_file_path -- Absolute path of Spark pool properties configuration file.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az synapse spark pool update", locals())


def delete(name, resource_group, workspace_name, no_wait=None, yes=None):
    '''
    Delete a Spark pool.

    Required Parameters:
    - name -- The name of the Spark pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az synapse spark pool delete", locals())


def wait(big_data_pool_name, resource_group, workspace_name, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of a Spark pool is met.

    Required Parameters:
    - big_data_pool_name -- Big Data pool name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
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
    return _call_az("az synapse spark pool wait", locals())

