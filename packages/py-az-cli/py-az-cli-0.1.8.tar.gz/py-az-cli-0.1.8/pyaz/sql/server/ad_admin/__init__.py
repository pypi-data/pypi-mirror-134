from .... pyaz_utils import _call_az

def create(resource_group, server_name, display_name=None, object_id=None):
    '''
    Create a new server Active Directory administrator.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`

    Optional Parameters:
    - display_name -- Display name of the Azure AD administrator user or group.
    - object_id -- The unique ID of the Azure AD administrator.
    '''
    return _call_az("az sql server ad-admin create", locals())


def list(resource_group, server_name):
    '''
    

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql server ad-admin list", locals())


def delete(resource_group, server_name):
    '''
    

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql server ad-admin delete", locals())


def update(resource_group, server_name, add=None, display_name=None, force_string=None, object_id=None, remove=None, set=None):
    '''
    Update an existing server Active Directory administrator.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - display_name -- Display name of the Azure AD administrator user or group.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - object_id -- The unique ID of the Azure AD administrator.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az sql server ad-admin update", locals())

