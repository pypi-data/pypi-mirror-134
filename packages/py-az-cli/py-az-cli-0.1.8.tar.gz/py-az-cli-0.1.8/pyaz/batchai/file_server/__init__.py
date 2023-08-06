from ... pyaz_utils import _call_az

def create(name, resource_group, workspace, caching_type=None, config_file=None, disk_count=None, disk_size=None, generate_ssh_keys=None, no_wait=None, password=None, ssh_key=None, storage_sku=None, subnet=None, user_name=None, vm_size=None):
    '''
    Create a file server.

    Required Parameters:
    - name -- Name of file server.
    - resource_group -- Name of resource group. You can configure a default value by setting up default workspace using `az batchai workspace set-default`.
    - workspace -- Name or ARM ID of the workspace. You can configure default workspace using `az batchai workspace set-default`

    Optional Parameters:
    - caching_type -- Caching type for premium disks. If not provided via command line or in configuration file, no caching will be used.
    - config_file -- A path to a json file containing file server create parameters (json representation of azure.mgmt.batchai.models.FileServerCreateParameters). Note, parameters given via command line will overwrite parameters specified in the configuration file.
    - disk_count -- Number of disks.
    - disk_size -- Disk size in Gb.
    - generate_ssh_keys -- Generate SSH public and private key files in ~/.ssh directory (if missing).
    - no_wait -- Do not wait for the long-running operation to finish.
    - password -- Optional password for the admin user created on the NFS node.
    - ssh_key -- Optional SSH public key value or path. If ommited and no password specified, default SSH key (~/.ssh/id_rsa.pub) will be used.
    - storage_sku -- The sku of storage account to persist VM.
    - subnet -- ARM ID of a virtual network subnet to put the file server in. If not provided via command line or in the configuration file, Batch AI will create a new virtual network and subnet under your subscription.
    - user_name -- Name of admin user account to be created on NFS node. If the value is not provided and no user configuration is provided in the config file, current user's name will be used.
    - vm_size -- VM size.
    '''
    return _call_az("az batchai file-server create", locals())


def list(resource_group, workspace):
    '''
    List file servers.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace -- Name of workspace.
    '''
    return _call_az("az batchai file-server list", locals())

