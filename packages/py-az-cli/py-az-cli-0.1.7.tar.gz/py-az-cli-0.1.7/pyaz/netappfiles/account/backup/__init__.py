'''
Manage Azure NetApp Files (ANF) Account Backup Resources.
'''
from .... pyaz_utils import _call_az

def show(account_name, backup_name, resource_group):
    '''
    Get Backup for a Netapp Files (ANF) Account.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - backup_name -- The name of the backup.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az netappfiles account backup show", locals())


def list(account_name, resource_group):
    '''
    Get list of all Azure NetApp Files (ANF) Account Backups.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az netappfiles account backup list", locals())


def delete(account_name, backup_name, resource_group, yes=None):
    '''
    Delete Backup for a Netapp Files (ANF) Account.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - backup_name -- The name of the backup.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az netappfiles account backup delete", locals())

