from ... pyaz_utils import _call_az
from . import subscription


def list(no_register=None):
    '''
    List all management groups.

    Optional Parameters:
    - no_register -- Skip registration for resource provider Microsoft.Management
    '''
    return _call_az("az account management-group list", locals())


def show(name, expand=None, no_register=None, recurse=None):
    '''
    Get a specific management group.

    Required Parameters:
    - name -- None

    Optional Parameters:
    - expand -- None
    - no_register -- Skip registration for resource provider Microsoft.Management
    - recurse -- None
    '''
    return _call_az("az account management-group show", locals())


def create(name, display_name=None, no_register=None, parent=None):
    '''
    Create a new management group.

    Required Parameters:
    - name -- None

    Optional Parameters:
    - display_name -- None
    - no_register -- Skip registration for resource provider Microsoft.Management
    - parent -- None
    '''
    return _call_az("az account management-group create", locals())


def delete(name, no_register=None):
    '''
    Delete an existing management group.

    Required Parameters:
    - name -- None

    Optional Parameters:
    - no_register -- Skip registration for resource provider Microsoft.Management
    '''
    return _call_az("az account management-group delete", locals())


def update(name, add=None, display_name=None, force_string=None, parent=None, remove=None, set=None):
    '''
    Update an existing management group.

    Required Parameters:
    - name -- None

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - display_name -- None
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - parent -- None
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az account management-group update", locals())

