from .... pyaz_utils import _call_az

def delete(account_name=None, id=None, name=None, resource_group=None, yes=None):
    '''
    Delete a private endpoint connection request for storage account.

    Optional Parameters:
    - account_name -- The storage account name.
    - id -- The ID of the private endpoint connection associated with the Storage Account. You can get it using `az storage account show`.
    - name -- The name of the private endpoint connection associated with the Storage Account.
    - resource_group -- The resource group name of specified storage account.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az storage account private-endpoint-connection delete", locals())


def show(account_name=None, id=None, name=None, resource_group=None):
    '''
    Show details of a private endpoint connection request for storage account.

    Optional Parameters:
    - account_name -- The storage account name.
    - id -- The ID of the private endpoint connection associated with the Storage Account. You can get it using `az storage account show`.
    - name -- The name of the private endpoint connection associated with the Storage Account.
    - resource_group -- The resource group name of specified storage account.
    '''
    return _call_az("az storage account private-endpoint-connection show", locals())


def approve(account_name=None, description=None, id=None, name=None, resource_group=None):
    '''
    Approve a private endpoint connection request for storage account.

    Optional Parameters:
    - account_name -- The storage account name.
    - description -- Comments for approve operation.
    - id -- The ID of the private endpoint connection associated with the Storage Account. You can get it using `az storage account show`.
    - name -- The name of the private endpoint connection associated with the Storage Account.
    - resource_group -- The resource group name of specified storage account.
    '''
    return _call_az("az storage account private-endpoint-connection approve", locals())


def reject(account_name=None, description=None, id=None, name=None, resource_group=None):
    '''
    Reject a private endpoint connection request for storage account.

    Optional Parameters:
    - account_name -- The storage account name.
    - description -- Comments for reject operation.
    - id -- The ID of the private endpoint connection associated with the Storage Account. You can get it using `az storage account show`.
    - name -- The name of the private endpoint connection associated with the Storage Account.
    - resource_group -- The resource group name of specified storage account.
    '''
    return _call_az("az storage account private-endpoint-connection reject", locals())

