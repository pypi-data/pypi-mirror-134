'''
An item which is already protected or backed up to an Azure Recovery services vault with an associated policy.
'''
from ... pyaz_utils import _call_az

def show(container_name, name, resource_group, vault_name, backup_management_type=None, use_secondary_region=None, workload_type=None):
    '''
    Show details of a particular backed up item.

    Required Parameters:
    - container_name -- Name of the backup container. Accepts 'Name' or 'FriendlyName' from the output of az backup container list command. If 'FriendlyName' is passed then BackupManagementType is required.
    - name -- Name of the backed up item. You can use the backup item list command to get the name of a backed up item.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vault_name -- Name of the Recovery services vault.

    Optional Parameters:
    - backup_management_type -- Specify the backup management type. Define how Azure Backup manages the backup of entities within the ARM resource. For eg: AzureWorkloads refers to workloads installed within Azure VMs, AzureStorage refers to entities within Storage account. Required only if friendly name is used as Container name.
    - use_secondary_region -- Use this flag to show item in secondary region.
    - workload_type -- Specify the type of applications within the Resource which should be discovered and protected by Azure Backup. 
    '''
    return _call_az("az backup item show", locals())


def list(resource_group, vault_name, backup_management_type=None, container_name=None, use_secondary_region=None, workload_type=None):
    '''
    List all backed up items within a container.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vault_name -- Name of the Recovery services vault.

    Optional Parameters:
    - backup_management_type -- Specify the backup management type. Define how Azure Backup manages the backup of entities within the ARM resource. For eg: AzureWorkloads refers to workloads installed within Azure VMs, AzureStorage refers to entities within Storage account. Required only if friendly name is used as Container name.
    - container_name -- Name of the backup container. Accepts 'Name' or 'FriendlyName' from the output of az backup container list command. If 'FriendlyName' is passed then BackupManagementType is required.
    - use_secondary_region -- Use this flag to list items in secondary region.
    - workload_type -- Specify the type of applications within the Resource which should be discovered and protected by Azure Backup. 
    '''
    return _call_az("az backup item list", locals())


def set_policy(container_name, name, policy_name, resource_group, vault_name, backup_management_type=None, workload_type=None):
    '''
    Update the policy associated with this item. Use this to change policies of the backup item.

    Required Parameters:
    - container_name -- Name of the backup container. Accepts 'Name' or 'FriendlyName' from the output of az backup container list command. If 'FriendlyName' is passed then BackupManagementType is required.
    - name -- Name of the backed up item. You can use the backup item list command to get the name of a backed up item.
    - policy_name -- Name of the Backup policy. You can use the backup policy list command to get the name of a backup policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vault_name -- Name of the Recovery services vault.

    Optional Parameters:
    - backup_management_type -- Specify the backup management type. Define how Azure Backup manages the backup of entities within the ARM resource. For eg: AzureWorkloads refers to workloads installed within Azure VMs, AzureStorage refers to entities within Storage account. Required only if friendly name is used as Container name.
    - workload_type -- Specify the type of applications within the Resource which should be discovered and protected by Azure Backup. 
    '''
    return _call_az("az backup item set-policy", locals())

