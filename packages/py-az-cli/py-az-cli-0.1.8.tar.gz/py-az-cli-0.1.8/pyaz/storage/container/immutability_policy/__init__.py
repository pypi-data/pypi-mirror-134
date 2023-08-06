from .... pyaz_utils import _call_az

def show(account_name, container_name, if_match=None, resource_group=None):
    '''
    

    Required Parameters:
    - account_name -- The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    - container_name -- The container name.

    Optional Parameters:
    - if_match -- The entity state (ETag) version of the immutability policy to update. A value of "*" can be used to apply the operation only if the immutability policy already exists. If omitted, this operation will always be applied.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage container immutability-policy show", locals())


def create(account_name, container_name, allow_protected_append_writes=None, allow_protected_append_writes_all=None, if_match=None, period=None, resource_group=None):
    '''
    Create or update an unlocked immutability policy.

    Required Parameters:
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT.
    - container_name -- The container name.

    Optional Parameters:
    - allow_protected_append_writes -- This property can only be changed for unlocked time-based retention policies. When enabled, new blocks can be written to an append blob while maintaining immutability protection and compliance. Only new blocks can be added and any existing blocks cannot be modified or deleted. This property cannot be changed with ExtendImmutabilityPolicy API.
    - allow_protected_append_writes_all -- This property can only be changed for unlocked time-based retention policies. When enabled, new blocks can be written to both 'Append and Block Blobs' while maintaining immutability protection and compliance. Only new blocks can be added and any existing blocks cannot be modified or deleted. This property cannot be changed with ExtendImmutabilityPolicy API. The 'allowProtectedAppendWrites' and 'allowProtectedAppendWritesAll' properties are mutually exclusive.
    - if_match -- An ETag value, or the wildcard character (*). Specify this header to perform the operation only if the resource's ETag matches the value specified.
    - period -- The immutability period for the blobs in the container since the policy creation, in days.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage container immutability-policy create", locals())


def delete(account_name, container_name, if_match, resource_group=None):
    '''
    

    Required Parameters:
    - account_name -- The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    - container_name -- The container name.
    - if_match -- The entity state (ETag) version of the immutability policy to update. A value of "*" can be used to apply the operation only if the immutability policy already exists. If omitted, this operation will always be applied.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage container immutability-policy delete", locals())


def lock(account_name, container_name, if_match, resource_group=None):
    '''
    

    Required Parameters:
    - account_name -- The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    - container_name -- The container name.
    - if_match -- The entity state (ETag) version of the immutability policy to update. A value of "*" can be used to apply the operation only if the immutability policy already exists. If omitted, this operation will always be applied.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage container immutability-policy lock", locals())


def extend(account_name, container_name, if_match, allow_protected_append_writes=None, allow_protected_append_writes_all=None, period=None, resource_group=None):
    '''
    Extend the immutabilityPeriodSinceCreationInDays of a locked immutabilityPolicy.

    Required Parameters:
    - account_name -- Storage account name. Related environment variable: AZURE_STORAGE_ACCOUNT.
    - container_name -- The container name.
    - if_match -- An ETag value, or the wildcard character (*). Specify this header to perform the operation only if the resource's ETag matches the value specified.

    Optional Parameters:
    - allow_protected_append_writes -- This property can only be changed for unlocked time-based retention policies. When enabled, new blocks can be written to an append blob while maintaining immutability protection and compliance. Only new blocks can be added and any existing blocks cannot be modified or deleted. This property cannot be changed with ExtendImmutabilityPolicy API.
    - allow_protected_append_writes_all -- This property can only be changed for unlocked time-based retention policies. When enabled, new blocks can be written to both 'Append and Block Blobs' while maintaining immutability protection and compliance. Only new blocks can be added and any existing blocks cannot be modified or deleted. This property cannot be changed with ExtendImmutabilityPolicy API. The 'allowProtectedAppendWrites' and 'allowProtectedAppendWritesAll' properties are mutually exclusive.
    - period -- The immutability period for the blobs in the container since the policy creation, in days.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage container immutability-policy extend", locals())

