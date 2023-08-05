'''
List reservation summaries.
'''
from .... pyaz_utils import _call_az

def list(grain, reservation_order_id, end_date=None, reservation_id=None, start_date=None):
    '''
    List reservation summaries for daily or monthly by order Id or reservation id.

    Required Parameters:
    - grain -- Reservation summary grain. Possible values are daily or monthly.
    - reservation_order_id -- Reservation order id.

    Optional Parameters:
    - end_date -- End date (YYYY-MM-DD in UTC). Only needed for daily grain and if specified, also requires --start-date.
    - reservation_id -- Reservation id.
    - start_date -- Start date (YYYY-MM-DD in UTC). Only needed for daily grain and if specified, also requires --end-date.
    '''
    return _call_az("az consumption reservation summary list", locals())

