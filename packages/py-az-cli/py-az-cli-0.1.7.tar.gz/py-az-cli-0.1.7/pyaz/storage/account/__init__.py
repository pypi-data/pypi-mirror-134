'''
Manage storage accounts.
'''
from ... pyaz_utils import _call_az
from . import blob_inventory_policy, blob_service_properties, encryption_scope, file_service_properties, hns_migration, keys, management_policy, network_rule, or_policy, private_endpoint_connection, private_link_resource


def check_name(name):
    '''
    Check that the storage account name is valid and is not already in use.

    Required Parameters:
    - name -- The name of the storage account within the specified resource group
    '''
    return _call_az("az storage account check-name", locals())


def create(name, resource_group, access_tier=None, action=None, allow_blob_public_access=None, allow_cross_tenant_replication=None, allow_protected_append_writes=None, allow_shared_key_access=None, assign_identity=None, azure_storage_sid=None, bypass=None, custom_domain=None, default_action=None, default_share_permission=None, domain_guid=None, domain_name=None, domain_sid=None, edge_zone=None, enable_alw=None, enable_files_aadds=None, enable_files_adds=None, enable_hierarchical_namespace=None, enable_large_file_share=None, enable_nfs_v3=None, encryption_key_name=None, encryption_key_source=None, encryption_key_type_for_queue=None, encryption_key_type_for_table=None, encryption_key_vault=None, encryption_key_version=None, encryption_services=None, forest_name=None, https_only=None, identity_type=None, immutability_period_in_days=None, immutability_state=None, key_expiration_period_in_days=None, key_vault_user_identity_id=None, kind=None, location=None, min_tls_version=None, net_bios_domain_name=None, public_network_access=None, publish_internet_endpoints=None, publish_microsoft_endpoints=None, require_infrastructure_encryption=None, routing_choice=None, sas_expiration_period=None, sku=None, subnet=None, tags=None, user_identity_id=None, vnet_name=None):
    '''
    Create a storage account.

    Required Parameters:
    - name -- The storage account name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - access_tier -- The access tier used for billing StandardBlob accounts. Cannot be set for StandardLRS, StandardGRS, StandardRAGRS, or PremiumLRS account types. It is required for StandardBlob accounts during creation
    - action -- The action of virtual network rule. Possible value is Allow.
    - allow_blob_public_access -- Allow or disallow public access to all blobs or containers in the storage account. The default value for this property is null, which is equivalent to true. When true, containers in the account may be configured for public access. Note that setting this property to true does not enable anonymous access to any data in the account. The additional step of configuring the public access setting for a container is required to enable anonymous access.
    - allow_cross_tenant_replication -- Allow or disallow cross AAD tenant object replication. The default interpretation is true for this property.
    - allow_protected_append_writes -- This property can only be changed for disabled and unlocked time-based retention policies. When enabled, new blocks can be written to an append blob while maintaining immutability protection and compliance. Only new blocks can be added and any existing blocks cannot be modified or deleted.
    - allow_shared_key_access -- Indicate whether the storage account permits requests to be authorized with the account access key via Shared Key. If false, then all requests, including shared access signatures, must be authorized with Azure Active Directory (Azure AD). The default value is null, which is equivalent to true.
    - assign_identity -- Generate and assign a new Storage Account Identity for this storage account for use with key management services like Azure KeyVault.
    - azure_storage_sid -- Specify the security identifier (SID) for Azure Storage. Required when --enable-files-adds is set to True
    - bypass -- Bypass traffic for space-separated uses.
    - custom_domain -- User domain assigned to the storage account. Name is the CNAME source.
    - default_action -- Default action to apply when no rule matches.
    - default_share_permission -- Default share permission for users using Kerberos authentication if RBAC role is not assigned.
    - domain_guid -- Specify the domain GUID. Required when --enable-files-adds is set to True
    - domain_name -- Specify the primary domain that the AD DNS server is authoritative for. Required when --enable-files-adds is set to True
    - domain_sid -- Specify the security identifier (SID). Required when --enable-files-adds is set to True
    - edge_zone -- The name of edge zone.
    - enable_alw -- The account level immutability property. The property is immutable and can only be set to true at the account creation time. When set to true, it enables object level immutability for all the containers in the account by default.
    - enable_files_aadds -- Enable Azure Active Directory Domain Services authentication for Azure Files
    - enable_files_adds -- Enable Azure Files Active Directory Domain Service Authentication for storage account. When --enable-files-adds is set to true, Azure Active Directory Properties arguments must be provided.
    - enable_hierarchical_namespace --  Allow the blob service to exhibit filesystem semantics. This property can be enabled only when storage account kind is StorageV2.
    - enable_large_file_share -- Enable the capability to support large file shares with more than 5 TiB capacity for storage account.Once the property is enabled, the feature cannot be disabled. Currently only supported for LRS and ZRS replication types, hence account conversions to geo-redundant accounts would not be possible. For more information, please refer to https://go.microsoft.com/fwlink/?linkid=2086047.
    - enable_nfs_v3 -- NFS 3.0 protocol support enabled if sets to true.
    - encryption_key_name -- The name of the KeyVault key.
    - encryption_key_source -- The default encryption key source
    - encryption_key_type_for_queue -- Set the encryption key type for Queue service. "Account": Queue will be encrypted with account-scoped encryption key. "Service": Queue will always be encrypted with service-scoped keys. Currently the default encryption key type is "Service".
    - encryption_key_type_for_table -- Set the encryption key type for Table service. "Account": Table will be encrypted with account-scoped encryption key. "Service": Table will always be encrypted with service-scoped keys. Currently the default encryption key type is "Service".
    - encryption_key_vault -- The Uri of the KeyVault.
    - encryption_key_version -- The version of the KeyVault key to use, which will opt out of implicit key rotation. Please use "" to opt in key auto-rotation again.
    - encryption_services -- Specifies which service(s) to encrypt.
    - forest_name -- Specify the Active Directory forest to get. Required when --enable-files-adds is set to True
    - https_only -- Allow https traffic only to storage service if set to true. The default value is true.
    - identity_type -- The identity type.
    - immutability_period_in_days -- The immutability period for the blobs in the container since the policy creation, in days.
    - immutability_state -- Defines the mode of the policy. Disabled state disables the policy, Unlocked state allows increase and decrease of immutability retention time and also allows toggling allow-protected-append-write property, Locked state only allows the increase of the immutability retention time. A policy can only be created in a Disabled or Unlocked state and can be toggled between the two states. Only a policy in an Unlocked state can transition to a Locked state which cannot be reverted.
    - key_expiration_period_in_days -- Expiration period in days of the Key Policy assigned to the storage account
    - key_vault_user_identity_id -- Resource identifier of the UserAssigned identity to be associated with server-side encryption on the storage account.
    - kind -- Indicate the type of storage account.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - min_tls_version -- The minimum TLS version to be permitted on requests to storage. The default interpretation is TLS 1.0 for this property
    - net_bios_domain_name -- Specify the NetBIOS domain name. Required when --enable-files-adds is set to True
    - public_network_access -- Enable or disable public network access to the storage account. Possible values include: `Enabled` or `Disabled`.
    - publish_internet_endpoints -- A boolean flag which indicates whether internet routing storage endpoints are to be published.
    - publish_microsoft_endpoints -- A boolean flag which indicates whether microsoft routing storage endpoints are to be published.
    - require_infrastructure_encryption -- A boolean indicating whether or not the service applies a secondary layer of encryption with platform managed keys for data at rest.
    - routing_choice -- Routing Choice defines the kind of network routing opted by the user.
    - sas_expiration_period -- Expiration period of the SAS Policy assigned to the storage account, DD.HH:MM:SS.
    - sku -- The storage account SKU.
    - subnet -- Name or ID of subnet. If name is supplied, `--vnet-name` must be supplied.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - user_identity_id -- The key is the ARM resource identifier of the identity. Only 1 User Assigned identity is permitted here.
    - vnet_name -- Name of a virtual network.
    '''
    return _call_az("az storage account create", locals())


