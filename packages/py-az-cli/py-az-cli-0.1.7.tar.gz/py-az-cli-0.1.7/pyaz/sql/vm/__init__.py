'''
Manage SQL virtual machines.
'''
from ... pyaz_utils import _call_az
from . import group


def update(name, resource_group, add=None, backup_pwd=None, backup_schedule_type=None, backup_system_dbs=None, connectivity_type=None, credential_name=None, day_of_week=None, enable_auto_backup=None, enable_auto_patching=None, enable_encryption=None, enable_key_vault_credential=None, enable_r_services=None, force_string=None, full_backup_duration=None, full_backup_frequency=None, full_backup_start_hour=None, image_sku=None, key_vault=None, license_type=None, log_backup_frequency=None, maintenance_window_duration=None, maintenance_window_start_hour=None, port=None, remove=None, retention_period=None, sa_key=None, set=None, sp_name=None, sp_secret=None, sql_mgmt_type=None, sql_workload_type=None, storage_account=None, tags=None, yes=None):
    '''
    Updates the properties of a SQL virtual machine.

    Required Parameters:
    - name -- Name of the SQL virtual machine.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - backup_pwd -- Password for encryption on backup.
    - backup_schedule_type -- Backup schedule type.
    - backup_system_dbs -- Include system databases on backup.
    - connectivity_type -- SQL Server connectivity option.
    - credential_name -- Credential name
    - day_of_week -- Day of week to apply the patch on.
    - enable_auto_backup -- Enable or disable autobackup on SQL virtual machine. If any backup settings provided, parameter automatically sets to true.
    - enable_auto_patching -- Enable or disable autopatching on SQL virtual machine. If any autopatching settings provided, parameter automatically sets to true.
    - enable_encryption --  Enable encryption for backup on SQL virtual machine.
    - enable_key_vault_credential -- Enable or disable key vault credential setting. If any key vault settings provided, parameter automatically sets to true.
    - enable_r_services -- Enable or disable R services (SQL 2016 onwards).
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - full_backup_duration -- Duration of the time window of a given day during which full backups can take place. 1-23 hours.
    - full_backup_frequency -- Frequency of full backups. In both cases, full backups begin during the next scheduled time window.
    - full_backup_start_hour -- Start time of a given day during which full backups can take place. 0-23 hours.
    - image_sku -- SQL image sku.
    - key_vault -- Azure Key Vault url.
    - license_type -- SQL Server license type.
    - log_backup_frequency -- Frequency of log backups. 5-60 minutes.
    - maintenance_window_duration -- Duration of patching. 30-180 minutes.
    - maintenance_window_start_hour -- Hour of the day when patching is initiated. Local VM time 0-23 hours.
    - port -- SQL Server port.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - retention_period -- Retention period of backup. 1-30 days.
    - sa_key -- Storage account key where backup will be taken to.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - sp_name -- Service principal name to access key vault.
    - sp_secret -- Service principal name secret to access key vault.
    - sql_mgmt_type -- SQL Server management type. Updates from LightWeight to Full.
    - sql_workload_type -- SQL Server workload type.
    - storage_account -- Storage account url where backup will be taken to.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - yes -- Do not prompt for confirmation. Requires --sql-mgmt-type.
    '''
    return _call_az("az sql vm update", locals())


def show(name, resource_group, expand=None):
    '''
    

    Required Parameters:
    - name -- Name of the SQL virtual machine.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expand -- Get the SQLIaaSExtension configuration settings. To view all settings, use *. To select only a few, the settings must be space-separted.
    '''
    return _call_az("az sql vm show", locals())


