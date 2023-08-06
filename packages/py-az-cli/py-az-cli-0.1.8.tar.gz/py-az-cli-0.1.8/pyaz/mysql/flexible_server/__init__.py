from ... pyaz_utils import _call_az
from . import db, deploy, firewall_rule, parameter, replica


def create(address_prefixes=None, admin_password=None, admin_user=None, backup_retention=None, database_name=None, geo_redundant_backup=None, high_availability=None, iops=None, location=None, name=None, private_dns_zone=None, public_access=None, resource_group=None, sku_name=None, standby_zone=None, storage_auto_grow=None, storage_size=None, subnet=None, subnet_prefixes=None, tags=None, tier=None, version=None, vnet=None, yes=None, zone=None):
    '''
    Create a MySQL flexible server.

    Optional Parameters:
    - address_prefixes -- The IP address prefix to use when creating a new virtual network in CIDR format. Default value is 10.0.0.0/16.
    - admin_password -- The password of the administrator. Minimum 8 characters and maximum 128 characters. Password must contain characters from three of the following categories: English uppercase letters, English lowercase letters, numbers, and non-alphanumeric characters.
    - admin_user -- Administrator username for the server. Once set, it cannot be changed. 
    - backup_retention -- The number of days a backup is retained. Range of 1 to 35 days. Default is 7 days.
    - database_name -- The name of the database to be created when provisioning the database server
    - geo_redundant_backup -- Whether or not geo redundant backup is enabled.
    - high_availability -- Enable (ZoneRedundant or SameZone) or disable high availability feature. Default value is Disabled. High availability can only be set during flexible server create time. 
    - iops -- Number of IOPS to be allocated for this server. You will get certain amount of free IOPS based on compute and storage provisioned. The default value for IOPS is free IOPS. To learn more about IOPS based on compute and storage, refer to IOPS in Azure Database for MySQL Flexible Server
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - private_dns_zone -- This parameter only applies for a server with private access. The name or id of new or existing private dns zone. You can use the private dns zone from same resource group, different resource group, or different subscription. If you want to use a zone from different resource group or subscription, please provide resource Id. CLI creates a new private dns zone within the same resource group as virtual network if not provided by users.
    - public_access -- Determines the public access. Enter single or range of IP addresses to be included in the allowed list of IPs. IP address ranges must be dash-separated and not contain any spaces. Specifying 0.0.0.0 allows public access from any resources deployed within Azure to access your server. Setting it to "None" sets the server in public access mode but does not create a firewall rule. 
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sku_name -- The name of the compute SKU. Follows the convention Standard_{VM name}. Examples: Standard_D4s_v3
    - standby_zone -- The availability zone information of the standby server when high availability is enabled.
    - storage_auto_grow -- Enable or disable autogrow of the storage. Default value is Enabled.
    - storage_size -- The storage capacity of the server. Minimum is 32 GiB and max is 16 TiB.
    - subnet -- Name or resource ID of a new or existing subnet. If you want to use a subnet from different resource group or subscription, please provide resource ID instead of name. Please note that the subnet will be delegated to flexibleServers. After delegation, this subnet cannot be used for any other type of Azure resources.
    - subnet_prefixes -- The subnet IP address prefix to use when creating a new subnet in CIDR format. Default value is 10.0.0.0/24.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - tier -- Compute tier of the server. Accepted values: Burstable, GeneralPurpose, Memory Optimized 
    - version -- Server major version.
    - vnet -- Name or ID of a new or existing virtual network. If you want to use a vnet from different resource group or subscription, please provide a resource ID. The name must be between 2 to 64 characters. The name must begin with a letter or number, end with a letter, number or underscore, and may contain only letters, numbers, underscores, periods, or hyphens.
    - yes -- Do not prompt for confirmation.
    - zone -- Availability zone into which to provision the resource.
    '''
    return _call_az("az mysql flexible-server create", locals())


def restore(name, resource_group, source_server, address_prefixes=None, no_wait=None, private_dns_zone=None, public_access=None, restore_time=None, subnet=None, subnet_prefixes=None, vnet=None, yes=None, zone=None):
    '''
    Restore a flexible server from backup.

    Required Parameters:
    - name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - source_server -- The name or resource ID of the source server to restore from.

    Optional Parameters:
    - address_prefixes -- The IP address prefix to use when creating a new virtual network in CIDR format. Default value is 10.0.0.0/16.
    - no_wait -- Do not wait for the long-running operation to finish.
    - private_dns_zone -- This parameter only applies for a server with private access. The name or id of new or existing private dns zone. You can use the private dns zone from same resource group, different resource group, or different subscription. If you want to use a zone from different resource group or subscription, please provide resource Id. CLI creates a new private dns zone within the same resource group as virtual network if not provided by users.
    - public_access -- Determines the public access. 
    - restore_time -- The point in time in UTC to restore from (ISO8601 format), e.g., 2017-04-26T02:10:00+00:00The default value is set to current time.
    - subnet -- Name or resource ID of a new or existing subnet. If you want to use a subnet from different resource group or subscription, please provide resource ID instead of name. Please note that the subnet will be delegated to flexibleServers. After delegation, this subnet cannot be used for any other type of Azure resources.
    - subnet_prefixes -- The subnet IP address prefix to use when creating a new subnet in CIDR format. Default value is 10.0.0.0/24.
    - vnet -- Name or ID of a new or existing virtual network. If you want to use a vnet from different resource group or subscription, please provide a resource ID. The name must be between 2 to 64 characters. The name must begin with a letter or number, end with a letter, number or underscore, and may contain only letters, numbers, underscores, periods, or hyphens.
    - yes -- Do not prompt for confirmation.
    - zone -- Availability zone into which to provision the resource.
    '''
    return _call_az("az mysql flexible-server restore", locals())


