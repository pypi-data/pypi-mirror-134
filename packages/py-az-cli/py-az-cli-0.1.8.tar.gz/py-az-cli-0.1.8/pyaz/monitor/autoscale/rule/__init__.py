'''
Manage autoscale scaling rules.
'''
from .... pyaz_utils import _call_az

def create(autoscale_name, condition, scale, cooldown=None, profile_name=None, resource=None, resource_group=None, resource_namespace=None, resource_parent=None, resource_type=None, timegrain=None):
    '''
    Add a new autoscale rule.

    Required Parameters:
    - autoscale_name -- Name of the autoscale settings.
    - condition -- Condition on which to scale.
    - scale -- The direction and amount to scale.

    Optional Parameters:
    - cooldown -- The number of minutes that must elapse before another scaling event can occur.
    - profile_name -- Name of the autoscale profile.
    - resource -- Name or ID of the target resource.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_namespace -- Target resource provider namespace.
    - resource_parent -- Target resource parent path, if applicable.
    - resource_type -- Target resource type. Can also accept namespace/type format (Ex: 'Microsoft.Compute/virtualMachines')
    - timegrain -- None
    '''
    return _call_az("az monitor autoscale rule create", locals())


def list(autoscale_name, resource_group, profile_name=None):
    '''
    List autoscale rules for a profile.

    Required Parameters:
    - autoscale_name -- Name of the autoscale settings.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - profile_name -- Name of the autoscale profile.
    '''
    return _call_az("az monitor autoscale rule list", locals())


def delete(autoscale_name, index, resource_group, profile_name=None):
    '''
    Remove autoscale rules from a profile.

    Required Parameters:
    - autoscale_name -- Name of the autoscale settings.
    - index -- Space-separated list of rule indices to remove, or '*' to clear all rules.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - profile_name -- Name of the autoscale profile.
    '''
    return _call_az("az monitor autoscale rule delete", locals())


def copy(autoscale_name, dest_schedule, index, resource_group, source_schedule=None):
    '''
    Copy autoscale rules from one profile to another.

    Required Parameters:
    - autoscale_name -- Name of the autoscale settings.
    - dest_schedule -- Name of the profile to copy rules to.
    - index -- Space-separated list of rule indices to copy, or '*' to copy all rules.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - source_schedule -- Name of the profile to copy rules from.
    '''
    return _call_az("az monitor autoscale rule copy", locals())