def list(resource_group=None):
    '''
    

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql vm list", locals())


def add_to_group(name, resource_group, sqlvm_group, operator_acc_pwd=None, service_acc_pwd=None):
    '''
    Adds SQL virtual machine to a SQL virtual machine group.

    Required Parameters:
    - name -- Name of the SQL virtual machine.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sqlvm_group -- Name or resource ID of the SQL virtual machine group. If only name provided, SQL virtual machine group should be in the same resource group of the SQL virtual machine.

    Optional Parameters:
    - operator_acc_pwd -- Password for the cluster operator account provided in the SQL virtual machine group.
    - service_acc_pwd -- Password for the SQL service account provided in the SQL virtual machine group.
    '''
    return _call_az("az sql vm add-to-group", locals())


def remove_from_group(name, resource_group):
    '''
    Remove SQL virtual machine from its current SQL virtual machine group.

    Required Parameters:
    - name -- Name of the SQL virtual machine.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql vm remove-from-group", locals())


def delete(name, resource_group, yes=None):
    '''
    

    Required Parameters:
    - name -- Name of the SQL virtual machine.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az sql vm delete", locals())


def create(name, resource_group, backup_pwd=None, backup_schedule_type=None, backup_system_dbs=None, connectivity_type=None, credential_name=None, day_of_week=None, enable_auto_backup=None, enable_auto_patching=None, enable_encryption=None, enable_key_vault_credential=None, enable_r_services=None, full_backup_duration=None, full_backup_frequency=None, full_backup_start_hour=None, image_offer=None, image_sku=None, key_vault=None, license_type=None, location=None, log_backup_frequency=None, maintenance_window_duration=None, maintenance_window_start_hour=None, port=None, retention_period=None, sa_key=None, sp_name=None, sp_secret=None, sql_auth_update_pwd=None, sql_auth_update_username=None, sql_mgmt_type=None, sql_workload_type=None, storage_account=None, tags=None):
    '''
    Creates a SQL virtual machine.

    Required Parameters:
    - name -- Name of the SQL virtual machine.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - backup_pwd -- Password for encryption on backup.
    - backup_schedule_type -- Backup schedule type.
    - backup_system_dbs -- Include system databases on backup.
    - connectivity_type -- SQL Server connectivity option.
    - credential_name -- Credential name
    - day_of_week -- Day of week to apply the patch on.
    - enable_auto_backup -- Enable or disable autobackup on SQL virtual machine. If any backup settings provided, parameter automatically sets to true.
    - enable_auto_patching -- Enable or disable autopatching on SQL virtual machine. If any autopatching settings provided, parameter automatically sets to true.
    - enable_encryption --  Enable encryption for backup on SQL virtual machine.
    - enable_key_vault_credential -- Enable or disable key vault credential setting. If any key vault settings provided, parameter automatically sets to true.
    - enable_r_services -- Enable or disable R services (SQL 2016 onwards).
    - full_backup_duration -- Duration of the time window of a given day during which full backups can take place. 1-23 hours.
    - full_backup_frequency -- Frequency of full backups. In both cases, full backups begin during the next scheduled time window.
    - full_backup_start_hour -- Start time of a given day during which full backups can take place. 0-23 hours.
    - image_offer -- SQL image offer. Examples include SQL2008R2-WS2008, SQL2008-WS2008.
    - image_sku -- SQL image sku.
    - key_vault -- Azure Key Vault url.
    - license_type -- SQL Server license type.
    - location -- Location. If not provided, virtual machine should be in the same region of resource group.You can configure the default location using `az configure --defaults location=<location>`.
    - log_backup_frequency -- Frequency of log backups. 5-60 minutes.
    - maintenance_window_duration -- Duration of patching. 30-180 minutes.
    - maintenance_window_start_hour -- Hour of the day when patching is initiated. Local VM time 0-23 hours.
    - port -- SQL Server port.
    - retention_period -- Retention period of backup. 1-30 days.
    - sa_key -- Storage account key where backup will be taken to.
    - sp_name -- Service principal name to access key vault.
    - sp_secret -- Service principal name secret to access key vault.
    - sql_auth_update_pwd -- SQL Server sysadmin login password.
    - sql_auth_update_username -- SQL Server sysadmin login to create.
    - sql_mgmt_type -- SQL Server management type. If NoAgent selected, please provide --image-sku and --offer-type.
    - sql_workload_type -- SQL Server workload type.
    - storage_account -- Storage account url where backup will be taken to.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az sql vm create", locals())

