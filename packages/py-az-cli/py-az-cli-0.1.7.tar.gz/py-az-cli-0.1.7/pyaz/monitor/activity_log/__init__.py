from ... pyaz_utils import _call_az
from . import alert


def list(caller=None, correlation_id=None, end_time=None, filters=None, max_events=None, namespace=None, offset=None, resource_group=None, resource_id=None, select=None, start_time=None, status=None):
    '''
    List and query activity log events.

    Optional Parameters:
    - caller -- None
    - correlation_id -- None
    - end_time -- End time of the query. Defaults to the current time. Format: date (yyyy-mm-dd) time (hh:mm:ss.xxxxx) timezone (+/-hh:mm)
    - filters -- OData filters. Will ignore other filter arguments.
    - max_events -- None
    - namespace -- None
    - offset -- None
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_id -- None
    - select -- None
    - start_time -- Start time of the query. Format: date (yyyy-mm-dd) time (hh:mm:ss.xxxxx) timezone (+/-hh:mm)
    - status -- None
    '''
    return _call_az("az monitor activity-log list", locals())


def list_categories():
    '''
    List the event categories of activity logs.
    '''
    return _call_az("az monitor activity-log list-categories", locals())

