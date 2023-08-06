'''
Inspect the marketplace usage data of an Azure subscription within a billing period.
'''
from ... pyaz_utils import _call_az

def list(billing_period_name=None, end_date=None, start_date=None, top=None):
    '''
    List the marketplace for an Azure subscription within a billing period.

    Optional Parameters:
    - billing_period_name -- Name of the billing period to get the marketplace.
    - end_date -- End date (YYYY-MM-DD in UTC). If specified, also requires --start-date.
    - start_date -- Start date (YYYY-MM-DD in UTC). If specified, also requires --end-date.
    - top -- Maximum number of items to return. Value range: 1-1000.
    '''
    return _call_az("az consumption marketplace list", locals())

