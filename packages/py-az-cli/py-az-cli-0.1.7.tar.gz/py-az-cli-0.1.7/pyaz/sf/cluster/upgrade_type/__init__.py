from .... pyaz_utils import _call_az

def set(cluster_name, resource_group, upgrade_mode, version=None):
    '''
    Change the  upgrade type for a cluster.

    Required Parameters:
    - cluster_name -- Specify the name of the cluster, if not given it will be same as resource group name
    - resource_group -- Specify the resource group name. You can configure the default group using `az configure --defaults group=<name>`
    - upgrade_mode -- cluster upgrade mode

    Optional Parameters:
    - version -- cluster code version
    '''
    return _call_az("az sf cluster upgrade-type set", locals())

