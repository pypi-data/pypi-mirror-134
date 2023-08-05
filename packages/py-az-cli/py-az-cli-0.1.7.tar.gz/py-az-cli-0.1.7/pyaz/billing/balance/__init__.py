'''
billing balance
'''
from ... pyaz_utils import _call_az

def show(account_name, profile_name):
    '''
    The available credit balance for a billing profile. This is the balance that can be used for pay now to settle due or past due invoices. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.
    - profile_name -- The ID that uniquely identifies a billing profile.
    '''
    return _call_az("az billing balance show", locals())

