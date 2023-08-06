'''
Manage and configure load balancers.
'''
from ... pyaz_utils import _call_az
from . import address_pool, frontend_ip, inbound_nat_pool, inbound_nat_rule, outbound_rule, probe, rule


def show(name, resource_group, expand=None):
    '''
    Get the details of a load balancer.

    Required Parameters:
    - name -- The load balancer name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expand -- Expands referenced resources.
    '''
    return _call_az("az network lb show", locals())


def create(name, resource_group, backend_pool_name=None, edge_zone=None, frontend_ip_name=None, frontend_ip_zone=None, location=None, no_wait=None, private_ip_address=None, private_ip_address_version=None, public_ip_address=None, public_ip_address_allocation=None, public_ip_dns_name=None, public_ip_zone=None, sku=None, subnet=None, subnet_address_prefix=None, tags=None, validate=None, vnet_address_prefix=None, vnet_name=None):
    '''
    Create a load balancer.

    Required Parameters:
    - name -- The load balancer name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - backend_pool_name -- The name of the backend address pool.
    - edge_zone -- The name of edge zone.
    - frontend_ip_name -- The name of the frontend IP configuration.
    - frontend_ip_zone -- used to create internal facing Load balancer
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - no_wait -- Do not wait for the long-running operation to finish.
    - private_ip_address -- Static private IP address to use.
    - private_ip_address_version -- The private IP address version to use.
    - public_ip_address -- Name or ID of the public IP address, or '' for none. Uses existing resource if available or will create a new resource with defaults if omitted.
    - public_ip_address_allocation -- IP allocation method.
    - public_ip_dns_name -- Globally unique DNS name for a new public IP.
    - public_ip_zone -- used to created a new public ip for the load balancer, a.k.a public facing Load balancer
    - sku -- Load balancer SKU
    - subnet -- Name or ID of a subnet. Uses existing resource or creates new if specified, or none if omitted. If name specified, also specify --vnet-name. If you want to use an existing subnet in other resource group or subscription, please provide the ID instead of the name of the subnet
    - subnet_address_prefix -- The CIDR address prefix to use when creating a new subnet.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - validate -- Generate and validate the ARM template without creating any resources.
    - vnet_address_prefix -- The CIDR address prefix to use when creating a new VNet.
    - vnet_name -- The virtual network (VNet) name.
    '''
    return _call_az("az network lb create", locals())


def delete(name, resource_group):
    '''
    Delete a load balancer.

    Required Parameters:
    - name -- The load balancer name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network lb delete", locals())


def list(resource_group=None):
    '''
    List load balancers.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network lb list", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, expand=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the load balancer is met.

    Required Parameters:
    - name -- The load balancer name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - created -- wait until created with 'provisioningState' at 'Succeeded'
    - custom -- Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running']
    - deleted -- wait until deleted
    - exists -- wait until the resource exists
    - expand -- Expands referenced resources.
    - interval -- polling interval in seconds
    - timeout -- maximum wait in seconds
    - updated -- wait until updated with provisioningState at 'Succeeded'
    '''
    return _call_az("az network lb wait", locals())


def update(name, resource_group, add=None, force_string=None, remove=None, set=None):
    '''
    Update a load balancer.

    Required Parameters:
    - name -- The load balancer name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az network lb update", locals())


def list_nic(name, resource_group):
    '''
    List associated load balancer network interfaces.

    Required Parameters:
    - name -- The load balancer name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network lb list-nic", locals())

