'''
billing policy
'''
from ... pyaz_utils import _call_az

def update(account_name, customer_name=None, marketplace_purchases=None, profile_name=None, reservation_purchases=None, view_charges=None):
    '''
    Update the policies for a billing profile. This operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.

    Optional Parameters:
    - customer_name -- The ID that uniquely identifies a customer
    - marketplace_purchases -- The policy that controls whether Azure marketplace purchases are allowed for a billing profile.
    - profile_name -- The ID that uniquely identifies a billing profile.
    - reservation_purchases -- The policy that controls whether Azure reservation purchases are allowed for a billing profile.
    - view_charges -- The policy that controls whether users with Azure RBAC access to a subscription can view its charges.
    '''
    return _call_az("az billing policy update", locals())


def show(account_name, customer_name=None, profile_name=None):
    '''
    Show the policies for a customer or for a billing profile. This operation is supported only for billing accounts with agreement type Microsoft Partner Agreement."

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account

    Optional Parameters:
    - customer_name -- The ID that uniquely identifies a customer
    - profile_name -- The ID that uniquely identifies a billing profile.
    '''
    return _call_az("az billing policy show", locals())

