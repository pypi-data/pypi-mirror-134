'''
List reservation details.
'''
from .... pyaz_utils import _call_az

def list(end_date, reservation_order_id, start_date, reservation_id=None):
    '''
    List the details of a reservation by order id or reservation id.

    Required Parameters:
    - end_date -- End date (YYYY-MM-DD in UTC). Only needed for daily grain and if specified, also requires --start-date.
    - reservation_order_id -- Reservation order id.
    - start_date -- Start date (YYYY-MM-DD in UTC). Only needed for daily grain and if specified, also requires --end-date.

    Optional Parameters:
    - reservation_id -- Reservation id.
    '''
    return _call_az("az consumption reservation detail list", locals())

