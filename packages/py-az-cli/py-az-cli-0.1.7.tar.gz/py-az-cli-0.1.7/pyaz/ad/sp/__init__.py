'''
Manage Azure Active Directory service principals for automation authentication.
'''
from ... pyaz_utils import _call_az
from . import credential, owner


def create(id):
    '''
    Create a service principal.

    Required Parameters:
    - id -- identifier uri, application id, or object id of the associated application
    '''
    return _call_az("az ad sp create", locals())


def delete(id):
    '''
    Delete a service principal and its role assignments.

    Required Parameters:
    - id -- service principal name, or object id
    '''
    return _call_az("az ad sp delete", locals())


def list(all=None, display_name=None, filter=None, show_mine=None, spn=None):
    '''
    List service principals.

    Optional Parameters:
    - all -- list all entities, expect long delay if under a big organization
    - display_name -- object's display name or its prefix
    - filter -- OData filter, e.g. --filter "displayname eq 'test' and servicePrincipalType eq 'Application'"
    - show_mine -- list entities owned by the current user
    - spn -- service principal name
    '''
    return _call_az("az ad sp list", locals())


def show(id):
    '''
    Get the details of a service principal.

    Required Parameters:
    - id -- service principal name, or object id
    '''
    return _call_az("az ad sp show", locals())


def update(id, add=None, force_string=None, remove=None, set=None):
    '''
    Update a service principal

    Required Parameters:
    - id -- service principal name, or object id

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az ad sp update", locals())


def create_for_rbac(cert=None, create_cert=None, keyvault=None, name=None, role=None, scopes=None, sdk_auth=None, skip_assignment=None, years=None):
    '''
    Create a service principal and configure its access to Azure resources.

    Optional Parameters:
    - cert -- None
    - create_cert -- None
    - keyvault -- None
    - name -- None
    - role -- None
    - scopes -- None
    - sdk_auth -- output result in compatible with Azure SDK auth file
    - skip_assignment -- Skip creating the default assignment, which allows the service principal to access resources under the current subscription. When specified, --scopes will be ignored. You may use `az role assignment create` to create role assignments for this service principal later.
    - years -- None
    '''
    return _call_az("az ad sp create-for-rbac", locals())

