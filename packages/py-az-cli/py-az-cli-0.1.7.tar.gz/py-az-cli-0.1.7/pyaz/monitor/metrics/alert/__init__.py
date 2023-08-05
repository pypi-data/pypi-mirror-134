'''
Manage near-realtime metric alert rules.
'''
from .... pyaz_utils import _call_az
from . import condition, dimension


def create(condition, name, resource_group, scopes, action=None, auto_mitigate=None, description=None, disabled=None, evaluation_frequency=None, severity=None, tags=None, target_resource_region=None, target_resource_type=None, window_size=None):
    '''
    Create a metric-based alert rule.

    Required Parameters:
    - condition -- None
    - name -- Name of the alert rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - scopes -- Space-separated list of scopes the rule applies to. The resources specified in this parameter must be of the same type and exist in the same location.

    Optional Parameters:
    - action -- None
    - auto_mitigate -- Automatically resolve the alert.
    - description -- Free-text description of the rule.
    - disabled -- None
    - evaluation_frequency -- Frequency with which to evaluate the rule in "##h##m##s" format.
    - severity -- Severity of the alert from 0 (critical) to 4 (verbose).
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - target_resource_region -- The region of the target resource(s) in scopes. This must be provided when scopes is resource group or subscription.
    - target_resource_type -- The resource type of the target resource(s) in scopes. This must be provided when scopes is resource group or subscription.
    - window_size -- Time over which to aggregate metrics in "##h##m##s" format.
    '''
    return _call_az("az monitor metrics alert create", locals())


def delete(name, resource_group):
    '''
    Delete a metrics-based alert rule.

    Required Parameters:
    - name -- Name of the alert rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az monitor metrics alert delete", locals())


def list(resource_group=None):
    '''
    List metric-based alert rules.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az monitor metrics alert list", locals())


def show(name, resource_group):
    '''
    Show a metrics-based alert rule.

    Required Parameters:
    - name -- Name of the alert rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az monitor metrics alert show", locals())


def update(name, resource_group, add=None, add_action=None, add_condition=None, auto_mitigate=None, description=None, enabled=None, evaluation_frequency=None, force_string=None, remove=None, remove_actions=None, remove_conditions=None, scopes=None, set=None, severity=None, tags=None, window_size=None):
    '''
    Update a metric-based alert rule.

    Required Parameters:
    - name -- Name of the alert rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - add_action -- None
    - add_condition -- None
    - auto_mitigate -- Automatically resolve the alert.
    - description -- Free-text description of the rule.
    - enabled -- Whether the metric alert rule is enabled.
    - evaluation_frequency -- Frequency with which to evaluate the rule in "##h##m##s" format.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - remove_actions -- None
    - remove_conditions -- None
    - scopes -- Space-separated list of scopes the rule applies to. The resources specified in this parameter must be of the same type and exist in the same location.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - severity -- Severity of the alert from 0 (critical) to 4 (verbose).
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - window_size -- Time over which to aggregate metrics in "##h##m##s" format.
    '''
    return _call_az("az monitor metrics alert update", locals())

