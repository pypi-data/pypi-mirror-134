from .... pyaz_utils import _call_az
from . import keys


def create(name, namespace_name, resource_group, rights=None):
    '''
    Create Authorization Rule for the given Relay Service Namespace

    Required Parameters:
    - name -- Name of Namespace Authorization Rule
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - rights -- Space-separated list of Authorization rule rights
    '''
    return _call_az("az relay namespace authorization-rule create", locals())


def show(name, namespace_name, resource_group):
    '''
    Shows the details of Relay Service Namespace Authorization Rule

    Required Parameters:
    - name -- Name of Namespace Authorization Rule
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az relay namespace authorization-rule show", locals())


def list(namespace_name, resource_group):
    '''
    Shows the list of Authorization Rule by Relay Service Namespace

    Required Parameters:
    - namespace_name -- Name of the Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az relay namespace authorization-rule list", locals())


def delete(name, namespace_name, resource_group):
    '''
    Deletes the Authorization Rule of the Relay Service Namespace.

    Required Parameters:
    - name -- Name of Namespace Authorization Rule
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az relay namespace authorization-rule delete", locals())


def update(name, namespace_name, resource_group, rights, add=None, force_string=None, remove=None, set=None):
    '''
    Updates Authorization Rule for the given Relay Service Namespace

    Required Parameters:
    - name -- Name of Namespace Authorization Rule
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rights -- Space-separated list of Authorization rule rights

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az relay namespace authorization-rule update", locals())

