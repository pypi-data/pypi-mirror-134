'''
Manage Azure NetApp Files (ANF) Snapshot Policy Resources.
'''
from .... pyaz_utils import _call_az

def show(account_name, resource_group, snapshot_policy_name):
    '''
    Get the specified ANF snapshot policy.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - snapshot_policy_name -- The name of the snapshot policy
    '''
    return _call_az("az netappfiles snapshot policy show", locals())


def list(account_name, resource_group):
    '''
    List the ANF snapshot policies for the specified account.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az netappfiles snapshot policy list", locals())


def volumes(account_name, resource_group, snapshot_policy_name):
    '''
    Get the all ANF volumes associated with snapshot policy.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - snapshot_policy_name -- The name of the snapshot policy
    '''
    return _call_az("az netappfiles snapshot policy volumes", locals())


def delete(account_name, resource_group, snapshot_policy_name):
    '''
    Delete the specified ANF snapshot policy.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - snapshot_policy_name -- The name of the snapshot policy
    '''
    return _call_az("az netappfiles snapshot policy delete", locals())


def update(account_name, location, resource_group, snapshot_policy_name, daily_hour=None, daily_minute=None, daily_snapshots=None, enabled=None, hourly_minute=None, hourly_snapshots=None, monthly_days=None, monthly_hour=None, monthly_minute=None, monthly_snapshots=None, weekly_day=None, weekly_hour=None, weekly_minute=None, weekly_snapshots=None):
    '''
    Update the specified ANF snapshot policy.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - snapshot_policy_name -- The name of the snapshot policy

    Optional Parameters:
    - daily_hour -- None
    - daily_minute -- None
    - daily_snapshots -- The amount of daily snapshots to keep
    - enabled -- The property to decide policy is enabled or not.
    - hourly_minute -- None
    - hourly_snapshots -- The amount of hourly snapshots to keep
    - monthly_days -- None
    - monthly_hour -- None
    - monthly_minute -- None
    - monthly_snapshots -- The amount of monthly snapshots to keep
    - weekly_day -- None
    - weekly_hour -- None
    - weekly_minute -- None
    - weekly_snapshots -- The amount of weekly snapshots to keep
    '''
    return _call_az("az netappfiles snapshot policy update", locals())


def create(account_name, location, resource_group, snapshot_policy_name, daily_hour=None, daily_minute=None, daily_snapshots=None, enabled=None, hourly_minute=None, hourly_snapshots=None, monthly_days=None, monthly_hour=None, monthly_minute=None, monthly_snapshots=None, tags=None, weekly_day=None, weekly_hour=None, weekly_minute=None, weekly_snapshots=None):
    '''
    Create a new Azure NetApp Files (ANF) snapshot policy.

    Required Parameters:
    - account_name -- Name of the ANF account.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - snapshot_policy_name -- The name of the snapshot policy

    Optional Parameters:
    - daily_hour -- None
    - daily_minute -- None
    - daily_snapshots -- The amount of daily snapshots to keep
    - enabled -- The property to decide policy is enabled or not.
    - hourly_minute -- None
    - hourly_snapshots -- The amount of hourly snapshots to keep
    - monthly_days -- None
    - monthly_hour -- None
    - monthly_minute -- None
    - monthly_snapshots -- The amount of monthly snapshots to keep
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - weekly_day -- None
    - weekly_hour -- None
    - weekly_minute -- None
    - weekly_snapshots -- The amount of weekly snapshots to keep
    '''
    return _call_az("az netappfiles snapshot policy create", locals())

