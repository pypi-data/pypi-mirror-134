'''
Commands to manage clusters.
'''
from ... pyaz_utils import _call_az
from . import file, node


def create(name, resource_group, workspace, afs_mount_path=None, afs_name=None, bfs_mount_path=None, bfs_name=None, config_file=None, custom_image=None, generate_ssh_keys=None, image=None, max=None, min=None, nfs=None, nfs_mount_path=None, password=None, setup_task=None, setup_task_output=None, ssh_key=None, storage_account_key=None, storage_account_name=None, subnet=None, target=None, use_auto_storage=None, user_name=None, vm_priority=None, vm_size=None):
    '''
    Create a cluster.

    Required Parameters:
    - name -- Name of cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace -- Name of workspace.

    Optional Parameters:
    - afs_mount_path -- Relative mount path for Azure File share. The file share will be available at $AZ_BATCHAI_MOUNT_ROOT/<relative_mount_path> folder.
    - afs_name -- Name of Azure File Share to be mounted on each cluster node. Must be used in conjunction with --storage-account-name. Multiple shares can be mounted using configuration file (see --config-file option).
    - bfs_mount_path -- Relative mount path for Azure Storage container. The container will be available at $AZ_BATCHAI_MOUNT_ROOT/<relative_mount_path> folder.
    - bfs_name -- Name of Azure Storage container to be mounted on each cluster node. Must be used in conjunction with --storage-account-name. Multiple containers can be mounted using configuration file (see --config-file option).
    - config_file -- A path to a json file containing cluster create parameters (json representation of azure.mgmt.batchai.models.ClusterCreateParameters).
    - custom_image -- ARM ID of a virtual machine image to be used for nodes creation. Note, you need to provide --image containing information about the base image used for this image creation.
    - generate_ssh_keys -- Generate SSH public and private key files in ~/.ssh directory (if missing).
    - image -- Operation system image for cluster nodes. The value may contain an alias (UbuntuLTS, UbuntuDSVM) or specify image details in the form "publisher:offer:sku:version". If image configuration is not provided via command line or configuration file, Batch AI will choose default OS image
    - max -- Max nodes count for the auto-scale cluster.
    - min -- Min nodes count for the auto-scale cluster.
    - nfs -- Name or ARM ID of a file server to be mounted on each cluster node. You need to provide full ARM ID if the file server belongs to a different workspace. Multiple NFS can be mounted using configuration file (see --config-file option).
    - nfs_mount_path -- Relative mount path for NFS. The NFS will be available at $AZ_BATCHAI_MOUNT_ROOT/<relative_mount_path> folder.
    - password -- Optional password for the admin user account to be created on each compute node.
    - setup_task -- A command line which should be executed on each compute node when it's got allocated or rebooted. The task is executed in a bash subshell under root account.
    - setup_task_output -- Directory path to store where setup-task's logs. Note, Batch AI will create several helper directories under this path. The created directories are reported as stdOutErrPathSuffix by 'az cluster show' command.
    - ssh_key -- Optional SSH public key value or path. If ommited and no password specified, default SSH key (~/.ssh/id_rsa.pub) will be used.
    - storage_account_key -- Storage account key. Required if the storage account belongs to a different subscription. Can be specified using AZURE_BATCHAI_STORAGE_KEY environment variable.
    - storage_account_name -- Storage account name for Azure File Shares and/or Azure Storage Containers to be mounted on each cluster node. Can be specified using AZURE_BATCHAI_STORAGE_ACCOUNT environment variable.
    - subnet -- ARM ID of a virtual network subnet to put the cluster in.
    - target -- Number of nodes which should be allocated immediately after cluster creation. If the cluster is in auto-scale mode, BatchAI can change the number of nodes later based on number of running and queued jobs.
    - use_auto_storage -- If provided, the command will create a storage account in a new or existing resource group named "batchaiautostorage". It will also create Azure File Share with name "batchaishare", Azure Blob Container with name "batchaicontainer". The File Share and Blob Container will be mounted on each cluster node at $AZ_BATCHAI_MOUNT_ROOT/autoafs and $AZ_BATCHAI_MOUNT_ROOT/autobfs. If the resource group already exists and contains an approapriate storage account belonging to the same region as cluster, this command will reuse existing storage account.
    - user_name -- Name of admin user account to be created on each compute node. If the value is not provided and no user configuration is provided in the config file, current user's name will be used.
    - vm_priority -- VM priority.
    - vm_size -- VM size for cluster nodes (e.g. Standard_NC6 for 1 GPU node)
    '''
    return _call_az("az batchai cluster create", locals())


def delete(name, resource_group, workspace, no_wait=None, yes=None):
    '''
    Delete a cluster.

    Required Parameters:
    - name -- Name of cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace -- Name of workspace.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az batchai cluster delete", locals())


def show(name, resource_group, workspace):
    '''
    Show information about a cluster.

    Required Parameters:
    - name -- Name of cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace -- Name of workspace.
    '''
    return _call_az("az batchai cluster show", locals())


def list(resource_group, workspace):
    '''
    List clusters.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace -- Name of workspace.
    '''
    return _call_az("az batchai cluster list", locals())


def resize(name, resource_group, target, workspace):
    '''
    Resize a cluster.

    Required Parameters:
    - name -- Name of cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - target -- Target number of compute nodes.
    - workspace -- Name of workspace.
    '''
    return _call_az("az batchai cluster resize", locals())


def auto_scale(max, min, name, resource_group, workspace):
    '''
    Set auto-scale parameters for a cluster.

    Required Parameters:
    - max -- Maximum number of nodes.
    - min -- Minimum number of nodes.
    - name -- Name of cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace -- Name of workspace.
    '''
    return _call_az("az batchai cluster auto-scale", locals())

