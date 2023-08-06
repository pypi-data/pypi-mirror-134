'''
Manage autoscaling profiles.
'''
from .... pyaz_utils import _call_az

def create(autoscale_name, count, name, resource_group, timezone, copy_rules=None, end=None, max_count=None, min_count=None, recurrence=None, start=None):
    '''
    Create a fixed or recurring autoscale profile.

    Required Parameters:
    - autoscale_name -- Name of the autoscale settings.
    - count -- The numer of instances to use. If used with --min/max-count, the default number of instances to use.
    - name -- Name of the autoscale profile.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - timezone -- None

    Optional Parameters:
    - copy_rules -- Name of an existing schedule from which to copy the scaling rules for the new schedule.
    - end -- End time. Format: date (yyyy-mm-dd) time (hh:mm:ss.xxxxx)
    - max_count -- The maximum number of instances.
    - min_count -- The minimum number of instances.
    - recurrence -- None
    - start -- Start time. Format: date (yyyy-mm-dd) time (hh:mm:ss.xxxxx)
    '''
    return _call_az("az monitor autoscale profile create", locals())


def list(autoscale_name, resource_group):
    '''
    List autoscale profiles.

    Required Parameters:
    - autoscale_name -- Name of the autoscale settings.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az monitor autoscale profile list", locals())


def show(autoscale_name, name, resource_group):
    '''
    Show details of an autoscale profile.

    Required Parameters:
    - autoscale_name -- Name of the autoscale settings.
    - name -- Name of the autoscale profile.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az monitor autoscale profile show", locals())


def delete(autoscale_name, name, resource_group):
    '''
    Delete an autoscale profile.

    Required Parameters:
    - autoscale_name -- Name of the autoscale settings.
    - name -- Name of the autoscale profile.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az monitor autoscale profile delete", locals())


def list_timezones(offset=None, search_query=None):
    '''
    Look up time zone information.

    Optional Parameters:
    - offset -- Filter results based on UTC hour offset.
    - search_query -- Query text to find.
    '''
    return _call_az("az monitor autoscale profile list-timezones", locals())

