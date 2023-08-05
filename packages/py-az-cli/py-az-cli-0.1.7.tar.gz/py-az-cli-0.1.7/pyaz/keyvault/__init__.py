'''
Manage KeyVault keys, secrets, and certificates.
'''
from .. pyaz_utils import _call_az
from . import backup, certificate, key, network_rule, private_endpoint_connection, private_link_resource, restore, secret, security_domain, storage


def create(resource_group, administrators=None, bypass=None, default_action=None, enable_purge_protection=None, enable_rbac_authorization=None, enable_soft_delete=None, enabled_for_deployment=None, enabled_for_disk_encryption=None, enabled_for_template_deployment=None, hsm_name=None, location=None, name=None, network_acls=None, network_acls_ips=None, network_acls_vnets=None, no_self_perms=None, no_wait=None, public_network_access=None, retention_days=None, sku=None, tags=None):
    '''
    Create a Vault or HSM.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - administrators -- [HSM Only] Administrator role for data plane operations for Managed HSM. It accepts a space separated list of OIDs that will be assigned.
    - bypass -- Bypass traffic for space-separated uses.
    - default_action -- Default action to apply when no rule matches.
    - enable_purge_protection -- Property specifying whether protection against purge is enabled for this vault. Setting this property to true activates protection against purge for this vault and its content - only the Key Vault service may initiate a hard, irrecoverable deletion. The setting is effective only if soft delete is also enabled. Enabling this functionality is irreversible - that is, the property does not accept false as its value.
    - enable_rbac_authorization -- Property that controls how data actions are authorized. When true, the key vault will use Role Based Access Control (RBAC) for authorization of data actions, and the access policies specified in vault properties will be  ignored (warning: this is a preview feature). When false, the key vault will use the access policies specified in vault properties, and any policy stored on Azure Resource Manager will be ignored. If null or not specified, the vault is created with the default value of false. Note that management actions are always authorized with RBAC.
    - enable_soft_delete -- [Vault Only] Property to specify whether the 'soft delete' functionality is enabled for this key vault. If it's not set to any value (true or false) when creating new key vault, it will be set to true by default. Once set to true, it cannot be reverted to false.
    - enabled_for_deployment -- [Vault Only] Property to specify whether Azure Virtual Machines are permitted to retrieve certificates stored as secrets from the key vault.
    - enabled_for_disk_encryption -- [Vault Only] Property to specify whether Azure Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys.
    - enabled_for_template_deployment -- [Vault Only] Property to specify whether Azure Resource Manager is permitted to retrieve secrets from the key vault.
    - hsm_name -- Name of the HSM. (--hsm-name and --name/-n are mutually exclusive, please specify just one of them)
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- Name of the Vault.
    - network_acls -- Network ACLs. It accepts a JSON filename or a JSON string. JSON format: `{\"ip\":[<ip1>, <ip2>...],\"vnet\":[<vnet_name_1>/<subnet_name_1>,<subnet_id2>...]}`
    - network_acls_ips -- Network ACLs IP rules. Space-separated list of IP addresses.
    - network_acls_vnets -- Network ACLS VNet rules. Space-separated list of Vnet/subnet pairs or subnet resource ids.
    - no_self_perms -- [Vault Only] Don't add permissions for the current user/service principal in the new vault.
    - no_wait -- Do not wait for the long-running operation to finish.
    - public_network_access -- Property to specify whether the vault will accept traffic from public internet. If set to 'disabled' all traffic except private endpoint traffic and that originates from trusted services will be blocked. This will override the set firewall rules, meaning that even if the firewall rules are present we will not honor the rules.
    - retention_days -- Soft delete data retention days. It accepts >=7 and <=90.
    - sku -- Required. SKU details. Allowed values for Vault: premium, standard. Default: standard. Allowed values for HSM: Standard_B1, Custom_B32. Default: Standard_B1
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az keyvault create", locals())


def recover(hsm_name=None, location=None, name=None, no_wait=None, resource_group=None):
    '''
    Recover a Vault or HSM.

    Optional Parameters:
    - hsm_name -- Name of the deleted HSM. (--hsm-name and --name/-n are mutually exclusive, please specify just one of them)
    - location -- Location of the deleted Vault or HSM
    - name -- Name of the deleted Vault.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- Resource group of the deleted Vault or HSM
    '''
    return _call_az("az keyvault recover", locals())


def list(resource_group=None, resource_type=None):
    '''
    List Vaults and/or HSMs.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_type -- When --resource-type is not present the command will list all Vaults and HSMs. Possible values for --resource-type are vault and hsm.
    '''
    return _call_az("az keyvault list", locals())


def show(hsm_name=None, name=None, resource_group=None):
    '''
    Show details of a Vault or HSM.

    Optional Parameters:
    - hsm_name -- Name of the HSM. (--hsm-name and --name/-n are mutually exclusive, please specify just one of them)
    - name -- Name of the Vault.
    - resource_group -- Proceed only if Key Vault belongs to the specified resource group.
    '''
    return _call_az("az keyvault show", locals())


def delete(hsm_name=None, name=None, no_wait=None, resource_group=None):
    '''
    Delete a Vault or HSM.

    Optional Parameters:
    - hsm_name -- Name of the HSM. (--hsm-name and --name/-n are mutually exclusive, please specify just one of them)
    - name -- Name of the Vault.
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- Proceed only if Key Vault belongs to the specified resource group.
    '''
    return _call_az("az keyvault delete", locals())


def purge(hsm_name=None, location=None, name=None, no_wait=None):
    '''
    Permanently delete the specified Vault or HSM. Aka Purges the deleted Vault or HSM.

    Optional Parameters:
    - hsm_name -- Name of the deleted HSM. (--hsm-name and --name/-n are mutually exclusive, please specify just one of them)
    - location -- Location of the deleted Vault or HSM
    - name -- Name of the deleted Vault.
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az keyvault purge", locals())


