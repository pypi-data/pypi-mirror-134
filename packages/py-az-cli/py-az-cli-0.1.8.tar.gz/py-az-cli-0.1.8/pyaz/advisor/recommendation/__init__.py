'''
Review Azure Advisor recommendations.
'''
from ... pyaz_utils import _call_az

def list(category=None, ids=None, refresh=None, resource_group=None):
    '''
    List Azure Advisor recommendations.

    Optional Parameters:
    - category -- Name of recommendation category.
    - ids -- One or more resource IDs (space-delimited). If provided, no other "Resource Id" arguments should be specified.
    - refresh -- Generate new recommendations.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az advisor recommendation list", locals())


def disable(days=None, ids=None, name=None, resource_group=None):
    '''
    Disable Azure Advisor recommendations.

    Optional Parameters:
    - days -- Number of days to disable. If not specified, the recommendation is disabled forever.
    - ids -- One or more resource IDs (space-delimited). If provided, no other "Resource Id" arguments should be specified.
    - name -- The name of the recommendation as output by the list command.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az advisor recommendation disable", locals())


def enable(ids=None, name=None, resource_group=None):
    '''
    Enable Azure Advisor recommendations.

    Optional Parameters:
    - ids -- One or more resource IDs (space-delimited). If provided, no other "Resource Id" arguments should be specified.
    - name -- The name of the recommendation as output by the list command.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az advisor recommendation enable", locals())

