from ..... pyaz_utils import _call_az

def list(policy_name, resource_group):
    '''
    List properties of a web application firewall global configuration.

    Required Parameters:
    - policy_name -- The name of the web application firewall policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway waf-policy policy-setting list", locals())


def update(policy_name, resource_group, add=None, file_upload_limit_in_mb=None, force_string=None, max_request_body_size_in_kb=None, mode=None, remove=None, request_body_check=None, set=None, state=None):
    '''
    Update properties of a web application firewall global configuration.

    Required Parameters:
    - policy_name -- The name of the web application firewall policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - file_upload_limit_in_mb -- Maximum file upload size in Mb for WAF."
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - max_request_body_size_in_kb -- Maximum request body size in Kb for WAF.
    - mode -- Describes if it is in detection mode or prevention mode at policy level.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - request_body_check -- Specified to require WAF to check request Body.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - state -- Describes if the policy is in enabled state or disabled state.
    '''
    return _call_az("az network application-gateway waf-policy policy-setting update", locals())

