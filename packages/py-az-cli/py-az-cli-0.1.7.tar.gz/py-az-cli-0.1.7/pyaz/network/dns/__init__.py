'''
Manage DNS domains in Azure.
'''
from ... pyaz_utils import _call_az
from . import record_set, zone


def list_references(parameters):
    '''
    

    Required Parameters:
    - parameters -- Properties for dns resource reference request.
    '''
    return _call_az("az network dns list-references", locals())

