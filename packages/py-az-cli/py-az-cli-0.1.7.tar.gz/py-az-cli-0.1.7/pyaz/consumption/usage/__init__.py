'''
Inspect the usage of Azure resources.
'''
from ... pyaz_utils import _call_az

def list(billing_period_name=None, end_date=None, include_additional_properties=None, include_meter_details=None, start_date=None, top=None):
    '''
    List the details of Azure resource consumption, either as an invoice or within a billing period.

    Optional Parameters:
    - billing_period_name -- Name of the billing period to get the usage details that associate with.
    - end_date -- End date (YYYY-MM-DD in UTC). If specified, also requires --start-date.
    - include_additional_properties -- Include additional properties in the usages.
    - include_meter_details -- Include meter details in the usages.
    - start_date -- Start date (YYYY-MM-DD in UTC). If specified, also requires --end-date.
    - top -- Maximum number of items to return. Value range: 1-1000.
    '''
    return _call_az("az consumption usage list", locals())

