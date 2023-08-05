'''
Manage HDInsight cluster's Autoscale configuration.
'''
from ... pyaz_utils import _call_az
from . import condition


def create(cluster_name, resource_group, type, days=None, max_workernode_count=None, min_workernode_count=None, no_wait=None, time=None, timezone=None, workernode_count=None, yes=None):
    '''
    Enable Autoscale for a running cluster.

    Required Parameters:
    - cluster_name -- The name of the cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - type -- The autoscale type.

    Optional Parameters:
    - days -- A space-delimited list of schedule day.
    - max_workernode_count -- The max workernode count for Load-based atuoscale.
    - min_workernode_count -- The minimal workernode count for Load-based atuoscale.
    - no_wait -- Do not wait for the long-running operation to finish.
    - time -- The 24-hour time in the form xx:xx in days.
    - timezone -- The timezone for schedule autoscale type. Values from `az hdinsight autoscale list-timezones`
    - workernode_count -- The schedule workernode count.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az hdinsight autoscale create", locals())


def update(cluster_name, resource_group, max_workernode_count=None, min_workernode_count=None, no_wait=None, timezone=None):
    '''
    Update the Autoscale configuration.

    Required Parameters:
    - cluster_name -- The name of the cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - max_workernode_count -- The max workernode count for Load-based atuoscale.
    - min_workernode_count -- The minimal workernode count for Load-based atuoscale.
    - no_wait -- Do not wait for the long-running operation to finish.
    - timezone -- The timezone for schedule autoscale type. Values from `az hdinsight autoscale list-timezones`
    '''
    return _call_az("az hdinsight autoscale update", locals())


def show(cluster_name, resource_group):
    '''
    Get the Autoscale configuration of a specified cluster.

    Required Parameters:
    - cluster_name -- The name of the cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az hdinsight autoscale show", locals())


def delete(cluster_name, resource_group, no_wait=None, yes=None):
    '''
    Disable Autoscale for a running cluster.

    Required Parameters:
    - cluster_name -- The name of the cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az hdinsight autoscale delete", locals())


def list_timezones():
    '''
    List the available timezone name when enabling Schedule-based Autoscale.
    '''
    return _call_az("az hdinsight autoscale list-timezones", locals())


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
    return _call_az("az hdinsight autoscale wait", locals())

