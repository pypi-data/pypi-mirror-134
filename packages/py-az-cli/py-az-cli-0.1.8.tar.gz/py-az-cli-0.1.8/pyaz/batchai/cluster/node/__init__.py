'''
Commands to work with cluster nodes.
'''
from .... pyaz_utils import _call_az

def list(cluster, resource_group, workspace):
    '''
    List remote login information for cluster's nodes.

    Required Parameters:
    - cluster -- Name of cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace -- Name of workspace.
    '''
    return _call_az("az batchai cluster node list", locals())


def exec(cluster, resource_group, workspace, address=None, exec=None, node_id=None, password=None, ssh_private_key=None):
    '''
    Executes a command line on a cluster's node with optional ports forwarding.

    Required Parameters:
    - cluster -- Name of cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace -- Name of workspace.

    Optional Parameters:
    - address -- Specifies that connections to the given TCP port or Unix socket on the local (client) host are to be forwarded to the given host and port, or Unix socket, on the remote side. e.g. -L 8080:localhost:8080
    - exec -- Optional command line to be executed on the node. If not provided, the command will perform ports forwarding only.
    - node_id -- ID of the node to forward the ports to. If not provided, the command will be executed on the first available node.
    - password -- Optional password to establish SSH connection.
    - ssh_private_key -- Optional SSH private key path to establish SSH connection. If omitted, the default SSH private key will be used.
    '''
    return _call_az("az batchai cluster node exec", locals())

