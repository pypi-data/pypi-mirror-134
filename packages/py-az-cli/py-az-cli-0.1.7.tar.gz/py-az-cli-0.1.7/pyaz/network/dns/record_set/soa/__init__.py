from ..... pyaz_utils import _call_az

def show(resource_group, zone_name, name=None, record_type=None):
    '''
    Get the details of an SOA record.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - zone_name -- The name of the zone.

    Optional Parameters:
    - name -- ==SUPPRESS==
    - record_type -- ==SUPPRESS==
    '''
    return _call_az("az network dns record-set soa show", locals())


def update(resource_group, zone_name, email=None, expire_time=None, host=None, if_none_match=None, minimum_ttl=None, refresh_time=None, retry_time=None, serial_number=None):
    '''
    Update properties of an SOA record.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - zone_name -- The name of the zone.

    Optional Parameters:
    - email -- Email address.
    - expire_time -- Expire time (seconds).
    - host -- Host name.
    - if_none_match -- Create the record set only if it does not already exist.
    - minimum_ttl -- Minimum TTL (time-to-live, seconds).
    - refresh_time -- Refresh value (seconds).
    - retry_time -- Retry time (seconds).
    - serial_number -- Serial number.
    '''
    return _call_az("az network dns record-set soa update", locals())

