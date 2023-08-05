'''
Manage Azure Relay Service Namespace
'''
from ... pyaz_utils import _call_az
from . import authorization_rule


def create(name, resource_group, location=None, tags=None):
    '''
    Create a Relay Service Namespace

    Required Parameters:
    - name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az relay namespace create", locals())


def show(name, resource_group):
    '''
    Shows the Relay Service Namespace details

    Required Parameters:
    - name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az relay namespace show", locals())


def list(resource_group=None):
    '''
    List the Relay Service Namespaces

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az relay namespace list", locals())


def delete(name, resource_group):
    '''
    Deletes the Relay Service Namespace

    Required Parameters:
    - name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az relay namespace delete", locals())


def exists(name):
    '''
    check for the availability of the given name for the Namespace

    Required Parameters:
    - name -- Namespace name. Name can contain only letters, numbers, and hyphens. The namespace must start with a letter, and it must end with a letter or number.
    '''
    return _call_az("az relay namespace exists", locals())


def update(name, resource_group, add=None, force_string=None, remove=None, set=None, tags=None):
    '''
    Updates a Relay Service Namespace

    Required Parameters:
    - name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az relay namespace update", locals())