def delete(name, resource_group=None, yes=None):
    '''
    Delete a storage account.

    Required Parameters:
    - name -- The storage account name.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az storage account delete", locals())


def show(name, expand=None, resource_group=None):
    '''
    Show storage account properties.

    Required Parameters:
    - name -- The storage account name.

    Optional Parameters:
    - expand -- May be used to expand the properties within account's properties. By default, data is not included when fetching properties. Currently we only support geoReplicationStats and blobRestoreStatus.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage account show", locals())


def list(resource_group=None):
    '''
    List storage accounts.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage account list", locals())


def show_usage(location):
    '''
    Show the current count and limit of the storage accounts under the subscription.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    '''
    return _call_az("az storage account show-usage", locals())


def show_connection_string(name, blob_endpoint=None, file_endpoint=None, key=None, protocol=None, queue_endpoint=None, resource_group=None, sas_token=None, table_endpoint=None):
    '''
    Get the connection string for a storage account.

    Required Parameters:
    - name -- The storage account name.

    Optional Parameters:
    - blob_endpoint -- Custom endpoint for blobs.
    - file_endpoint -- Custom endpoint for files.
    - key -- The key to use.
    - protocol -- The default endpoint protocol.
    - queue_endpoint -- Custom endpoint for queues.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sas_token -- The SAS token to be used in the connection-string.
    - table_endpoint -- Custom endpoint for tables.
    '''
    return _call_az("az storage account show-connection-string", locals())


def update(name, access_tier=None, add=None, allow_blob_public_access=None, allow_cross_tenant_replication=None, allow_protected_append_writes=None, allow_shared_key_access=None, assign_identity=None, azure_storage_sid=None, bypass=None, custom_domain=None, default_action=None, default_share_permission=None, domain_guid=None, domain_name=None, domain_sid=None, enable_files_aadds=None, enable_files_adds=None, enable_large_file_share=None, encryption_key_name=None, encryption_key_source=None, encryption_key_vault=None, encryption_key_version=None, encryption_services=None, force_string=None, forest_name=None, https_only=None, identity_type=None, immutability_period_in_days=None, immutability_state=None, key_expiration_period_in_days=None, key_vault_user_identity_id=None, min_tls_version=None, net_bios_domain_name=None, public_network_access=None, publish_internet_endpoints=None, publish_microsoft_endpoints=None, remove=None, resource_group=None, routing_choice=None, sas_expiration_period=None, set=None, sku=None, tags=None, use_subdomain=None, user_identity_id=None):
    '''
    Update the properties of a storage account.

    Required Parameters:
    - name -- The storage account name.

    Optional Parameters:
    - access_tier -- The access tier used for billing StandardBlob accounts. Cannot be set for StandardLRS, StandardGRS, StandardRAGRS, or PremiumLRS account types. It is required for StandardBlob accounts during creation
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - allow_blob_public_access -- Allow or disallow public access to all blobs or containers in the storage account. The default value for this property is null, which is equivalent to true. When true, containers in the account may be configured for public access. Note that setting this property to true does not enable anonymous access to any data in the account. The additional step of configuring the public access setting for a container is required to enable anonymous access.
    - allow_cross_tenant_replication -- Allow or disallow cross AAD tenant object replication. The default interpretation is true for this property.
    - allow_protected_append_writes -- This property can only be changed for disabled and unlocked time-based retention policies. When enabled, new blocks can be written to an append blob while maintaining immutability protection and compliance. Only new blocks can be added and any existing blocks cannot be modified or deleted.
    - allow_shared_key_access -- Indicate whether the storage account permits requests to be authorized with the account access key via Shared Key. If false, then all requests, including shared access signatures, must be authorized with Azure Active Directory (Azure AD). The default value is null, which is equivalent to true.
    - assign_identity -- Generate and assign a new Storage Account Identity for this storage account for use with key management services like Azure KeyVault.
    - azure_storage_sid -- Specify the security identifier (SID) for Azure Storage. Required when --enable-files-adds is set to True
    - bypass -- Bypass traffic for space-separated uses.
    - custom_domain -- User domain assigned to the storage account. Name is the CNAME source. Use "" to clear existing value.
    - default_action -- Default action to apply when no rule matches.
    - default_share_permission -- Default share permission for users using Kerberos authentication if RBAC role is not assigned.
    - domain_guid -- Specify the domain GUID. Required when --enable-files-adds is set to True
    - domain_name -- Specify the primary domain that the AD DNS server is authoritative for. Required when --enable-files-adds is set to True
    - domain_sid -- Specify the security identifier (SID). Required when --enable-files-adds is set to True
    - enable_files_aadds -- Enable Azure Active Directory Domain Services authentication for Azure Files
    - enable_files_adds -- Enable Azure Files Active Directory Domain Service Authentication for storage account. When --enable-files-adds is set to true, Azure Active Directory Properties arguments must be provided.
    - enable_large_file_share -- Enable the capability to support large file shares with more than 5 TiB capacity for storage account.Once the property is enabled, the feature cannot be disabled. Currently only supported for LRS and ZRS replication types, hence account conversions to geo-redundant accounts would not be possible. For more information, please refer to https://go.microsoft.com/fwlink/?linkid=2086047.
    - encryption_key_name -- The name of the KeyVault key.
    - encryption_key_source -- The default encryption key source
    - encryption_key_vault -- The Uri of the KeyVault.
    - encryption_key_version -- The version of the KeyVault key to use, which will opt out of implicit key rotation. Please use "" to opt in key auto-rotation again.
    - encryption_services -- Specifies which service(s) to encrypt.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - forest_name -- Specify the Active Directory forest to get. Required when --enable-files-adds is set to True
    - https_only -- Allows https traffic only to storage service.
    - identity_type -- The identity type.
    - immutability_period_in_days -- The immutability period for the blobs in the container since the policy creation, in days.
    - immutability_state -- Defines the mode of the policy. Disabled state disables the policy, Unlocked state allows increase and decrease of immutability retention time and also allows toggling allow-protected-append-write property, Locked state only allows the increase of the immutability retention time. A policy can only be created in a Disabled or Unlocked state and can be toggled between the two states. Only a policy in an Unlocked state can transition to a Locked state which cannot be reverted.
    - key_expiration_period_in_days -- Expiration period in days of the Key Policy assigned to the storage account
    - key_vault_user_identity_id -- Resource identifier of the UserAssigned identity to be associated with server-side encryption on the storage account.
    - min_tls_version -- The minimum TLS version to be permitted on requests to storage. The default interpretation is TLS 1.0 for this property
    - net_bios_domain_name -- Specify the NetBIOS domain name. Required when --enable-files-adds is set to True
    - public_network_access -- Enable or disable public network access to the storage account. Possible values include: `Enabled` or `Disabled`.
    - publish_internet_endpoints -- A boolean flag which indicates whether internet routing storage endpoints are to be published.
    - publish_microsoft_endpoints -- A boolean flag which indicates whether microsoft routing storage endpoints are to be published.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - routing_choice -- Routing Choice defines the kind of network routing opted by the user.
    - sas_expiration_period -- Expiration period of the SAS Policy assigned to the storage account, DD.HH:MM:SS.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - sku -- Note that the SKU name cannot be updated to Standard_ZRS, Premium_LRS or Premium_ZRS, nor can accounts of those SKU names be updated to any other value
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - use_subdomain -- Specify whether to use indirect CNAME validation.
    - user_identity_id -- The key is the ARM resource identifier of the identity. Only 1 User Assigned identity is permitted here.
    '''
    return _call_az("az storage account update", locals())


def failover(name, no_wait=None, resource_group=None, yes=None):
    '''
    Failover request can be triggered for a storage account in case of availability issues.

    Required Parameters:
    - name -- The storage account name.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az storage account failover", locals())


