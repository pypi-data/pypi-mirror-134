'''
Get policy metadata resources.
'''
from ... pyaz_utils import _call_az

def list(top=None):
    '''
    List policy metadata resources.

    Optional Parameters:
    - top -- Maximum number of records to return.
    '''
    return _call_az("az policy metadata list", locals())


def show(name):
    '''
    Get a single policy metadata resource.

    Required Parameters:
    - name -- The name of the metadata resource.
    '''
    return _call_az("az policy metadata show", locals())

