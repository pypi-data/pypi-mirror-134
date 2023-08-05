from .... pyaz_utils import _call_az
from . import keys


def create(name, namespace_name, resource_group, topic_name, rights=None):
    '''
    Create Authorization Rule for given Service Bus Topic

    Required Parameters:
    - name -- Name of Authorization Rule
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - topic_name -- name of Topic

    Optional Parameters:
    - rights -- Space-separated list of Authorization rule rights
    '''
    return _call_az("az servicebus topic authorization-rule create", locals())


def show(name, namespace_name, resource_group, topic_name):
    '''
    Shows the details of Authorization Rule for given Service Bus Topic

    Required Parameters:
    - name -- name of Topic Authorization Rule
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - topic_name -- name of Topic
    '''
    return _call_az("az servicebus topic authorization-rule show", locals())


def list(namespace_name, resource_group, topic_name):
    '''
    shows list of Authorization Rule by Service Bus Topic

    Required Parameters:
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - topic_name -- name of Topic
    '''
    return _call_az("az servicebus topic authorization-rule list", locals())


def delete(name, namespace_name, resource_group, topic_name):
    '''
    Deletes the Authorization Rule of the given Service Bus Topic.

    Required Parameters:
    - name -- name of Topic Authorization Rule
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - topic_name -- name of Topic
    '''
    return _call_az("az servicebus topic authorization-rule delete", locals())


def update(name, namespace_name, resource_group, rights, topic_name, add=None, force_string=None, remove=None, set=None):
    '''
    Create Authorization Rule for given Service Bus Topic

    Required Parameters:
    - name -- name of Topic Authorization Rule
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rights -- Space-separated list of Authorization rule rights
    - topic_name -- name of Topic

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az servicebus topic authorization-rule update", locals())

