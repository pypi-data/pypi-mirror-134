from .... pyaz_utils import _call_az

def list(account_name, resource_group):
    '''
    Get the private link resources that need to be created for a storage account.

    Required Parameters:
    - account_name -- The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage account private-link-resource list", locals())

