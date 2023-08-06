'''
Manage Classic Azure Monitor logs integration on an HDInsight cluster.
'''
from ... pyaz_utils import _call_az

def show(name, resource_group):
    '''
    Get the status of Classic Azure Monitor logs integration on an HDInsight cluster.

    Required Parameters:
    - name -- The name of the cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az hdinsight monitor show", locals())


def enable(name, resource_group, workspace, no_validation_timeout=None, primary_key=None):
    '''
    Enable the Classic Azure Monitor logs integration on an HDInsight cluster.

    Required Parameters:
    - name -- The name of the cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace -- The name, resource ID or workspace ID of Log Analytics workspace.

    Optional Parameters:
    - no_validation_timeout -- Permit timeout error during argument validation phase. If omitted, validation timeout error will be permitted.
    - primary_key -- The certificate for the Log Analytics workspace. Required when workspace ID is provided.
    '''
    return _call_az("az hdinsight monitor enable", locals())


def disable(name, resource_group):
    '''
    Disable the Classic Azure Monitor logs integration on an HDInsight cluster.

    Required Parameters:
    - name -- The name of the cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az hdinsight monitor disable", locals())

