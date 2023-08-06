'''
Display billing agreement
'''
from ... pyaz_utils import _call_az

def list(account_name, expand=None):
    '''
    List the agreements for a billing account.

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.

    Optional Parameters:
    - expand -- May be used to expand the participants.
    '''
    return _call_az("az billing agreement list", locals())


def show(account_name, name, expand=None):
    '''
    Get an agreement by ID.

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.
    - name -- The ID that uniquely identifies an agreement.

    Optional Parameters:
    - expand -- May be used to expand the participants.
    '''
    return _call_az("az billing agreement show", locals())

