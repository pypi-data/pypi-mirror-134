'''
Manage databases.
'''
from ... pyaz_utils import _call_az
from . import audit_policy, classification, ledger_digest_uploads, ltr_backup, ltr_policy, op, replica, str_policy, tde, threat_policy


def show_connection_string(client, auth_type=None, name=None, server=None):
    '''
    Generates a connection string to a database.

    Required Parameters:
    - client -- Type of client connection provider.

    Optional Parameters:
    - auth_type -- Type of authentication.
    - name -- Name of the Azure SQL Database.
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql db show-connection-string", locals())


def create(name, resource_group, server, auto_pause_delay=None, backup_storage_redundancy=None, capacity=None, catalog_collation=None, collation=None, compute_model=None, elastic_pool=None, family=None, ledger_on=None, license_type=None, maint_config_id=None, max_size=None, min_capacity=None, no_wait=None, read_replicas=None, read_scale=None, sample_name=None, service_objective=None, tags=None, tier=None, yes=None, zone_redundant=None):
    '''
    Create a database.

    Required Parameters:
    - name -- Name of the Azure SQL Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`

    Optional Parameters:
    - auto_pause_delay -- Time in minutes after which database is automatically paused. A value of -1 means that automatic pause is disabled.
    - backup_storage_redundancy -- Backup storage redundancy used to store backups. Allowed values include: Local, Zone, Geo.
    - capacity -- The capacity component of the sku in integer number of DTUs or vcores.
    - catalog_collation -- Collation of the metadata catalog. Possible values include: "DATABASE_DEFAULT", "SQL_Latin1_General_CP1_CI_AS".
    - collation -- The collation of the database.
    - compute_model -- The compute model of the database.
    - elastic_pool -- The name or resource id of the elastic pool to create the database in.
    - family -- The compute generation component of the sku (for vcore skus only). Allowed values include: Gen4, Gen5.
    - ledger_on -- Create a ledger database, in which the integrity of all data is protected by the ledger feature. All tables in the ledger database must be ledger tables. Note: the value of this property cannot be changed after the database has been created. 
    - license_type -- The license type to apply for this database. ``LicenseIncluded`` if you need a license, or ``BasePrice`` if you have a license and are eligible for the Azure Hybrid Benefit. Possible values include: "LicenseIncluded", "BasePrice".
    - maint_config_id -- Specified maintenance configuration id or name for this resource.
    - max_size -- The max storage size. If no unit is specified, defaults to bytes (B).
    - min_capacity -- Minimal capacity that database will always have allocated, if not paused
    - no_wait -- Do not wait for the long-running operation to finish.
    - read_replicas -- The number of high availability replicas to provision for the database. Only settable for Hyperscale edition.
    - read_scale -- If enabled, connections that have application intent set to readonly in their connection string may be routed to a readonly secondary replica. This property is only settable for Premium and Business Critical databases.
    - sample_name -- The name of the sample schema to apply when creating this database. Possible values include: "AdventureWorksLT", "WideWorldImportersStd", "WideWorldImportersFull".
    - service_objective -- The service objective for the new database. For example: Basic, S0, P1, GP_Gen4_1, GP_Gen5_S_8, BC_Gen5_2, HS_Gen5_32.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - tier -- The edition component of the sku. Allowed values include: Basic, Standard, Premium, GeneralPurpose, BusinessCritical, Hyperscale.
    - yes -- Do not prompt for confirmation.
    - zone_redundant -- Specifies whether to enable zone redundancy
    '''
    return _call_az("az sql db create", locals())


def copy(dest_name, name, resource_group, server, auto_pause_delay=None, backup_storage_redundancy=None, capacity=None, compute_model=None, dest_resource_group=None, dest_server=None, elastic_pool=None, family=None, license_type=None, min_capacity=None, no_wait=None, read_replicas=None, read_scale=None, service_objective=None, tags=None, zone_redundant=None):
    '''
    Create a copy of a database.

    Required Parameters:
    - dest_name -- Name of the database that will be created as the copy destination.
    - name -- Name of the Azure SQL Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`

    Optional Parameters:
    - auto_pause_delay -- Time in minutes after which database is automatically paused. A value of -1 means that automatic pause is disabled.
    - backup_storage_redundancy -- Backup storage redundancy used to store backups. Allowed values include: Local, Zone, Geo.
    - capacity -- The capacity component of the sku in integer number of DTUs or vcores.
    - compute_model -- The compute model of the database.
    - dest_resource_group -- Name of the resouce group to create the copy in. If unspecified, defaults to the origin resource group.
    - dest_server -- Name of the server to create the copy in. If unspecified, defaults to the origin server.
    - elastic_pool -- The name or resource id of the elastic pool to create the database in.
    - family -- The compute generation component of the sku (for vcore skus only). Allowed values include: Gen4, Gen5.
    - license_type -- The license type to apply for this database. ``LicenseIncluded`` if you need a license, or ``BasePrice`` if you have a license and are eligible for the Azure Hybrid Benefit. Possible values include: "LicenseIncluded", "BasePrice".
    - min_capacity -- Minimal capacity that database will always have allocated, if not paused
    - no_wait -- Do not wait for the long-running operation to finish.
    - read_replicas -- The number of high availability replicas to provision for the database. Only settable for Hyperscale edition.
    - read_scale -- If enabled, connections that have application intent set to readonly in their connection string may be routed to a readonly secondary replica. This property is only settable for Premium and Business Critical databases.
    - service_objective -- The service objective for the new database. For example: Basic, S0, P1, GP_Gen4_1, GP_Gen5_S_8, BC_Gen5_2, HS_Gen5_32.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - zone_redundant -- Specifies whether to enable zone redundancy
    '''
    return _call_az("az sql db copy", locals())


def restore(dest_name, name, resource_group, server, auto_pause_delay=None, backup_storage_redundancy=None, capacity=None, compute_model=None, deleted_time=None, elastic_pool=None, family=None, license_type=None, min_capacity=None, no_wait=None, read_replicas=None, read_scale=None, service_objective=None, tags=None, tier=None, time=None, zone_redundant=None):
    '''
    Create a new database by restoring from a backup.

    Required Parameters:
    - dest_name -- Name of the database that will be created as the restore destination.
    - name -- Name of the Azure SQL Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`

    Optional Parameters:
    - auto_pause_delay -- Time in minutes after which database is automatically paused. A value of -1 means that automatic pause is disabled.
    - backup_storage_redundancy -- Backup storage redundancy used to store backups. Allowed values include: Local, Zone, Geo.
    - capacity -- The capacity component of the sku in integer number of DTUs or vcores.
    - compute_model -- The compute model of the database.
    - deleted_time -- If specified, restore from a deleted database instead of from an existing database. Must match the deleted time of a deleted database in the same server. Either --time or --deleted-time (or both) must be specified. Time should be in following format: "YYYY-MM-DDTHH:MM:SS".
    - elastic_pool -- The name or resource id of the elastic pool to create the database in.
    - family -- The compute generation component of the sku (for vcore skus only). Allowed values include: Gen4, Gen5.
    - license_type -- The license type to apply for this database. ``LicenseIncluded`` if you need a license, or ``BasePrice`` if you have a license and are eligible for the Azure Hybrid Benefit. Possible values include: "LicenseIncluded", "BasePrice".
    - min_capacity -- Minimal capacity that database will always have allocated, if not paused
    - no_wait -- Do not wait for the long-running operation to finish.
    - read_replicas -- The number of high availability replicas to provision for the database. Only settable for Hyperscale edition.
    - read_scale -- If enabled, connections that have application intent set to readonly in their connection string may be routed to a readonly secondary replica. This property is only settable for Premium and Business Critical databases.
    - service_objective -- The service objective for the new database. For example: Basic, S0, P1, GP_Gen4_1, GP_Gen5_S_8, BC_Gen5_2, HS_Gen5_32.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - tier -- The edition component of the sku. Allowed values include: Basic, Standard, Premium, GeneralPurpose, BusinessCritical, Hyperscale.
    - time -- The point in time of the source database that will be restored to create the new database. Must be greater than or equal to the source database's earliestRestoreDate value. Either --time or --deleted-time (or both) must be specified. Time should be in following format: "YYYY-MM-DDTHH:MM:SS".
    - zone_redundant -- Specifies whether to enable zone redundancy
    '''
    return _call_az("az sql db restore", locals())


def rename(name, new_name, resource_group, server):
    '''
    Rename a database.

    Required Parameters:
    - name -- Name of the Azure SQL Database.
    - new_name -- The new name that the database will be renamed to.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql db rename", locals())


def show(name, resource_group, server):
    '''
    Get the details for a database.

    Required Parameters:
    - name -- Name of the Azure SQL Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql db show", locals())


def list(resource_group, server, elastic_pool=None):
    '''
    List databases on a server or elastic pool.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`

    Optional Parameters:
    - elastic_pool -- If specified, lists only the databases in this elastic pool
    '''
    return _call_az("az sql db list", locals())


def delete(name, resource_group, server, no_wait=None, yes=None):
    '''
    Delete a database.

    Required Parameters:
    - name -- Name of the Azure SQL Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az sql db delete", locals())


