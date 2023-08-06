'''
Manage kusto pool with synapse
'''
from .... pyaz_utils import _call_az

def list_sku(name, resource_group, workspace_name):
    '''
    Returns the SKUs available for the provided resource.

    Required Parameters:
    - name -- The name of the Kusto pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace
    '''
    return _call_az("az synapse kusto pool list-sku", locals())


def list(resource_group, workspace_name):
    '''
    List all Kusto pools.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace
    '''
    return _call_az("az synapse kusto pool list", locals())


def show(name, resource_group, workspace_name):
    '''
    Gets a Kusto pool.

    Required Parameters:
    - name -- The name of the Kusto pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace
    '''
    return _call_az("az synapse kusto pool show", locals())


def delete(name, resource_group, workspace_name, no_wait=None, yes=None):
    '''
    Deletes a Kusto pool.

    Required Parameters:
    - name -- The name of the Kusto pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az synapse kusto pool delete", locals())


def list_follower_database(name, resource_group, workspace_name):
    '''
    Returns a list of databases that are owned by this Kusto Pool and were followed by another Kusto Pool.

    Required Parameters:
    - name -- The name of the Kusto pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace
    '''
    return _call_az("az synapse kusto pool list-follower-database", locals())


def list_language_extension(name, resource_group, workspace_name):
    '''
    Returns a list of language extensions that can run within KQL queries.

    Required Parameters:
    - name -- The name of the Kusto pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace
    '''
    return _call_az("az synapse kusto pool list-language-extension", locals())


def start(name, resource_group, workspace_name, no_wait=None):
    '''
    Starts a Kusto pool.

    Required Parameters:
    - name -- The name of the Kusto pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az synapse kusto pool start", locals())


def stop(name, resource_group, workspace_name, no_wait=None):
    '''
    Stops a Kusto pool.

    Required Parameters:
    - name -- The name of the Kusto pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az synapse kusto pool stop", locals())


def wait(name, resource_group, workspace_name, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the synapse kusto pool is met.

    Required Parameters:
    - name -- The name of the Kusto pool.
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
    return _call_az("az synapse kusto pool wait", locals())


def create(name, resource_group, sku, workspace_name, enable_purge=None, enable_streaming_ingest=None, if_match=None, if_none_match=None, location=None, no_wait=None, optimized_autoscale=None, tags=None, workspace_uid=None):
    '''
    Create a Kusto pool.

    Required Parameters:
    - name -- The name of the Kusto pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sku -- The SKU of the kusto pool.
    - workspace_name -- The name of the workspace

    Optional Parameters:
    - enable_purge -- A boolean value that indicates if the purge operations are enabled.
    - enable_streaming_ingest -- A boolean value that indicates if the streaming ingest is enabled.
    - if_match -- The ETag of the Kusto Pool. Omit this value to always overwrite the current Kusto Pool. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes.
    - if_none_match -- Set to '*' to allow a new Kusto Pool to be created, but to prevent updating an existing Kusto Pool. Other values will result in a 412 Pre-condition Failed response.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - no_wait -- Do not wait for the long-running operation to finish.
    - optimized_autoscale -- Optimized auto scale definition.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - workspace_uid -- The workspace unique identifier.
    '''
    return _call_az("az synapse kusto pool create", locals())


def update(name, resource_group, workspace_name, enable_purge=None, enable_streaming_ingest=None, if_match=None, no_wait=None, optimized_autoscale=None, sku=None, tags=None, workspace_uid=None):
    '''
    Update a Kusto Kusto Pool.

    Required Parameters:
    - name -- The name of the Kusto pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace

    Optional Parameters:
    - enable_purge -- A boolean value that indicates if the purge operations are enabled.
    - enable_streaming_ingest -- A boolean value that indicates if the streaming ingest is enabled.
    - if_match -- The ETag of the Kusto Pool. Omit this value to always overwrite the current Kusto Pool. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes.
    - no_wait -- Do not wait for the long-running operation to finish.
    - optimized_autoscale -- Optimized auto scale definition.
    - sku -- The SKU of the kusto pool.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - workspace_uid -- The workspace unique identifier.
    '''
    return _call_az("az synapse kusto pool update", locals())


def add_language_extension(name, resource_group, workspace_name, no_wait=None, value=None):
    '''
    Add a list of language extensions that can run within KQL queries.

    Required Parameters:
    - name -- The name of the Kusto pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - value -- The list of language extensions.
    '''
    return _call_az("az synapse kusto pool add-language-extension", locals())


def detach_follower_database(attached_database_configuration_name, kusto_pool_resource_id, name, resource_group, workspace_name, no_wait=None):
    '''
    Detaches all followers of a database owned by this Kusto Pool.

    Required Parameters:
    - attached_database_configuration_name -- Resource name of the attached database configuration in the follower cluster.
    - kusto_pool_resource_id -- Resource id of the cluster that follows a database owned by this cluster.
    - name -- The name of the Kusto pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az synapse kusto pool detach-follower-database", locals())


def remove_language_extension(name, resource_group, workspace_name, no_wait=None, value=None):
    '''
    Remove a list of language extensions that can run within KQL queries.

    Required Parameters:
    - name -- The name of the Kusto pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - value -- The list of language extensions.
    '''
    return _call_az("az synapse kusto pool remove-language-extension", locals())

