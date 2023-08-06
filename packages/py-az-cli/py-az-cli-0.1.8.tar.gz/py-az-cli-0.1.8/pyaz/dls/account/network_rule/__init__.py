from .... pyaz_utils import _call_az

def create(account_name, name, subnet, resource_group=None, vnet_name=None):
    '''
    Creates a virtual network rule in a Data Lake Store account.

    Required Parameters:
    - account_name -- Name of the Data Lake Store account.
    - name -- The virtual network rule name
    - subnet -- Name or ID of the subnet that allows access to DLS. If subnet name is provided, --name must be provided.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vnet_name -- The virtual network rule name
    '''
    return _call_az("az dls account network-rule create", locals())


def update(account_name, name, subnet, add=None, force_string=None, remove=None, resource_group=None, set=None, vnet_name=None):
    '''
    Updates a virtual network rule in a Data Lake Store account.

    Required Parameters:
    - account_name -- Name of the Data Lake Store account.
    - name -- The virtual network rule name
    - subnet -- Name or ID of the subnet that allows access to DLS. If subnet name is provided, --name must be provided.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - vnet_name -- The virtual network rule name
    '''
    return _call_az("az dls account network-rule update", locals())


def list(account_name, resource_group=None):
    '''
    Lists virtual network rules in a Data Lake Store account.

    Required Parameters:
    - account_name -- Name of the Data Lake Store account.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az dls account network-rule list", locals())


def show(account_name, name, resource_group=None):
    '''
    Get the details of a virtual network rule in a Data Lake Store account.

    Required Parameters:
    - account_name -- Name of the Data Lake Store account.
    - name -- The virtual network rule name

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az dls account network-rule show", locals())


def delete(account_name, name, resource_group=None):
    '''
    Deletes a virtual network rule in a Data Lake Store account.

    Required Parameters:
    - account_name -- Name of the Data Lake Store account.
    - name -- The virtual network rule name

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az dls account network-rule delete", locals())

