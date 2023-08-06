'''
Manage Azure Kusto databases.
'''
from ... pyaz_utils import _call_az

def create(cluster_name, name, resource_group, hot_cache_period=None, no_wait=None, soft_delete_period=None):
    '''
    Create a Kusto database.

    Required Parameters:
    - cluster_name -- The name of the cluster.
    - name -- The name of the database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - hot_cache_period -- Amount of time that data should be kept in cache.Duration in ISO8601 format (for example, 100 days would be P100D).
    - no_wait -- Do not wait for the long-running operation to finish.
    - soft_delete_period -- Amount of time that data should be kept so it is available to query. Duration in ISO8601 format (for example, 100 days would be P100D).
    '''
    return _call_az("az kusto database create", locals())


def delete(cluster_name, name, resource_group, yes=None):
    '''
    Delete a Kusto database.

    Required Parameters:
    - cluster_name -- The name of the cluster.
    - name -- The name of the database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az kusto database delete", locals())


def update(cluster_name, name, resource_group, soft_delete_period, add=None, force_string=None, hot_cache_period=None, no_wait=None, remove=None, set=None):
    '''
    Update a Kusto database.

    Required Parameters:
    - cluster_name -- The name of the cluster.
    - name -- The name of the database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - soft_delete_period -- Amount of time that data should be kept so it is available to query. Duration in ISO8601 format (for example, 100 days would be P100D).

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - hot_cache_period -- Amount of time that data should be kept in cache.Duration in ISO8601 format (for example, 100 days would be P100D).
    - no_wait -- Do not wait for the long-running operation to finish.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az kusto database update", locals())


def list(cluster_name, resource_group):
    '''
    List a Kusto database.

    Required Parameters:
    - cluster_name -- The name of the cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az kusto database list", locals())


def show(cluster_name, name, resource_group):
    '''
    Get a Kusto database.

    Required Parameters:
    - cluster_name -- The name of the cluster.
    - name -- The name of the database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az kusto database show", locals())


def wait(cluster_name, name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Wait for a managed Kusto database to reach a desired state.

    Required Parameters:
    - cluster_name -- The name of the cluster.
    - name -- The name of the database.
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
    return _call_az("az kusto database wait", locals())