def set_policy(name, application_id=None, certificate_permissions=None, key_permissions=None, no_wait=None, object_id=None, resource_group=None, secret_permissions=None, spn=None, storage_permissions=None, upn=None):
    '''
    Update security policy settings for a Key Vault.

    Required Parameters:
    - name -- Name of the Vault.

    Optional Parameters:
    - application_id -- Application ID of the client making request on behalf of a principal. Exposed for compound identity using on-behalf-of authentication flow.
    - certificate_permissions -- Space-separated list of certificate permissions to assign.
    - key_permissions -- Space-separated list of key permissions to assign.
    - no_wait -- Do not wait for the long-running operation to finish.
    - object_id -- a GUID that identifies the principal that will receive permissions
    - resource_group -- Proceed only if Key Vault belongs to the specified resource group.
    - secret_permissions -- Space-separated list of secret permissions to assign.
    - spn -- name of a service principal that will receive permissions
    - storage_permissions -- Space-separated list of storage permissions to assign.
    - upn -- name of a user principal that will receive permissions
    '''
    return _call_az("az keyvault set-policy", locals())


def delete_policy(name, application_id=None, no_wait=None, object_id=None, resource_group=None, spn=None, upn=None):
    '''
    

    Required Parameters:
    - name -- Name of the Vault.

    Optional Parameters:
    - application_id -- Application ID of the client making request on behalf of a principal. Exposed for compound identity using on-behalf-of authentication flow.
    - no_wait -- Do not wait for the long-running operation to finish.
    - object_id -- a GUID that identifies the principal that will receive permissions
    - resource_group -- Proceed only if Key Vault belongs to the specified resource group.
    - spn -- name of a service principal that will receive permissions
    - upn -- name of a user principal that will receive permissions
    '''
    return _call_az("az keyvault delete-policy", locals())


def list_deleted(resource_type=None):
    '''
    Get information about the deleted Vaults or HSMs in a subscription.

    Optional Parameters:
    - resource_type -- When --resource-type is not present the command will list all deleted Vaults and HSMs. Possible values for --resource-type are vault and hsm.
    '''
    return _call_az("az keyvault list-deleted", locals())


def show_deleted(hsm_name=None, location=None, name=None):
    '''
    Show details of a deleted Vault or HSM.

    Optional Parameters:
    - hsm_name -- Name of the deleted HSM. (--hsm-name and --name/-n are mutually exclusive, please specify just one of them)
    - location -- Location of the deleted Vault or HSM
    - name -- Name of the deleted Vault.
    '''
    return _call_az("az keyvault show-deleted", locals())


