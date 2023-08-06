'''
Manage web apps.
'''
from .. pyaz_utils import _call_az
from . import auth, config, connection, cors, deleted, deployment, hybrid_connection, identity, log, traffic_routing, vnet_integration


def create(name, plan, resource_group, assign_identity=None, deployment_container_image_name=None, deployment_local_git=None, deployment_source_branch=None, deployment_source_url=None, docker_registry_server_password=None, docker_registry_server_user=None, multicontainer_config_file=None, multicontainer_config_type=None, role=None, runtime=None, scope=None, startup_file=None, subnet=None, tags=None, vnet=None):
    '''
    Create a web app.

    Required Parameters:
    - name -- name of the new web app
    - plan -- name or resource id of the app service plan. Use 'appservice plan create' to get one
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - assign_identity -- accept system or user assigned identities separated by spaces. Use '[system]' to refer system assigned identity, or a resource id to refer user assigned identity. Check out help for more examples
    - deployment_container_image_name -- Container image name from Docker Hub, e.g. publisher/image-name:tag
    - deployment_local_git -- enable local git
    - deployment_source_branch -- the branch to deploy
    - deployment_source_url -- Git repository URL to link with manual integration
    - docker_registry_server_password -- The container registry server password. Required for private registries.
    - docker_registry_server_user -- the container registry server username
    - multicontainer_config_file -- Linux only. Config file for multicontainer apps. (local or remote)
    - multicontainer_config_type -- Linux only.
    - role -- Role name or id the system assigned identity will have
    - runtime -- canonicalized web runtime in the format of Framework|Version, e.g. "PHP|7.2". Allowed delimiters: "|" or ":". Use `az webapp list-runtimes` for available list
    - scope -- Scope that the system assigned identity can access
    - startup_file -- Linux only. The web's startup file
    - subnet -- Name or resource ID of the pre-existing subnet to have the webapp join. The --vnet is argument also needed if specifying subnet by name.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - vnet -- Name or resource ID of the regional virtual network. If there are multiple vnets of the same name across different resource groups, use vnet resource id to specify which vnet to use. If vnet name is used, by default, the vnet in the same resource group as the webapp will be used. Must be used with --subnet argument.
    '''
    return _call_az("az webapp create", locals())


def up(app_service_environment=None, dryrun=None, html=None, launch_browser=None, location=None, logs=None, name=None, os_type=None, plan=None, resource_group=None, runtime=None, sku=None):
    '''
    Create a webapp and deploy code from a local workspace to the app. The command is required to run from the folder where the code is present. Current support includes Node, Python, .NET Core and ASP.NET. Node, Python apps are created as Linux apps. .Net Core, ASP.NET, and static HTML apps are created as Windows apps. Append the html flag to deploy as a static HTML app.


    Optional Parameters:
    - app_service_environment -- name of the (pre-existing) App Service Environment to deploy to. Requires an Isolated V2 sku [I1v2, I2v2, I3v2]
    - dryrun -- show summary of the create and deploy operation instead of executing it
    - html -- Ignore app detection and deploy as an html app
    - launch_browser -- Launch the created app using the default browser
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - logs -- Configure default logging required to enable viewing log stream immediately after launching the webapp
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - os_type -- Set the OS type for the app to be created.
    - plan -- name of the appserviceplan associated with the webapp
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - runtime -- canonicalized web runtime in the format of Framework|Version, e.g. "PHP|7.2". Allowed delimiters: "|" or ":". Use `az webapp list-runtimes` for available list.
    - sku -- The pricing tiers, e.g., F1(Free), D1(Shared), B1(Basic Small), B2(Basic Medium), B3(Basic Large), S1(Standard Small), P1V2(Premium V2 Small), P1V3(Premium V3 Small), P2V3(Premium V3 Medium), P3V3(Premium V3 Large), PC2 (Premium Container Small), PC3 (Premium Container Medium), PC4 (Premium Container Large), I1 (Isolated Small), I2 (Isolated Medium), I3 (Isolated Large), I1v2 (Isolated V2 Small), I2v2 (Isolated V2 Medium), I3v2 (Isolated V2 Large)
    '''
    return _call_az("az webapp up", locals())


def ssh(name, resource_group, instance=None, port=None, slot=None, timeout=None):
    '''
    SSH command establishes a ssh session to the web container and developer would get a shell terminal remotely.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - instance -- Webapp instance to connect to. Defaults to none.
    - port -- Port for the remote connection. Default: Random available port
    - slot -- the name of the slot. Default to the productions slot if not specified
    - timeout -- timeout in seconds. Defaults to none
    '''
    return _call_az("az webapp ssh", locals())


