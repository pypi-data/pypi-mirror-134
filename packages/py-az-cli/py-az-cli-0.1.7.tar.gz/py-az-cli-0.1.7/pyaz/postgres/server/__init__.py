'''
Manage PostgreSQL servers.
'''
from ... pyaz_utils import _call_az
from . import ad_admin, configuration, firewall_rule, key, private_endpoint_connection, private_link_resource, replica, vnet_rule


def create(admin_password=None, admin_user=None, assign_identity=None, auto_grow=None, backup_retention=None, geo_redundant_backup=None, infrastructure_encryption=None, location=None, minimal_tls_version=None, name=None, public_network_access=None, resource_group=None, sku_name=None, ssl_enforcement=None, storage_size=None, tags=None, version=None):
    '''
    Create a server.

    Optional Parameters:
    - admin_password -- The password of the administrator. Minimum 8 characters and maximum 128 characters. Password must contain characters from three of the following categories: English uppercase letters, English lowercase letters, numbers, and non-alphanumeric characters.
    - admin_user -- Administrator username for the server. Once set, it cannot be changed.
    - assign_identity -- Generate and assign an Azure Active Directory Identity for this server for use with key management services like Azure KeyVault.
    - auto_grow -- Enable or disable autogrow of the storage. Default value is Enabled.
    - backup_retention -- The number of days a backup is retained. Range of 7 to 35 days. Default is 7 days.
    - geo_redundant_backup -- Enable or disable geo-redundant backups. Default value is Disabled. Not supported in Basic pricing tier.
    - infrastructure_encryption -- Add an optional second layer of encryption for data using new encryption algorithm. Default value is Disabled.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - minimal_tls_version -- Set the minimal TLS version for connections to server when SSL is enabled. Default is TLSEnforcementDisabled.
    - name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - public_network_access -- Enable or disable public network access to server. When disabled, only connections made through Private Links can reach this server. Allowed values are : Enabled, Disabled, all, 0.0.0.0, <SingleIP>, <StartIP-DestinationIP>. Default is Enabled.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sku_name -- The name of the sku. Follows the convention {pricing tier}_{compute generation}_{vCores} in shorthand. Examples: B_Gen5_1, GP_Gen5_4, MO_Gen5_16. 
    - ssl_enforcement -- Enable or disable ssl enforcement for connections to server. Default is Enabled.
    - storage_size -- The storage capacity of the server (unit is megabytes). Minimum 5120 and increases in 1024 increments. Default is 51200.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - version -- Server major version.
    '''
    return _call_az("az postgres server create", locals())


def restore(name, resource_group, restore_point_in_time, source_server, no_wait=None):
    '''
    Restore a server from backup.

    Required Parameters:
    - name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - restore_point_in_time -- The point in time in UTC to restore from (ISO8601 format), e.g., 2017-04-26T02:10:00+08:00
    - source_server -- The name or resource ID of the source server to restore from.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az postgres server restore", locals())


def georestore(location, name, resource_group, source_server, backup_retention=None, geo_redundant_backup=None, no_wait=None, sku_name=None):
    '''
    Geo-restore a server from backup.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - source_server -- The name or ID of the source server to restore from.

    Optional Parameters:
    - backup_retention -- The number of days a backup is retained. Range of 7 to 35 days. Default is 7 days.
    - geo_redundant_backup -- Enable or disable geo-redundant backups. Default value is Disabled. Not supported in Basic pricing tier.
    - no_wait -- Do not wait for the long-running operation to finish.
    - sku_name -- The name of the sku. Defaults to sku of the source server. Follows the convention {pricing tier}_{compute generation}_{vCores} in shorthand. Examples: B_Gen5_1, GP_Gen5_4, MO_Gen5_16.
    '''
    return _call_az("az postgres server georestore", locals())


def delete(name, resource_group, yes=None):
    '''
    Delete a server.

    Required Parameters:
    - name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az postgres server delete", locals())


def show(name, resource_group):
    '''
    Get the details of a server.

    Required Parameters:
    - name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az postgres server show", locals())


def list(resource_group=None):
    '''
    List available servers.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az postgres server list", locals())


def update(name, resource_group, add=None, admin_password=None, assign_identity=None, auto_grow=None, backup_retention=None, force_string=None, minimal_tls_version=None, public_network_access=None, remove=None, set=None, sku_name=None, ssl_enforcement=None, storage_size=None, tags=None):
    '''
    Update a server.

    Required Parameters:
    - name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - admin_password -- The password of the administrator. Minimum 8 characters and maximum 128 characters. Password must contain characters from three of the following categories: English uppercase letters, English lowercase letters, numbers, and non-alphanumeric characters.
    - assign_identity -- Generate and assign an Azure Active Directory Identity for this server for use with key management services like Azure KeyVault.
    - auto_grow -- Enable or disable autogrow of the storage. Default value is Enabled.
    - backup_retention -- The number of days a backup is retained. Range of 7 to 35 days. Default is 7 days.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - minimal_tls_version -- Set the minimal TLS version for connections to server when SSL is enabled. Default is TLSEnforcementDisabled.
    - public_network_access -- Enable or disable public network access to server. When disabled, only connections made through Private Links can reach this server. Allowed values are : Enabled, Disabled, all, 0.0.0.0, <SingleIP>, <StartIP-DestinationIP>. Default is Enabled.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - sku_name -- The name of the sku. Follows the convention {pricing tier}_{compute generation}_{vCores} in shorthand. Examples: B_Gen5_1, GP_Gen5_4, MO_Gen5_16.
    - ssl_enforcement -- Enable or disable ssl enforcement for connections to server. Default is Enabled.
    - storage_size -- The storage capacity of the server (unit is megabytes). Minimum 5120 and increases in 1024 increments. Default is 51200.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az postgres server update", locals())


def wait(name, resource_group, custom=None, exists=None, interval=None, timeout=None):
    '''
    Wait for server to satisfy certain conditions.

    Required Parameters:
    - name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    '''
    return _call_az("az postgres server wait", locals())


def restart(name, resource_group):
    '''
    Restart a server.

    Required Parameters:
    - name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az postgres server restart", locals())


def list_skus(location):
    '''
    List available sku's in the given region.

    Required Parameters:
    - location -- The name of the location.
    '''
    return _call_az("az postgres server list-skus", locals())


def show_connection_string(admin_password=None, admin_user=None, database_name=None, server_name=None):
    '''
    Show the connection strings for a PostgreSQL server database.

    Optional Parameters:
    - admin_password -- The login password of the administrator.
    - admin_user -- The login username of the administrator.
    - database_name -- The name of a database.
    - server_name -- Name of the server.
    '''
    return _call_az("az postgres server show-connection-string", locals())

