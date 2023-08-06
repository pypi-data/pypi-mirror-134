'''
Manage template specs at subscription or resource group scope.
'''
from .. pyaz_utils import _call_az

def create(name, resource_group, description=None, display_name=None, location=None, tags=None, template_file=None, ui_form_definition=None, version=None, version_description=None, yes=None):
    '''
    Create a template spec and or template spec version.

    Required Parameters:
    - name -- The name of the template spec.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - description -- The description of the parent template spec.
    - display_name -- The display name of the template spec
    - location -- The location to store the template-spec and template-spec version(s). Cannot be changed after creation.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - template_file -- a path to a template file or Bicep file in the file system
    - ui_form_definition -- The uiFormDefinition file path in the file system for the template spec version.
    - version -- The template spec version.
    - version_description -- The description of the template spec version.
    - yes -- Do not prompt for confirmation
    '''
    return _call_az("az ts create", locals())


def update(description=None, display_name=None, name=None, resource_group=None, tags=None, template_file=None, template_spec=None, ui_form_definition=None, version=None, version_description=None, yes=None):
    '''
    Update a template spec version.

    Optional Parameters:
    - description -- The description of the parent template spec.
    - display_name -- The display name of the template spec
    - name -- The name of the template spec.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - template_file -- a path to a template file or Bicep file in the file system
    - template_spec -- The template spec resource id.
    - ui_form_definition -- The uiFormDefinition file path in the file system for the template spec version.
    - version -- The template spec version.
    - version_description -- The description of the template spec version.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az ts update", locals())


def export(output_folder, name=None, resource_group=None, template_spec=None, version=None):
    '''
    Export the specified template spec version and artifacts (if any) to the specified output folder.

    Required Parameters:
    - output_folder -- Existing folder to output export(s).

    Optional Parameters:
    - name -- The name of the template spec.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - template_spec -- The template spec resource id.
    - version -- The template spec version.
    '''
    return _call_az("az ts export", locals())


def show(name=None, resource_group=None, template_spec=None, version=None):
    '''
    Get the specified template spec or template spec version.

    Optional Parameters:
    - name -- The name of the template spec.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - template_spec -- The template spec resource id.
    - version -- The template spec version.
    '''
    return _call_az("az ts show", locals())


def list(name=None, resource_group=None):
    '''
    List template specs or template spec versions.

    Optional Parameters:
    - name -- The name of the template spec.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ts list", locals())


def delete(name=None, resource_group=None, template_spec=None, version=None, yes=None):
    '''
    Delete a specified template spec or template spec version by name or resource ID..

    Optional Parameters:
    - name -- The name of the template spec.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - template_spec -- The template spec resource id.
    - version -- The template spec version.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az ts delete", locals())

