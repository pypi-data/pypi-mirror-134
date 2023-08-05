'''
See detail usage in 'az aks command invoke', 'az aks command result'.
'''
from ... pyaz_utils import _call_az

def invoke(name, resource_group, command=None, file=None, no_wait=None):
    '''
    Run a shell command (with kubectl, helm) on your aks cluster, support attaching files as well.

    Required Parameters:
    - name -- Name of the managed cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - command -- the command to run
    - file -- attach any files the command may use, or use '.' to upload the current folder.
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az aks command invoke", locals())


def result(name, resource_group, command_id=None):
    '''
    Fetch result from previously triggered 'aks command invoke'.

    Required Parameters:
    - name -- Name of the managed cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - command_id -- the command ID from "aks command invoke"
    '''
    return _call_az("az aks command result", locals())

