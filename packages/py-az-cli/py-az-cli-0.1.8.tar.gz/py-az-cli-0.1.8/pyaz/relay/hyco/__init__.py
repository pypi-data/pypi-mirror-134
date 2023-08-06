'''
Manage Azure Relay Service Hybrid Connection and Authorization Rule
'''
from ... pyaz_utils import _call_az
from . import authorization_rule


def create(name, namespace_name, resource_group, requires_client_authorization=None, user_metadata=None):
    '''
    Create the Relay Service Hybrid Connection

    Required Parameters:
    - name -- Name of Hybrid Connection
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - requires_client_authorization -- Indicates whether client authorization is required
    - user_metadata -- Endpoint metadata
    '''
    return _call_az("az relay hyco create", locals())


def show(name, namespace_name, resource_group):
    '''
    Shows the Relay Service Hybrid Connection Details

    Required Parameters:
    - name -- Name of Hybrid Connection
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az relay hyco show", locals())


def list(namespace_name, resource_group):
    '''
    List the Hybrid Connection by Relay Service Namespace

    Required Parameters:
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az relay hyco list", locals())


def delete(name, namespace_name, resource_group):
    '''
    Deletes the Relay Service Hybrid Connection

    Required Parameters:
    - name -- Name of Hybrid Connection
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az relay hyco delete", locals())


def update(name, namespace_name, resource_group, add=None, force_string=None, remove=None, requires_client_authorization=None, set=None, status=None, user_metadata=None):
    '''
    Updates the Relay Service Hybrid Connection

    Required Parameters:
    - name -- Name of Hybrid Connection
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - requires_client_authorization -- Indicates whether client authorization is required
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - status -- Enumerates the possible values for the status of a messaging entity.
    - user_metadata -- Endpoint metadata
    '''
    return _call_az("az relay hyco update", locals())

