'''
Manage Azure Media Services accounts.
'''
from ... pyaz_utils import _call_az
from . import encryption, mru, sp, storage


def show(name, resource_group=None):
    '''
    Show the details of an Azure Media Services account.

    Required Parameters:
    - name -- The name of the Azure Media Services account.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams account show", locals())


def delete(name, resource_group):
    '''
    Delete an Azure Media Services account.

    Required Parameters:
    - name -- The name of the Azure Media Services account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams account delete", locals())


def update(name, resource_group, add=None, force_string=None, remove=None, set=None, tags=None):
    '''
    Update the details of an Azure Media Services account.

    Required Parameters:
    - name -- The name of the Azure Media Services account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az ams account update", locals())


def list(resource_group=None):
    '''
    List Azure Media Services accounts for the entire subscription.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams account list", locals())


def create(name, resource_group, storage_account, location=None, mi_system_assigned=None, tags=None):
    '''
    Create an Azure Media Services account.

    Required Parameters:
    - name -- The name of the Azure Media Services account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - storage_account -- The name or resource ID of the primary storage account to attach to the Azure Media Services account. The storage account MUST be in the same Azure subscription as the Media Services account. It is strongly recommended that the storage account be in the same resource group as the Media Services account. Blob only accounts are not allowed as primary.

    Optional Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - mi_system_assigned -- Set the system managed identity on the media services account.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az ams account create", locals())


def check_name(name, location=None):
    '''
    Checks whether the Media Service resource name is available.

    Required Parameters:
    - name -- The name of the Azure Media Services account.

    Optional Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    '''
    return _call_az("az ams account check-name", locals())

