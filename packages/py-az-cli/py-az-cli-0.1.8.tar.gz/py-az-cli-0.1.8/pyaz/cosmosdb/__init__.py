'''
Manage Azure Cosmos DB database accounts.
'''
from .. pyaz_utils import _call_az
from . import collection, database, identity, keys, locations, mongodb, network_rule, private_endpoint_connection, private_link_resource, restorable_database_account, sql, table


def show(name, resource_group):
    '''
    Get the details of an Azure Cosmos DB database account.

    Required Parameters:
    - name -- Name of the Cosmos DB database account
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb show", locals())


def list_keys(name, resource_group):
    '''
    List the access keys for a Azure Cosmos DB database account.

    Required Parameters:
    - name -- Name of the Cosmos DB database account
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb list-keys", locals())


def list_read_only_keys(name, resource_group):
    '''
    List the read-only access keys for a Azure Cosmos DB database account.

    Required Parameters:
    - name -- Name of the Cosmos DB database account
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb list-read-only-keys", locals())


def list_connection_strings(name, resource_group):
    '''
    List the connection strings for a Azure Cosmos DB database account.

    Required Parameters:
    - name -- Name of the Cosmos DB database account
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb list-connection-strings", locals())


def regenerate_key(key_kind, name, resource_group):
    '''
    Regenerate an access key for a Azure Cosmos DB database account.

    Required Parameters:
    - key_kind -- The access key to regenerate.
    - name -- Name of the Cosmos DB database account
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb regenerate-key", locals())


def check_name_exists(name):
    '''
    Checks if an Azure Cosmos DB account name exists.

    Required Parameters:
    - name -- Name of the Cosmos DB database account
    '''
    return _call_az("az cosmosdb check-name-exists", locals())


def delete(name, resource_group, yes=None):
    '''
    Deletes an Azure Cosmos DB database account.

    Required Parameters:
    - name -- Name of the Cosmos DB database account
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az cosmosdb delete", locals())


