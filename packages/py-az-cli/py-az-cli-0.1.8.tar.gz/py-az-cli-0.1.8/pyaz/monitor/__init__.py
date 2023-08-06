'''
Manage the Azure Monitor Service.
'''
from .. pyaz_utils import _call_az
from . import action_group, activity_log, alert, autoscale, autoscale_settings, diagnostic_settings, log_profiles, metrics, private_link_scope


def clone(source_resource, target_resource, always_clone=None, types=None):
    '''
    Clone metrics alert rules from one resource to another resource.

    Required Parameters:
    - source_resource -- Resource ID of the source resource.
    - target_resource -- Resource ID of the target resource.

    Optional Parameters:
    - always_clone -- If this argument is applied, all monitor settings would be cloned instead of expanding its scope.
    - types -- List of types of monitor settings which would be cloned.
    '''
    return _call_az("az monitor clone", locals())

