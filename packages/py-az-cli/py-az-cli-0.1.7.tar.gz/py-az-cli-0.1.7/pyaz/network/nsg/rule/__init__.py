'''
Manage network security group rules.
'''
from .... pyaz_utils import _call_az

def delete(name, nsg_name, resource_group):
    '''
    Delete a network security group rule.

    Required Parameters:
    - name -- Name of the network security group rule
    - nsg_name -- Name of the network security group
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network nsg rule delete", locals())


def list(nsg_name, resource_group, include_default=None):
    '''
    List all rules in a network security group.

    Required Parameters:
    - nsg_name -- Name of the network security group
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - include_default -- Include default security rules in the output.
    '''
    return _call_az("az network nsg rule list", locals())


def show(name, nsg_name, resource_group):
    '''
    Get the details of a network security group rule.

    Required Parameters:
    - name -- Name of the network security group rule
    - nsg_name -- Name of the network security group
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network nsg rule show", locals())


def create(name, nsg_name, priority, resource_group, access=None, description=None, destination_address_prefixes=None, destination_asgs=None, destination_port_ranges=None, direction=None, protocol=None, source_address_prefixes=None, source_asgs=None, source_port_ranges=None):
    '''
    Create a network security group rule.

    Required Parameters:
    - name -- Name of the network security group rule
    - nsg_name -- Name of the network security group
    - priority -- Rule priority, between 100 (highest priority) and 4096 (lowest priority). Must be unique for each rule in the collection.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - access -- None
    - description -- Rule description
    - destination_address_prefixes -- Space-separated list of CIDR prefixes or IP ranges. Alternatively, specify ONE of 'VirtualNetwork', 'AzureLoadBalancer', 'Internet' or '*' to match all IPs. Besides, it also supports all available Service Tags like 'ApiManagement', 'SqlManagement', 'AzureMonitor', etc.
    - destination_asgs -- Space-separated list of application security group names or IDs. Limited by backend server, temporarily this argument only supports one application security group name or ID
    - destination_port_ranges -- Space-separated list of ports or port ranges between 0-65535. Use '*' to match all ports.
    - direction -- None
    - protocol -- Network protocol this rule applies to.
    - source_address_prefixes -- Space-separated list of CIDR prefixes or IP ranges. Alternatively, specify ONE of 'VirtualNetwork', 'AzureLoadBalancer', 'Internet' or '*' to match all IPs. Besides, it also supports all available Service Tags like 'ApiManagement', 'SqlManagement', 'AzureMonitor', etc.
    - source_asgs -- Space-separated list of application security group names or IDs. Limited by backend server, temporarily this argument only supports one application security group name or ID
    - source_port_ranges -- Space-separated list of ports or port ranges between 0-65535. Use '*' to match all ports.
    '''
    return _call_az("az network nsg rule create", locals())


def update(name, nsg_name, resource_group, access=None, add=None, description=None, destination_address_prefixes=None, destination_asgs=None, destination_port_ranges=None, direction=None, force_string=None, priority=None, protocol=None, remove=None, set=None, source_address_prefixes=None, source_asgs=None, source_port_ranges=None):
    '''
    Update a network security group rule.

    Required Parameters:
    - name -- Name of the network security group rule
    - nsg_name -- Name of the network security group
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - access -- None
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - description -- Rule description
    - destination_address_prefixes -- Space-separated list of CIDR prefixes or IP ranges. Alternatively, specify ONE of 'VirtualNetwork', 'AzureLoadBalancer', 'Internet' or '*' to match all IPs. Besides, it also supports all available Service Tags like 'ApiManagement', 'SqlManagement', 'AzureMonitor', etc.
    - destination_asgs -- Space-separated list of application security group names or IDs. Limited by backend server, temporarily this argument only supports one application security group name or ID
    - destination_port_ranges -- Space-separated list of ports or port ranges between 0-65535. Use '*' to match all ports.
    - direction -- None
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - priority -- Rule priority, between 100 (highest priority) and 4096 (lowest priority). Must be unique for each rule in the collection.
    - protocol -- Network protocol this rule applies to.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - source_address_prefixes -- Space-separated list of CIDR prefixes or IP ranges. Alternatively, specify ONE of 'VirtualNetwork', 'AzureLoadBalancer', 'Internet' or '*' to match all IPs. Besides, it also supports all available Service Tags like 'ApiManagement', 'SqlManagement', 'AzureMonitor', etc.
    - source_asgs -- Space-separated list of application security group names or IDs. Limited by backend server, temporarily this argument only supports one application security group name or ID
    - source_port_ranges -- Space-separated list of ports or port ranges between 0-65535. Use '*' to match all ports.
    '''
    return _call_az("az network nsg rule update", locals())

