from .... pyaz_utils import _call_az

def list(custom_domains, date_time_begin, date_time_end, granularity, metrics, profile_name, protocols, resource_group, continents=None, country_or_regions=None, group_by=None):
    '''
    

    Required Parameters:
    - custom_domains -- The domains to be included.
    - date_time_begin -- The start datetime.
    - date_time_end -- The end datetime.
    - granularity -- The interval granularity.
    - metrics -- Metric types to include.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - protocols -- The protocols to be included.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - continents -- ISO 3316-1 alpha-2 continent code.
    - country_or_regions -- ISO 3316-1 alpha-2 region code.
    - group_by -- Aggregate demensions.
    '''
    return _call_az("az afd log-analytic metric list", locals())

