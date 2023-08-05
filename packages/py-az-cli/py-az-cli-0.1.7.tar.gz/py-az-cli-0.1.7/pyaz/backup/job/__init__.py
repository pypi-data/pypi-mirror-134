'''
Entity which contains details of the job.
'''
from ... pyaz_utils import _call_az

def list(resource_group, vault_name, backup_management_type=None, end_date=None, operation=None, start_date=None, status=None, use_secondary_region=None):
    '''
    List all backup jobs of a Recovery Services vault.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vault_name -- Name of the Recovery services vault.

    Optional Parameters:
    - backup_management_type -- Specify the backup management type. Define how Azure Backup manages the backup of entities within the ARM resource. For eg: AzureWorkloads refers to workloads installed within Azure VMs, AzureStorage refers to entities within Storage account. Required only if friendly name is used as Container name.
    - end_date -- The end date of the range in UTC (d-m-Y).
    - operation -- User initiated operation.
    - start_date -- The start date of the range in UTC (d-m-Y).
    - status -- Status of the Job.
    - use_secondary_region -- Use this flag to show recoverypoints in secondary region.
    '''
    return _call_az("az backup job list", locals())


def show(name, resource_group, vault_name, use_secondary_region=None):
    '''
    Show details of a particular job.

    Required Parameters:
    - name -- Name of the job. You can use the backup job list command to get the name of a job.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vault_name -- Name of the Recovery services vault.

    Optional Parameters:
    - use_secondary_region -- Use this flag to show recoverypoints in secondary region.
    '''
    return _call_az("az backup job show", locals())


def stop(name, resource_group, vault_name, use_secondary_region=None):
    '''
    Suspend or terminate a currently running job.

    Required Parameters:
    - name -- Name of the job. You can use the backup job list command to get the name of a job.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vault_name -- Name of the Recovery services vault.

    Optional Parameters:
    - use_secondary_region -- Use this flag to show recoverypoints in secondary region.
    '''
    return _call_az("az backup job stop", locals())


def wait(name, resource_group, vault_name, timeout=None, use_secondary_region=None):
    '''
    Wait until either the job completes or the specified timeout value is reached.

    Required Parameters:
    - name -- Name of the job. You can use the backup job list command to get the name of a job.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vault_name -- Name of the Recovery services vault.

    Optional Parameters:
    - timeout -- Maximum time, in seconds, to wait before aborting.
    - use_secondary_region -- Use this flag to show recoverypoints in secondary region.
    '''
    return _call_az("az backup job wait", locals())

