from ... pyaz_utils import _call_az

def create(name, storage_account, default_encryption_scope=None, deny_encryption_scope_override=None, enable_vlw=None, fail_on_exist=None, metadata=None, public_access=None, resource_group=None, root_squash=None):
    '''
    Create a new container under the specified storage account.

    Required Parameters:
    - name -- The container name.
    - storage_account -- The name or ID of the storage account.

    Optional Parameters:
    - default_encryption_scope -- Default the container to use specified encryption scope for all writes.
    - deny_encryption_scope_override -- Block override of encryption scope from the container default.
    - enable_vlw -- The object level immutability property of the container. The property is immutable and can only be set to true at the container creation time. Existing containers must undergo a migration process.
    - fail_on_exist -- Throw an exception if the container already exists.
    - metadata -- Metadata in space-separated key=value pairs. This overwrites any existing metadata.
    - public_access -- Specify whether data in the container may be accessed publicly.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - root_squash -- Enable NFSv3 squash on blob container.
    '''
    return _call_az("az storage container-rm create", locals())


def delete(name, storage_account, resource_group=None, yes=None):
    '''
    Delete the specified container under its account.

    Required Parameters:
    - name -- The container name.
    - storage_account -- The name or ID of the storage account.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az storage container-rm delete", locals())


def update(name, storage_account, add=None, default_encryption_scope=None, deny_encryption_scope_override=None, force_string=None, metadata=None, public_access=None, remove=None, resource_group=None, root_squash=None, set=None):
    '''
    Update the properties for a container.

    Required Parameters:
    - name -- The container name.
    - storage_account -- The name or ID of the storage account.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - default_encryption_scope -- Default the container to use specified encryption scope for all writes.
    - deny_encryption_scope_override -- Block override of encryption scope from the container default.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - metadata -- Metadata in space-separated key=value pairs. This overwrites any existing metadata.
    - public_access -- Specify whether data in the container may be accessed publicly.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - root_squash -- Enable NFSv3 squash on blob container.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az storage container-rm update", locals())


def list(storage_account, include_deleted=None, resource_group=None):
    '''
    List all containers under the specified storage account.

    Required Parameters:
    - storage_account -- The name or ID of the storage account.

    Optional Parameters:
    - include_deleted -- Include soft deleted containers when specified.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage container-rm list", locals())


def exists(name, storage_account, resource_group=None):
    '''
    Check for the existence of a container.

    Required Parameters:
    - name -- The container name.
    - storage_account -- The name or ID of the storage account.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage container-rm exists", locals())


def show(name, storage_account, resource_group=None):
    '''
    Show the properties for a specified container.

    Required Parameters:
    - name -- The container name.
    - storage_account -- The name or ID of the storage account.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage container-rm show", locals())


def migrate_vlw(name, storage_account, no_wait=None, resource_group=None):
    '''
    Migrate a blob container from container level WORM to object level immutability enabled container.

    Required Parameters:
    - name -- The container name.
    - storage_account -- The name or ID of the storage account.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage container-rm migrate-vlw", locals())

