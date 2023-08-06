from ..... pyaz_utils import _call_az

def add(gateway_name, name, private_link, resource_group, ip_address=None, no_wait=None, primary=None):
    '''
    Add an IP configuration to a Private Link to scale up its capability

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- The name of the private IP for Private Link
    - private_link -- The name of Private Link.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - ip_address -- The static private IP address of a subnet for Private Link. If omitting, a dynamic one will be created
    - no_wait -- Do not wait for the long-running operation to finish.
    - primary -- Whether the IP configuration is primary or not
    '''
    return _call_az("az network application-gateway private-link ip-config add", locals())


def remove(gateway_name, name, private_link, resource_group, no_wait=None, yes=None):
    '''
    Remove an IP configuration from a Private Link to scale down its capability

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- The name of the private IP for Private Link
    - private_link -- The name of Private Link.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az network application-gateway private-link ip-config remove", locals())


def show(gateway_name, name, private_link, resource_group):
    '''
    Show an IP configuration of a Private Link

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - name -- The name of the private IP for Private Link
    - private_link -- The name of Private Link.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway private-link ip-config show", locals())


def list(gateway_name, private_link, resource_group):
    '''
    List all the IP configuration of a Private Link

    Required Parameters:
    - gateway_name -- Name of the application gateway.
    - private_link -- The name of Private Link.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network application-gateway private-link ip-config list", locals())


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
    return _call_az("az network application-gateway private-link ip-config wait", locals())

