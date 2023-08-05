'''
Manage private registries with Azure Container Registries.
'''
from .. pyaz_utils import _call_az
from . import agentpool, connected_registry, credential, encryption, helm, identity, network_rule, pack, private_endpoint_connection, private_link_resource, replication, repository, scope_map, task, taskrun, token, webhook


def check_name(name):
    '''
    Checks if an Azure Container Registry name is valid and available for use.

    Required Parameters:
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`
    '''
    return _call_az("az acr check-name", locals())


def list(resource_group=None):
    '''
    Lists all the container registries under the current subscription.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr list", locals())


def create(name, resource_group, sku, admin_enabled=None, allow_exports=None, allow_trusted_services=None, default_action=None, identity=None, key_encryption_key=None, location=None, public_network_enabled=None, tags=None, workspace=None, zone_redundancy=None):
    '''
    Create an Azure Container Registry.

    Required Parameters:
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sku -- The SKU of the container registry

    Optional Parameters:
    - admin_enabled -- Indicates whether the admin user is enabled
    - allow_exports -- Configure exportPolicy to allow/disallow artifacts from being exported from this registry. Artifacts can be exported via import or transfer operations. For more information, please visit https://aka.ms/acr/export-policy.
    - allow_trusted_services -- Allow trusted Azure Services to access network restricted registries. For more information, please visit https://aka.ms/acr/trusted-services. The Default is to allow.
    - default_action -- Default action to apply when no rule matches. Only applicable to Premium SKU.
    - identity -- Use assigned managed identity resource id or name if in the same resource group
    - key_encryption_key -- Key vault key uri. To enable automated rotation, provide a version-less key uri. For manual rotation, provide a versioned key uri.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - public_network_enabled -- Allow public network access for the container registry. The Default is to allow.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - workspace -- Name or ID of the Log Analytics workspace to send registry diagnostic logs to. All events will be enabled. You can use "az monitor log-analytics workspace create" to create one. Extra billing may apply.
    - zone_redundancy -- Indicates whether or not zone redundancy should be enabled for this registry or replication. For more information, such as supported locations, please visit https://aka.ms/acr/az. Zone-redundancy cannot be updated. Defaults to 'Disabled'.
    '''
    return _call_az("az acr create", locals())


def delete(name, resource_group=None, yes=None):
    '''
    Deletes an Azure Container Registry.

    Required Parameters:
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az acr delete", locals())


def show(name, resource_group=None):
    '''
    Get the details of an Azure Container Registry.

    Required Parameters:
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr show", locals())


def show_usage(name, resource_group=None):
    '''
    Get the storage usage for an Azure Container Registry.

    Required Parameters:
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr show-usage", locals())


def show_endpoints(name, resource_group=None):
    '''
    Display registry endpoints

    Required Parameters:
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr show-endpoints", locals())


def update(name, add=None, admin_enabled=None, allow_exports=None, allow_trusted_services=None, anonymous_pull_enabled=None, data_endpoint_enabled=None, default_action=None, force_string=None, public_network_enabled=None, remove=None, resource_group=None, set=None, sku=None, tags=None):
    '''
    Update an Azure Container Registry.

    Required Parameters:
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - admin_enabled -- Indicates whether the admin user is enabled
    - allow_exports -- Configure exportPolicy to allow/disallow artifacts from being exported from this registry. Artifacts can be exported via import or transfer operations. For more information, please visit https://aka.ms/acr/export-policy.
    - allow_trusted_services -- Allow trusted Azure Services to access network restricted registries. For more information, please visit https://aka.ms/acr/trusted-services.
    - anonymous_pull_enabled -- Enable registry-wide pull from unauthenticated clients
    - data_endpoint_enabled -- Enable dedicated data endpoint for client firewall configuration
    - default_action -- Default action to apply when no rule matches. Only applicable to Premium SKU.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - public_network_enabled -- Allow public network access for the container registry.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - sku -- The SKU of the container registry
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az acr update", locals())


def login(name, expose_token=None, password=None, resource_group=None, suffix=None, username=None):
    '''
    Log in to an Azure Container Registry through the Docker CLI.

    Required Parameters:
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - expose_token -- Expose access token instead of automatically logging in through Docker CLI
    - password -- The password used to log into a container registry
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - suffix -- The tenant suffix in registry login server. You may specify '--suffix tenant' if your registry login server is in the format 'registry-tenant.azurecr.io'. Applicable if you're accessing the registry from a different subscription or you have permission to access images but not the permission to manage the registry resource.
    - username -- The username used to log into a container registry
    '''
    return _call_az("az acr login", locals())


