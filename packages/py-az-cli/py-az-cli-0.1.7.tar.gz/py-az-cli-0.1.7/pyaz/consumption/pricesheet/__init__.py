'''
Inspect the price sheet of an Azure subscription within a billing period.
'''
from ... pyaz_utils import _call_az

def show(billing_period_name=None, include_meter_details=None):
    '''
    Show the price sheet for an Azure subscription within a billing period.

    Optional Parameters:
    - billing_period_name -- Name of the billing period to get the price sheet.
    - include_meter_details -- Include meter details in the price sheet.
    '''
    return _call_az("az consumption pricesheet show", locals())

