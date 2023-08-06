'''
Manage an existing web app's container settings.
'''
from .... pyaz_utils import _call_az

def set(name, resource_group, docker_custom_image_name=None, docker_registry_server_password=None, docker_registry_server_url=None, docker_registry_server_user=None, enable_app_service_storage=None, multicontainer_config_file=None, multicontainer_config_type=None, slot=None):
    '''
    Set an existing web app's container settings.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - docker_custom_image_name -- the container custom image name and optionally the tag name
    - docker_registry_server_password -- the container registry server password
    - docker_registry_server_url -- the container registry server url
    - docker_registry_server_user -- the container registry server username
    - enable_app_service_storage -- enables platform storage (custom container only)
    - multicontainer_config_file -- config file for multicontainer apps
    - multicontainer_config_type -- config type
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp config container set", locals())


def delete(name, resource_group, slot=None):
    '''
    Delete an existing web app's container settings.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp config container delete", locals())


def show(name, resource_group, show_multicontainer_config=None, slot=None):
    '''
    Get details of a web app's container settings.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - show_multicontainer_config -- shows decoded config if a multicontainer config is set
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp config container show", locals())

