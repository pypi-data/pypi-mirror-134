from .... pyaz_utils import _call_az

def create(name, resource_group, server_name, subnet, ignore_missing_endpoint=None, vnet_name=None):
    '''
    Create a virtual network rule to allows access to a MariaDB server.

    Required Parameters:
    - name -- The name of the vnet rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - subnet -- Name or ID of the subnet that allows access to an Azure Postgres Server. If subnet name is provided, --vnet-name must be provided.

    Optional Parameters:
    - ignore_missing_endpoint -- Create vnet rule before virtual network has vnet service endpoint enabled
    - vnet_name -- The virtual network name
    '''
    return _call_az("az mariadb server vnet-rule create", locals())


def delete(name, resource_group, server_name):
    '''
    

    Required Parameters:
    - name -- The name of the vnet rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    '''
    return _call_az("az mariadb server vnet-rule delete", locals())


def show(name, resource_group, server_name):
    '''
    

    Required Parameters:
    - name -- The name of the vnet rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    '''
    return _call_az("az mariadb server vnet-rule show", locals())


def list(resource_group, server_name):
    '''
    

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    '''
    return _call_az("az mariadb server vnet-rule list", locals())


def update(name, resource_group, server_name, subnet, add=None, force_string=None, ignore_missing_endpoint=None, remove=None, set=None, vnet_name=None):
    '''
    Update a virtual network rule.

    Required Parameters:
    - name -- The name of the vnet rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - subnet -- Name or ID of the subnet that allows access to an Azure Postgres Server. If subnet name is provided, --vnet-name must be provided.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - ignore_missing_endpoint -- Create vnet rule before virtual network has vnet service endpoint enabled
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - vnet_name -- The virtual network name
    '''
    return _call_az("az mariadb server vnet-rule update", locals())

