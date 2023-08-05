'''
Manage the reliability of a cluster.
'''
from .... pyaz_utils import _call_az

def update(cluster_name, reliability_level, resource_group, auto_add_node=None):
    '''
    Update the reliability tier for the primary node in a cluster.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - reliability_level -- durability level.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - auto_add_node -- Add node count automatically when changing reliability.
    '''
    return _call_az("az sf cluster reliability update", locals())

