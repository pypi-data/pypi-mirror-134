from .... pyaz_utils import _call_az

def list(date_time_begin, date_time_end, granularity, metrics, profile_name, resource_group, actions=None, group_by=None, rule_types=None):
    '''
    

    Required Parameters:
    - date_time_begin -- The start datetime.
    - date_time_end -- The end datetime.
    - granularity -- The interval granularity.
    - metrics -- Metric types to be included.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - actions -- The WAF actions to be included.
    - group_by -- Aggregate demensions.
    - rule_types -- The WAF rule types to be included.
    '''
    return _call_az("az afd waf-log-analytic metric list", locals())

