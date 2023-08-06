'''
Resource which houses items or applications to be protected.
'''
from ... pyaz_utils import _call_az

def show(name, resource_group, vault_name, backup_management_type=None, use_secondary_region=None):
    '''
    Show details of a container registered to a Recovery services vault.

    Required Parameters:
    - name -- Name of the container. You can use the backup container list command to get the name of a container.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vault_name -- Name of the Recovery services vault.

    Optional Parameters:
    - backup_management_type -- Specify the backup management type. Define how Azure Backup manages the backup of entities within the ARM resource. For eg: AzureWorkloads refers to workloads installed within Azure VMs, AzureStorage refers to entities within Storage account. Required only if friendly name is used as Container name.
    - use_secondary_region -- Use this flag to show container in secondary region.
    '''
    return _call_az("az backup container show", locals())


def list(backup_management_type, resource_group, vault_name, use_secondary_region=None):
    '''
    List containers registered to a Recovery services vault.

    Required Parameters:
    - backup_management_type -- Specify the backup management type. Define how Azure Backup manages the backup of entities within the ARM resource. For eg: AzureWorkloads refers to workloads installed within Azure VMs, AzureStorage refers to entities within Storage account. Required only if friendly name is used as Container name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vault_name -- Name of the Recovery services vault.

    Optional Parameters:
    - use_secondary_region -- Use this flag to list containers in secondary region.
    '''
    return _call_az("az backup container list", locals())


def unregister(container_name, resource_group, vault_name, backup_management_type=None, yes=None):
    '''
    Unregister a Backup Container to make the underlying 'resource' be protected by another vault.

    Required Parameters:
    - container_name -- Name of the backup container. Accepts 'Name' or 'FriendlyName' from the output of az backup container list command. If 'FriendlyName' is passed then BackupManagementType is required.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vault_name -- Name of the Recovery services vault.

    Optional Parameters:
    - backup_management_type -- Specify the backup management type. Define how Azure Backup manages the backup of entities within the ARM resource. For eg: AzureWorkloads refers to workloads installed within Azure VMs, AzureStorage refers to entities within Storage account. Required only if friendly name is used as Container name.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az backup container unregister", locals())


def re_register(container_name, resource_group, vault_name, workload_type, backup_management_type=None, yes=None):
    '''
    Reset the registration details for a given container.

    Required Parameters:
    - container_name -- Name of the backup container. Accepts 'Name' or 'FriendlyName' from the output of az backup container list command. If 'FriendlyName' is passed then BackupManagementType is required.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vault_name -- Name of the Recovery services vault.
    - workload_type -- Specify the type of applications within the Resource which should be discovered and protected by Azure Backup. 

    Optional Parameters:
    - backup_management_type -- Specify the backup management type. Define how Azure Backup manages the backup of entities within the ARM resource. For eg: AzureWorkloads refers to workloads installed within Azure VMs, AzureStorage refers to entities within Storage account. Required only if friendly name is used as Container name.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az backup container re-register", locals())


def register(resource_group, resource_id, vault_name, workload_type, backup_management_type=None):
    '''
    Register a Resource to the given Recovery Services Vault.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_id -- ID of the Azure Resource containing items to be protected by Azure Backup service. Currently, only Azure VM resource IDs are supported.
    - vault_name -- Name of the Recovery services vault.
    - workload_type -- Specify the type of applications within the Resource which should be discovered and protected by Azure Backup. 

    Optional Parameters:
    - backup_management_type -- Specify the backup management type. Define how Azure Backup manages the backup of entities within the ARM resource. For eg: AzureWorkloads refers to workloads installed within Azure VMs, AzureStorage refers to entities within Storage account. Required only if friendly name is used as Container name.
    '''
    return _call_az("az backup container register", locals())

