'''
Manage a collection of steps for building, testing and OS & Framework patching container images using Azure Container Registries.
'''
from ... pyaz_utils import _call_az
from . import credential, identity, timer


def create(name, registry, agent_pool=None, arg=None, assign_identity=None, auth_mode=None, base_image_trigger_enabled=None, base_image_trigger_name=None, base_image_trigger_type=None, commit_trigger_enabled=None, context=None, cpu=None, file=None, git_access_token=None, image=None, is_system_task=None, log_template=None, no_cache=None, no_push=None, platform=None, pull_request_trigger_enabled=None, resource_group=None, schedule=None, secret_arg=None, set=None, set_secret=None, source_trigger_name=None, status=None, target=None, timeout=None, update_trigger_endpoint=None, update_trigger_payload_type=None, values=None):
    '''
    Create a series of steps for building, testing and OS & Framework patching containers. Tasks support triggers from git commits and base image updates.

    Required Parameters:
    - name -- The name of the task.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - agent_pool -- The name of the agent pool.
    - arg -- Build argument in '--arg name[=value]' format. Multiples supported by passing '--arg` multiple times.
    - assign_identity -- Assigns managed identities to the task. Use '[system]' to refer to the system-assigned identity or a resource ID to refer to a user-assigned identity. Please see https://aka.ms/acr/tasks/task-create-managed-identity for more information.
    - auth_mode -- Auth mode of the source registry.
    - base_image_trigger_enabled -- Indicates whether the base image trigger is enabled.
    - base_image_trigger_name -- The name of the base image trigger.
    - base_image_trigger_type -- The type of the auto trigger for base image dependency updates.
    - commit_trigger_enabled -- Indicates whether the source control commit trigger is enabled.
    - context -- The full URL to the source code repository (Requires '.git' suffix for a github repo) or the repository of an OCI artifact in an Azure container registry (e.g., 'oci://myregistry.azurecr.io/myartifact:mytag'). If '/dev/null' is specified, the value will be set to None and ignored. This is a required argument if the task is not a system task.
    - cpu -- The CPU configuration in terms of number of cores required for the run.
    - file -- Relative path of the the task/docker file to the source code root folder. Task files must be suffixed with '.yaml' or piped from the standard input using '-'.
    - git_access_token -- The access token used to access the source control provider.
    - image -- The name and tag of the image using the format: '-t repo/image:tag'. Multiple tags are supported by passing -t multiple times.
    - is_system_task -- Indicates whether the task resource is a system task. The name of the task must be 'quicktask'. Only applicable to CMK enabled registry.
    - log_template -- The repository and tag template for run log artifact using the format: 'log/repo:tag' (e.g., 'acr/logs:{{.Run.ID}}'). Only applicable to CMK enabled registry.
    - no_cache -- Indicates whether the image cache is enabled.
    - no_push -- Indicates whether the image built should be pushed to the registry.
    - platform -- The platform where build/task is run, Eg, 'windows' and 'linux'. When it's used in build commands, it also can be specified in 'os/arch/variant' format for the resulting image. Eg, linux/arm/v7. The 'arch' and 'variant' parts are optional.
    - pull_request_trigger_enabled -- Indicates whether the source control pull request trigger is enabled. The trigger is disabled by default.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - schedule -- Schedule for a timer trigger represented as a cron expression. An optional trigger name can be specified using `--schedule name:schedule` format. Multiples supported by passing --schedule multiple times.
    - secret_arg -- Secret build argument in '--secret-arg name[=value]' format. Multiples supported by passing --secret-arg multiple times.
    - set -- Task value in '--set name[=value]' format. Multiples supported by passing --set multiple times.
    - set_secret -- Secret task value in '--set-secret name[=value]' format. Multiples supported by passing --set-secret multiple times.
    - source_trigger_name -- The name of the source trigger.
    - status -- The current status of task.
    - target -- The name of the target build stage.
    - timeout -- The timeout in seconds.
    - update_trigger_endpoint -- The full URL of the endpoint to receive base image update trigger notifications.
    - update_trigger_payload_type -- Indicates whether to include metadata about the base image trigger in the payload alongwith the update trigger token, when a notification is sent.
    - values -- The task values/parameters file path relative to the source context.
    '''
    return _call_az("az acr task create", locals())


