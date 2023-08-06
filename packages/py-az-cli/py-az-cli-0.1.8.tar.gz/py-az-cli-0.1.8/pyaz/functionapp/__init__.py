'''
Manage function apps. To install the Azure Functions Core tools see https://github.com/Azure/azure-functions-core-tools
'''
from .. pyaz_utils import _call_az
from . import config, cors, deployment, function, hybrid_connection, identity, keys, plan, vnet_integration


def create(name, resource_group, storage_account, app_insights=None, app_insights_key=None, assign_identity=None, consumption_plan_location=None, deployment_container_image_name=None, deployment_local_git=None, deployment_source_branch=None, deployment_source_url=None, disable_app_insights=None, docker_registry_server_password=None, docker_registry_server_user=None, functions_version=None, os_type=None, plan=None, role=None, runtime=None, runtime_version=None, scope=None, subnet=None, tags=None, vnet=None):
    '''
    Create a function app.

    Required Parameters:
    - name -- name of the new function app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - storage_account -- Provide a string value of a Storage Account in the provided Resource Group. Or Resource ID of a Storage Account in a different Resource Group

    Optional Parameters:
    - app_insights -- Name of the existing App Insights project to be added to the function app. Must be in the same resource group.
    - app_insights_key -- Instrumentation key of App Insights to be added.
    - assign_identity -- accept system or user assigned identities separated by spaces. Use '[system]' to refer system assigned identity, or a resource id to refer user assigned identity. Check out help for more examples
    - consumption_plan_location -- Geographic location where function app will be hosted. Use `az functionapp list-consumption-locations` to view available locations.
    - deployment_container_image_name -- Container image name from Docker Hub, e.g. publisher/image-name:tag
    - deployment_local_git -- enable local git
    - deployment_source_branch -- the branch to deploy
    - deployment_source_url -- Git repository URL to link with manual integration
    - disable_app_insights -- Disable creating application insights resource during functionapp create. No logs will be available.
    - docker_registry_server_password -- The container registry server password. Required for private registries.
    - docker_registry_server_user -- The container registry server username.
    - functions_version -- The functions app version. NOTE: This will be required starting the next release cycle
    - os_type -- Set the OS type for the app to be created.
    - plan -- name or resource id of the functionapp app service plan. Use 'appservice plan create' to get one. If using an App Service plan from a different resource group, the full resource id must be used and not the plan name.
    - role -- Role name or id the system assigned identity will have
    - runtime -- The functions runtime stack.
    - runtime_version -- The version of the functions runtime stack. Allowed values for each --runtime are: dotnet-isolated -> [5.0 (preview), 6.0], node -> [12, 14], java -> [8, 11], powershell -> [7.0 (preview)], python -> [3.6, 3.7, 3.8, 3.9]
    - scope -- Scope that the system assigned identity can access
    - subnet -- Name or resource ID of the pre-existing subnet to have the webapp join. The --vnet is argument also needed if specifying subnet by name.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - vnet -- Name or resource ID of the regional virtual network. If there are multiple vnets of the same name across different resource groups, use vnet resource id to specify which vnet to use. If vnet name is used, by default, the vnet in the same resource group as the webapp will be used. Must be used with --subnet argument.
    '''
    return _call_az("az functionapp create", locals())


def list(resource_group=None):
    '''
    List function apps.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az functionapp list", locals())


def show(name, resource_group, slot=None):
    '''
    Get the details of a function app.

    Required Parameters:
    - name -- name of the function app.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az functionapp show", locals())


def delete(name, resource_group, slot=None):
    '''
    Delete a function app.

    Required Parameters:
    - name -- name of the function app.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az functionapp delete", locals())


def stop(name, resource_group, slot=None):
    '''
    Stop a function app.

    Required Parameters:
    - name -- name of the function app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az functionapp stop", locals())


def start(name, resource_group, slot=None):
    '''
    Start a function app.

    Required Parameters:
    - name -- name of the function app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az functionapp start", locals())


def restart(name, resource_group, slot=None):
    '''
    Restart a function app.

    Required Parameters:
    - name -- name of the function app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az functionapp restart", locals())


def list_consumption_locations():
    '''
    List available locations for running function apps.
    '''
    return _call_az("az functionapp list-consumption-locations", locals())


def deploy(name, resource_group, async_=None, clean=None, ignore_stack=None, restart=None, slot=None, src_path=None, src_url=None, target_path=None, timeout=None, type=None):
    '''
    Deploys a provided artifact to Azure functionapp.

    Required Parameters:
    - name -- Name of the function app to deploy to.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - async_ -- Asynchronous deployment
    - clean -- If true, cleans the target directory prior to deploying the file(s). Default value is determined based on artifact type.
    - ignore_stack -- If true, any stack-specific defaults are ignored.
    - restart -- If true, the web app will be restarted following the deployment, default value is true. Set this to false if you are deploying multiple artifacts and do not want to restart the site on the earlier deployments.
    - slot -- The name of the slot. Default to the productions slot if not specified.
    - src_path -- Path of the artifact to be deployed. Ex: "myapp.zip" or "/myworkspace/apps/myapp.war"
    - src_url -- URL of the artifact. The webapp will pull the artifact from this URL. Ex: "http://mysite.com/files/myapp.war?key=123"
    - target_path -- Absolute path that the artifact should be deployed to. Defaults to "home/site/wwwroot/". Ex: "/home/site/deployments/tools/", "/home/site/scripts/startup-script.sh".
    - timeout -- Timeout for the deployment operation in milliseconds.
    - type -- Used to override the type of artifact being deployed.
    '''
    return _call_az("az functionapp deploy", locals())


def update(name, resource_group, add=None, force=None, force_string=None, plan=None, remove=None, set=None, slot=None):
    '''
    Update a function app.

    Required Parameters:
    - name -- name of the function app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force -- Required if attempting to migrate functionapp from Premium to Consumption --plan.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - plan -- The name or resource id of the plan to update the functionapp with.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az functionapp update", locals())

