'''
Manage shared access policies of an IoT hub.
'''
from .... pyaz_utils import _call_az

def list(hub_name, resource_group=None):
    '''
    List shared access policies of an IoT hub.

    Required Parameters:
    - hub_name -- IoT Hub name.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot hub policy list", locals())


def show(hub_name, name, resource_group=None):
    '''
    Get the details of a shared access policy of an IoT hub.

    Required Parameters:
    - hub_name -- IoT Hub name.
    - name -- Shared access policy name.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot hub policy show", locals())


def create(hub_name, name, permissions, resource_group=None):
    '''
    Create a new shared access policy in an IoT hub.

    Required Parameters:
    - hub_name -- IoT Hub name.
    - name -- Shared access policy name.
    - permissions -- Permissions of shared access policy. Use space-separated list for multiple permissions. Possible values: RegistryRead, RegistryWrite, ServiceConnect, DeviceConnect

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot hub policy create", locals())


def delete(hub_name, name, resource_group=None):
    '''
    Delete a shared access policy from an IoT hub.

    Required Parameters:
    - hub_name -- IoT Hub name.
    - name -- Shared access policy name.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot hub policy delete", locals())


def renew_key(hub_name, name, renew_key, no_wait=None, resource_group=None):
    '''
    Regenerate keys of a shared access policy of an IoT hub.

    Required Parameters:
    - hub_name -- IoT Hub name.
    - name -- Shared access policy name.
    - renew_key -- Regenerate keys

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot hub policy renew-key", locals())

