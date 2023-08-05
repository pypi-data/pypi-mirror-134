from .... pyaz_utils import _call_az

def show(name, resource_group, server):
    '''
    

    Required Parameters:
    - name -- Name of the Azure SQL Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql db threat-policy show", locals())


def update(name, resource_group, server, add=None, disabled_alerts=None, email_account_admins=None, email_addresses=None, force_string=None, remove=None, retention_days=None, set=None, state=None, storage_account=None, storage_endpoint=None, storage_key=None):
    '''
    Update a database's threat detection policy.

    Required Parameters:
    - name -- Name of the Azure SQL Database.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - disabled_alerts -- List of disabled alerts.
    - email_account_admins -- Whether the alert is sent to the account administrators.
    - email_addresses -- List of email addresses that alerts are sent to.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - retention_days -- The number of days to retain threat detection logs.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - state -- Threat detection policy state
    - storage_account -- Name of the storage account.
    - storage_endpoint -- The storage account endpoint.
    - storage_key -- Access key for the storage account.
    '''
    return _call_az("az sql db threat-policy update", locals())

