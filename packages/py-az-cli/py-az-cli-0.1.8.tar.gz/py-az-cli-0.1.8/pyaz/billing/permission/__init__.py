'''
List billing permissions
'''
from ... pyaz_utils import _call_az

def list(account_name, customer_name=None, invoice_section_name=None, profile_name=None):
    '''
    List the billing permissions the caller has on a billing account.

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.

    Optional Parameters:
    - customer_name -- The ID that uniquely identifies a customer.
    - invoice_section_name -- The ID that uniquely identifies an invoice section.
    - profile_name -- The ID that uniquely identifies a billing profile.
    '''
    return _call_az("az billing permission list", locals())