def import_(name, source, force=None, image=None, no_wait=None, password=None, registry=None, repository=None, resource_group=None, username=None):
    '''
    Imports an image to an Azure Container Registry from another Container Registry. Import removes the need to docker pull, docker tag, docker push. For larger images consider using `--no-wait`.

    Required Parameters:
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`
    - source -- Source image name or fully qualified source containing the registry login server. If `--registry` is used, `--source` will always be interpreted as a source image, even if it contains the login server.

    Optional Parameters:
    - force -- Overwrite the existing tag of the image to be imported.
    - image -- The name and tag of the image using the format: '-t repo/image:tag'. Multiple tags are supported by passing -t multiple times.
    - no_wait -- Do not wait for the import to complete and return immediately after queuing the import.
    - password -- The password of source container registry
    - registry -- The source Azure container registry. This can be name, login server or resource ID of the source registry.
    - repository -- The repository name for a manifest-only copy of images. Multiple copies supported by passing --repository multiple times.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - username -- The username of source container registry
    '''
    return _call_az("az acr import", locals())


def build(registry, agent_pool=None, auth_mode=None, build_arg=None, file=None, image=None, log_template=None, no_format=None, no_logs=None, no_push=None, no_wait=None, platform=None, resource_group=None, secret_build_arg=None, target=None, timeout=None):
    '''
    Queues a quick build, providing streaming logs for an Azure Container Registry.

    Required Parameters:
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - agent_pool -- The name of the agent pool.
    - auth_mode -- Auth mode of the source registry.
    - build_arg -- Build argument in '--build-arg name[=value]' format. Multiples supported by passing --build-arg multiple times.
    - file -- The relative path of the the docker file to the source code root folder. Default to 'Dockerfile'.
    - image -- The name and tag of the image using the format: '-t repo/image:tag'. Multiple tags are supported by passing -t multiple times.
    - log_template -- The repository and tag template for run log artifact using the format: 'log/repo:tag' (e.g., 'acr/logs:{{.Run.ID}}'). Only applicable to CMK enabled registry.
    - no_format -- Indicates whether the logs should be displayed in raw format
    - no_logs -- Do not show logs after successfully queuing the build.
    - no_push -- Indicates whether the image built should be pushed to the registry.
    - no_wait -- Do not wait for the build to complete and return immediately after queuing the build.
    - platform -- The platform where build/task is run, Eg, 'windows' and 'linux'. When it's used in build commands, it also can be specified in 'os/arch/variant' format for the resulting image. Eg, linux/arm/v7. The 'arch' and 'variant' parts are optional.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - secret_build_arg -- Secret build argument in '--secret-build-arg name[=value]' format. Multiples supported by passing '--secret-build-arg name[=value]' multiple times.
    - target -- The name of the target build stage.
    - timeout -- The timeout in seconds.
    '''
    return _call_az("az acr build", locals())


def run(registry, agent_pool=None, auth_mode=None, file=None, log_template=None, no_format=None, no_logs=None, no_wait=None, platform=None, resource_group=None, set=None, set_secret=None, timeout=None, values=None):
    '''
    Queues a quick run providing streamed logs for an Azure Container Registry.

    Required Parameters:
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - agent_pool -- The name of the agent pool.
    - auth_mode -- Auth mode of the source registry.
    - file -- The task template/definition file path relative to the source context. It can be '-' to pipe a file from the standard input.
    - log_template -- The repository and tag template for run log artifact using the format: 'log/repo:tag' (e.g., 'acr/logs:{{.Run.ID}}'). Only applicable to CMK enabled registry.
    - no_format -- Indicates whether the logs should be displayed in raw format
    - no_logs -- Do not show logs after successfully queuing the build.
    - no_wait -- Do not wait for the run to complete and return immediately after queuing the run.
    - platform -- The platform where build/task is run, Eg, 'windows' and 'linux'. When it's used in build commands, it also can be specified in 'os/arch/variant' format for the resulting image. Eg, linux/arm/v7. The 'arch' and 'variant' parts are optional.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - set -- Value in 'name[=value]' format. Multiples supported by passing --set multiple times.
    - set_secret -- Secret value in '--set name[=value]' format. Multiples supported by passing --set multiple times.
    - timeout -- The timeout in seconds.
    - values -- The task values file path relative to the source context.
    '''
    return _call_az("az acr run", locals())


def check_health(ignore_errors=None, name=None, vnet=None, yes=None):
    '''
    Gets health information on the environment and optionally a target registry.

    Optional Parameters:
    - ignore_errors -- Provide all health checks, even if errors are found
    - name -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`
    - vnet -- Virtual network ID so to run this command inside a VNET to verify the DNS routing to private endpoints
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az acr check-health", locals())

