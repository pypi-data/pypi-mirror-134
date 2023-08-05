'''
Manage the durability of a cluster.
'''
from .... pyaz_utils import _call_az

def update(cluster_name, durability_level, node_type, resource_group):
    '''
    Update the durability tier or VM SKU of a node type in the cluster.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - durability_level -- durability level.
    - node_type -- the Node type name.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sf cluster durability update", locals())

