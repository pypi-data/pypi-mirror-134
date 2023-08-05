'''
Manage Batch service options for a subscription at the region level.
'''
from ... pyaz_utils import _call_az
from . import quotas


def list_skus(location, filter=None, maxresults=None):
    '''
    List virtual machine SKUs available in a location.

    Required Parameters:
    - location -- The region for which to display the available Batch VM SKUs.

    Optional Parameters:
    - filter -- OData filter expression. Valid properties for filtering are "familyName".
    - maxresults -- The maximum number of items to return in the response.
    '''
    return _call_az("az batch location list-skus", locals())

