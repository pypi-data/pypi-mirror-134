from .... pyaz_utils import _call_az

def show(resource_group, workspace_name):
    '''
    Get the SQL Azure Active Directory administrator.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse sql ad-admin show", locals())


def create(display_name, object_id, resource_group, workspace_name, no_wait=None):
    '''
    Create the SQL Azure Active Directory administrator.

    Required Parameters:
    - display_name -- Display name of the Azure AD administrator user or group.
    - object_id -- The unique ID of the Azure AD administrator.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az synapse sql ad-admin create", locals())


def update(resource_group, workspace_name, add=None, display_name=None, force_string=None, no_wait=None, object_id=None, remove=None, set=None):
    '''
    Update the SQL Azure Active Directory administrator.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - display_name -- Display name of the Azure AD administrator user or group.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - no_wait -- Do not wait for the long-running operation to finish.
    - object_id -- The unique ID of the Azure AD administrator.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az synapse sql ad-admin update", locals())


def delete(resource_group, workspace_name, no_wait=None, yes=None):
    '''
    Delete the SQL Azure Active Directory administrator.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- The workspace name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az synapse sql ad-admin delete", locals())


def wait(resource_group, workspace_name, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition is met.

    Required Parameters:
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
    return _call_az("az synapse sql ad-admin wait", locals())

