from ... pyaz_utils import _call_az
from . import address_pool, auth_cert, client_cert, frontend_ip, frontend_port, http_listener, http_settings, identity, private_link, probe, redirect_config, rewrite_rule, root_cert, rule, ssl_cert, ssl_policy, ssl_profile, url_path_map, waf_config, waf_policy


def create(name, resource_group, capacity=None, cert_file=None, cert_password=None, connection_draining_timeout=None, custom_error_pages=None, enable_private_link=None, frontend_port=None, http2=None, http_settings_cookie_based_affinity=None, http_settings_port=None, http_settings_protocol=None, identity=None, key_vault_secret_id=None, location=None, max_capacity=None, min_capacity=None, no_wait=None, private_ip_address=None, private_link_ip_address=None, private_link_primary=None, private_link_subnet=None, private_link_subnet_prefix=None, public_ip_address=None, public_ip_address_allocation=None, routing_rule_type=None, servers=None, sku=None, ssl_certificate_name=None, ssl_profile=None, ssl_profile_id=None, subnet=None, subnet_address_prefix=None, tags=None, trusted_client_cert=None, validate=None, vnet_address_prefix=None, vnet_name=None, waf_policy=None, zones=None):
    '''
    Create an application gateway.

    Required Parameters:
    - name -- Name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - capacity -- The number of instances to use with the application gateway.
    - cert_file -- The path to the PFX certificate file.
    - cert_password -- The certificate password
    - connection_draining_timeout -- The time in seconds after a backend server is removed during which on open connection remains active. Range: 0 (disabled) to 3600
    - custom_error_pages -- Space-separated list of custom error pages in `STATUS_CODE=URL` format.
    - enable_private_link -- Enable Private Link feature for this application gateway. If both public IP and private IP are enbaled, taking effect only in public frontend IP
    - frontend_port -- The front end port number.
    - http2 -- Use HTTP2 for the application gateway.
    - http_settings_cookie_based_affinity -- Enable or disable HTTP settings cookie-based affinity.
    - http_settings_port -- The HTTP settings port.
    - http_settings_protocol -- The HTTP settings protocol.
    - identity -- Name or ID of the ManagedIdentity Resource
    - key_vault_secret_id -- Secret Id of (base-64 encoded unencrypted pfx) 'Secret' or 'Certificate' object stored in Azure KeyVault. You need enable soft delete for keyvault to use this feature.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - max_capacity -- Upper bound on the number of application gateway instances.
    - min_capacity -- Lower bound on the number of application gateway instances.
    - no_wait -- Do not wait for the long-running operation to finish.
    - private_ip_address -- Static private IP address to use.
    - private_link_ip_address -- The static private IP address of a subnet for Private Link. If omitting, a dynamic one will be created
    - private_link_primary -- Whether the IP configuration is primary or not
    - private_link_subnet -- The name of the subnet within the same vnet of an application gateway
    - private_link_subnet_prefix -- The CIDR prefix to use when creating a new subnet
    - public_ip_address -- Name or ID of a public IP address. Uses existing resource or creates new if specified, or none if omitted.
    - public_ip_address_allocation -- The kind of IP allocation to use when creating a new public IP.
    - routing_rule_type -- The request routing rule type.
    - servers -- Space-separated list of IP addresses or DNS names corresponding to backend servers.
    - sku -- The name of the SKU.
    - ssl_certificate_name -- The certificate name. Default will be `<application-gateway-name>SslCert`.
    - ssl_profile -- None
    - ssl_profile_id -- SSL profile resource of the application gateway.
    - subnet -- Name or ID of the subnet. Will create resource if it does not exist. If name specified, also specify --vnet-name. If you want to use an existing subnet in other resource group or subscription, please provide the ID instead of the name of the subnet
    - subnet_address_prefix -- The CIDR prefix to use when creating a new subnet.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - trusted_client_cert -- None
    - validate -- Generate and validate the ARM template without creating any resources.
    - vnet_address_prefix -- The CIDR prefix to use when creating a new VNet.
    - vnet_name -- The virtual network (VNet) name.
    - waf_policy -- Name or ID of a web application firewall (WAF) policy.
    - zones -- Space-separated list of availability zones into which to provision the resource.
    '''
    return _call_az("az network application-gateway create", locals())


def delete(name, resource_group, no_wait=None):
    '''
    Delete an application gateway.

    Required Parameters:
    - name -- Name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network application-gateway delete", locals())


def show(name, resource_group):
    '''
    Get the details of an application gateway.

    Required Parameters:
    - name -- Name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway show", locals())


def list(resource_group=None):
    '''
    List application gateways.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway list", locals())


def start(name, resource_group):
    '''
    Start an application gateway.

    Required Parameters:
    - name -- Name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway start", locals())


def stop(name, resource_group):
    '''
    Stop an application gateway.

    Required Parameters:
    - name -- Name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway stop", locals())


def show_backend_health(name, resource_group, address_pool=None, expand=None, host=None, host_name_from_http_settings=None, http_settings=None, match_body=None, match_status_codes=None, path=None, protocol=None, timeout=None):
    '''
    Get information on the backend health of an application gateway.

    Required Parameters:
    - name -- Name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - address_pool -- The name or ID of the backend address pool.
    - expand -- Expands BackendAddressPool and BackendHttpSettings referenced in backend health.
    - host -- The name of the host to send the probe.
    - host_name_from_http_settings -- Use host header from HTTP settings.
    - http_settings -- The name or ID of the HTTP settings.
    - match_body -- Body that must be contained in the health response.
    - match_status_codes -- Space-separated list of allowed ranges of healthy status codes for the health response.
    - path -- The relative path of the probe. Valid paths start from "/"
    - protocol -- The HTTP settings protocol.
    - timeout -- The probe timeout in seconds.
    '''
    return _call_az("az network application-gateway show-backend-health", locals())


def update(name, resource_group, add=None, capacity=None, custom_error_pages=None, force_string=None, http2=None, max_capacity=None, min_capacity=None, no_wait=None, remove=None, set=None, sku=None, tags=None):
    '''
    Update an application gateway.

    Required Parameters:
    - name -- Name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - capacity -- The number of instances to use with the application gateway.
    - custom_error_pages -- Space-separated list of custom error pages in `STATUS_CODE=URL` format.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - http2 -- Use HTTP2 for the application gateway.
    - max_capacity -- Upper bound on the number of application gateway instances.
    - min_capacity -- Lower bound on the number of application gateway instances.
    - no_wait -- Do not wait for the long-running operation to finish.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - sku -- The name of the SKU.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az network application-gateway update", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the application gateway is met.

    Required Parameters:
    - name -- Name of the application gateway.
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
    return _call_az("az network application-gateway wait", locals())

