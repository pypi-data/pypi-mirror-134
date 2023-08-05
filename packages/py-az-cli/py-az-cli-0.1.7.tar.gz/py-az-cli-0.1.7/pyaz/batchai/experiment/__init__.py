'''
Commands to manage experiments.
'''
from ... pyaz_utils import _call_az

def create(name, resource_group, workspace):
    '''
    Create an experiment.

    Required Parameters:
    - name -- Name of experiment.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace -- Name of workspace.
    '''
    return _call_az("az batchai experiment create", locals())


def show(name, resource_group, workspace):
    '''
    Show information about an experiment.

    Required Parameters:
    - name -- Name of experiment.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace -- Name of workspace.
    '''
    return _call_az("az batchai experiment show", locals())


def list(resource_group, workspace):
    '''
    List experiments.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace -- Name of workspace.
    '''
    return _call_az("az batchai experiment list", locals())


def delete(name, resource_group, workspace, no_wait=None, yes=None):
    '''
    Delete an experiment.

    Required Parameters:
    - name -- Name of experiment.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace -- Name of workspace.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az batchai experiment delete", locals())

