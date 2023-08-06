from .... pyaz_utils import _call_az

def list(application_name, gallery_name, resource_group):
    '''
    

    Required Parameters:
    - application_name -- The name of the gallery Application
    - gallery_name -- gallery name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sig gallery-application version list", locals())


def show(application_name, gallery_name, name, resource_group, expand=None):
    '''
    

    Required Parameters:
    - application_name -- The name of the gallery Application
    - gallery_name -- gallery name
    - name -- The name of the gallery Application Version
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expand -- The expand expression to apply on the operation.
    '''
    return _call_az("az sig gallery-application version show", locals())


def create(application_name, gallery_name, install_command, name, package_file_link, remove_command, resource_group, default_file_link=None, end_of_life_date=None, exclude_from=None, location=None, no_wait=None, tags=None, target_regions=None, update_command=None):
    '''
    Create a gallery Application Version.

    Required Parameters:
    - application_name -- The name of the gallery Application
    - gallery_name -- gallery name
    - install_command -- The path and arguments to install the gallery application.
    - name -- The name of the gallery Application Version
    - package_file_link -- The mediaLink of the artifact, must be a readable storage page blob.
    - remove_command -- The path and arguments to remove the gallery application.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - default_file_link -- The default configuration link of the artifact, must be a readable storage page blob.
    - end_of_life_date -- The end of life date of the gallery image version. This property can be used for decommissioning purposes. This property is updatable.
    - exclude_from -- If set to true, Virtual Machines deployed from the latest version of the Image Definition won't use this Image Version.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - no_wait -- Do not wait for the long-running operation to finish.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - target_regions -- The target regions where the Image Version is going to be replicated to. This property is updatable. Expected value: json-string/json-file/@json-file.
    - update_command -- The path and arguments to update the gallery application. If not present, then update operation will invoke remove command on the previous version and install command on the current version of the gallery application.
    '''
    return _call_az("az sig gallery-application version create", locals())


def update(application_name, gallery_name, name, package_file_link, resource_group, default_file_link=None, end_of_life_date=None, exclude_from=None, location=None, no_wait=None, tags=None, target_regions=None):
    '''
    Update a gallery Application Version.

    Required Parameters:
    - application_name -- The name of the gallery Application
    - gallery_name -- gallery name
    - name -- The name of the gallery Application Version
    - package_file_link -- The mediaLink of the artifact, must be a readable storage page blob.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - default_file_link -- The default configuration link of the artifact, must be a readable storage page blob.
    - end_of_life_date -- The end of life date of the gallery image version. This property can be used for decommissioning purposes. This property is updatable.
    - exclude_from -- If set to true, Virtual Machines deployed from the latest version of the Image Definition won't use this Image Version.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - no_wait -- Do not wait for the long-running operation to finish.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - target_regions -- The target regions where the Image Version is going to be replicated to. This property is updatable. Expected value: json-string/json-file/@json-file.
    '''
    return _call_az("az sig gallery-application version update", locals())


def delete(application_name, gallery_name, name, resource_group, no_wait=None, yes=None):
    '''
    

    Required Parameters:
    - application_name -- The name of the gallery Application
    - gallery_name -- gallery name
    - name -- The name of the gallery Application Version
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az sig gallery-application version delete", locals())

