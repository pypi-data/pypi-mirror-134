'''
Manage near-realtime metric alert rule dimensions.
'''
from ..... pyaz_utils import _call_az

def create(name, value, operator=None):
    '''
    Build a metric alert rule dimension.

    Required Parameters:
    - name -- Name of the dimension.
    - value -- The values to apply on the operation.

    Optional Parameters:
    - operator -- Dimension operator.
    '''
    return _call_az("az monitor metrics alert dimension create", locals())

