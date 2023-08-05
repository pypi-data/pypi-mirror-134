from .... pyaz_utils import _call_az
from . import condition, set


def create(gateway_name, name, resource_group, rule_set_name, enable_reroute=None, modified_path=None, modified_query_string=None, no_wait=None, request_headers=None, response_headers=None, sequence=None):
    '''
    Create a rewrite rule.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- Name of the rewrite rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_set_name -- Name of the rewrite rule set.

    Optional Parameters:
    - enable_reroute -- If set as true, it will re-evaluate the url path map provided in path based request routing rules using modified path.
    - modified_path -- Url path for url rewrite
    - modified_query_string -- Query string for url rewrite.
    - no_wait -- Do not wait for the long-running operation to finish.
    - request_headers -- Space-separated list of HEADER=VALUE pairs.
    - response_headers -- Space-separated list of HEADER=VALUE pairs.
    - sequence -- Determines the execution order of the rule in the rule set.
    '''
    return _call_az("az network application-gateway rewrite-rule create", locals())


def show(gateway_name, name, resource_group, rule_set_name):
    '''
    Get the details of a rewrite rule.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- Name of the rewrite rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_set_name -- Name of the rewrite rule set.
    '''
    return _call_az("az network application-gateway rewrite-rule show", locals())


def list(gateway_name, resource_group, rule_set_name):
    '''
    List rewrite rules.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_set_name -- Name of the rewrite rule set.
    '''
    return _call_az("az network application-gateway rewrite-rule list", locals())


def delete(gateway_name, name, resource_group, rule_set_name, no_wait=None):
    '''
    Delete a rewrite rule.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- Name of the rewrite rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_set_name -- Name of the rewrite rule set.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network application-gateway rewrite-rule delete", locals())


def update(gateway_name, name, resource_group, rule_set_name, add=None, enable_reroute=None, force_string=None, modified_path=None, modified_query_string=None, no_wait=None, remove=None, request_headers=None, response_headers=None, sequence=None, set=None):
    '''
    Update a rewrite rule.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- Name of the rewrite rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_set_name -- Name of the rewrite rule set.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - enable_reroute -- If set as true, it will re-evaluate the url path map provided in path based request routing rules using modified path.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - modified_path -- Url path for url rewrite
    - modified_query_string -- Query string for url rewrite.
    - no_wait -- Do not wait for the long-running operation to finish.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - request_headers -- Space-separated list of HEADER=VALUE pairs.
    - response_headers -- Space-separated list of HEADER=VALUE pairs.
    - sequence -- Determines the execution order of the rule in the rule set.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az network application-gateway rewrite-rule update", locals())


def list_request_headers():
    return _call_az("az network application-gateway rewrite-rule list-request-headers", locals())


def list_response_headers():
    return _call_az("az network application-gateway rewrite-rule list-response-headers", locals())

