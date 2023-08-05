'''
Manage Azure NetApp Files (ANF) Vault Resources.
'''
from ... pyaz_utils import _call_az

def list(account_name, resource_group):
    '''
    List the ANF vaults for NetApp Account.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az netappfiles vault list", locals())

