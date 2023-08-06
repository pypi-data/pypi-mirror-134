'''
Commands to manage workspaces.
'''
from ... pyaz_utils import _call_az

def create(resource_group, workspace, location=None):
    '''
    Create a workspace.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace -- Name of workspace.

    Optional Parameters:
    - location -- Location of the workspace. If omitted, the location of the resource group will be used.
    '''
    return _call_az("az batchai workspace create", locals())


def show(resource_group, workspace):
    '''
    Show information about a workspace.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace -- Name of workspace.
    '''
    return _call_az("az batchai workspace show", locals())


def list(resource_group=None):
    '''
    List workspaces.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az batchai workspace list", locals())


def delete(resource_group, workspace, no_wait=None, yes=None):
    '''
    Delete a workspace.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace -- Name of workspace.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az batchai workspace delete", locals())