def list(resource_group=None):
    '''
    List web apps.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az webapp list", locals())


def show(name, resource_group, slot=None):
    '''
    Get the details of a web app.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp show", locals())


def delete(name, resource_group, keep_dns_registration=None, keep_empty_plan=None, keep_metrics=None, slot=None):
    '''
    Delete a web app.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - keep_dns_registration -- keep DNS registration
    - keep_empty_plan -- keep empty app service plan
    - keep_metrics -- keep app metrics
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp delete", locals())


def stop(name, resource_group, slot=None):
    '''
    Stop a web app.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp stop", locals())


def start(name, resource_group, slot=None):
    '''
    Start a web app.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp start", locals())


def restart(name, resource_group, slot=None):
    '''
    Restart a web app.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp restart", locals())


def browse(name, resource_group, logs=None, slot=None):
    '''
    Open a web app in a browser.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - logs -- Enable viewing the log stream immediately after launching the web app
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp browse", locals())


def list_instances(name, resource_group, slot=None):
    '''
    List all scaled out instances of a web app or web app slot.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- Name of the web app slot. Default to the productions slot if not specified.
    '''
    return _call_az("az webapp list-instances", locals())


def list_runtimes(linux=None):
    '''
    List available built-in stacks which can be used for web apps.

    Optional Parameters:
    - linux -- list runtime stacks for linux based web apps
    '''
    return _call_az("az webapp list-runtimes", locals())


def create_remote_connection(name, resource_group, instance=None, port=None, slot=None, timeout=None):
    '''
    Creates a remote connection using a tcp tunnel to your web app

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - instance -- Webapp instance to connect to. Defaults to none.
    - port -- Port for the remote connection. Default: Random available port
    - slot -- the name of the slot. Default to the productions slot if not specified
    - timeout -- timeout in seconds. Defaults to none
    '''
    return _call_az("az webapp create-remote-connection", locals())


def deploy(name, resource_group, async_=None, clean=None, ignore_stack=None, restart=None, slot=None, src_path=None, src_url=None, target_path=None, timeout=None, type=None):
    '''
    Deploys a provided artifact to Azure Web Apps.

    Required Parameters:
    - name -- Name of the webapp to deploy to.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - async_ -- If true, the artifact is deployed asynchronously. (The command will exit once the artifact is pushed to the web app.)
    - clean -- If true, cleans the target directory prior to deploying the file(s). Default value is determined based on artifact type.
    - ignore_stack -- If true, any stack-specific defaults are ignored.
    - restart -- If true, the web app will be restarted following the deployment. Set this to false if you are deploying multiple artifacts and do not want to restart the site on the earlier deployments.
    - slot -- The name of the slot. Default to the productions slot if not specified.
    - src_path -- Path of the artifact to be deployed. Ex: "myapp.zip" or "/myworkspace/apps/myapp.war"
    - src_url -- URL of the artifact. The webapp will pull the artifact from this URL. Ex: "http://mysite.com/files/myapp.war?key=123"
    - target_path -- Absolute path that the artifact should be deployed to. Defaults to "home/site/wwwroot/" Ex: "/home/site/deployments/tools/", "/home/site/scripts/startup-script.sh".
    - timeout -- Timeout for the deployment operation in milliseconds.
    - type -- Used to override the type of artifact being deployed.
    '''
    return _call_az("az webapp deploy", locals())


def update(name, resource_group, add=None, client_affinity_enabled=None, force_dns_registration=None, force_string=None, https_only=None, remove=None, set=None, skip_custom_domain_verification=None, skip_dns_registration=None, slot=None, ttl_in_seconds=None):
    '''
    Update an existing web app.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - client_affinity_enabled -- Enables sending session affinity cookies.
    - force_dns_registration -- If true, web app hostname is force registered with DNS
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - https_only -- Redirect all traffic made to an app using HTTP to HTTPS.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - skip_custom_domain_verification -- If true, custom (non *.azurewebsites.net) domains associated with web app are not verified
    - skip_dns_registration -- If true web app hostname is not registered with DNS on creation
    - slot -- the name of the slot. Default to the productions slot if not specified
    - ttl_in_seconds -- Time to live in seconds for web app's default domain name
    '''
    return _call_az("az webapp update", locals())

