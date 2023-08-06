from .... pyaz_utils import _call_az

def list(database_name, kusto_pool_name, resource_group, workspace_name):
    '''
    Lists all Kusto pool database principalAssignments.

    Required Parameters:
    - database_name -- The name of the database in the Kusto pool.
    - kusto_pool_name -- The name of the Kusto pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace
    '''
    return _call_az("az synapse kusto database-principal-assignment list", locals())


def show(database_name, kusto_pool_name, principal_assignment_name, resource_group, workspace_name):
    '''
    Gets a Kusto pool database principalAssignment.

    Required Parameters:
    - database_name -- The name of the database in the Kusto pool.
    - kusto_pool_name -- The name of the Kusto pool.
    - principal_assignment_name -- The name of the Kusto principalAssignment.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace
    '''
    return _call_az("az synapse kusto database-principal-assignment show", locals())


def create(database_name, kusto_pool_name, principal_assignment_name, resource_group, workspace_name, no_wait=None, principal_id=None, principal_type=None, role=None, tenant_id=None):
    '''
    Creates a Kusto pool database principalAssignment.

    Required Parameters:
    - database_name -- The name of the database in the Kusto pool.
    - kusto_pool_name -- The name of the Kusto pool.
    - principal_assignment_name -- The name of the Kusto principalAssignment.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - principal_id -- The principal ID assigned to the database principal. It can be a user email, application ID, or security group name.
    - principal_type -- Principal type.
    - role -- Database principal role.
    - tenant_id -- The tenant id of the principal
    '''
    return _call_az("az synapse kusto database-principal-assignment create", locals())


def update(database_name, kusto_pool_name, principal_assignment_name, resource_group, workspace_name, add=None, force_string=None, no_wait=None, principal_id=None, principal_type=None, remove=None, role=None, set=None, tenant_id=None):
    '''
    Update a Kusto pool database principalAssignment.

    Required Parameters:
    - database_name -- The name of the database in the Kusto pool.
    - kusto_pool_name -- The name of the Kusto pool.
    - principal_assignment_name -- The name of the Kusto principalAssignment.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - no_wait -- Do not wait for the long-running operation to finish.
    - principal_id -- The principal ID assigned to the database principal. It can be a user email, application ID, or security group name.
    - principal_type -- Principal type.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - role -- Database principal role.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tenant_id -- The tenant id of the principal
    '''
    return _call_az("az synapse kusto database-principal-assignment update", locals())


def delete(database_name, kusto_pool_name, principal_assignment_name, resource_group, workspace_name, no_wait=None, yes=None):
    '''
    Deletes a Kusto pool principalAssignment.

    Required Parameters:
    - database_name -- The name of the database in the Kusto pool.
    - kusto_pool_name -- The name of the Kusto pool.
    - principal_assignment_name -- The name of the Kusto principalAssignment.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The name of the workspace

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az synapse kusto database-principal-assignment delete", locals())


def wait(database_name, kusto_pool_name, principal_assignment_name, resource_group, workspace_name, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the synapse kusto database-principal-assignment is met.

    Required Parameters:
    - database_name -- The name of the database in the Kusto pool.
    - kusto_pool_name -- The name of the Kusto pool.
    - principal_assignment_name -- The name of the Kusto principalAssignment.
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
    return _call_az("az synapse kusto database-principal-assignment wait", locals())

