'''
Manage marketplace agreement with marketplaceordering
'''
from .. pyaz_utils import _call_az

def show(plan, product, publisher):
    '''
    Get marketplace terms.

    Required Parameters:
    - plan -- Plan identifier string of image being deployed.
    - product -- Offeridentifier string of image being deployed.
    - publisher -- Publisher identifier string of image being deployed.
    '''
    return _call_az("az term show", locals())


def accept(plan, product, publisher):
    '''
    Accept marketplace terms.

    Required Parameters:
    - plan -- Plan identifier string of image being deployed.
    - product -- Offer identifier string of image being deployed.
    - publisher -- Publisher identifier string of image being deployed.
    '''
    return _call_az("az term accept", locals())

