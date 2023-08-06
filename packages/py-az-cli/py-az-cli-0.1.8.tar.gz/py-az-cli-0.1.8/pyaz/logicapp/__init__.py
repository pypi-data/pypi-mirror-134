'''
Manage logic apps.
'''
from .. pyaz_utils import _call_az

def delete(name, resource_group, slot=None, yes=None):
    '''
    Delete a logic app.

    Required Parameters:
    - name -- name of the logic app.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az logicapp delete", locals())


def stop(name, resource_group, slot=None):
    '''
    Stop a logic app.

    Required Parameters:
    - name -- name of the logic app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az logicapp stop", locals())


def start(name, resource_group, slot=None):
    '''
    Start a logic app.

    Required Parameters:
    - name -- name of the logic app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az logicapp start", locals())


def restart(name, resource_group, slot=None):
    '''
    Restart a logic app.

    Required Parameters:
    - name -- name of the logic app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az logicapp restart", locals())


def create(name, resource_group, storage_account, app_insights=None, app_insights_key=None, consumption_plan_location=None, deployment_container_image_name=None, deployment_local_git=None, deployment_source_branch=None, deployment_source_url=None, disable_app_insights=None, docker_registry_server_password=None, docker_registry_server_user=None, os_type=None, plan=None, tags=None):
    '''
    Create a logic app.

    Required Parameters:
    - name -- name of the new logic app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - storage_account -- Provide a string value of a Storage Account in the provided Resource Group. Or Resource ID of a Storage Account in a different Resource Group

    Optional Parameters:
    - app_insights -- Name of the existing App Insights project to be added to the logic app. Must be in the same resource group.
    - app_insights_key -- Instrumentation key of App Insights to be added.
    - consumption_plan_location -- Geographic location where logic app will be hosted. Use `az logicapp list-consumption-locations` to view available locations.
    - deployment_container_image_name -- Container image name from Docker Hub, e.g. publisher/image-name:tag
    - deployment_local_git -- enable local git
    - deployment_source_branch -- the branch to deploy
    - deployment_source_url -- Git repository URL to link with manual integration
    - disable_app_insights -- Disable creating application insights resource during logicapp create. No logs will be available.
    - docker_registry_server_password -- The container registry server password. Required for private registries.
    - docker_registry_server_user -- The container registry server username.
    - os_type -- Set the OS type for the app to be created.
    - plan -- name or resource id of the logicapp app service plan. Use 'appservice plan create' to get one. If using an App Service plan from a different resource group, the full resource id must be used and not the plan name.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az logicapp create", locals())


def list(resource_group=None):
    '''
    List logic apps.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az logicapp list", locals())


def show(name, resource_group, slot=None):
    '''
    Get the details of a logic app.

    Required Parameters:
    - name -- name of the logic app.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az logicapp show", locals())

