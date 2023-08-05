from .... pyaz_utils import _call_az

def show(account_name, resource_group=None):
    '''
    Show the properties of a storage account's blob service.

    Required Parameters:
    - account_name -- The storage account name.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage account blob-service-properties show", locals())


def update(account_name, add=None, change_feed_retention_days=None, container_delete_retention_days=None, default_service_version=None, delete_retention_days=None, enable_change_feed=None, enable_container_delete_retention=None, enable_delete_retention=None, enable_last_access_tracking=None, enable_restore_policy=None, enable_versioning=None, force_string=None, remove=None, resource_group=None, restore_days=None, set=None):
    '''
    Update the properties of a storage account's blob service.

    Required Parameters:
    - account_name -- The storage account name.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - change_feed_retention_days -- Indicate the duration of changeFeed retention in days. Minimum value is 1 day and maximum value is 146000 days (400 years). A null value indicates an infinite retention of the change feed.(Use `--enable-change-feed` without `--change-feed-days` to indicate null)
    - container_delete_retention_days -- Indicate the number of days that the deleted container should be retained. The minimum specified value can be 1 and the maximum value can be 365.
    - default_service_version -- Indicate the default version to use for requests to the Blob service if an incoming request's version is not specified.
    - delete_retention_days -- None
    - enable_change_feed -- None
    - enable_container_delete_retention -- Enable container delete retention policy for container soft delete when set to true. Disable container delete retention policy when set to false.
    - enable_delete_retention -- None
    - enable_last_access_tracking -- When set to true last access time based tracking policy is enabled.
    - enable_restore_policy -- Enable blob restore policy when it set to true.
    - enable_versioning -- Versioning is enabled if set to true.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - restore_days -- The number of days for the blob can be restored. It should be greater than zero and less than Delete Retention Days.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az storage account blob-service-properties update", locals())

