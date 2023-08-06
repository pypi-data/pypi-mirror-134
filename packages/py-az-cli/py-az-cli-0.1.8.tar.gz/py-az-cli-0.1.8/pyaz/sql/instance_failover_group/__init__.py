from ... pyaz_utils import _call_az

def show(location, name, resource_group):
    '''
    

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- The name of the Instance Failover Group
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql instance-failover-group show", locals())


def create(name, partner_mi, partner_resource_group, resource_group, source_mi, failover_policy=None, grace_period=None):
    '''
    Creates an instance failover group between two connected managed instances.

    Required Parameters:
    - name -- The name of the Instance Failover Group
    - partner_mi -- The name of the partner managed instance of a Instance Failover Group
    - partner_resource_group -- The name of the resource group of the partner managed instance
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - source_mi -- Name of the Azure SQL managed instance.

    Optional Parameters:
    - failover_policy -- The failover policy of the Instance Failover Group
    - grace_period -- Interval in hours before automatic failover is initiated if an outage occurs on the primary server. This indicates that Azure SQL Database will not initiate automatic failover before the grace period expires. Please note that failover operation with --allow-data-loss option might cause data loss due to the nature of asynchronous synchronization.
    '''
    return _call_az("az sql instance-failover-group create", locals())


def update(location, name, resource_group, add=None, failover_policy=None, force_string=None, grace_period=None, remove=None, set=None):
    '''
    Updates the instance failover group.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- The name of the Instance Failover Group
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - failover_policy -- The failover policy of the Instance Failover Group
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - grace_period -- Interval in hours before automatic failover is initiated if an outage occurs on the primary server. This indicates that Azure SQL Database will not initiate automatic failover before the grace period expires. Please note that failover operation with --allow-data-loss option might cause data loss due to the nature of asynchronous synchronization.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az sql instance-failover-group update", locals())


def delete(location, name, resource_group):
    '''
    

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- The name of the Instance Failover Group
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql instance-failover-group delete", locals())


def set_primary(location, name, resource_group, allow_data_loss=None):
    '''
    Set the primary of the instance failover group by failing over all databases from the current primary managed instance.

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - name -- The name of the Instance Failover Group
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - allow_data_loss -- Complete the failover even if doing so may result in data loss. This will allow the failover to proceed even if a primary database is unavailable.
    '''
    return _call_az("az sql instance-failover-group set-primary", locals())

