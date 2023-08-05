'''
Commands to manage jobs.
'''
from ... pyaz_utils import _call_az
from . import file, node


def create(cluster, config_file, experiment, name, resource_group, workspace, afs_mount_path=None, afs_name=None, bfs_mount_path=None, bfs_name=None, nfs=None, nfs_mount_path=None, storage_account_key=None, storage_account_name=None):
    '''
    Create a job.

    Required Parameters:
    - cluster -- Name or ARM ID of the cluster to run the job. You need to provide ARM ID if the cluster belongs to a different workspace.
    - config_file -- A path to a json file containing job create parameters (json representation of azure.mgmt.batchai.models.JobCreateParameters).
    - experiment -- Name of experiment.
    - name -- Name of job.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace -- Name of workspace.

    Optional Parameters:
    - afs_mount_path -- Relative mount path for Azure File Share. The File Share will be available at $AZ_BATCHAI_JOB_MOUNT_ROOT/<relative_mount_path> folder.
    - afs_name -- Name of Azure File Share to mount during the job execution. The File Share will be mounted only on the nodes which are executing the job. Must be used in conjunction with --storage-account-name.  Multiple shares can be mounted using configuration file (see --config-file option).
    - bfs_mount_path -- Relative mount path for Azure Storage Blob Container. The container will be available at $AZ_BATCHAI_JOB_MOUNT_ROOT/<relative_mount_path> folder.
    - bfs_name -- Name of Azure Storage Blob Container to mount during the job execution. The container will be mounted only on the nodes which are executing the job. Must be used in conjunction with --storage-account-name. Multiple containers can be mounted using configuration file (see --config-file option).
    - nfs -- Name or ARM ID of the file server to be mounted during the job execution. You need to provide ARM ID if the file server belongs to a different workspace. You can configure multiple file servers using job's  configuration file.
    - nfs_mount_path -- Relative mount path for NFS. The NFS will be available at $AZ_BATCHAI_JOB_MOUNT_ROOT/<relative_mount_path> folder.
    - storage_account_key -- Storage account key. Required if the storage account belongs to a different subscription. Can be specified using AZURE_BATCHAI_STORAGE_KEY environment variable.
    - storage_account_name -- Storage account name for Azure File Shares and/or Azure Storage Containers to be mounted on each cluster node. Can be specified using AZURE_BATCHAI_STORAGE_ACCOUNT environment variable.
    '''
    return _call_az("az batchai job create", locals())


def delete(experiment, name, resource_group, workspace, no_wait=None, yes=None):
    '''
    Delete a job.

    Required Parameters:
    - experiment -- Name of experiment.
    - name -- Name of job.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace -- Name of workspace.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az batchai job delete", locals())


def terminate(experiment, name, resource_group, workspace, no_wait=None, yes=None):
    '''
    Terminate a job.

    Required Parameters:
    - experiment -- Name of experiment.
    - name -- Name of job.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace -- Name of workspace.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az batchai job terminate", locals())


def show(experiment, name, resource_group, workspace):
    '''
    Show information about a job.

    Required Parameters:
    - experiment -- Name of experiment.
    - name -- Name of job.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace -- Name of workspace.
    '''
    return _call_az("az batchai job show", locals())


def list(experiment, resource_group, workspace):
    '''
    List jobs.

    Required Parameters:
    - experiment -- Name of experiment.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace -- Name of workspace.
    '''
    return _call_az("az batchai job list", locals())


def wait(experiment, name, resource_group, workspace, interval=None):
    '''
    Waits for specified job completion and setups the exit code to the job's exit code.

    Required Parameters:
    - experiment -- Name of experiment.
    - name -- Name of job.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace -- Name of workspace.

    Optional Parameters:
    - interval -- Polling interval in sec.
    '''
    return _call_az("az batchai job wait", locals())

