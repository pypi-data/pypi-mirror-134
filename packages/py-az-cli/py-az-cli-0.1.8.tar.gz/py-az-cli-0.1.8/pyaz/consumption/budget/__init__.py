'''
Manage budgets for an Azure subscription.
'''
from ... pyaz_utils import _call_az

def list(resource_group=None):
    '''
    List budgets for an Azure subscription.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az consumption budget list", locals())


def show(budget_name, resource_group=None):
    '''
    Show budget for an Azure subscription.

    Required Parameters:
    - budget_name -- Name of a budget.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az consumption budget show", locals())


def create(amount, budget_name, category, end_date, start_date, time_grain, meter_filter=None, resource_filter=None, resource_group=None, resource_group_filter=None):
    '''
    Create a budget for an Azure subscription.

    Required Parameters:
    - amount -- Amount of a budget.
    - budget_name -- Name of a budget.
    - category -- Category of the budget can be cost or usage.
    - end_date -- End date (YYYY-MM-DD in UTC) of time period of a budget.
    - start_date -- Start date (YYYY-MM-DD in UTC) of time period of a budget.
    - time_grain -- Time grain of the budget can be monthly, quarterly, or annually.

    Optional Parameters:
    - meter_filter -- Space-separated list of meters to filter on. Required if category is usage.
    - resource_filter -- Space-separated list of resource instances to filter on.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_group_filter -- Space-separated list of resource groups to filter on.
    '''
    return _call_az("az consumption budget create", locals())


def delete(budget_name, resource_group=None):
    '''
    Delete a budget for an Azure subscription.

    Required Parameters:
    - budget_name -- Name of a budget.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az consumption budget delete", locals())

