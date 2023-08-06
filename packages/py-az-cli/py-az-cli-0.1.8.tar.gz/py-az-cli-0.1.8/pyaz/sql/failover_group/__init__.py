from ... pyaz_utils import _call_az

def show(name, resource_group, server):
    '''
    

    Required Parameters:
    - name -- The name of the Failover Group
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql failover-group show", locals())


def list(resource_group, server):
    '''
    

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql failover-group list", locals())


def create(name, partner_server, resource_group, server, add_db=None, failover_policy=None, grace_period=None, partner_resource_group=None):
    '''
    Creates a failover group.

    Required Parameters:
    - name -- The name of the Failover Group
    - partner_server -- The name of the partner server of a Failover Group
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`

    Optional Parameters:
    - add_db -- List of databases to add to Failover Group
    - failover_policy -- The failover policy of the Failover Group
    - grace_period -- Interval in hours before automatic failover is initiated if an outage occurs on the primary server. This indicates that Azure SQL Database will not initiate automatic failover before the grace period expires. Please note that failover operation with --allow-data-loss option might cause data loss due to the nature of asynchronous synchronization.
    - partner_resource_group -- The name of the resource group of the partner server
    '''
    return _call_az("az sql failover-group create", locals())


def update(name, resource_group, server, add=None, add_db=None, failover_policy=None, force_string=None, grace_period=None, remove=None, remove_db=None, set=None):
    '''
    Updates the failover group.

    Required Parameters:
    - name -- The name of the Failover Group
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - add_db -- List of databases to add to Failover Group
    - failover_policy -- The failover policy of the Failover Group
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - grace_period -- Interval in hours before automatic failover is initiated if an outage occurs on the primary server. This indicates that Azure SQL Database will not initiate automatic failover before the grace period expires. Please note that failover operation with --allow-data-loss option might cause data loss due to the nature of asynchronous synchronization.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - remove_db -- List of databases to remove from Failover Group
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az sql failover-group update", locals())


def delete(name, resource_group, server):
    '''
    

    Required Parameters:
    - name -- The name of the Failover Group
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`
    '''
    return _call_az("az sql failover-group delete", locals())


def set_primary(name, resource_group, server, allow_data_loss=None):
    '''
    Set the primary of the failover group by failing over all databases from the current primary server.

    Required Parameters:
    - name -- The name of the Failover Group
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server -- Name of the Azure SQL server. You can configure the default using `az configure --defaults sql-server=<name>`

    Optional Parameters:
    - allow_data_loss -- Complete the failover even if doing so may result in data loss. This will allow the failover to proceed even if a primary database is unavailable.
    '''
    return _call_az("az sql failover-group set-primary", locals())

