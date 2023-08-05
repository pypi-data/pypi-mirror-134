'''
Manage Azure Managed Applications.
'''
from ... pyaz_utils import _call_az

def create(authorizations, description, display_name, lock_level, name, resource_group, create_ui_definition=None, location=None, main_template=None, package_file_uri=None, tags=None):
    '''
    Create a managed application definition.

    Required Parameters:
    - authorizations -- space-separated authorization pairs in a format of `<principalId>:<roleDefinitionId>`
    - description -- the managed application definition description
    - display_name -- the managed application definition display name
    - lock_level -- The type of lock restriction.
    - name -- the managed application definition name
    - resource_group -- the resource group of the managed application definition

    Optional Parameters:
    - create_ui_definition -- JSON formatted string or a path to a file with such content
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - main_template -- JSON formatted string or a path to a file with such content
    - package_file_uri -- the managed application definition package file uri
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az managedapp definition create", locals())


def update(authorizations, description, display_name, lock_level, name, resource_group, create_ui_definition=None, location=None, main_template=None, package_file_uri=None, tags=None):
    '''
    Update a managed application definition.

    Required Parameters:
    - authorizations -- space-separated authorization pairs in a format of `<principalId>:<roleDefinitionId>`
    - description -- the managed application definition description
    - display_name -- the managed application definition display name
    - lock_level -- The type of lock restriction.
    - name -- the managed application definition name
    - resource_group -- the resource group of the managed application definition

    Optional Parameters:
    - create_ui_definition -- JSON formatted string or a path to a file with such content
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - main_template -- JSON formatted string or a path to a file with such content
    - package_file_uri -- the managed application definition package file uri
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az managedapp definition update", locals())


def delete(name, resource_group):
    '''
    Delete a managed application definition.

    Required Parameters:
    - name -- The name of the managed application definition to delete.
    - resource_group -- the resource group of the managed application definition
    '''
    return _call_az("az managedapp definition delete", locals())


def show(name=None, resource_group=None):
    '''
    

    Optional Parameters:
    - name -- the managed application definition name
    - resource_group -- the resource group of the managed application definition
    '''
    return _call_az("az managedapp definition show", locals())


def list(resource_group):
    '''
    List managed application definitions.

    Required Parameters:
    - resource_group -- the resource group of the managed application definition
    '''
    return _call_az("az managedapp definition list", locals())

