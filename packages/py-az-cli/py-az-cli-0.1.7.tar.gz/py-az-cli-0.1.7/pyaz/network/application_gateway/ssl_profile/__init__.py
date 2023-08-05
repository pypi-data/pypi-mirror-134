from .... pyaz_utils import _call_az

def add(gateway_name, name, resource_group, cipher_suites=None, client_auth_configuration=None, disabled_ssl_protocols=None, min_protocol_version=None, policy_name=None, policy_type=None, trusted_client_certificates=None):
    '''
    Add ssl profiles of the application gateway.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- Name of the SSL profile that is unique within an Application Gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - cipher_suites -- Ssl cipher suites to be enabled in the specified order to application gateway.
    - client_auth_configuration -- Client authentication configuration of the application gateway resource.
    - disabled_ssl_protocols -- Space-separated list of protocols to disable.
    - min_protocol_version -- Minimum version of Ssl protocol to be supported on application gateway.
    - policy_name -- Name of Ssl Policy.
    - policy_type -- Type of Ssl Policy.
    - trusted_client_certificates -- Array of references to application gateway trusted client certificates.
    '''
    return _call_az("az network application-gateway ssl-profile add", locals())


def remove(gateway_name, name, resource_group):
    '''
    Remove an existing ssl profiles of the application gateway.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- Name of the SSL profile that is unique within an Application Gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway ssl-profile remove", locals())


def list(gateway_name, resource_group):
    '''
    List the existing ssl profiles of the application gateway.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway ssl-profile list", locals())


def show(gateway_name, name, resource_group):
    '''
    Show an existing ssl profiles of the application gateway.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- Name of the SSL profile that is unique within an Application Gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway ssl-profile show", locals())


def update(gateway_name, name, resource_group, cipher_suites=None, client_auth_configuration=None, disabled_ssl_protocols=None, min_protocol_version=None, policy_name=None, policy_type=None, trusted_client_certificates=None):
    '''
    Update ssl profiles of the application gateway.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- Name of the SSL profile that is unique within an Application Gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - cipher_suites -- Ssl cipher suites to be enabled in the specified order to application gateway.
    - client_auth_configuration -- Client authentication configuration of the application gateway resource.
    - disabled_ssl_protocols -- Space-separated list of protocols to disable.
    - min_protocol_version -- Minimum version of Ssl protocol to be supported on application gateway.
    - policy_name -- Name of Ssl Policy.
    - policy_type -- Type of Ssl Policy.
    - trusted_client_certificates -- Array of references to application gateway trusted client certificates.
    '''
    return _call_az("az network application-gateway ssl-profile update", locals())

