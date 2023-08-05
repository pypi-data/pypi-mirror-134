from .... pyaz_utils import _call_az

def show(account_name, resource_group=None):
    '''
    Show the properties of file service in storage account.

    Required Parameters:
    - account_name -- The storage account name.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage account file-service-properties show", locals())


def update(account_name, add=None, auth_methods=None, channel_encryption=None, delete_retention_days=None, enable_delete_retention=None, enable_smb_multichannel=None, force_string=None, kerb_ticket_encryption=None, remove=None, resource_group=None, set=None, versions=None):
    '''
    Update the properties of file service in storage account.

    Required Parameters:
    - account_name -- The storage account name.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - auth_methods -- SMB authentication methods supported by server. Valid values are NTLMv2, Kerberos. Should be passed as a string with delimiter ';'.
    - channel_encryption -- SMB channel encryption supported by server. Valid values are AES-128-CCM, AES-128-GCM, AES-256-GCM. Should be passed as a string with delimiter ';' 
    - delete_retention_days -- Indicate the number of days that the deleted item should be retained. The minimum specified value can be 1 and the maximum value can be 365.
    - enable_delete_retention -- Enable file service properties for share soft delete.
    - enable_smb_multichannel -- Set SMB Multichannel setting for file service. Applies to Premium FileStorage only.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - kerb_ticket_encryption -- Kerberos ticket encryption supported by server. Valid values are RC4-HMAC, AES-256. Should be passed as a string with delimiter ';'.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - versions -- SMB protocol versions supported by server. Valid values are SMB2.1, SMB3.0, SMB3.1.1. Should be passed as a string with delimiter ';'.
    '''
    return _call_az("az storage account file-service-properties update", locals())

