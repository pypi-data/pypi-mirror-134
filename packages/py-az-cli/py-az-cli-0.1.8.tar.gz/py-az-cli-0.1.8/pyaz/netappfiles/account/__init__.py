'''
Manage Azure NetApp Files (ANF) Account Resources.
'''
from ... pyaz_utils import _call_az
from . import ad, backup, backup_policy


def show(name, resource_group):
    '''
    Get the specified ANF account.

    Required Parameters:
    - name -- Name of the ANF account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az netappfiles account show", locals())


def delete(name, resource_group):
    '''
    Delete the specified ANF account.

    Required Parameters:
    - name -- Name of the ANF account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az netappfiles account delete", locals())


def list(resource_group=None):
    '''
    List ANF accounts by subscription or by resource group name.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az netappfiles account list", locals())


def create(location, name, resource_group, encryption=None, tags=None):
    '''
    Create a new Azure NetApp Files (ANF) account. Note that active directories are added using the subgroup commands.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- Name of the ANF account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - encryption -- Encryption settings.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az netappfiles account create", locals())


def update(name, resource_group, add=None, encryption=None, force_string=None, remove=None, set=None, tags=None):
    '''
    Set/modify the tags for a specified ANF account.

    Required Parameters:
    - name -- Name of the ANF account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - encryption -- Encryption settings.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az netappfiles account update", locals())

