from .... pyaz_utils import _call_az

def start(name, resource_group, filter=None, no_wait=None):
    '''
    Start packet capture on a virtual network gateway.

    Required Parameters:
    - name -- Name of the VNet gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - filter -- Data filter.
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network vnet-gateway packet-capture start", locals())


def stop(name, resource_group, sas_url, no_wait=None):
    '''
    Stop packet capture on a virtual network gateway.

    Required Parameters:
    - name -- Name of the VNet gateway.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sas_url -- The SAS url to be used for packet capture.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az network vnet-gateway packet-capture stop", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None):
    '''
    Place the CLI in a waiting state until a condition of the vnet gateway packet capture is met.

    Required Parameters:
    - name -- Name of the VNet gateway.
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
    return _call_az("az network vnet-gateway packet-capture wait", locals())