def update(name, add=None, bypass=None, default_action=None, enable_purge_protection=None, enable_rbac_authorization=None, enable_soft_delete=None, enabled_for_deployment=None, enabled_for_disk_encryption=None, enabled_for_template_deployment=None, force_string=None, no_wait=None, public_network_access=None, remove=None, resource_group=None, retention_days=None, set=None):
    '''
    Update the properties of a Vault.

    Required Parameters:
    - name -- Name of the Vault.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - bypass -- Bypass traffic for space-separated uses.
    - default_action -- Default action to apply when no rule matches.
    - enable_purge_protection -- Property specifying whether protection against purge is enabled for this vault. Setting this property to true activates protection against purge for this vault and its content - only the Key Vault service may initiate a hard, irrecoverable deletion. The setting is effective only if soft delete is also enabled. Enabling this functionality is irreversible - that is, the property does not accept false as its value.
    - enable_rbac_authorization -- Property that controls how data actions are authorized. When true, the key vault will use Role Based Access Control (RBAC) for authorization of data actions, and the access policies specified in vault properties will be  ignored (warning: this is a preview feature). When false, the key vault will use the access policies specified in vault properties, and any policy stored on Azure Resource Manager will be ignored. If null or not specified, the vault is created with the default value of false. Note that management actions are always authorized with RBAC.
    - enable_soft_delete -- [Vault Only] Property to specify whether the 'soft delete' functionality is enabled for this key vault. If it's not set to any value (true or false) when creating new key vault, it will be set to true by default. Once set to true, it cannot be reverted to false.
    - enabled_for_deployment -- [Vault Only] Property to specify whether Azure Virtual Machines are permitted to retrieve certificates stored as secrets from the key vault.
    - enabled_for_disk_encryption -- [Vault Only] Property to specify whether Azure Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys.
    - enabled_for_template_deployment -- [Vault Only] Property to specify whether Azure Resource Manager is permitted to retrieve secrets from the key vault.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - no_wait -- Do not wait for the long-running operation to finish.
    - public_network_access -- Property to specify whether the vault will accept traffic from public internet. If set to 'disabled' all traffic except private endpoint traffic and that originates from trusted services will be blocked. This will override the set firewall rules, meaning that even if the firewall rules are present we will not honor the rules.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - resource_group -- Proceed only if Key Vault belongs to the specified resource group.
    - retention_days -- Soft delete data retention days. It accepts >=7 and <=90.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az keyvault update", locals())


def wait(name, created=None, custom=None, deleted=None, exists=None, interval=None, resource_group=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the Vault is met.

    Required Parameters:
    - name -- Name of the Vault.

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - resource_group -- Proceed only if Key Vault belongs to the specified resource group.
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az keyvault wait", locals())


def update_hsm(hsm_name, add=None, bypass=None, default_action=None, enable_purge_protection=None, force_string=None, no_wait=None, remove=None, resource_group=None, secondary_locations=None, set=None):
    '''
    Update the properties of a HSM.

    Required Parameters:
    - hsm_name -- Name of the HSM.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - bypass -- Bypass traffic for space-separated uses.
    - default_action -- Default action to apply when no rule matches.
    - enable_purge_protection -- Property specifying whether protection against purge is enabled for this managed HSM pool. Setting this property to true activates protection against purge for this managed HSM pool and its content - only the Managed HSM service may initiate a hard, irrecoverable deletion. The setting is effective only if soft delete is also enabled. Enabling this functionality is irreversible.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - no_wait -- Do not wait for the long-running operation to finish.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - resource_group -- Proceed only if Key Vault belongs to the specified resource group.
    - secondary_locations -- --secondary-locations extends/contracts an HSM pool to listed regions. The primary location where the resource was originally created CANNOT be removed.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az keyvault update-hsm", locals())


def wait_hsm(hsm_name, created=None, custom=None, deleted=None, exists=None, interval=None, resource_group=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the HSM is met.

    Required Parameters:
    - hsm_name -- Name of the HSM.

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - resource_group -- Proceed only if HSM belongs to the specified resource group.
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az keyvault wait-hsm", locals())

