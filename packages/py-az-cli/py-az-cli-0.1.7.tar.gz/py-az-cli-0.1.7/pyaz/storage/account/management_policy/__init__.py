from .... pyaz_utils import _call_az

def show(account_name, resource_group):
    '''
    Get the data policy rules associated with the specified storage account.

    Required Parameters:
    - account_name -- The name of the storage account within the specified resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage account management-policy show", locals())


def create(account_name, policy, resource_group):
    '''
    Create the data policy rules associated with the specified storage account.

    Required Parameters:
    - account_name -- The name of the storage account within the specified resource group.
    - policy -- The Storage Account ManagementPolicies Rules, in JSON format. See more details in: https://docs.microsoft.com/azure/storage/common/storage-lifecycle-managment-concepts.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage account management-policy create", locals())


def update(account_name, resource_group, add=None, force_string=None, remove=None, set=None):
    '''
    Update the data policy rules associated with the specified storage account.

    Required Parameters:
    - account_name -- The name of the storage account within the specified resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az storage account management-policy update", locals())


def delete(account_name, resource_group):
    '''
    Delete the data policy rules associated with the specified storage account.

    Required Parameters:
    - account_name -- The name of the storage account within the specified resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage account management-policy delete", locals())

