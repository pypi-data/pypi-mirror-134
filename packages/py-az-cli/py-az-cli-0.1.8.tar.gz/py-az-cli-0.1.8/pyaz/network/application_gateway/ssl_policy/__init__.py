from .... pyaz_utils import _call_az
from . import predefined


def set(gateway_name, resource_group, cipher_suites=None, disabled_ssl_protocols=None, min_protocol_version=None, name=None, no_wait=None, policy_type=None):
    '''
    Update or clear SSL policy settings.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - cipher_suites -- Ssl cipher suites to be enabled in the specified order to application gateway.
    - disabled_ssl_protocols -- Space-separated list of protocols to disable.
    - min_protocol_version -- Minimum version of Ssl protocol to be supported on application gateway. Possible values include: "TLSv1_0", "TLSv1_1", "TLSv1_2".
    - name -- Name of Ssl predefined policy. Possible values include: "AppGwSslPolicy20150501", "AppGwSslPolicy20170401", "AppGwSslPolicy20170401S".
    - no_wait -- Do not wait for the long-running operation to finish.
    - policy_type -- Type of Ssl Policy. Possible values include: "Predefined", "Custom".
    '''
    return _call_az("az network application-gateway ssl-policy set", locals())


def show(gateway_name, resource_group):
    '''
    Get the details of gateway's SSL policy settings.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway ssl-policy show", locals())


def list_options():
    '''
    Lists available SSL options for configuring SSL policy.
    '''
    return _call_az("az network application-gateway ssl-policy list-options", locals())

