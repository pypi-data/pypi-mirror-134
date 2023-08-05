'''
Information on available virtual machine images.
'''
from ... pyaz_utils import _call_az
from . import terms


def list_offers(location, publisher, edge_zone=None):
    '''
    List the VM image offers available in the Azure Marketplace.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - publisher -- image publisher

    Optional Parameters:
    - edge_zone -- The name of edge zone.
    '''
    return _call_az("az vm image list-offers", locals())


def list_publishers(location, edge_zone=None):
    '''
    List the VM image publishers available in the Azure Marketplace.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.

    Optional Parameters:
    - edge_zone -- The name of edge zone.
    '''
    return _call_az("az vm image list-publishers", locals())


def list_skus(location, offer, publisher, edge_zone=None):
    '''
    List the VM image SKUs available in the Azure Marketplace.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - offer -- image offer
    - publisher -- image publisher

    Optional Parameters:
    - edge_zone -- The name of edge zone.
    '''
    return _call_az("az vm image list-skus", locals())


def list(all=None, edge_zone=None, location=None, offer=None, publisher=None, sku=None):
    '''
    List the VM/VMSS images available in the Azure Marketplace.

    Optional Parameters:
    - all -- None
    - edge_zone -- The name of edge zone.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - offer -- image offer
    - publisher -- image publisher
    - sku -- image sku
    '''
    return _call_az("az vm image list", locals())


def accept_terms(offer=None, plan=None, publisher=None, urn=None):
    '''
    Accept Azure Marketplace term so that the image can be used to create VMs

    Optional Parameters:
    - offer -- image offer
    - plan -- image billing plan
    - publisher -- image publisher
    - urn -- URN, in format of 'publisher:offer:sku:version' or 'publisher:offer:sku:edge_zone:version'. If specified, other argument values can be omitted
    '''
    return _call_az("az vm image accept-terms", locals())


def show(edge_zone=None, location=None, offer=None, publisher=None, sku=None, urn=None, version=None):
    '''
    Get the details for a VM image available in the Azure Marketplace.

    Optional Parameters:
    - edge_zone -- The name of edge zone.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - offer -- image offer
    - publisher -- image publisher
    - sku -- image sku
    - urn -- URN, in format of 'publisher:offer:sku:version' or 'publisher:offer:sku:edge_zone:version'. If specified, other argument values can be omitted
    - version -- image sku's version
    '''
    return _call_az("az vm image show", locals())

