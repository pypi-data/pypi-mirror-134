from .... pyaz_utils import _call_az
from . import ip_config


def add(frontend_ip, gateway_name, name, resource_group, subnet, ip_address=None, no_wait=None, primary=None, subnet_prefix=None):
    '''
    Add a new Private Link with a default IP Configuration and associate it with an existing Frontend IP

    Required Parameters:
    - frontend_ip -- The frontend IP which the Private Link will associate to
    - gateway_name -- Name of the application gateway.
    - name -- The name of Private Link.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - subnet -- The name or an existing ID of a subnet within the same vnet of an application gateway

    Optional Parameters:
    - ip_address -- The static private IP address of a subnet for Private Link. If omitting, a dynamic one will be created
    - no_wait -- Do not wait for the long-running operation to finish.
    - primary -- Whether the IP configuration is primary or not
    - subnet_prefix -- The CIDR prefix to use when creating a new subnet
    '''
    return _call_az("az network application-gateway private-link add", locals())


def remove(gateway_name, name, resource_group, no_wait=None, yes=None):
    '''
    Remove a Private Link and clear association with Frontend IP. The subnet associate with a Private Link might need to clear manually

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- The name of Private Link.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az network application-gateway private-link remove", locals())


def show(gateway_name, name, resource_group):
    '''
    Show a Private Link

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- The name of Private Link.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway private-link show", locals())


def list(gateway_name, resource_group):
    '''
    List all the Private Link

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway private-link list", locals())


def wait(gateway_name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until the condition of corresponding application gateway is met

    Required Parameters:
    - gateway_name -- Name of the application gateway.
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
    return _call_az("az network application-gateway private-link wait", locals())

