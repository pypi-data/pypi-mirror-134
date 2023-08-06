'''
Manage Azure Marketplace image terms.
'''
from .... pyaz_utils import _call_az

def accept(offer=None, plan=None, publisher=None, urn=None):
    '''
    Accept Azure Marketplace image terms so that the image can be used to create VMs.

    Optional Parameters:
    - offer -- Image offer
    - plan -- Image billing plan
    - publisher -- Image publisher
    - urn -- URN, in the format of 'publisher:offer:sku:version'. If specified, other argument values can be omitted
    '''
    return _call_az("az vm image terms accept", locals())


def cancel(offer=None, plan=None, publisher=None, urn=None):
    '''
    Cancel Azure Marketplace image terms.

    Optional Parameters:
    - offer -- Image offer
    - plan -- Image billing plan
    - publisher -- Image publisher
    - urn -- URN, in the format of 'publisher:offer:sku:version'. If specified, other argument values can be omitted
    '''
    return _call_az("az vm image terms cancel", locals())


def show(offer=None, plan=None, publisher=None, urn=None):
    '''
    Get the details of Azure Marketplace image terms.

    Optional Parameters:
    - offer -- Image offer
    - plan -- Image billing plan
    - publisher -- Image publisher
    - urn -- URN, in the format of 'publisher:offer:sku:version'. If specified, other argument values can be omitted
    '''
    return _call_az("az vm image terms show", locals())

