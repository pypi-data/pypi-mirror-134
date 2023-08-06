'''
Manage schedule condition of the HDInsight cluster which enabled Schedule-based Autoscale.
'''
from .... pyaz_utils import _call_az

def create(cluster_name, days, resource_group, time, workernode_count, no_wait=None):
    '''
    Add a new schedule condition.

    Required Parameters:
    - cluster_name -- The name of the cluster.
    - days -- A space-delimited list of schedule day.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - time -- The 24-hour time in the form xx:xx in days.
    - workernode_count -- The schedule workernode count.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az hdinsight autoscale condition create", locals())


def update(cluster_name, index, resource_group, days=None, no_wait=None, time=None, workernode_count=None):
    '''
    Update a schedule condition.

    Required Parameters:
    - cluster_name -- The name of the cluster.
    - index -- The schedule condition index which starts with 0.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - days -- A space-delimited list of schedule day.
    - no_wait -- Do not wait for the long-running operation to finish.
    - time -- The 24-hour time in the form xx:xx in days.
    - workernode_count -- The schedule workernode count.
    '''
    return _call_az("az hdinsight autoscale condition update", locals())


def list(cluster_name, resource_group):
    '''
    List all schedule conditions.

    Required Parameters:
    - cluster_name -- The name of the cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az hdinsight autoscale condition list", locals())


def delete(cluster_name, index, resource_group, no_wait=None, yes=None):
    '''
    Delete schedule condition.

    Required Parameters:
    - cluster_name -- The name of the cluster.
    - index -- The Space-separated list of condition indices which starts with 0 to delete.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az hdinsight autoscale condition delete", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until an operation is complete.

    Required Parameters:
    - name -- The name of the cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az hdinsight autoscale condition wait", locals())

