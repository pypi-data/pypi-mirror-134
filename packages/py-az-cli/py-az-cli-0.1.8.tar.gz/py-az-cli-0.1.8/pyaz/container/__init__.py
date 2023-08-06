'''
Manage Azure Container Instances.
'''
from .. pyaz_utils import _call_az

def list(resource_group=None):
    '''
    List container groups.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az container list", locals())


def create(resource_group, acr_identity=None, assign_identity=None, azure_file_volume_account_key=None, azure_file_volume_account_name=None, azure_file_volume_mount_path=None, azure_file_volume_share_name=None, command_line=None, cpu=None, dns_name_label=None, environment_variables=None, file=None, gitrepo_dir=None, gitrepo_mount_path=None, gitrepo_revision=None, gitrepo_url=None, image=None, ip_address=None, location=None, log_analytics_workspace=None, log_analytics_workspace_key=None, memory=None, name=None, no_wait=None, os_type=None, ports=None, protocol=None, registry_login_server=None, registry_password=None, registry_username=None, restart_policy=None, role=None, scope=None, secrets=None, secrets_mount_path=None, secure_environment_variables=None, subnet=None, subnet_address_prefix=None, vnet=None, vnet_address_prefix=None, vnet_name=None, zone=None):
    '''
    Create a container group.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - acr_identity -- The identity with access to the container registry
    - assign_identity -- Space-separated list of assigned identities. Assigned identities are either user assigned identities (resource IDs) and / or the system assigned identity ('[system]'). See examples for more info.
    - azure_file_volume_account_key -- The storage account access key used to access the Azure File share
    - azure_file_volume_account_name -- The name of the storage account that contains the Azure File share
    - azure_file_volume_mount_path -- The path within the container where the azure file volume should be mounted. Must not contain colon ':'.
    - azure_file_volume_share_name -- The name of the Azure File share to be mounted as a volume
    - command_line -- The command line to run when the container is started, e.g. '/bin/bash -c myscript.sh'
    - cpu -- The required number of CPU cores of the containers, accurate to one decimal place
    - dns_name_label -- The dns name label for container group with public IP
    - environment_variables -- A list of environment variable for the container. Space-separated values in 'key=value' format.
    - file -- The path to the input file.
    - gitrepo_dir -- The target directory path in the git repository. Must not contain '..'.
    - gitrepo_mount_path -- The path within the container where the git repo volume should be mounted. Must not contain colon ':'.
    - gitrepo_revision -- The commit hash for the specified revision
    - gitrepo_url -- The URL of a git repository to be mounted as a volume
    - image -- The container image name
    - ip_address -- The IP address type of the container group
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - log_analytics_workspace -- The Log Analytics workspace name or id. Use the current subscription or use --subscription flag to set the desired subscription.
    - log_analytics_workspace_key -- The Log Analytics workspace key.
    - memory -- The required memory of the containers in GB, accurate to one decimal place
    - name -- The name of the container group
    - no_wait -- Do not wait for the long-running operation to finish.
    - os_type -- The OS type of the containers
    - ports -- A list of ports to open. Space-separated list of ports
    - protocol -- The network protocol to use
    - registry_login_server -- The container image registry login server
    - registry_password -- The password to log in container image registry server
    - registry_username -- The username to log in container image registry server
    - restart_policy -- Restart policy for all containers within the container group
    - role -- Role name or id the system assigned identity will have
    - scope -- Scope that the system assigned identity can access
    - secrets -- space-separated secrets in 'key=value' format.
    - secrets_mount_path -- The path within the container where the secrets volume should be mounted. Must not contain colon ':'.
    - secure_environment_variables -- A list of secure environment variable for the container. Space-separated values in 'key=value' format.
    - subnet -- The name of the subnet when creating a new VNET or referencing an existing one. Can also reference an existing subnet by ID.
    - subnet_address_prefix -- The subnet IP address prefix to use when creating a new VNET in CIDR format.
    - vnet -- The name of the VNET when creating a new one or referencing an existing one. Can also reference an existing vnet by ID. This allows using vnets from other resource groups.
    - vnet_address_prefix -- The IP address prefix to use when creating a new VNET in CIDR format.
    - vnet_name -- The name of the VNET when creating a new one or referencing an existing one.
    - zone -- The zone to place the container group.
    '''
    return _call_az("az container create", locals())


def show(name, resource_group):
    '''
    Get the details of a container group.

    Required Parameters:
    - name -- The name of the container group
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az container show", locals())


def delete(name, resource_group, yes=None):
    '''
    Delete a container group.

    Required Parameters:
    - name -- The name of the container group
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az container delete", locals())


def logs(name, resource_group, container_name=None, follow=None):
    '''
    Examine the logs for a container in a container group.

    Required Parameters:
    - name -- The name of the container group
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - container_name -- The container name to tail the logs. If omitted, the first container in the container group will be chosen
    - follow -- Indicate to stream the tailing logs
    '''
    return _call_az("az container logs", locals())


def exec(exec_command, name, resource_group, container_name=None):
    '''
    Execute a command from within a running container of a container group.

    Required Parameters:
    - exec_command -- The command to run from within the container
    - name -- The name of the container group
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - container_name -- The container name where to execute the command. Can be ommitted for container groups with only one container.
    '''
    return _call_az("az container exec", locals())


def export(file, name, resource_group):
    '''
    Export a container group in yaml format.

    Required Parameters:
    - file -- The file path to export the container group.
    - name -- The name of the container group
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az container export", locals())


def attach(name, resource_group, container_name=None):
    '''
    Attach local standard output and error streams to a container in a container group.

    Required Parameters:
    - name -- The name of the container group
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - container_name -- The container to attach to. If omitted, the first container in the container group will be chosen
    '''
    return _call_az("az container attach", locals())


def restart(name, resource_group, no_wait=None):
    '''
    

    Required Parameters:
    - name -- The name of the container group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az container restart", locals())


def stop(name, resource_group):
    '''
    

    Required Parameters:
    - name -- The name of the container group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az container stop", locals())


def start(name, resource_group, no_wait=None):
    '''
    

    Required Parameters:
    - name -- The name of the container group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az container start", locals())

