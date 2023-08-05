'''
Manage Azure NetApp Files (ANF) Pool Resources.
'''
from ... pyaz_utils import _call_az

def show(account_name, pool_name, resource_group):
    '''
    Get the specified ANF pool.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az netappfiles pool show", locals())


def list(account_name, resource_group):
    '''
    L:ist the ANF pools for the specified account.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az netappfiles pool list", locals())


def delete(account_name, pool_name, resource_group):
    '''
    Delete the specified ANF pool.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az netappfiles pool delete", locals())


def create(account_name, location, pool_name, resource_group, service_level, size, cool_access=None, encryption_type=None, qos_type=None, tags=None):
    '''
    Create a new Azure NetApp Files (ANF) pool.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - service_level -- Service level
    - size -- Required. Provisioned size of the pool (in bytes). Allowed values are in 4TiB chunks (value must be multiply of 4398046511104).

    Optional Parameters:
    - cool_access -- If enabled (true) the pool can contain cool Access enabled volumes.
    - encryption_type -- Encryption type of the capacity pool, set encryption type for data at rest for this pool and all volumes in it. This value can only be set when creating new pool. Possible values include: "Single", "Double". Default value: "Single".
    - qos_type -- The qos type of the pool. Possible values include: "Auto", "Manual".
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az netappfiles pool create", locals())


def update(account_name, pool_name, resource_group, add=None, force_string=None, qos_type=None, remove=None, set=None, size=None, tags=None):
    '''
    Update the tags of the specified ANF pool.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - pool_name -- Name of the ANF pool.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - qos_type -- The qos type of the pool. Possible values include: "Auto", "Manual".
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - size -- Provisioned size of the pool (in bytes). Allowed values are in 4TiB chunks (value must be multiply of 4398046511104).
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az netappfiles pool update", locals())

