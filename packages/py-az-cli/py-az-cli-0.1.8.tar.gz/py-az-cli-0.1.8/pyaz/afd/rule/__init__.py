'''
Manage delivery rules within the specified rule set.
'''
from ... pyaz_utils import _call_az
from . import action, condition


def show(profile_name, resource_group, rule_name, rule_set_name):
    '''
    Show delivery rule details.

    Required Parameters:
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_name -- Name of the rule.
    - rule_set_name -- Name of the rule set.
    '''
    return _call_az("az afd rule show", locals())


def list(profile_name, resource_group, rule_set_name):
    '''
    

    Required Parameters:
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_set_name -- Name of the rule set.
    '''
    return _call_az("az afd rule list", locals())


def create(action_name, order, profile_name, resource_group, rule_name, rule_set_name, cache_behavior=None, cache_duration=None, custom_fragment=None, custom_hostname=None, custom_path=None, custom_querystring=None, destination=None, header_action=None, header_name=None, header_value=None, match_processing_behavior=None, match_values=None, match_variable=None, negate_condition=None, operator=None, preserve_unmatched_path=None, query_parameters=None, query_string_behavior=None, redirect_protocol=None, redirect_type=None, selector=None, source_pattern=None, transform=None):
    '''
    Creates a new delivery rule within the specified rule set.

    Required Parameters:
    - action_name -- Name of the action.
    - order -- The order in which the rules are applied for the endpoint. Possible values {0,1,2,3,………}. A rule with a lower order will be applied before one with a higher order. Rule with order 0 is a special rule. It does not require any condition and actions listed in it will always be applied.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_name -- Name of the rule.
    - rule_set_name -- Name of the rule set.

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
    - match_processing_behavior -- Indicate whether rules engine should continue to run the remaining rules or stop if matched. Defaults to Continue.
    - match_values -- Match values of the match condition (comma separated).
    - match_variable -- Name of the match condition.
    - negate_condition -- If true, negates the condition
    - operator -- Operator of the match condition.
    - preserve_unmatched_path -- If True, the remaining path after the source                pattern will be appended to the new destination path.
    - query_parameters -- Query parameters to include or exclude (comma separated).
    - query_string_behavior -- Query string behavior for the requests.
    - redirect_protocol -- Protocol to use for the redirect.
    - redirect_type -- The redirect type the rule will use when redirecting traffic.
    - selector -- Selector of the match condition.
    - source_pattern -- A request URI pattern that identifies the type of requests that may be rewritten.
    - transform -- Transform to apply before matching.
    '''
    return _call_az("az afd rule create", locals())


def delete(profile_name, resource_group, rule_name, rule_set_name, yes=None):
    '''
    Remove a delivery rule from rule set.

    Required Parameters:
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_name -- Name of the rule.
    - rule_set_name -- Name of the rule set.

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az afd rule delete", locals())

