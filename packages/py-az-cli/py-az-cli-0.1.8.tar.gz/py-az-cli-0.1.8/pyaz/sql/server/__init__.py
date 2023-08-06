'''
Manage SQL servers.
'''
from ... pyaz_utils import _call_az
from . import ad_admin, ad_only_auth, audit_policy, conn_policy, dns_alias, firewall_rule, key, outbound_firewall_rule, tde_key, vnet_rule


def create(name, resource_group, admin_password=None, admin_user=None, assign_identity=None, enable_ad_only_auth=None, enable_public_network=None, external_admin_name=None, external_admin_principal_type=None, external_admin_sid=None, identity_type=None, key_id=None, location=None, minimal_tls_version=None, no_wait=None, primary_user_assigned_identity_id=None, restrict_outbound_network_access=None, user_assigned_identity_id=None):
    '''
    Create a server.

    Required Parameters:
    - name -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - admin_password -- The administrator login password (required for server creation).
    - admin_user -- Administrator username for the server. Once created it cannot be changed.
    - assign_identity -- Generate and assign an Azure Active Directory Identity for this server for use with key management services like Azure KeyVault.
    - enable_ad_only_auth -- Enable Azure Active Directory Only Authentication for this server.
    - enable_public_network -- Set whether public network access to server is allowed or not. When false,only connections made through Private Links can reach this server.
    - external_admin_name -- Display name of the Azure AD administrator user, group or application.
    - external_admin_principal_type -- User, Group or Application
    - external_admin_sid -- The unique ID of the Azure AD administrator. Object Id for User or Group, Client Id for Applications
    - identity_type -- Type of Identity to be used. Possible values are SystemAsssigned,UserAssigned, SystemAssigned,UserAssigned and None.
    - key_id -- The key vault URI for encryption.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - minimal_tls_version -- The minimal TLS version enforced by the sql server for inbound connections.
    - no_wait -- Do not wait for the long-running operation to finish.
    - primary_user_assigned_identity_id -- The ID of the primary user managed identity.
    - restrict_outbound_network_access -- Set whether outbound network access to server is restricted or not. When true,the outbound connections from the server will be restricted.
    - user_assigned_identity_id -- Generate and assign an User Managed Identity(UMI) for this server.
    '''
    return _call_az("az sql server create", locals())


def delete(name, resource_group, yes=None):
    '''
    

    Required Parameters:
    - name -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az sql server delete", locals())


def show(name, resource_group, expand_ad_admin=None):
    '''
    

    Required Parameters:
    - name -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expand_ad_admin -- Expand the Active Directory Administrator for the server.
    '''
    return _call_az("az sql server show", locals())


def list(expand_ad_admin=None, resource_group=None):
    '''
    List available servers.

    Optional Parameters:
    - expand_ad_admin -- Expand the Active Directory Administrator for the server.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql server list", locals())


def update(name, resource_group, add=None, admin_password=None, assign_identity=None, enable_public_network=None, force_string=None, identity_type=None, key_id=None, minimal_tls_version=None, no_wait=None, primary_user_assigned_identity_id=None, remove=None, restrict_outbound_network_access=None, set=None, user_assigned_identity_id=None):
    '''
    Update a server.

    Required Parameters:
    - name -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - admin_password -- The administrator login password.
    - assign_identity -- Generate and assign an Azure Active Directory Identity for this server for use with key management services like Azure KeyVault.
    - enable_public_network -- Set whether public network access to server is allowed or not. When false,only connections made through Private Links can reach this server.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - identity_type -- Type of Identity to be used. Possible values are SystemAsssigned,UserAssigned, SystemAssigned,UserAssigned and None.
    - key_id -- The key vault URI for encryption.
    - minimal_tls_version -- The minimal TLS version enforced by the sql server for inbound connections.
    - no_wait -- Do not wait for the long-running operation to finish.
    - primary_user_assigned_identity_id -- The ID of the primary user managed identity.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - restrict_outbound_network_access -- Set whether outbound network access to server is restricted or not. When true,the outbound connections from the server will be restricted.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - user_assigned_identity_id -- Generate and assign an User Managed Identity(UMI) for this server.
    '''
    return _call_az("az sql server update", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, expand=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the SQL server is met.

    Required Parameters:
    - name -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - expand -- The child resources to include in the response.
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az sql server wait", locals())


def list_usages(name, resource_group):
    '''
    

    Required Parameters:
    - name -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql server list-usages", locals())

