from .... pyaz_utils import _call_az
from . import keys


def create(eventhub_name, name, namespace_name, resource_group, rights=None):
    '''
    Creates Authorizationrule for the given Eventhub

    Required Parameters:
    - eventhub_name -- Name of EventHub
    - name -- Name of Authorization Rule
    - namespace_name -- name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - rights -- Space-separated list of Authorization rule rights
    '''
    return _call_az("az eventhubs eventhub authorization-rule create", locals())


def show(eventhub_name, name, namespace_name, resource_group):
    '''
    shows the details of Authorizationrule

    Required Parameters:
    - eventhub_name -- Name of EventHub
    - name -- Name of EventHub AuthorizationRule
    - namespace_name -- name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventhubs eventhub authorization-rule show", locals())


def list(eventhub_name, namespace_name, resource_group):
    '''
    shows the list of Authorization-rules by Eventhub

    Required Parameters:
    - eventhub_name -- Name of EventHub
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventhubs eventhub authorization-rule list", locals())


def delete(eventhub_name, name, namespace_name, resource_group):
    '''
    Deletes the Authorizationrule of Eventhub.

    Required Parameters:
    - eventhub_name -- Name of EventHub
    - name -- Name of EventHub AuthorizationRule
    - namespace_name -- name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventhubs eventhub authorization-rule delete", locals())


def update(eventhub_name, name, namespace_name, resource_group, rights, add=None, force_string=None, remove=None, set=None):
    '''
    Updates Authorizationrule for the given Eventhub

    Required Parameters:
    - eventhub_name -- Name of EventHub
    - name -- Name of EventHub AuthorizationRule
    - namespace_name -- name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rights -- Space-separated list of Authorization rule rights

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az eventhubs eventhub authorization-rule update", locals())

