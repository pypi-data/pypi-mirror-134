from .... pyaz_utils import _call_az

def set(account_name, container_name, tags, allow_protected_append_writes_all=None, resource_group=None):
    '''
    Set legal hold tags.

    Required Parameters:
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT.
    - container_name -- The container name.
    - tags -- Space-separated tags. Each tag should be 3 to 23 alphanumeric characters and is normalized to lower case

    Optional Parameters:
    - allow_protected_append_writes_all -- When enabled, new blocks can be written to both Append and Block Blobs while maintaining legal hold protection and compliance. Only new blocks can be added and any existing blocks cannot be modified or deleted.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage container legal-hold set", locals())


def clear(account_name, container_name, tags, allow_protected_append_writes_all=None, resource_group=None):
    '''
    Clear legal hold tags.

    Required Parameters:
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT.
    - container_name -- The container name.
    - tags -- Space-separated tags. Each tag should be 3 to 23 alphanumeric characters and is normalized to lower case

    Optional Parameters:
    - allow_protected_append_writes_all -- When enabled, new blocks can be written to both Append and Block Blobs while maintaining legal hold protection and compliance. Only new blocks can be added and any existing blocks cannot be modified or deleted.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage container legal-hold clear", locals())


def show(account_name, container_name, resource_group=None):
    '''
    Get the legal hold properties of a container.

    Required Parameters:
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT.
    - container_name -- The container name.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage container legal-hold show", locals())

