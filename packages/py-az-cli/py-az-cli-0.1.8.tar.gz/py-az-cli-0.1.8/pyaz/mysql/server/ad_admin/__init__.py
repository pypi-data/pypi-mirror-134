from .... pyaz_utils import _call_az

def create(resource_group, server_name, display_name=None, no_wait=None, object_id=None):
    '''
    Create an Active Directory administrator for MySQL server.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.

    Optional Parameters:
    - display_name -- Display name of the Azure AD administrator user or group.
    - no_wait -- Do not wait for the long-running operation to finish.
    - object_id -- The unique ID of the Azure AD administrator.
    '''
    return _call_az("az mysql server ad-admin create", locals())


def list(resource_group, server_name):
    '''
    List all Active Directory Administrators for MySQL server.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    '''
    return _call_az("az mysql server ad-admin list", locals())


def delete(resource_group, server_name, yes=None):
    '''
    Delete an Active Directory Administrator for MySQL server.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az mysql server ad-admin delete", locals())


def show(resource_group, server_name):
    '''
    Get Active Directory Administrator information for a MySQL server.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    '''
    return _call_az("az mysql server ad-admin show", locals())


def wait(resource_group, server_name, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the MySQL server Active Directory Administrator is met.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az mysql server ad-admin wait", locals())

