'''
Manage Azure EventHubs Clusters
'''
from ... pyaz_utils import _call_az
from . import namespace


def create(name, resource_group, capacity=None, location=None, tags=None):
    '''
    Create EventHubs Cluster

    Required Parameters:
    - name -- Name of Cluster
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - capacity -- Capacity for Sku, allowed value : 1
    - location -- Location of the Cluster, for locations of available pre-provision clusters, please check az evetnhubs 
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az eventhubs cluster create", locals())


def show(name, resource_group):
    '''
    Get the resource description of the specified Event Hubs Cluster.

    Required Parameters:
    - name -- Name of Cluster
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventhubs cluster show", locals())


def list(resource_group):
    '''
    List the available Event Hubs Clusters within an ARM resource group.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventhubs cluster list", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the Cluster operation is completed.

    Required Parameters:
    - name -- Name of Cluster
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az eventhubs cluster wait", locals())


def delete(name, resource_group, no_wait=None, yes=None):
    '''
    Delete an existing Event Hubs Cluster.

    Required Parameters:
    - name -- Name of Cluster
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az eventhubs cluster delete", locals())


def available_region():
    '''
    List the quantity of available pre-provisioned Event Hubs Clusters, indexed by Azure region.
    '''
    return _call_az("az eventhubs cluster available-region", locals())


def update(name, resource_group, add=None, force_string=None, remove=None, set=None, tags=None):
    '''
    Update tags of EventHubs Cluster

    Required Parameters:
    - name -- Name of Cluster
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az eventhubs cluster update", locals())