def update(name, resource_group, server, add=None, auto_pause_delay=None, backup_storage_redundancy=None, capacity=None, compute_model=None, elastic_pool=None, family=None, force_string=None, maint_config_id=None, max_size=None, min_capacity=None, no_wait=None, read_replicas=None, read_scale=None, remove=None, service_objective=None, set=None, tier=None, zone_redundant=None):
    '''
    Update a database.

    Required Parameters:
    - name -- Name of the Azure SQL Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - auto_pause_delay -- Time in minutes after which database is automatically paused. A value of -1 means that automatic pause is disabled.
    - backup_storage_redundancy -- Backup storage redundancy used to store backups. Allowed values include: Local, Zone, Geo.
    - capacity -- The capacity component of the sku in integer number of DTUs or vcores.
    - compute_model -- The compute model of the database.
    - elastic_pool -- The name or resource id of the elastic pool to move the database into.
    - family -- The compute generation component of the sku (for vcore skus only). Allowed values include: Gen4, Gen5.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - maint_config_id -- Specified maintenance configuration id or name for this resource.
    - max_size -- The new maximum size of the database expressed in bytes.
    - min_capacity -- Minimal capacity that database will always have allocated, if not paused
    - no_wait -- Do not wait for the long-running operation to finish.
    - read_replicas -- The number of high availability replicas to provision for the database. Only settable for Hyperscale edition.
    - read_scale -- If enabled, connections that have application intent set to readonly in their connection string may be routed to a readonly secondary replica. This property is only settable for Premium and Business Critical databases.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - service_objective -- The name of the new service objective. If this is a standalone db service objective and the db is currently in an elastic pool, then the db is removed from the pool.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tier -- The edition component of the sku. Allowed values include: Basic, Standard, Premium, GeneralPurpose, BusinessCritical, Hyperscale.
    - zone_redundant -- Specifies whether to enable zone redundancy
    '''
    return _call_az("az sql db update", locals())


