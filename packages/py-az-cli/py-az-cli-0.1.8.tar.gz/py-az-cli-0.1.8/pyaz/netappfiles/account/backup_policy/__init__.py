from .... pyaz_utils import _call_az

def show(account_name, backup_policy_name, resource_group):
    '''
    Get the specified ANF backup policy.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - backup_policy_name -- The name of the backup policy
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az netappfiles account backup-policy show", locals())


def list(account_name, resource_group):
    '''
    List the ANF backup policy for the specified account.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az netappfiles account backup-policy list", locals())


def delete(account_name, backup_policy_name, resource_group):
    '''
    Delete the specified ANF backup policy.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - backup_policy_name -- The name of the backup policy
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az netappfiles account backup-policy delete", locals())


def update(account_name, backup_policy_name, resource_group, daily_backups=None, enabled=None, location=None, monthly_backups=None, tags=None, weekly_backups=None):
    '''
    Update the specified ANF backup policy.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - backup_policy_name -- The name of the backup policy
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - daily_backups -- Daily backups count to keep
    - enabled -- The property to decide policy is enabled or not.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - monthly_backups -- Monthly backups count to keep
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - weekly_backups -- Weekly backups count to keep
    '''
    return _call_az("az netappfiles account backup-policy update", locals())


def create(account_name, backup_policy_name, location, resource_group, daily_backups=None, enabled=None, monthly_backups=None, tags=None, weekly_backups=None):
    '''
    Create a new Azure NetApp Files (ANF) backup policy.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - backup_policy_name -- The name of the backup policy
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - daily_backups -- Daily backups count to keep
    - enabled -- The property to decide policy is enabled or not.
    - monthly_backups -- Monthly backups count to keep
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - weekly_backups -- Weekly backups count to keep
    '''
    return _call_az("az netappfiles account backup-policy create", locals())

