'''
billing customer
'''
from ... pyaz_utils import _call_az

def list(account_name, filter=None, profile_name=None, search=None):
    '''
    List the customers that are billed to a billing account. The operation is supported only for billing accounts with agreement type Microsoft Partner Agreement.

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.

    Optional Parameters:
    - filter -- May be used to filter the list of customers.
    - profile_name -- The ID that uniquely identifies a billing profile.
    - search -- Used for searching customers by their name. Any customer with name containing the search text will be included in the response
    '''
    return _call_az("az billing customer list", locals())


def show(account_name, name, expand=None):
    '''
    Get a customer by its ID. The operation is supported only for billing accounts with agreement type Microsoft Partner Agreement.

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.
    - name -- The ID that uniquely identifies a customer.

    Optional Parameters:
    - expand -- May be used to expand enabledAzurePlans and resellers
    '''
    return _call_az("az billing customer show", locals())

