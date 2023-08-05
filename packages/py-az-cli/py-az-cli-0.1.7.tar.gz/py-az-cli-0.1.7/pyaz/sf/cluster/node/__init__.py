'''
Manage the node instance of a cluster.
'''
from .... pyaz_utils import _call_az

def add(cluster_name, node_type, number_of_nodes_to_add, resource_group):
    '''
    Add nodes to a node type in a cluster.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - node_type -- the Node type name.
    - number_of_nodes_to_add -- number of nodes to add.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sf cluster node add", locals())


def remove(cluster_name, node_type, number_of_nodes_to_remove, resource_group):
    '''
    Remove nodes from a node type in a cluster.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - node_type -- the Node type name.
    - number_of_nodes_to_remove -- number of nodes to remove.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sf cluster node remove", locals())

