from .... pyaz_utils import _call_az

def list(kusto_pool_name, resource_group, workspace_name):
    '''
    Returns the list of attached database configurations of the given Kusto Pool.

    Required Parameters:
    - kusto_pool_name -- The name of the Kusto pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace
    '''
    return _call_az("az synapse kusto attached-database-configuration list", locals())


def show(attached_database_configuration_name, kusto_pool_name, resource_group, workspace_name):
    '''
    Returns an attached database configuration.

    Required Parameters:
    - attached_database_configuration_name -- The name of the attached database configuration.
    - kusto_pool_name -- The name of the Kusto pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace
    '''
    return _call_az("az synapse kusto attached-database-configuration show", locals())


def create(attached_database_configuration_name, kusto_pool_name, resource_group, workspace_name, database_name=None, default_principals_modification_kind=None, kusto_pool_resource_id=None, location=None, no_wait=None, table_level_sharing_properties=None):
    '''
    Create an attached database configuration.

    Required Parameters:
    - attached_database_configuration_name -- The name of the attached database configuration.
    - kusto_pool_name -- The name of the Kusto pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace

    Optional Parameters:
    - database_name -- The name of the database which you would like to attach, use * if you want to follow all current and future databases.
    - default_principals_modification_kind -- The default principals modification kind
    - kusto_pool_resource_id -- The resource id of the kusto pool where the databases you would like to attach reside.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - no_wait -- Do not wait for the long-running operation to finish.
    - table_level_sharing_properties -- Table level sharing specifications
    '''
    return _call_az("az synapse kusto attached-database-configuration create", locals())


def update(attached_database_configuration_name, kusto_pool_name, resource_group, workspace_name, add=None, database_name=None, default_principals_modification_kind=None, force_string=None, kusto_pool_resource_id=None, location=None, no_wait=None, remove=None, set=None, table_level_sharing_properties=None):
    '''
    Update an attached database configuration.

    Required Parameters:
    - attached_database_configuration_name -- The name of the attached database configuration.
    - kusto_pool_name -- The name of the Kusto pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - database_name -- The name of the database which you would like to attach, use * if you want to follow all current and future databases.
    - default_principals_modification_kind -- The default principals modification kind
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - kusto_pool_resource_id -- The resource id of the kusto pool where the databases you would like to attach reside.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - no_wait -- Do not wait for the long-running operation to finish.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - table_level_sharing_properties -- Table level sharing specifications
    '''
    return _call_az("az synapse kusto attached-database-configuration update", locals())


def delete(attached_database_configuration_name, kusto_pool_name, resource_group, workspace_name, no_wait=None, yes=None):
    '''
    Deletes the attached database configuration with the given name.

    Required Parameters:
    - attached_database_configuration_name -- The name of the attached database configuration.
    - kusto_pool_name -- The name of the Kusto pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az synapse kusto attached-database-configuration delete", locals())


def wait(attached_database_configuration_name, kusto_pool_name, resource_group, workspace_name, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the synapse kusto attached-database-configuration is met.

    Required Parameters:
    - attached_database_configuration_name -- The name of the attached database configuration.
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
    return _call_az("az synapse kusto attached-database-configuration wait", locals())

