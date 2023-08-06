'''
Manage classic metric-based alert rules.
'''
from ... pyaz_utils import _call_az

def create(condition, name, target, action=None, description=None, disabled=None, email_service_owners=None, location=None, resource_group=None, tags=None, target_namespace=None, target_parent=None, target_type=None):
    '''
    Create a classic metric-based alert rule.

    Required Parameters:
    - condition -- None
    - name -- Name of the alert rule.
    - target -- Name or ID of the target resource.

    Optional Parameters:
    - action -- None
    - description -- None
    - disabled -- None
    - email_service_owners -- None
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - target_namespace -- Target resource provider namespace.
    - target_parent -- Target resource parent path, if applicable.
    - target_type -- Target resource type. Can also accept namespace/type format (Ex: 'Microsoft.Compute/virtualMachines')
    '''
    return _call_az("az monitor alert create", locals())


def delete(name, resource_group):
    '''
    Delete an alert rule.

    Required Parameters:
    - name -- Name of the alert rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az monitor alert delete", locals())


def show(name, resource_group):
    '''
    Show an alert rule.

    Required Parameters:
    - name -- Name of the alert rule.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az monitor alert show", locals())


def list(resource_group):
    '''
    List alert rules in a resource group.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az monitor alert list", locals())


def show_incident(name, resource_group, rule_name):
    '''
    Get the details of an alert rule incident.

    Required Parameters:
    - name -- The name of the incident to retrieve.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_name -- Name of the alert rule.
    '''
    return _call_az("az monitor alert show-incident", locals())


def list_incidents(resource_group, rule_name):
    '''
    List all incidents for an alert rule.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_name -- Name of the alert rule.
    '''
    return _call_az("az monitor alert list-incidents", locals())


def update(name, add=None, add_action=None, aggregation=None, condition=None, description=None, email_service_owners=None, enabled=None, force_string=None, metric=None, operator=None, period=None, remove=None, remove_action=None, resource=None, resource_group=None, resource_namespace=None, resource_parent=None, resource_type=None, set=None, tags=None, threshold=None):
    '''
    Update a classic metric-based alert rule.

    Required Parameters:
    - name -- Name of the alert rule.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - add_action -- None
    - aggregation -- None
    - condition -- None
    - description -- None
    - email_service_owners -- None
    - enabled -- None
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - metric -- None
    - operator -- None
    - period -- None
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - remove_action -- None
    - resource -- Name or ID of the target resource.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_namespace -- Target resource provider namespace.
    - resource_parent -- Target resource parent path, if applicable.
    - resource_type -- Target resource type. Can also accept namespace/type format (Ex: 'Microsoft.Compute/virtualMachines')
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - threshold -- None
    '''
    return _call_az("az monitor alert update", locals())

