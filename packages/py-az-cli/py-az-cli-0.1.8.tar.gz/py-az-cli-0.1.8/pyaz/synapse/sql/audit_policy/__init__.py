from .... pyaz_utils import _call_az

def show(resource_group, workspace_name):
    '''
    Get a SQL's auditing policy.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse sql audit-policy show", locals())


def update(resource_group, workspace_name, actions=None, add=None, blob_auditing_policy_name=None, blob_storage_target_state=None, enable_azure_monitor=None, event_hub=None, event_hub_authorization_rule_id=None, event_hub_target_state=None, force_string=None, log_analytics_target_state=None, log_analytics_workspace_resource_id=None, no_wait=None, queue_delay_time=None, remove=None, retention_days=None, set=None, state=None, storage_account=None, storage_endpoint=None, storage_key=None, storage_subscription=None, use_secondary_key=None):
    '''
    Update a SQL's auditing policy.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.

    Optional Parameters:
    - actions -- List of actions and action groups to audit.
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - blob_auditing_policy_name -- None
    - blob_storage_target_state -- Indicate whether blob storage is a destination for audit records.
    - enable_azure_monitor -- Whether enabling azure monitor target or not.
    - event_hub -- The name of the event hub. If none is specified when providing event_hub_authorization_rule_id, the default event hub will be selected.
    - event_hub_authorization_rule_id -- The resource Id for the event hub authorization rule.
    - event_hub_target_state -- Indicate whether event hub is a destination for audit records.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - log_analytics_target_state -- Indicate whether log analytics is a destination for audit records.
    - log_analytics_workspace_resource_id -- The workspace ID (resource ID of a Log Analytics workspace) for a Log Analytics workspace to which you would like to send Audit Logs.
    - no_wait -- Do not wait for the long-running operation to finish.
    - queue_delay_time -- The amount of time in milliseconds that can elapse before audit actions are forced to be processed
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - retention_days -- The number of days to retain audit logs.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - state -- Auditing policy state
    - storage_account -- Name of the storage account.
    - storage_endpoint -- The storage account endpoint.
    - storage_key -- Access key for the storage account.
    - storage_subscription -- The subscription id of storage account
    - use_secondary_key -- Indicates whether using the secondary storeage key or not
    '''
    return _call_az("az synapse sql audit-policy update", locals())


def wait(blob_auditing_policy_name, resource_group, workspace_name, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition is met.

    Required Parameters:
    - blob_auditing_policy_name -- The name of the blob auditing policy.
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
    return _call_az("az synapse sql audit-policy wait", locals())