def failover_priority_change(failover_policies, name, resource_group):
    '''
    Changes the failover priority for the Azure Cosmos DB database account.

    Required Parameters:
    - failover_policies -- space-separated failover policies in 'regionName=failoverPriority' format. E.g eastus=0 westus=1
    - name -- Name of the Cosmos DB database account
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb failover-priority-change", locals())


def create(name, resource_group, analytical_storage_schema_type=None, assign_identity=None, backup_interval=None, backup_policy_type=None, backup_redundancy=None, backup_retention=None, capabilities=None, databases_to_restore=None, default_consistency_level=None, default_identity=None, disable_key_based_metadata_write_access=None, enable_analytical_storage=None, enable_automatic_failover=None, enable_free_tier=None, enable_multiple_write_locations=None, enable_public_network=None, enable_virtual_network=None, ip_range_filter=None, is_restore_request=None, key_uri=None, kind=None, locations=None, max_interval=None, max_staleness_prefix=None, network_acl_bypass=None, network_acl_bypass_resource_ids=None, restore_source=None, restore_timestamp=None, server_version=None, tags=None, virtual_network_rules=None):
    '''
    Creates a new Azure Cosmos DB database account.

    Required Parameters:
    - name -- Name of the Cosmos DB database account
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - analytical_storage_schema_type -- Schema type for analytical storage.
    - assign_identity -- Assign system or user assigned identities separated by spaces. Use '[system]' to refer system assigned identity.
    - backup_interval -- the frequency(in minutes) with which backups are taken (only for accounts with periodic mode backups)
    - backup_policy_type -- The type of backup policy of the account to create
    - backup_redundancy -- The redundancy type of the backup Storage account
    - backup_retention -- the time(in hours) for which each backup is retained (only for accounts with periodic mode backups)
    - capabilities -- set custom capabilities on the Cosmos DB database account.
    - databases_to_restore -- None
    - default_consistency_level -- default consistency level of the Cosmos DB database account
    - default_identity -- The primary identity to access key vault in CMK related features. e.g. 'FirstPartyIdentity', 'SystemAssignedIdentity' and more.
    - disable_key_based_metadata_write_access -- Disable write operations on metadata resources (databases, containers, throughput) via account keys
    - enable_analytical_storage -- Flag to enable log storage on the account.
    - enable_automatic_failover -- Enables automatic failover of the write region in the rare event that the region is unavailable due to an outage. Automatic failover will result in a new write region for the account and is chosen based on the failover priorities configured for the account.
    - enable_free_tier -- If enabled the account is free-tier.
    - enable_multiple_write_locations -- Enable Multiple Write Locations
    - enable_public_network -- Enable or disable public network access to server.
    - enable_virtual_network -- Enables virtual network on the Cosmos DB database account
    - ip_range_filter -- firewall support. Specifies the set of IP addresses or IP address ranges in CIDR form to be included as the allowed list of client IPs for a given database account. IP addresses/ranges must be comma-separated and must not contain any spaces
    - is_restore_request -- Restore from an existing/deleted account.
    - key_uri -- The URI of the key vault
    - kind -- The type of Cosmos DB database account to create
    - locations -- None
    - max_interval -- when used with Bounded Staleness consistency, this value represents the time amount of staleness (in seconds) tolerated. Accepted range for this value is 1 - 100
    - max_staleness_prefix -- when used with Bounded Staleness consistency, this value represents the number of stale requests tolerated. Accepted range for this value is 1 - 2,147,483,647
    - network_acl_bypass -- Flag to enable or disable Network Acl Bypass.
    - network_acl_bypass_resource_ids -- List of Resource Ids to allow Network Acl Bypass.
    - restore_source -- The restorable-database-account Id of the source account from which the account has to be restored. Required if --is-restore-request is set to true.
    - restore_timestamp -- The timestamp to which the account has to be restored to. Required if --is-restore-request is set to true.
    - server_version -- Valid only for MongoDB accounts.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - virtual_network_rules -- ACL's for virtual network
    '''
    return _call_az("az cosmosdb create", locals())


def update(name, resource_group, analytical_storage_schema_type=None, backup_interval=None, backup_policy_type=None, backup_redundancy=None, backup_retention=None, capabilities=None, default_consistency_level=None, default_identity=None, disable_key_based_metadata_write_access=None, enable_analytical_storage=None, enable_automatic_failover=None, enable_multiple_write_locations=None, enable_public_network=None, enable_virtual_network=None, ip_range_filter=None, locations=None, max_interval=None, max_staleness_prefix=None, network_acl_bypass=None, network_acl_bypass_resource_ids=None, server_version=None, tags=None, virtual_network_rules=None):
    '''
    Update an Azure Cosmos DB database account.

    Required Parameters:
    - name -- Name of the Cosmos DB database account
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - analytical_storage_schema_type -- Schema type for analytical storage.
    - backup_interval -- the frequency(in minutes) with which backups are taken (only for accounts with periodic mode backups)
    - backup_policy_type -- The type of backup policy of the account to create
    - backup_redundancy -- The redundancy type of the backup Storage account
    - backup_retention -- the time(in hours) for which each backup is retained (only for accounts with periodic mode backups)
    - capabilities -- set custom capabilities on the Cosmos DB database account.
    - default_consistency_level -- default consistency level of the Cosmos DB database account
    - default_identity -- The primary identity to access key vault in CMK related features. e.g. 'FirstPartyIdentity', 'SystemAssignedIdentity' and more.
    - disable_key_based_metadata_write_access -- Disable write operations on metadata resources (databases, containers, throughput) via account keys
    - enable_analytical_storage -- Flag to enable log storage on the account.
    - enable_automatic_failover -- Enables automatic failover of the write region in the rare event that the region is unavailable due to an outage. Automatic failover will result in a new write region for the account and is chosen based on the failover priorities configured for the account.
    - enable_multiple_write_locations -- Enable Multiple Write Locations
    - enable_public_network -- Enable or disable public network access to server.
    - enable_virtual_network -- Enables virtual network on the Cosmos DB database account
    - ip_range_filter -- firewall support. Specifies the set of IP addresses or IP address ranges in CIDR form to be included as the allowed list of client IPs for a given database account. IP addresses/ranges must be comma-separated and must not contain any spaces
    - locations -- None
    - max_interval -- when used with Bounded Staleness consistency, this value represents the time amount of staleness (in seconds) tolerated. Accepted range for this value is 1 - 100
    - max_staleness_prefix -- when used with Bounded Staleness consistency, this value represents the number of stale requests tolerated. Accepted range for this value is 1 - 2,147,483,647
    - network_acl_bypass -- Flag to enable or disable Network Acl Bypass.
    - network_acl_bypass_resource_ids -- List of Resource Ids to allow Network Acl Bypass.
    - server_version -- Valid only for MongoDB accounts.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - virtual_network_rules -- ACL's for virtual network
    '''
    return _call_az("az cosmosdb update", locals())


def list(resource_group=None):
    '''
    List Azure Cosmos DB database accounts.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cosmosdb list", locals())


def restore(account_name, location, resource_group, restore_timestamp, target_database_account_name, databases_to_restore=None):
    '''
    Create a new Azure Cosmos DB database account by restoring from an existing database account.

    Required Parameters:
    - account_name -- Name of the source Cosmos DB database account for the restore
    - location -- The location of the source account from which restore is triggered. This will also be the write region of the restored account
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - restore_timestamp -- The timestamp to which the account has to be restored to.
    - target_database_account_name -- Name of the new target Cosmos DB database account after the restore

    Optional Parameters:
    - databases_to_restore -- None
    '''
    return _call_az("az cosmosdb restore", locals())