def show(name, registry, resource_group=None, with_secure_properties=None):
    '''
    Get the properties of a named task for an Azure Container Registry.

    Required Parameters:
    - name -- The name of the task.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - with_secure_properties -- Indicates whether the secure properties of a task should be returned.
    '''
    return _call_az("az acr task show", locals())


def list(registry, resource_group=None):
    '''
    List the tasks for an Azure Container Registry.

    Required Parameters:
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr task list", locals())


def delete(name, registry, resource_group=None, yes=None):
    '''
    Delete a task from an Azure Container Registry.

    Required Parameters:
    - name -- The name of the task.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az acr task delete", locals())


def update(name, registry, agent_pool=None, arg=None, auth_mode=None, base_image_trigger_enabled=None, base_image_trigger_type=None, commit_trigger_enabled=None, context=None, cpu=None, file=None, git_access_token=None, image=None, log_template=None, no_cache=None, no_push=None, platform=None, pull_request_trigger_enabled=None, resource_group=None, secret_arg=None, set=None, set_secret=None, status=None, target=None, timeout=None, update_trigger_endpoint=None, update_trigger_payload_type=None, values=None):
    '''
    Update a task for an Azure Container Registry.

    Required Parameters:
    - name -- The name of the task.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - agent_pool -- The name of the agent pool.
    - arg -- Build argument in '--arg name[=value]' format. Multiples supported by passing '--arg` multiple times.
    - auth_mode -- Auth mode of the source registry.
    - base_image_trigger_enabled -- Indicates whether the base image trigger is enabled.
    - base_image_trigger_type -- The type of the auto trigger for base image dependency updates.
    - commit_trigger_enabled -- Indicates whether the source control commit trigger is enabled.
    - context -- The full URL to the source code repository (Requires '.git' suffix for a github repo) or the repository of an OCI artifact in an Azure container registry (e.g., 'oci://myregistry.azurecr.io/myartifact:mytag'). If '/dev/null' is specified, the value will be set to None and ignored. This is a required argument if the task is not a system task.
    - cpu -- The CPU configuration in terms of number of cores required for the run.
    - file -- Relative path of the the task/docker file to the source code root folder. Task files must be suffixed with '.yaml' or piped from the standard input using '-'.
    - git_access_token -- The access token used to access the source control provider.
    - image -- The name and tag of the image using the format: '-t repo/image:tag'. Multiple tags are supported by passing -t multiple times.
    - log_template -- The repository and tag template for run log artifact using the format: 'log/repo:tag' (e.g., 'acr/logs:{{.Run.ID}}'). Only applicable to CMK enabled registry.
    - no_cache -- Indicates whether the image cache is enabled.
    - no_push -- Indicates whether the image built should be pushed to the registry.
    - platform -- The platform where build/task is run, Eg, 'windows' and 'linux'. When it's used in build commands, it also can be specified in 'os/arch/variant' format for the resulting image. Eg, linux/arm/v7. The 'arch' and 'variant' parts are optional.
    - pull_request_trigger_enabled -- Indicates whether the source control pull request trigger is enabled. The trigger is disabled by default.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - secret_arg -- Secret build argument in '--secret-arg name[=value]' format. Multiples supported by passing --secret-arg multiple times.
    - set -- Task value in '--set name[=value]' format. Multiples supported by passing --set multiple times.
    - set_secret -- Secret task value in '--set-secret name[=value]' format. Multiples supported by passing --set-secret multiple times.
    - status -- The current status of task.
    - target -- The name of the target build stage.
    - timeout -- The timeout in seconds.
    - update_trigger_endpoint -- The full URL of the endpoint to receive base image update trigger notifications.
    - update_trigger_payload_type -- Indicates whether to include metadata about the base image trigger in the payload alongwith the update trigger token, when a notification is sent.
    - values -- The task values/parameters file path relative to the source context.
    '''
    return _call_az("az acr task update", locals())