def geo_restore(location, name, resource_group, source_server, address_prefixes=None, no_wait=None, private_dns_zone=None, public_access=None, subnet=None, subnet_prefixes=None, vnet=None, yes=None, zone=None):
    '''
    Geo-restore a flexible server from backup.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - source_server -- The name or resource ID of the source server to restore from.

    Optional Parameters:
    - address_prefixes -- The IP address prefix to use when creating a new virtual network in CIDR format. Default value is 10.0.0.0/16.
    - no_wait -- Do not wait for the long-running operation to finish.
    - private_dns_zone -- This parameter only applies for a server with private access. The name or id of new or existing private dns zone. You can use the private dns zone from same resource group, different resource group, or different subscription. If you want to use a zone from different resource group or subscription, please provide resource Id. CLI creates a new private dns zone within the same resource group as virtual network if not provided by users.
    - public_access -- Determines the public access. 
    - subnet -- Name or resource ID of a new or existing subnet. If you want to use a subnet from different resource group or subscription, please provide resource ID instead of name. Please note that the subnet will be delegated to flexibleServers. After delegation, this subnet cannot be used for any other type of Azure resources.
    - subnet_prefixes -- The subnet IP address prefix to use when creating a new subnet in CIDR format. Default value is 10.0.0.0/24.
    - vnet -- Name or ID of a new or existing virtual network. If you want to use a vnet from different resource group or subscription, please provide a resource ID. The name must be between 2 to 64 characters. The name must begin with a letter or number, end with a letter, number or underscore, and may contain only letters, numbers, underscores, periods, or hyphens.
    - yes -- Do not prompt for confirmation.
    - zone -- Availability zone into which to provision the resource.
    '''
    return _call_az("az mysql flexible-server geo-restore", locals())


def start(name, resource_group):
    '''
    Start a flexible server.

    Required Parameters:
    - name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az mysql flexible-server start", locals())


def stop(name=None, resource_group=None):
    '''
    Stop a flexible server.

    Optional Parameters:
    - name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az mysql flexible-server stop", locals())


def delete(name, resource_group, yes=None):
    '''
    Delete a flexible server.

    Required Parameters:
    - name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az mysql flexible-server delete", locals())


def show(name, resource_group):
    '''
    Get the details of a flexible server.

    Required Parameters:
    - name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az mysql flexible-server show", locals())


def list(resource_group=None):
    '''
    List available flexible servers.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az mysql flexible-server list", locals())


def update(name, resource_group, add=None, admin_password=None, backup_retention=None, force_string=None, high_availability=None, iops=None, maintenance_window=None, remove=None, replication_role=None, set=None, sku_name=None, standby_zone=None, storage_auto_grow=None, storage_size=None, tags=None, tier=None):
    '''
    Update a flexible server.

    Required Parameters:
    - name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - admin_password -- The password of the administrator. Minimum 8 characters and maximum 128 characters. Password must contain characters from three of the following categories: English uppercase letters, English lowercase letters, numbers, and non-alphanumeric characters.
    - backup_retention -- The number of days a backup is retained. Range of 1 to 35 days. Default is 7 days.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - high_availability -- Enable (ZoneRedundant or SameZone) or disable high availability feature. Default value is Disabled. High availability can only be set during flexible server create time. 
    - iops -- Number of IOPS to be allocated for this server. You will get certain amount of free IOPS based on compute and storage provisioned. The default value for IOPS is free IOPS. To learn more about IOPS based on compute and storage, refer to IOPS in Azure Database for MySQL Flexible Server
    - maintenance_window -- Period of time (UTC) designated for maintenance. Examples: "Sun:23:30" to schedule on Sunday, 11:30pm UTC. To set back to default pass in "Disabled".
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - replication_role -- The replication role of the server.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - sku_name -- The name of the compute SKU. Follows the convention Standard_{VM name}. Examples: Standard_D4s_v3
    - standby_zone -- The availability zone information of the standby server when high availability is enabled.
    - storage_auto_grow -- Enable or disable autogrow of the storage. Default value is Enabled.
    - storage_size -- The storage capacity of the server. Minimum is 32 GiB and max is 16 TiB.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - tier -- Compute tier of the server. Accepted values: Burstable, GeneralPurpose, Memory Optimized 
    '''
    return _call_az("az mysql flexible-server update", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Wait for the flexible server to satisfy certain conditions.

    Required Parameters:
    - name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az mysql flexible-server wait", locals())


def restart(name, resource_group, failover=None):
    '''
    Restart a flexible server.

    Required Parameters:
    - name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - failover -- Forced failover for server restart operation. Allowed values: Forced
    '''
    return _call_az("az mysql flexible-server restart", locals())


def list_skus(location):
    '''
    Lists available sku's in the given region.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    '''
    return _call_az("az mysql flexible-server list-skus", locals())


def show_connection_string(admin_password=None, admin_user=None, database_name=None, server_name=None):
    '''
    Show the connection strings for a MySQL flexible-server database.

    Optional Parameters:
    - admin_password -- The password of the administrator. Minimum 8 characters and maximum 128 characters. Password must contain characters from three of the following categories: English uppercase letters, English lowercase letters, numbers, and non-alphanumeric characters.
    - admin_user -- Administrator username for the server. Once set, it cannot be changed. 
    - database_name -- The name of the database to be created when provisioning the database server
    - server_name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    '''
    return _call_az("az mysql flexible-server show-connection-string", locals())

