'''
Manage image builder template customizers.
'''
from .... pyaz_utils import _call_az

def add(customizer_name, name, resource_group, type, dest_path=None, exit_codes=None, file_source=None, filters=None, inline_script=None, restart_check_command=None, restart_command=None, restart_timeout=None, script_url=None, search_criteria=None, update_limit=None):
    '''
    Add an image builder customizer to an image builder template.

    Required Parameters:
    - customizer_name -- Name of the customizer.
    - name -- The name of the image template.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - type -- Type of customizer to be added to the image template.

    Optional Parameters:
    - dest_path -- The absolute destination path where the file specified in --file-source will be downloaded to in the image
    - exit_codes -- Space-separated list of valid exit codes, as integers
    - file_source -- The URI of the file to be downloaded into the image. It can be a github link, SAS URI for Azure Storage, etc.
    - filters -- Space delimited filters to select updates to apply. Omit or specify empty array to use the default (no filter)
    - inline_script -- Space-separated list of inline script lines to customize the image with.
    - restart_check_command -- Command to verify that restart succeeded.
    - restart_command -- Command to execute the restart operation.
    - restart_timeout -- Restart timeout specified as a string consisting of a magnitude and unit, e.g. '5m' (5 minutes) or '2h' (2 hours)
    - script_url -- URL of script to customize the image with. The URL must be publicly accessible.
    - search_criteria -- Criteria to search updates. Omit or specify empty string to use the default (search all). Refer to above link for examples and detailed description of this field.
    - update_limit -- Maximum number of updates to apply at a time. Omit or specify 0 to use the default (1000)
    '''
    return _call_az("az image builder customizer add", locals())


def remove(customizer_name, name, resource_group):
    '''
    Remove an image builder customizer from an image builder template.

    Required Parameters:
    - customizer_name -- Name of the customizer.
    - name -- The name of the image template.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az image builder customizer remove", locals())


def clear(name, resource_group):
    '''
    Remove all image builder customizers from an image builder template.

    Required Parameters:
    - name -- The name of the image template.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az image builder customizer clear", locals())

