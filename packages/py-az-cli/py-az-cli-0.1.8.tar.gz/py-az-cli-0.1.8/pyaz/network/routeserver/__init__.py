'''
Manage the route server.
'''
from ... pyaz_utils import _call_az
from . import peering


def create(hosted_subnet, name, resource_group, location=None, public_ip_address=None, tags=None):
    '''
    Create a route server.

    Required Parameters:
    - hosted_subnet -- The ID of a subnet where Route Server would be deployed
    - name -- The name of the Route Server.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - public_ip_address -- The name or ID of the public IP address.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az network routeserver create", locals())


def update(name, resource_group, add=None, allow_b2b_traffic=None, force_string=None, remove=None, set=None, tags=None):
    '''
    Update a route server.

    Required Parameters:
    - name -- The name of the Route Server.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - allow_b2b_traffic -- Allow branch to branch traffic.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az network routeserver update", locals())


def delete(name, resource_group, no_wait=None, yes=None):
    '''
    Delete a route server under a resource group.

    Required Parameters:
    - name -- The name of the Route Server.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az network routeserver delete", locals())


def show(name, resource_group):
    '''
    Show a route server.

    Required Parameters:
    - name -- The name of the Route Server.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network routeserver show", locals())


def list(resource_group=None):
    '''
    List all route servers under a subscription or a resource group.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network routeserver list", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the route server is met.

    Required Parameters:
    - name -- The name of the Route Server.
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
    return _call_az("az network routeserver wait", locals())

