from ..... pyaz_utils import _call_az

def create(gateway_name, resource_group, rule_name, rule_set_name, variable, ignore_case=None, negate=None, no_wait=None, pattern=None):
    '''
    Create a rewrite rule condition.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_name -- Name of the rewrite rule.
    - rule_set_name -- Name of the rewrite rule set.
    - variable -- The variable whose value is being evaluated.

    Optional Parameters:
    - ignore_case -- Make comparison case-insensitive.
    - negate -- Check the negation of the condition.
    - no_wait -- Do not wait for the long-running operation to finish.
    - pattern -- The pattern, either fixed string or regular expression, that evaluates the truthfulness of the condition
    '''
    return _call_az("az network application-gateway rewrite-rule condition create", locals())


def show(gateway_name, resource_group, rule_name, rule_set_name, variable):
    '''
    Get the details of a rewrite rule condition.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_name -- Name of the rewrite rule.
    - rule_set_name -- Name of the rewrite rule set.
    - variable -- The variable whose value is being evaluated.
    '''
    return _call_az("az network application-gateway rewrite-rule condition show", locals())


def list(gateway_name, resource_group, rule_name, rule_set_name):
    '''
    List rewrite rule conditions.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_name -- Name of the rewrite rule.
    - rule_set_name -- Name of the rewrite rule set.
    '''
    return _call_az("az network application-gateway rewrite-rule condition list", locals())


def delete(gateway_name, resource_group, rule_name, rule_set_name, variable, no_wait=None):
    '''
    Delete a rewrite rule condition.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_name -- Name of the rewrite rule.
    - rule_set_name -- Name of the rewrite rule set.
    - variable -- The variable whose value is being evaluated.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network application-gateway rewrite-rule condition delete", locals())


def update(gateway_name, resource_group, rule_name, rule_set_name, variable, add=None, force_string=None, ignore_case=None, negate=None, no_wait=None, pattern=None, remove=None, set=None):
    '''
    Update a rewrite rule condition.

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_name -- Name of the rewrite rule.
    - rule_set_name -- Name of the rewrite rule set.
    - variable -- The variable whose value is being evaluated.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - ignore_case -- Make comparison case-insensitive.
    - negate -- Check the negation of the condition.
    - no_wait -- Do not wait for the long-running operation to finish.
    - pattern -- The pattern, either fixed string or regular expression, that evaluates the truthfulness of the condition
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az network application-gateway rewrite-rule condition update", locals())


def list_server_variables():
    return _call_az("az network application-gateway rewrite-rule condition list-server-variables", locals())

