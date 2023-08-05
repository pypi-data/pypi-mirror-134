'''
Manage Azure Relay Service WCF Relay and Authorization Rule
'''
from ... pyaz_utils import _call_az
from . import authorization_rule


def create(name, namespace_name, relay_type, resource_group, requires_client_authorization=None, requires_transport_security=None, user_metadata=None):
    '''
    Create the Relay Service WCF Relay

    Required Parameters:
    - name -- Name of WCF Relay
    - namespace_name -- Name of Namespace
    - relay_type -- Relay type
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - requires_client_authorization -- Indicates whether client authorization is required
    - requires_transport_security -- Indicates whether transport security is required
    - user_metadata -- Endpoint metadata
    '''
    return _call_az("az relay wcfrelay create", locals())


def show(name, namespace_name, resource_group):
    '''
    shows the Relay Service WCF Relay Details

    Required Parameters:
    - name -- Name of WCF Relay
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az relay wcfrelay show", locals())


def list(namespace_name, resource_group):
    '''
    List the WCF Relay by Relay Service Namespace

    Required Parameters:
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az relay wcfrelay list", locals())


def delete(name, namespace_name, resource_group):
    '''
    Deletes the Relay Service WCF Relay

    Required Parameters:
    - name -- Name of WCF Relay
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az relay wcfrelay delete", locals())


def update(name, namespace_name, resource_group, add=None, force_string=None, relay_type=None, remove=None, set=None, status=None, user_metadata=None):
    '''
    Updates existing Relay Service WCF Relay

    Required Parameters:
    - name -- Name of WCF Relay
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - relay_type -- Relay type
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - status -- Enumerates the possible values for the status of a messaging entity.
    - user_metadata -- Endpoint metadata
    '''
    return _call_az("az relay wcfrelay update", locals())

