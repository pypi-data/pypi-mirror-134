from .... pyaz_utils import _call_az

def add(capacity, cluster_name, node_type, resource_group, vm_password, vm_user_name, durability_level=None, vm_sku=None, vm_tier=None):
    '''
    Add a new node type to a cluster.

    Required Parameters:
    - capacity -- The capacity tag applied to nodes in the node type. The cluster resource manager uses these tags to understand how much capacity a node has.
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - node_type -- the Node type name.
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    - vm_password -- The password of the Vm
    - vm_user_name -- The user name for logging to Vm. Default will be adminuser

    Optional Parameters:
    - durability_level -- durability level.
    - vm_sku -- VM Sku
    - vm_tier -- VM tier.
    '''
    return _call_az("az sf cluster node-type add", locals())

