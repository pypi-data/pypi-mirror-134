'''
Manage HDInsight cluster's virtual hosts.
'''
from ... pyaz_utils import _call_az

def list(cluster_name, resource_group):
    '''
    List the hosts of the specified HDInsight cluster.

    Required Parameters:
    - cluster_name -- The name of the cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az hdinsight host list", locals())


def restart(cluster_name, host_names, resource_group, yes=None):
    '''
    Restart the specific hosts of the specified HDInsight cluster.

    Required Parameters:
    - cluster_name -- The name of the cluster.
    - host_names -- A space-delimited list of host names that need to be restarted.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az hdinsight host restart", locals())

