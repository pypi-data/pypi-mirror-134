from .... pyaz_utils import _call_az

def configure(nsg, enabled=None, format=None, interval=None, log_version=None, resource_group=None, retention=None, storage_account=None, traffic_analytics=None, workspace=None):
    '''
    Configure flow logging on a network security group.

    Required Parameters:
    - nsg -- Name or ID of the network security group.

    Optional Parameters:
    - enabled -- Enable logging
    - format -- File type of the flow log.
    - interval -- Interval in minutes at which to conduct flow analytics. Temporarily allowed values are 10 and 60.
    - log_version -- Version (revision) of the flow log.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - retention -- Number of days to retain logs
    - storage_account -- Name or ID of the storage account in which to save the flow logs. Must be in the same region of flow log.
    - traffic_analytics -- Enable traffic analytics. Defaults to true if `--workspace` is provided.
    - workspace -- Name or ID of a Log Analytics workspace. Must be in the same region of flow log
    '''
    return _call_az("az network watcher flow-log configure", locals())


def show(location=None, name=None, nsg=None, resource_group=None):
    '''
    Get the flow log configuration of a network security group.

    Optional Parameters:
    - location -- Location to identify the exclusive Network Watcher under a region. Only one Network Watcher can be existed per subscription and region.
    - name -- The name of the flow logger
    - nsg -- Name or ID of the network security group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network watcher flow-log show", locals())


def list(location):
    '''
    List all flow log resources for the specified Network Watcher

    Required Parameters:
    - location -- Location to identify the exclusive Network Watcher under a region. Only one Network Watcher can be existed per subscription and region.
    '''
    return _call_az("az network watcher flow-log list", locals())


def delete(location, name):
    '''
    Delete the specified flow log resource.

    Required Parameters:
    - location -- Location to identify the exclusive Network Watcher under a region. Only one Network Watcher can be existed per subscription and region.
    - name -- The name of the flow logger
    '''
    return _call_az("az network watcher flow-log delete", locals())


def create(location, name, nsg, enabled=None, format=None, interval=None, log_version=None, resource_group=None, retention=None, storage_account=None, tags=None, traffic_analytics=None, workspace=None):
    '''
    Create a flow log on a network security group.

    Required Parameters:
    - location -- Location to identify the exclusive Network Watcher under a region. Only one Network Watcher can be existed per subscription and region.
    - name -- The name of the flow logger
    - nsg -- Name or ID of the network security group.

    Optional Parameters:
    - enabled -- Enable logging
    - format -- File type of the flow log.
    - interval -- Interval in minutes at which to conduct flow analytics. Temporarily allowed values are 10 and 60.
    - log_version -- Version (revision) of the flow log.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - retention -- Number of days to retain logs
    - storage_account -- Name or ID of the storage account in which to save the flow logs. Must be in the same region of flow log.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - traffic_analytics -- Enable traffic analytics. Defaults to true if `--workspace` is provided.
    - workspace -- Name or ID of a Log Analytics workspace. Must be in the same region of flow log
    '''
    return _call_az("az network watcher flow-log create", locals())


def update(location, name, add=None, enabled=None, force_string=None, format=None, interval=None, log_version=None, nsg=None, remove=None, resource_group=None, retention=None, set=None, storage_account=None, tags=None, traffic_analytics=None, workspace=None):
    '''
    Update the flow log configuration of a network security group

    Required Parameters:
    - location -- Location to identify the exclusive Network Watcher under a region. Only one Network Watcher can be existed per subscription and region.
    - name -- The name of the flow logger

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - enabled -- Enable logging
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - format -- File type of the flow log.
    - interval -- Interval in minutes at which to conduct flow analytics. Temporarily allowed values are 10 and 60.
    - log_version -- Version (revision) of the flow log.
    - nsg -- Name or ID of the network security group.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - retention -- Number of days to retain logs
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - storage_account -- Name or ID of the storage account in which to save the flow logs. Must be in the same region of flow log.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - traffic_analytics -- Enable traffic analytics. Defaults to true if `--workspace` is provided.
    - workspace -- Name or ID of a Log Analytics workspace. Must be in the same region of flow log
    '''
    return _call_az("az network watcher flow-log update", locals())

