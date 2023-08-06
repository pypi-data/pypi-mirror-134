'''
Manage deployment operations at management group.
'''
from .... pyaz_utils import _call_az

def list(management_group_id, name):
    '''
    List deployment operations at management group.

    Required Parameters:
    - management_group_id -- The management group id.
    - name -- The deployment name.
    '''
    return _call_az("az deployment operation mg list", locals())


def show(management_group_id, name, operation_ids):
    '''
    Show a deployment operation at management group.

    Required Parameters:
    - management_group_id -- The management group id.
    - name -- The deployment name.
    - operation_ids -- A list of operation ids to show
    '''
    return _call_az("az deployment operation mg show", locals())

