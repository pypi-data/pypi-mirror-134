'''
Manage SQL managed instances.
'''
from ... pyaz_utils import _call_az
from . import ad_admin, ad_only_auth, key, op, tde_key


def create(name, resource_group, subnet, admin_password=None, admin_user=None, assign_identity=None, backup_storage_redundancy=None, capacity=None, collation=None, enable_ad_only_auth=None, external_admin_name=None, external_admin_principal_type=None, external_admin_sid=None, family=None, identity_type=None, key_id=None, license_type=None, location=None, maint_config_id=None, minimal_tls_version=None, no_wait=None, primary_user_assigned_identity_id=None, proxy_override=None, public_data_endpoint_enabled=None, storage=None, tags=None, tier=None, timezone_id=None, user_assigned_identity_id=None, vnet_name=None, yes=None):
    '''
    Create a managed instance.

    Required Parameters:
    - name -- The managed instance name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - subnet -- Name or ID of the subnet that allows access to an Azure Sql Managed Instance. If subnet name is provided, --vnet-name must be provided.

    Optional Parameters:
    - admin_password -- The administrator login password (required for managed instance creation).
    - admin_user -- Administrator username for the managed instance. Can only be specified when the managed instance is being created (and is required for creation).
    - assign_identity -- Generate and assign an Azure Active Directory Identity for this managed instance for use with key management services like Azure KeyVault.
    - backup_storage_redundancy -- Backup storage redundancy used to store backups. Allowed values include: Local, Zone, Geo.
    - capacity -- The capacity of the managed instance in integer number of vcores.
    - collation -- The collation of the managed instance.
    - enable_ad_only_auth -- Enable Azure Active Directory Only Authentication for this server.
    - external_admin_name -- Display name of the Azure AD administrator user, group or application.
    - external_admin_principal_type -- User, Group or Application
    - external_admin_sid -- The unique ID of the Azure AD administrator. Object Id for User or Group, Client Id for Applications
    - family -- The compute generation component of the sku. Allowed values include: Gen4, Gen5.
    - identity_type -- Type of Identity to be used. Possible values are SystemAsssigned,UserAssigned, SystemAssignedUserAssigned and None.
    - key_id -- The key vault URI for encryption.
    - license_type -- The license type to apply for this managed instance.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - maint_config_id -- Assign maintenance configuration to this managed instance.
    - minimal_tls_version -- The minimal TLS version enforced by the managed instance for inbound connections.
    - no_wait -- Do not wait for the long-running operation to finish.
    - primary_user_assigned_identity_id -- The ID of the primary user managed identity.
    - proxy_override -- The connection type used for connecting to the instance.
    - public_data_endpoint_enabled -- Whether or not the public data endpoint is enabled for the instance.
    - storage -- The storage size of the managed instance. Storage size must be specified in increments of 32 GB
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - tier -- The edition component of the sku. Allowed values include: GeneralPurpose, BusinessCritical.
    - timezone_id -- The time zone id for the instance to set. A list of time zone ids is exposed through the sys.time_zone_info (Transact-SQL) view.
    - user_assigned_identity_id -- Generate and assign an User Managed Identity(UMI) for this server.
    - vnet_name -- The virtual network name
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az sql mi create", locals())


def delete(name, resource_group, no_wait=None, yes=None):
    '''
    Delete a managed instance.

    Required Parameters:
    - name -- The managed instance name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az sql mi delete", locals())


def show(name, resource_group, expand_ad_admin=None):
    '''
    Get the details for a managed instance.

    Required Parameters:
    - name -- The managed instance name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expand_ad_admin -- Expand the Active Directory Administrator for the server.
    '''
    return _call_az("az sql mi show", locals())


def list(expand_ad_admin=None, resource_group=None):
    '''
    List available managed instances.

    Optional Parameters:
    - expand_ad_admin -- Expand the Active Directory Administrator for the server.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql mi list", locals())


def update(name, resource_group, add=None, admin_password=None, assign_identity=None, capacity=None, family=None, force_string=None, identity_type=None, key_id=None, license_type=None, maint_config_id=None, minimal_tls_version=None, no_wait=None, primary_user_assigned_identity_id=None, proxy_override=None, public_data_endpoint_enabled=None, remove=None, set=None, storage=None, subnet=None, tags=None, tier=None, user_assigned_identity_id=None, vnet_name=None):
    '''
    Update a managed instance.

    Required Parameters:
    - name -- The managed instance name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - admin_password -- The administrator login password (required for managed instance creation).
    - assign_identity -- Generate and assign an Azure Active Directory Identity for this managed instance for use with key management services like Azure KeyVault. If identity is already assigned - do nothing.
    - capacity -- The capacity of the managed instance in integer number of vcores.
    - family -- The compute generation component of the sku. Allowed values include: Gen4, Gen5.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - identity_type -- Type of Identity to be used. Possible values are SystemAsssigned,UserAssigned, SystemAssignedUserAssigned and None.
    - key_id -- The key vault URI for encryption.
    - license_type -- The license type to apply for this managed instance.
    - maint_config_id -- Change maintenance configuration for this managed instance.
    - minimal_tls_version -- The minimal TLS version enforced by the managed instance for inbound connections.
    - no_wait -- Do not wait for the long-running operation to finish.
    - primary_user_assigned_identity_id -- The ID of the primary user managed identity.
    - proxy_override -- The connection type used for connecting to the instance.
    - public_data_endpoint_enabled -- Whether or not the public data endpoint is enabled for the instance.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - storage -- The storage size of the managed instance. Storage size must be specified in increments of 32 GB
    - subnet -- Name or ID of the subnet that allows access to an Azure Sql Managed Instance. If subnet name is provided, --vnet-name must be provided.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - tier -- The edition component of the sku. Allowed values include: GeneralPurpose, BusinessCritical.
    - user_assigned_identity_id -- Generate and assign an User Managed Identity(UMI) for this server.
    - vnet_name -- The virtual network name
    '''
    return _call_az("az sql mi update", locals())


def failover(name, resource_group, no_wait=None, replica_type=None):
    '''
    Failover a managed instance.

    Required Parameters:
    - name -- The managed instance name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - replica_type -- The type of replica to be failed over.
    '''
    return _call_az("az sql mi failover", locals())

