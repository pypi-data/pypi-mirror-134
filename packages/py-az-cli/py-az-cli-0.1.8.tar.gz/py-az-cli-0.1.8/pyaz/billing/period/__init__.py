'''
Get billing periods for a subscription.
'''
from ... pyaz_utils import _call_az

def list(filter=None, skiptoken=None, top=None):
    '''
    

    Optional Parameters:
    - filter -- May be used to filter billing periods by billingPeriodEndDate. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'.
    - skiptoken -- Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    - top -- May be used to limit the number of results to the most recent N billing periods.
    '''
    return _call_az("az billing period list", locals())


def show(name):
    '''
    

    Required Parameters:
    - name -- name of the billing period
    '''
    return _call_az("az billing period show", locals())

