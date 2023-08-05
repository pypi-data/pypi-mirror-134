'''
Manage assets for an Azure Media Services account.
'''
from ... pyaz_utils import _call_az

def show(account_name, name, resource_group):
    '''
    Show the details of an asset.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the asset.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams asset show", locals())


def list(account_name, resource_group, filter=None, orderby=None, top=None):
    '''
    List all the assets of an Azure Media Services account.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - filter -- Restricts the set of items returned.
    - orderby -- Specifies the key by which the result collection should be ordered.
    - top -- Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n.
    '''
    return _call_az("az ams asset list", locals())


def delete(account_name, name, resource_group):
    '''
    Delete an asset.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the asset.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams asset delete", locals())


def list_streaming_locators(account_name, name, resource_group):
    '''
    List streaming locators which are associated with this asset.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the asset.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams asset list-streaming-locators", locals())


def get_encryption_key(account_name, name, resource_group):
    '''
    Get the asset storage encryption keys used to decrypt content created by version 2 of the Media Services API.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the asset.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams asset get-encryption-key", locals())


def update(account_name, name, resource_group, add=None, alternate_id=None, description=None, force_string=None, remove=None, set=None):
    '''
    Update the details of an asset.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the asset.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - alternate_id -- The alternate id of the asset.
    - description -- The asset description.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az ams asset update", locals())


def get_sas_urls(account_name, name, resource_group, expiry=None, permissions=None):
    '''
    Lists storage container URLs with shared access signatures (SAS) for uploading and downloading Asset content. The signatures are derived from the storage account keys.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the asset.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expiry -- Specifies the UTC datetime (Y-m-d'T'H:M:S'Z') at which the SAS becomes invalid. This must be less than 24 hours from the current time.
    - permissions -- The permissions to set on the SAS URL.
    '''
    return _call_az("az ams asset get-sas-urls", locals())


def create(account_name, name, resource_group, alternate_id=None, container=None, description=None, storage_account=None):
    '''
    Create an asset.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the asset.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - alternate_id -- The alternate id of the asset.
    - container -- The name of the asset blob container.
    - description -- The asset description.
    - storage_account -- The name of the storage account.
    '''
    return _call_az("az ams asset create", locals())

