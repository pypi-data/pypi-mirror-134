from ...... pyaz_utils import _call_az

def add(match_variables, name, operator, policy_name, resource_group, values, negate=None, transforms=None):
    '''
    A match condition to an application gateway WAF policy custom rule.

    Required Parameters:
    - match_variables -- Space-separated list of variables to use when matching. Variable values: RemoteAddr, RequestMethod, QueryString, PostArgs, RequestUri, RequestHeaders, RequestBody, RequestCookies
    - name -- Name of the WAF policy rule.
    - operator -- Operator for matching.
    - policy_name -- The name of the application gateway WAF policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - values -- Space-separated list of values to match.

    Optional Parameters:
    - negate -- Match the negative of the condition.
    - transforms -- Space-separated list of transforms to apply when matching.
    '''
    return _call_az("az network application-gateway waf-policy custom-rule match-condition add", locals())


def list(name, policy_name, resource_group):
    '''
    List application gateway WAF policy custom rule match conditions.

    Required Parameters:
    - name -- Name of the WAF policy rule.
    - policy_name -- The name of the application gateway WAF policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway waf-policy custom-rule match-condition list", locals())


def remove(index, name, policy_name, resource_group):
    '''
    Remove a match condition from an application gateway WAF policy custom rule.

    Required Parameters:
    - index -- Index of the match condition to remove.
    - name -- Name of the WAF policy rule.
    - policy_name -- The name of the application gateway WAF policy.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway waf-policy custom-rule match-condition remove", locals())

