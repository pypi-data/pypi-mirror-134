from .... pyaz_utils import _call_az

def show(name, resource_group):
    '''
    

    Required Parameters:
    - name -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql server audit-policy show", locals())


def update(name, resource_group, actions=None, add=None, blob_storage_target_state=None, event_hub=None, event_hub_authorization_rule_id=None, event_hub_target_state=None, force_string=None, log_analytics_target_state=None, log_analytics_workspace_resource_id=None, no_wait=None, remove=None, retention_days=None, set=None, state=None, storage_account=None, storage_endpoint=None, storage_key=None):
    '''
    Update a server's auditing policy.

    Required Parameters:
    - name -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - actions -- List of actions and action groups to audit.
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - blob_storage_target_state -- Indicate whether blob storage is a destination for audit records.
    - event_hub -- The name of the event hub. If none is specified when providing event_hub_authorization_rule_id, the default event hub will be selected.
    - event_hub_authorization_rule_id -- The resource Id for the event hub authorization rule.
    - event_hub_target_state -- Indicate whether event hub is a destination for audit records.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - log_analytics_target_state -- Indicate whether log analytics is a destination for audit records.
    - log_analytics_workspace_resource_id -- The workspace ID (resource ID of a Log Analytics workspace) for a Log Analytics workspace to which you would like to send Audit Logs.
    - no_wait -- Do not wait for the long-running operation to finish.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - retention_days -- The number of days to retain audit logs.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - state -- Auditing policy state
    - storage_account -- Name of the storage account.
    - storage_endpoint -- The storage account endpoint.
    - storage_key -- Access key for the storage account.
    '''
    return _call_az("az sql server audit-policy update", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the server's audit policy is met.

    Required Parameters:
    - name -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
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
    return _call_az("az sql server audit-policy wait", locals())

