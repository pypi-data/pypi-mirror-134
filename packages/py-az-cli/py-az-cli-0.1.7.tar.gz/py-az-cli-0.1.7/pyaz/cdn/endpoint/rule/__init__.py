'''
Manage delivery rules for an endpoint.
'''
from .... pyaz_utils import _call_az
from . import action, condition


def show(name, profile_name, resource_group):
    '''
    Show delivery rules asscociate with the endpoint.

    Required Parameters:
    - name -- Name of the CDN endpoint.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cdn endpoint rule show", locals())


def add(action_name, name, order, profile_name, resource_group, cache_behavior=None, cache_duration=None, custom_fragment=None, custom_hostname=None, custom_path=None, custom_querystring=None, destination=None, header_action=None, header_name=None, header_value=None, match_values=None, match_variable=None, negate_condition=None, operator=None, origin_group=None, preserve_unmatched_path=None, query_parameters=None, query_string_behavior=None, redirect_protocol=None, redirect_type=None, rule_name=None, selector=None, source_pattern=None, transform=None):
    '''
    Add a delivery rule to a CDN endpoint.

    Required Parameters:
    - action_name -- Name of the action.
    - name -- Name of the CDN endpoint.
    - order -- The order in which the rules are applied for the endpoint. Possible values {0,1,2,3,………}. A rule with a lower order will be applied before one with a higher order. Rule with order 0 is a special rule. It does not require any condition and actions listed in it will always be applied.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - cache_behavior -- Caching behavior for the requests.
    - cache_duration -- The duration for which the content needs to be cached.                Allowed format is [d.]hh:mm:ss.
    - custom_fragment -- Fragment to add to the redirect URL.
    - custom_hostname -- Host to redirect.                Leave empty to use the incoming host as the destination host.
    - custom_path -- The full path to redirect. Path cannot be empty and must start with /.                Leave empty to use the incoming path as destination path.
    - custom_querystring -- The set of query strings to be placed in the redirect URL.                leave empty to preserve the incoming query string.
    - destination -- The destination path to be used in the rewrite.
    - header_action -- Header action for the requests.
    - header_name -- Name of the header to modify.
    - header_value -- Value of the header.
    - match_values -- Match values of the match condition (comma separated).
    - match_variable -- Name of the match condition.
    - negate_condition -- If true, negates the condition
    - operator -- Operator of the match condition.
    - origin_group -- Name or ID of the OriginGroup that would override the default OriginGroup
    - preserve_unmatched_path -- If True, the remaining path after the source                pattern will be appended to the new destination path.
    - query_parameters -- Query parameters to include or exclude (comma separated).
    - query_string_behavior -- Query string behavior for the requests.
    - redirect_protocol -- Protocol to use for the redirect.
    - redirect_type -- The redirect type the rule will use when redirecting traffic.
    - rule_name -- Name of the rule.
    - selector -- Selector of the match condition.
    - source_pattern -- A request URI pattern that identifies the type of requests that may be rewritten.
    - transform -- Transform to apply before matching.
    '''
    return _call_az("az cdn endpoint rule add", locals())


def remove(name, profile_name, resource_group, order=None, rule_name=None):
    '''
    Remove a delivery rule from an endpoint.

    Required Parameters:
    - name -- Name of the CDN endpoint.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - order -- The order in which the rules are applied for the endpoint. Possible values {0,1,2,3,………}. A rule with a lower order will be applied before one with a higher order. Rule with order 0 is a special rule. It does not require any condition and actions listed in it will always be applied.
    - rule_name -- Name of the rule.
    '''
    return _call_az("az cdn endpoint rule remove", locals())

