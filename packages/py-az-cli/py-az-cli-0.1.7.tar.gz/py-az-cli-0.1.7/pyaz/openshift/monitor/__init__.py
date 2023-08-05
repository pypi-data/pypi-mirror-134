'''
Commands to manage Log Analytics monitoring in an ARO 3.11 cluster.
'''
from ... pyaz_utils import _call_az

def enable(name, resource_group, workspace_id, no_wait=None):
    '''
    Enable Log Analytics monitoring in an ARO 3.11 cluster.

    Required Parameters:
    - name -- Name of the managed OpenShift cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_id -- The resource ID of an existing Log Analytics Workspace to use for storing monitoring data.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az openshift monitor enable", locals())


def disable(name, resource_group, no_wait=None):
    '''
    Disable Log Analytics monitoring in an ARO 3.11 cluster.

    Required Parameters:
    - name -- Name of the managed OpenShift cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az openshift monitor disable", locals())

