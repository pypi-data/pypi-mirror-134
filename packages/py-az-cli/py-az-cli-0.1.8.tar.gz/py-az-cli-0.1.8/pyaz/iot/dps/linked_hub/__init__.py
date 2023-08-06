from .... pyaz_utils import _call_az

def list(dps_name, resource_group):
    '''
    List all linked IoT hubs in an Azure IoT Hub device provisioning service.

    Required Parameters:
    - dps_name -- IoT Provisioning Service name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot dps linked-hub list", locals())


def show(dps_name, linked_hub, resource_group):
    '''
    Show details of a linked IoT hub in an Azure IoT Hub device provisioning service.

    Required Parameters:
    - dps_name -- IoT Provisioning Service name
    - linked_hub -- Host name of linked IoT Hub.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot dps linked-hub show", locals())


def create(connection_string, dps_name, location, resource_group, allocation_weight=None, apply_allocation_policy=None, no_wait=None):
    '''
    Create a linked IoT hub in an Azure IoT Hub device provisioning service.

    Required Parameters:
    - connection_string -- Connection string of the IoT hub.
    - dps_name -- IoT Provisioning Service name
    - location -- Location of the IoT hub.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - allocation_weight -- Allocation weight of the IoT hub.
    - apply_allocation_policy -- A boolean indicating whether to apply allocation policy to the IoT hub.
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az iot dps linked-hub create", locals())


def update(dps_name, linked_hub, resource_group, allocation_weight=None, apply_allocation_policy=None, no_wait=None):
    '''
    Update a linked IoT hub in an Azure IoT Hub device provisioning service.

    Required Parameters:
    - dps_name -- IoT Provisioning Service name
    - linked_hub -- Host name of linked IoT Hub.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - allocation_weight -- Allocation weight of the IoT hub.
    - apply_allocation_policy -- A boolean indicating whether to apply allocation policy to the Iot hub.
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az iot dps linked-hub update", locals())


def delete(dps_name, linked_hub, resource_group, no_wait=None):
    '''
    Update a linked IoT hub in an Azure IoT Hub device provisioning service.

    Required Parameters:
    - dps_name -- IoT Provisioning Service name
    - linked_hub -- Host name of linked IoT Hub.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az iot dps linked-hub delete", locals())

