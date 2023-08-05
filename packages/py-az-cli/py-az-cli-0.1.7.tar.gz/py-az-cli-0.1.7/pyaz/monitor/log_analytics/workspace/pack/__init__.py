from ..... pyaz_utils import _call_az

def list(resource_group, workspace_name):
    '''
    List all the intelligence packs possible and whether they are enabled or disabled for a given workspace.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- Name of the Log Analytics Workspace.
    '''
    return _call_az("az monitor log-analytics workspace pack list", locals())


def enable(name, resource_group, workspace_name):
    '''
    Enable an intelligence pack for a given workspace.

    Required Parameters:
    - name -- The name of the intelligence pack to be enabled.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- Name of the Log Analytics Workspace.
    '''
    return _call_az("az monitor log-analytics workspace pack enable", locals())


def disable(name, resource_group, workspace_name):
    '''
    Disable an intelligence pack for a given workspace.

    Required Parameters:
    - name -- The name of the intelligence pack to be disabled.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace_name -- Name of the Log Analytics Workspace.
    '''
    return _call_az("az monitor log-analytics workspace pack disable", locals())

