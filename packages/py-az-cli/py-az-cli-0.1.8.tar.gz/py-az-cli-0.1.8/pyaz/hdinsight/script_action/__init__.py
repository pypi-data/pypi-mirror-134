from ... pyaz_utils import _call_az

def show_execution_details(cluster_name, execution_id, resource_group):
    '''
    

    Required Parameters:
    - cluster_name -- The name of the cluster.
    - execution_id -- The script execution id
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az hdinsight script-action show-execution-details", locals())


def list(cluster_name, resource_group):
    '''
    

    Required Parameters:
    - cluster_name -- The name of the cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az hdinsight script-action list", locals())


def delete(cluster_name, name, resource_group):
    '''
    

    Required Parameters:
    - cluster_name -- The name of the cluster.
    - name -- The name of the script.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az hdinsight script-action delete", locals())


def execute(cluster_name, name, resource_group, roles, script_uri, persist_on_success=None, script_parameters=None):
    '''
    Execute script actions on the specified HDInsight cluster.

    Required Parameters:
    - cluster_name -- The name of the cluster.
    - name -- The name of the script action.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - roles -- A space-delimited list of roles (nodes) where the script will be executed. Valid roles are headnode, workernode, zookeepernode, edgenode.
    - script_uri -- The URI to the script.

    Optional Parameters:
    - persist_on_success -- If the scripts needs to be persisted.
    - script_parameters -- The parameters for the script.
    '''
    return _call_az("az hdinsight script-action execute", locals())


def list_execution_history(cluster_name, resource_group):
    '''
    

    Required Parameters:
    - cluster_name -- The name of the cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az hdinsight script-action list-execution-history", locals())


def promote(cluster_name, execution_id, resource_group):
    '''
    

    Required Parameters:
    - cluster_name -- The name of the cluster.
    - execution_id -- The script execution id
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az hdinsight script-action promote", locals())

