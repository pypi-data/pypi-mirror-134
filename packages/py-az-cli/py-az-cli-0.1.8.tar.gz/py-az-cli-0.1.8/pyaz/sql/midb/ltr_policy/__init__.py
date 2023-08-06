from .... pyaz_utils import _call_az

def set(managed_instance, name, resource_group, monthly_retention=None, week_of_year=None, weekly_retention=None, yearly_retention=None):
    '''
    Update long term retention settings for a managed database.

    Required Parameters:
    - managed_instance -- Name of the Azure SQL managed instance.
    - name -- The name of the Azure SQL Managed Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - monthly_retention -- Retention for the monthly backup. If just a number is passed instead of an ISO 8601 string, days will be assumed as the units.There is a minimum of 7 days and a maximum of 10 years.
    - week_of_year -- The Week of Year, 1 to 52, in which to take the yearly LTR backup.
    - weekly_retention -- Retention for the weekly backup. If just a number is passed instead of an ISO 8601 string, days will be assumed as the units.There is a minimum of 7 days and a maximum of 10 years.
    - yearly_retention -- Retention for the yearly backup. If just a number is passed instead of an ISO 8601 string, days will be assumed as the units.There is a minimum of 7 days and a maximum of 10 years.
    '''
    return _call_az("az sql midb ltr-policy set", locals())


def show(managed_instance, name, resource_group):
    '''
    Show the long term retention policy for a managed database.

    Required Parameters:
    - managed_instance -- Name of the Azure SQL managed instance.
    - name -- The name of the Azure SQL Managed Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql midb ltr-policy show", locals())

