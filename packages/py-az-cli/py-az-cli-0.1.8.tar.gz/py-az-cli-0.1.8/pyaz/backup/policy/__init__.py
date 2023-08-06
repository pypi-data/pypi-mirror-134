'''
A backup policy defines when you want to take a backup and for how long you would retain each backup copy.
'''
from ... pyaz_utils import _call_az

def get_default_for_vm(resource_group, vault_name):
    '''
    Get the default policy with default values to backup a VM.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vault_name -- Name of the Recovery services vault.
    '''
    return _call_az("az backup policy get-default-for-vm", locals())


def show(name, resource_group, vault_name):
    '''
    Show details of a particular policy.

    Required Parameters:
    - name -- Name of the backup policy. You can use the backup policy list command to get the name of a policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vault_name -- Name of the Recovery services vault.
    '''
    return _call_az("az backup policy show", locals())


def list(resource_group, vault_name, backup_management_type=None, workload_type=None):
    '''
    List all policies for a Recovery services vault.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vault_name -- Name of the Recovery services vault.

    Optional Parameters:
    - backup_management_type -- Specify the backup management type. Define how Azure Backup manages the backup of entities within the ARM resource. For eg: AzureWorkloads refers to workloads installed within Azure VMs, AzureStorage refers to entities within Storage account. Required only if friendly name is used as Container name.
    - workload_type -- Specify the type of applications within the Resource which should be discovered and protected by Azure Backup. 
    '''
    return _call_az("az backup policy list", locals())


def list_associated_items(name, resource_group, vault_name, backup_management_type=None):
    '''
    List all items protected by a backup policy.

    Required Parameters:
    - name -- Name of the backup policy. You can use the backup policy list command to get the name of a policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vault_name -- Name of the Recovery services vault.

    Optional Parameters:
    - backup_management_type -- Specify the backup management type. Define how Azure Backup manages the backup of entities within the ARM resource. For eg: AzureWorkloads refers to workloads installed within Azure VMs, AzureStorage refers to entities within Storage account. Required only if friendly name is used as Container name.
    '''
    return _call_az("az backup policy list-associated-items", locals())


def set(resource_group, vault_name, backup_management_type=None, fix_for_inconsistent_items=None, name=None, policy=None):
    '''
    Update the existing policy with the provided details.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vault_name -- Name of the Recovery services vault.

    Optional Parameters:
    - backup_management_type -- Specify the backup management type. Define how Azure Backup manages the backup of entities within the ARM resource. For eg: AzureWorkloads refers to workloads installed within Azure VMs, AzureStorage refers to entities within Storage account. Required only if friendly name is used as Container name.
    - fix_for_inconsistent_items -- Specify whether or not to retry Policy Update for failed items.
    - name -- Name of the Policy.
    - policy -- JSON encoded policy definition. Use the show command with JSON output to obtain a policy object. Modify the values using a file editor and pass the object.
    '''
    return _call_az("az backup policy set", locals())


def delete(name, resource_group, vault_name):
    '''
    Delete a backup policy which doesn't have any associated backup items.

    Required Parameters:
    - name -- Name of the backup policy. You can use the backup policy list command to get the name of a policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vault_name -- Name of the Recovery services vault.
    '''
    return _call_az("az backup policy delete", locals())


def create(backup_management_type, name, policy, resource_group, vault_name, workload_type=None):
    '''
    Create a new policy for the given BackupManagementType and workloadType.

    Required Parameters:
    - backup_management_type -- Specify the backup management type. Define how Azure Backup manages the backup of entities within the ARM resource. For eg: AzureWorkloads refers to workloads installed within Azure VMs, AzureStorage refers to entities within Storage account. Required only if friendly name is used as Container name.
    - name -- Name of the Policy.
    - policy -- JSON encoded policy definition. Use the show command with JSON output to obtain a policy object. Modify the values using a file editor and pass the object.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vault_name -- Name of the Recovery services vault.

    Optional Parameters:
    - workload_type -- Specify the type of applications within the Resource which should be discovered and protected by Azure Backup. 
    '''
    return _call_az("az backup policy create", locals())

