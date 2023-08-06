from .... pyaz_utils import _call_az

def list(date_time_begin, date_time_end, max_ranking, metrics, profile_name, rankings, resource_group, actions=None, rule_types=None):
    '''
    

    Required Parameters:
    - date_time_begin -- The start datetime.
    - date_time_end -- The end datetime.
    - max_ranking -- The maximum number of rows to return based on the ranking.
    - metrics -- Metric types to be included.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - rankings -- The dimemsions to be included for ranking.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - actions -- The WAF actions to be included.
    - rule_types -- The WAF rule types to be included.
    '''
    return _call_az("az afd waf-log-analytic ranking list", locals())