def revoke_delegation_keys(name, resource_group=None):
    '''
    Revoke all user delegation keys for a storage account.

    Required Parameters:
    - name -- The storage account name.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az storage account revoke-delegation-keys", locals())


def generate_sas(expiry, permissions, resource_types, services, account_key=None, account_name=None, connection_string=None, https_only=None, ip=None, start=None):
    '''
    Generate a shared access signature for the storage account.

    Required Parameters:
    - expiry -- None
    - permissions -- The permissions the SAS grants. Allowed values: (a)dd (c)reate (d)elete (l)ist (p)rocess (r)ead (u)pdate (w)rite (a)dd (c)reate (d)elete (l)ist (p)rocess (r)ead (u)pdate (w)rite. Can be combined.
    - resource_types -- None
    - services -- None

    Optional Parameters:
    - account_key -- Storage account key. Must be used in conjunction with storage account name. Environment variable: AZURE_STORAGE_KEY
    - account_name -- The storage account name.
    - connection_string -- Storage account connection string. Environment variable: AZURE_STORAGE_CONNECTION_STRING
    - https_only -- Only permit requests made with the HTTPS protocol. If omitted, requests from both the HTTP and HTTPS protocol are permitted.
    - ip -- Specifies the IP address or range of IP addresses from which to accept requests. Supports only IPv4 style addresses.
    - start -- None
    '''
    return _call_az("az storage account generate-sas", locals())

