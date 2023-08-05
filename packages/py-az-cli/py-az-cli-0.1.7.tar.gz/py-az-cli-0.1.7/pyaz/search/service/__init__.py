'''
Manage Azure Search services.
'''
from ... pyaz_utils import _call_az

def list(resource_group):
    '''
    

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az search service list", locals())


def show(name, resource_group):
    '''
    

    Required Parameters:
    - name -- The name of the search service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az search service show", locals())


def delete(name, resource_group, yes=None):
    '''
    

    Required Parameters:
    - name -- The name of the search service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az search service delete", locals())


def update(name, resource_group, add=None, force_string=None, identity_type=None, ip_rules=None, no_wait=None, partition_count=None, public_network_access=None, remove=None, replica_count=None, set=None):
    '''
    Update partition and replica of the given search service.

    Required Parameters:
    - name -- The name of the search service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - identity_type -- The identity type; possible values include: "None", "SystemAssigned".
    - ip_rules -- Public IP(v4) addresses or CIDR ranges to the search service, seperated by comma(',') or semicolon(';'); If spaces (' '), ',' or ';' is provided, any existing IP rule will be nullified and no public IP rule is applied. These IP rules are applicable only when public_network_access is "enabled".
    - no_wait -- Do not wait for the long-running operation to finish.
    - partition_count -- Number of partitions in the search service.
    - public_network_access -- Public accessibility to the search service; allowed values are "enabled" or "disabled".
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - replica_count -- Number of replicas in the search service.
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az search service update", locals())


def create(name, resource_group, sku, identity_type=None, ip_rules=None, location=None, no_wait=None, partition_count=None, public_network_access=None, replica_count=None):
    '''
    Creates a Search service in the given resource group.

    Required Parameters:
    - name -- The name of the search service.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sku -- Search Service SKU

    Optional Parameters:
    - identity_type -- The identity type; possible values include: "None", "SystemAssigned".
    - ip_rules -- Public IP(v4) addresses or CIDR ranges to the search service, seperated by comma or semicolon; these IP rules are applicable only when --public-network-access is "enabled".
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - no_wait -- Do not wait for the long-running operation to finish.
    - partition_count -- Number of partitions in the search service.
    - public_network_access -- Public accessibility to the search service; allowed values are "enabled" or "disabled".
    - replica_count -- Number of replicas in the search service.
    '''
    return _call_az("az search service create", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Wait for async service operations.

    Required Parameters:
    - name -- The name of the search service.
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
    return _call_az("az search service wait", locals())

