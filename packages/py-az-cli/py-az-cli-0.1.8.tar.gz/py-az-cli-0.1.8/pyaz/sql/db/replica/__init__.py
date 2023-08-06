'''
Manage replication between databases.
'''
from .... pyaz_utils import _call_az

def create(name, partner_server, resource_group, server, auto_pause_delay=None, backup_storage_redundancy=None, capacity=None, compute_model=None, elastic_pool=None, family=None, license_type=None, min_capacity=None, no_wait=None, partner_database=None, partner_resource_group=None, read_replicas=None, read_scale=None, secondary_type=None, service_objective=None, tags=None, zone_redundant=None):
    '''
    Create a database as a readable secondary replica of an existing database.

    Required Parameters:
    - name -- Name of the Azure SQL Database.
    - partner_server -- Name of the server to create the new replica in.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`

    Optional Parameters:
    - auto_pause_delay -- Time in minutes after which database is automatically paused. A value of -1 means that automatic pause is disabled.
    - backup_storage_redundancy -- Backup storage redundancy used to store backups. Allowed values include: Local, Zone, Geo.
    - capacity -- The capacity component of the sku in integer number of DTUs or vcores.
    - compute_model -- The compute model of the database.
    - elastic_pool -- The name or resource id of the elastic pool to create the database in.
    - family -- The compute generation component of the sku (for vcore skus only). Allowed values include: Gen4, Gen5.
    - license_type -- The license type to apply for this database. ``LicenseIncluded`` if you need a license, or ``BasePrice`` if you have a license and are eligible for the Azure Hybrid Benefit. Possible values include: "LicenseIncluded", "BasePrice".
    - min_capacity -- Minimal capacity that database will always have allocated, if not paused
    - no_wait -- Do not wait for the long-running operation to finish.
    - partner_database -- Name of the new replica. If unspecified, defaults to the source database name.
    - partner_resource_group -- Name of the resource group to create the new replica in. If unspecified, defaults to the origin resource group.
    - read_replicas -- The number of high availability replicas to provision for the database. Only settable for Hyperscale edition.
    - read_scale -- If enabled, connections that have application intent set to readonly in their connection string may be routed to a readonly secondary replica. This property is only settable for Premium and Business Critical databases.
    - secondary_type -- Type of secondary to create. Allowed values include: Geo, Named.
    - service_objective -- The service objective for the new database. For example: Basic, S0, P1, GP_Gen4_1, GP_Gen5_S_8, BC_Gen5_2, HS_Gen5_32.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - zone_redundant -- Specifies whether to enable zone redundancy
    '''
    return _call_az("az sql db replica create", locals())


def list_links(name, resource_group, server):
    '''
    List the replicas of a database and their replication status.

    Required Parameters:
    - name -- Name of the Azure SQL Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql db replica list-links", locals())


def delete_link(name, partner_server, resource_group, server, partner_resource_group=None, yes=None):
    '''
    Permanently stop data replication between two database replicas.

    Required Parameters:
    - name -- Name of the Azure SQL Database.
    - partner_server -- Name of the server that the other replica is in.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`

    Optional Parameters:
    - partner_resource_group -- Name of the resource group that the other replica is in. If unspecified, defaults to the first database's resource group.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az sql db replica delete-link", locals())


def set_primary(name, resource_group, server, allow_data_loss=None):
    '''
    Set the primary replica database by failing over from the current primary replica database.

    Required Parameters:
    - name -- Name of the database to fail over.
    - resource_group -- Name of the resource group containing the secondary replica that will become the new primary.
    - server -- Name of the server containing the secondary replica that will become the new primary. You can configure the default using `az configure --defaults sql-server=<name>`

    Optional Parameters:
    - allow_data_loss -- If specified, the failover operation will allow data loss.
    '''
    return _call_az("az sql db replica set-primary", locals())

