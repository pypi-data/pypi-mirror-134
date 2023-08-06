from .... pyaz_utils import _call_az

def create(account_name, name, require_infrastructure_encryption=None, resource_group=None):
    '''
    Create an encryption scope within storage account.

    Required Parameters:
    - account_name -- The storage account name.
    - name -- The name of the encryption scope within the specified storage account.

    Optional Parameters:
    - require_infrastructure_encryption -- A boolean indicating whether or not the service applies a secondary layer of encryption with platform managed keys for data at rest.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage account encryption-scope create", locals())


def show(account_name, name, resource_group=None):
    '''
    Show properties for specified encryption scope within storage account.

    Required Parameters:
    - account_name -- The storage account name.
    - name -- The name of the encryption scope within the specified storage account.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage account encryption-scope show", locals())


def list(account_name, resource_group=None):
    '''
    List encryption scopes within storage account.

    Required Parameters:
    - account_name -- The storage account name.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage account encryption-scope list", locals())


def update(account_name, name, resource_group=None, state=None):
    '''
    Update properties for specified encryption scope within storage account.

    Required Parameters:
    - account_name -- The storage account name.
    - name -- The name of the encryption scope within the specified storage account.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - state -- Change the state the encryption scope. When disabled, all blob read/write operations using this encryption scope will fail.
    '''
    return _call_az("az storage account encryption-scope update", locals())

