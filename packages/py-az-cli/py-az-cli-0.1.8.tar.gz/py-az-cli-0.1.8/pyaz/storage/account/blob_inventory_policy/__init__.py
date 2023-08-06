from .... pyaz_utils import _call_az

def create(account_name, policy, resource_group=None):
    '''
    Create Blob Inventory Policy for storage account.

    Required Parameters:
    - account_name -- The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    - policy -- The Storage Account Blob Inventory Policy, string in JSON format or json file path. See more details in https://docs.microsoft.com/azure/storage/blobs/blob-inventory#inventory-policy.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage account blob-inventory-policy create", locals())


def update(account_name, add=None, force_string=None, remove=None, resource_group=None, set=None):
    '''
    Update Blob Inventory Policy associated with the specified storage account.

    Required Parameters:
    - account_name -- The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az storage account blob-inventory-policy update", locals())


def delete(account_name, resource_group=None, yes=None):
    '''
    Delete Blob Inventory Policy associated with the specified storage account.

    Required Parameters:
    - account_name -- The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az storage account blob-inventory-policy delete", locals())


def show(account_name, resource_group=None):
    '''
    Show Blob Inventory Policy properties associated with the specified storage account.

    Required Parameters:
    - account_name -- The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage account blob-inventory-policy show", locals())

