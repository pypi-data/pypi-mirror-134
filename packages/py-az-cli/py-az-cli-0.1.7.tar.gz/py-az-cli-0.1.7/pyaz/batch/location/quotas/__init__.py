'''
Manage Batch service quotas at the region level.
'''
from .... pyaz_utils import _call_az

def show(location):
    '''
    

    Required Parameters:
    - location -- The region for which to display the Batch service quotas.
    '''
    return _call_az("az batch location quotas show", locals())

