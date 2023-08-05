from .... pyaz_utils import _call_az
from . import keys


def create(hybrid_connection_name, name, namespace_name, resource_group, rights=None):
    '''
    Create Authorization Rule for given Relay Service Hybrid Connection

    Required Parameters:
    - hybrid_connection_name -- name of Hybrid Connection
    - name -- name of Hybrid Connection Authorization Rule
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - rights -- Space-separated list of Authorization rule rights
    '''
    return _call_az("az relay hyco authorization-rule create", locals())


def show(hybrid_connection_name, name, namespace_name, resource_group):
    '''
    Shows the details of Authorization Rule for given Relay Service Hybrid Connection

    Required Parameters:
    - hybrid_connection_name -- name of Hybrid Connection
    - name -- name of Hybrid Connection Authorization Rule
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az relay hyco authorization-rule show", locals())


def list(hybrid_connection_name, namespace_name, resource_group):
    '''
    shows list of Authorization Rule by Relay Service Hybrid Connection

    Required Parameters:
    - hybrid_connection_name -- name of Hybrid Connection
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az relay hyco authorization-rule list", locals())


def delete(hybrid_connection_name, name, namespace_name, resource_group):
    '''
    Deletes the Authorization Rule of the given Relay Service Hybrid Connection.

    Required Parameters:
    - hybrid_connection_name -- name of Hybrid Connection
    - name -- name of Hybrid Connection Authorization Rule
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az relay hyco authorization-rule delete", locals())


def update(hybrid_connection_name, name, namespace_name, resource_group, rights, add=None, force_string=None, remove=None, set=None):
    '''
    Create Authorization Rule for given Relay Service Hybrid Connection

    Required Parameters:
    - hybrid_connection_name -- name of Hybrid Connection
    - name -- name of Hybrid Connection Authorization Rule
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rights -- Space-separated list of Authorization rule rights

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az relay hyco authorization-rule update", locals())

