from .... pyaz_utils import _call_az

def set(name, resource_group, server, monthly_retention=None, week_of_year=None, weekly_retention=None, yearly_retention=None):
    '''
    Update long term retention settings for a database.

    Required Parameters:
    - name -- Name of the Azure SQL Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`

    Optional Parameters:
    - monthly_retention -- Retention for the monthly backup. If just a number is passed instead of an ISO 8601 string, days will be assumed as the units.There is a minimum of 7 days and a maximum of 10 years.
    - week_of_year -- The Week of Year, 1 to 52, in which to take the yearly LTR backup.
    - weekly_retention -- Retention for the weekly backup. If just a number is passed instead of an ISO 8601 string, days will be assumed as the units.There is a minimum of 7 days and a maximum of 10 years.
    - yearly_retention -- Retention for the yearly backup. If just a number is passed instead of an ISO 8601 string, days will be assumed as the units.There is a minimum of 7 days and a maximum of 10 years.
    '''
    return _call_az("az sql db ltr-policy set", locals())


def show(name, resource_group, server):
    '''
    Show the long term retention policy for a database.

    Required Parameters:
    - name -- Name of the Azure SQL Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql db ltr-policy show", locals())