def export(admin_password, admin_user, name, resource_group, server, storage_key, storage_key_type, storage_uri, auth_type=None):
    '''
    Export a database to a bacpac.

    Required Parameters:
    - admin_password -- Required. Administrator login password.
    - admin_user -- Required. Administrator login name.
    - name -- Name of the Azure SQL Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    - storage_key -- Required. Storage key.
    - storage_key_type -- Required. Storage key type. Possible values include: "SharedAccessKey", "StorageAccessKey".
    - storage_uri -- Required. Storage Uri.

    Optional Parameters:
    - auth_type -- Authentication type.
    '''
    return _call_az("az sql db export", locals())


def import_(admin_password, admin_user, name, resource_group, server, storage_key, storage_key_type, storage_uri, auth_type=None):
    '''
    Imports a bacpac into an existing database.

    Required Parameters:
    - admin_password -- Required. Administrator login password.
    - admin_user -- Required. Administrator login name.
    - name -- Name of the Azure SQL Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    - storage_key -- Required. Storage key.
    - storage_key_type -- Required. Storage key type. Possible values include: "SharedAccessKey", "StorageAccessKey".
    - storage_uri -- Required. Storage Uri.

    Optional Parameters:
    - auth_type -- Authentication type.
    '''
    return _call_az("az sql db import", locals())


def list_editions(location, available=None, dtu=None, service_objective=None, show_details=None, tier=None, vcores=None):
    '''
    Show database editions available for the currently active subscription.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.

    Optional Parameters:
    - available -- If specified, show only results that are available in the specified region.
    - dtu -- Number of DTUs to search for. If unspecified, all DTU sizes are shown.
    - service_objective -- Service objective to search for. If unspecified, all service objectives are shown.
    - show_details -- List of additional details to include in output.
    - tier -- Edition to search for. If unspecified, all editions are shown.
    - vcores -- Number of vcores to search for. If unspecified, all vcore sizes are shown.
    '''
    return _call_az("az sql db list-editions", locals())


def list_deleted(resource_group, server):
    '''
    

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql db list-deleted", locals())


def list_usages(name, resource_group, server):
    '''
    

    Required Parameters:
    - name -- Name of the Azure SQL Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql db list-usages", locals())

