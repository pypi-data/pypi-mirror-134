'''
Commands to manage NAT gateways.
'''
from .... pyaz_utils import _call_az

def create(name, resource_group, idle_timeout=None, location=None, no_wait=None, public_ip_addresses=None, public_ip_prefixes=None, zone=None):
    '''
    Create a NAT gateway.

    Required Parameters:
    - name -- Name of the NAT gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - idle_timeout -- Idle timeout in minutes.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - no_wait -- Do not wait for the long-running operation to finish.
    - public_ip_addresses -- Space-separated list of public IP addresses (names or IDs).
    - public_ip_prefixes -- Space-separated list of public IP prefixes (names or IDs).
    - zone -- Availability zone into which to provision the resource.
    '''
    return _call_az("az network nat gateway create", locals())


def delete(name, resource_group):
    '''
    Delete a NAT gateway.

    Required Parameters:
    - name -- Name of the NAT gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network nat gateway delete", locals())


def list(resource_group=None):
    '''
    List NAT gateways.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network nat gateway list", locals())


def show(name, resource_group):
    '''
    Show details of a NAT gateway.

    Required Parameters:
    - name -- Name of the NAT gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network nat gateway show", locals())


def update(name, resource_group, add=None, force_string=None, idle_timeout=None, public_ip_addresses=None, public_ip_prefixes=None, remove=None, set=None):
    '''
    Update a NAT gateway.

    Required Parameters:
    - name -- Name of the NAT gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - idle_timeout -- Idle timeout in minutes.
    - public_ip_addresses -- Space-separated list of public IP addresses (names or IDs).
    - public_ip_prefixes -- Space-separated list of public IP prefixes (names or IDs).
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az network nat gateway update", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the NAT gateway is met.

    Required Parameters:
    - name -- Name of the NAT gateway.
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
    return _call_az("az network nat gateway wait", locals())

