'''
Manage App Service plans.
'''
from .. pyaz_utils import _call_az
from . import ase, domain, hybrid_connection, plan, vnet_integration


def list_locations(sku, linux_workers_enabled=None):
    '''
    List regions where a plan sku is available.

    Required Parameters:
    - sku -- The pricing tiers, e.g., F1(Free), D1(Shared), B1(Basic Small), B2(Basic Medium), B3(Basic Large), S1(Standard Small), P1V2(Premium V2 Small), P1V3(Premium V3 Small), P2V3(Premium V3 Medium), P3V3(Premium V3 Large), PC2 (Premium Container Small), PC3 (Premium Container Medium), PC4 (Premium Container Large), I1 (Isolated Small), I2 (Isolated Medium), I3 (Isolated Large), I1v2 (Isolated V2 Small), I2v2 (Isolated V2 Medium), I3v2 (Isolated V2 Large)

    Optional Parameters:
    - linux_workers_enabled -- get regions which support hosting web apps on Linux workers
    '''
    return _call_az("az appservice list-locations", locals())

