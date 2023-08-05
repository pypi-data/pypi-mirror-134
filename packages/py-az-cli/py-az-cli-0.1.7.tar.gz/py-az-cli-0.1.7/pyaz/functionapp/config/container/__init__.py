'''
Manage an existing function app's container settings.
'''
from .... pyaz_utils import _call_az

def set(name, resource_group, docker_custom_image_name=None, docker_registry_server_password=None, docker_registry_server_url=None, docker_registry_server_user=None, slot=None):
    '''
    Set an existing function app's container settings.

    Required Parameters:
    - name -- name of the function app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - docker_custom_image_name -- the container custom image name and optionally the tag name
    - docker_registry_server_password -- the container registry server password
    - docker_registry_server_url -- the container registry server url
    - docker_registry_server_user -- the container registry server username
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az functionapp config container set", locals())


def delete(name, resource_group, slot=None):
    '''
    Delete an existing function app's container settings.

    Required Parameters:
    - name -- name of the function app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az functionapp config container delete", locals())


def show(name, resource_group, slot=None):
    '''
    Get details of a function app's container settings.

    Required Parameters:
    - name -- name of the function app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az functionapp config container show", locals())

