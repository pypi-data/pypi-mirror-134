from .... pyaz_utils import _call_az

def reimage(cluster_name, node_name, resource_group, force=None):
    '''
    Reimage nodes of a node type.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - node_name -- list of target nodes to perform the operation.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - force -- Using this flag will force the operation even if service fabric is unable to disable the nodes. Use with caution as this might cause data loss if stateful workloads are running on the node.
    '''
    return _call_az("az sf managed-node-type node reimage", locals())


def restart(cluster_name, node_name, resource_group, force=None):
    '''
    Restart nodes of a node type.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - node_name -- list of target nodes to perform the operation.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - force -- Using this flag will force the operation even if service fabric is unable to disable the nodes. Use with caution as this might cause data loss if stateful workloads are running on the node.
    '''
    return _call_az("az sf managed-node-type node restart", locals())


def delete(cluster_name, node_name, resource_group, force=None):
    '''
    Delete nodes of a node type.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - node_name -- list of target nodes to perform the operation.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - force -- Using this flag will force the operation even if service fabric is unable to disable the nodes. Use with caution as this might cause data loss if stateful workloads are running on the node.
    '''
    return _call_az("az sf managed-node-type node delete", locals())