def run(name, registry, agent_pool=None, arg=None, context=None, file=None, log_template=None, no_logs=None, no_wait=None, resource_group=None, secret_arg=None, set=None, set_secret=None, target=None, update_trigger_token=None):
    '''
    Manually trigger a task that might otherwise be waiting for git commits or base image update triggers.

    Required Parameters:
    - name -- The name of the task.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - agent_pool -- The name of the agent pool.
    - arg -- Build argument in '--arg name[=value]' format. Multiples supported by passing '--arg` multiple times.
    - context -- The full URL to the source code repository (Requires '.git' suffix for a github repo) or the repository of an OCI artifact in an Azure container registry (e.g., 'oci://myregistry.azurecr.io/myartifact:mytag'). If '/dev/null' is specified, the value will be set to None and ignored. This is a required argument if the task is not a system task.
    - file -- Relative path of the the task/docker file to the source code root folder. Task files must be suffixed with '.yaml' or piped from the standard input using '-'.
    - log_template -- The repository and tag template for run log artifact using the format: 'log/repo:tag' (e.g., 'acr/logs:{{.Run.ID}}'). Only applicable to CMK enabled registry.
    - no_logs -- Do not show logs after successfully queuing the build.
    - no_wait -- Do not wait for the run to complete and return immediately after queuing the run.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - secret_arg -- Secret build argument in '--secret-arg name[=value]' format. Multiples supported by passing --secret-arg multiple times.
    - set -- Task value in '--set name[=value]' format. Multiples supported by passing --set multiple times.
    - set_secret -- Secret task value in '--set-secret name[=value]' format. Multiples supported by passing --set-secret multiple times.
    - target -- The name of the target build stage.
    - update_trigger_token -- The payload that will be passed back alongwith the base image trigger notification.
    '''
    return _call_az("az acr task run", locals())


def list_runs(registry, image=None, name=None, resource_group=None, run_status=None, top=None):
    '''
    List all of the executed runs for an Azure Container Registry, with the ability to filter by a specific Task.

    Required Parameters:
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - image -- The name of the image. May include a tag in the format 'name:tag' or digest in the format 'name@digest'.
    - name -- The name of the task.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - run_status -- The current status of run.
    - top -- Limit the number of latest runs in the results.
    '''
    return _call_az("az acr task list-runs", locals())


def show_run(registry, run_id, resource_group=None):
    '''
    Get the properties of a specified run of an Azure Container Registry Task.

    Required Parameters:
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`
    - run_id -- The unique run identifier.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr task show-run", locals())


def cancel_run(registry, run_id, resource_group=None):
    '''
    Cancel a specified run of an Azure Container Registry.

    Required Parameters:
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`
    - run_id -- The unique run identifier.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr task cancel-run", locals())


def update_run(registry, run_id, no_archive=None, resource_group=None):
    '''
    Patch the run properties of an Azure Container Registry Task.

    Required Parameters:
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`
    - run_id -- The unique run identifier.

    Optional Parameters:
    - no_archive -- Indicates whether the run should be archived.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr task update-run", locals())


def logs(registry, image=None, name=None, resource_group=None, run_id=None):
    '''
    Show logs for a particular run. If no run-id is supplied, show logs for the last created run.

    Required Parameters:
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - image -- The name of the image. May include a tag in the format 'name:tag' or digest in the format 'name@digest'.
    - name -- The name of the task.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - run_id -- The unique run identifier.
    '''
    return _call_az("az acr task logs", locals())

