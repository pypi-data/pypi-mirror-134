'''
Manage the rollouts.
'''
from ... pyaz_utils import _call_az

def show(resource_group, rollout_name, retry_attempt=None):
    '''
    Gets the rollout.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rollout_name -- The name of the rollout

    Optional Parameters:
    - retry_attempt -- Rollout retry attempt ordinal to get the result of. If not specified, result of the latest attempt will be returned.
    '''
    return _call_az("az deploymentmanager rollout show", locals())


def list(resource_group):
    '''
    List all rollouts in a resource group

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az deploymentmanager rollout list", locals())


def stop(resource_group, rollout_name, yes=None):
    '''
    Stop the rollout.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rollout_name -- The name of the rollout

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az deploymentmanager rollout stop", locals())


def restart(resource_group, rollout_name, skip_succeeded=None, yes=None):
    '''
    Restarts the rollout.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rollout_name -- The name of the rollout

    Optional Parameters:
    - skip_succeeded -- Skips all the steps that have succeeded in the previous retries of this rollout.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az deploymentmanager rollout restart", locals())


def delete(resource_group, rollout_name):
    '''
    

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rollout_name -- The name of the rollout
    '''
    return _call_az("az deploymentmanager rollout delete", locals())

