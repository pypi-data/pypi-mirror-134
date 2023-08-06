from .... pyaz_utils import _call_az
from . import a, aaaa, caa, cname, mx, ns, ptr, soa, srv, txt


def list(resource_group, zone_name, record_type=None):
    '''
    List all record sets within a DNS zone.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - zone_name -- The name of the zone.

    Optional Parameters:
    - record_type -- ==SUPPRESS==
    '''
    return _call_az("az network dns record-set list", locals())

