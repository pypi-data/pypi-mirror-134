from .... pyaz_utils import _call_az

def set(enabled, gateway_name, resource_group, disabled_rule_groups=None, disabled_rules=None, exclusion=None, file_upload_limit=None, firewall_mode=None, max_request_body_size=None, no_wait=None, request_body_check=None, rule_set_type=None, rule_set_version=None):
    '''
    Update the firewall configuration of a web application.

    Required Parameters:
    - enabled -- Specify whether the application firewall is enabled.
    - gateway_name -- Name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - disabled_rule_groups -- None
    - disabled_rules -- None
    - exclusion -- None
    - file_upload_limit -- File upload size limit in MB.
    - firewall_mode -- Web application firewall mode.
    - max_request_body_size -- Max request body size in KB.
    - no_wait -- Do not wait for the long-running operation to finish.
    - request_body_check -- Allow WAF to check the request body.
    - rule_set_type -- None
    - rule_set_version -- None
    '''
    return _call_az("az network application-gateway waf-config set", locals())


def show(gateway_name, resource_group):
    '''
    Get the firewall configuration of a web application.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway waf-config show", locals())


def list_rule_sets(group=None, type=None, version=None):
    '''
    Get information on available WAF rule sets, rule groups, and rule IDs.

    Optional Parameters:
    - group -- None
    - type -- None
    - version -- None
    '''
    return _call_az("az network application-gateway waf-config list-rule-sets", locals())

