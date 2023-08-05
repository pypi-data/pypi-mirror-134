from .. pyaz_utils import _call_az

def create(key_url, name, resource_group, source_vault, enable_auto_key_rotation=None, encryption_type=None, location=None, no_wait=None, tags=None):
    '''
    Create a disk encryption set.

    Required Parameters:
    - key_url -- URL pointing to a key or secret in KeyVault.
    - name -- Name of disk encryption set.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - source_vault -- Name or ID of the KeyVault containing the key or secret.

    Optional Parameters:
    - enable_auto_key_rotation -- Enable automatic rotation of keys.
    - encryption_type -- The type of key used to encrypt the data of the disk. EncryptionAtRestWithPlatformKey: Disk is encrypted at rest with Platform managed key. It is the default encryption type. EncryptionAtRestWithCustomerKey: Disk is encrypted at rest with Customer managed key that can be changed and revoked by a customer. EncryptionAtRestWithPlatformAndCustomerKeys: Disk is encrypted at rest with 2 layers of encryption. One of the keys is Customer managed and the other key is Platform managed.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - no_wait -- Do not wait for the long-running operation to finish.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az disk-encryption-set create", locals())


def delete(name, resource_group):
    '''
    Delete a disk encryption set.

    Required Parameters:
    - name -- Name of disk encryption set.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az disk-encryption-set delete", locals())


def update(name, resource_group, add=None, enable_auto_key_rotation=None, force_string=None, key_url=None, remove=None, set=None, source_vault=None):
    '''
    Update a disk encryption set.

    Required Parameters:
    - name -- Name of disk encryption set.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - enable_auto_key_rotation -- Enable automatic rotation of keys.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - key_url -- URL pointing to a key or secret in KeyVault.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - source_vault -- Name or ID of the KeyVault containing the key or secret.
    '''
    return _call_az("az disk-encryption-set update", locals())


def show(name, resource_group):
    '''
    Get information of a disk encryption sets.

    Required Parameters:
    - name -- Name of disk encryption set.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az disk-encryption-set show", locals())


def list(resource_group=None):
    '''
    List disk encryption sets.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az disk-encryption-set list", locals())


def list_associated_resources(name, resource_group):
    '''
    

    Required Parameters:
    - name -- Name of disk encryption set.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az disk-encryption-set list-associated-resources", locals())

