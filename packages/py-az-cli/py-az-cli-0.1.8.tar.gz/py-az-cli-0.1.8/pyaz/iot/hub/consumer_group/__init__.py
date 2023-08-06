from .... pyaz_utils import _call_az

def create(hub_name, name, event_hub_name=None, resource_group=None):
    '''
    Create an event hub consumer group.

    Required Parameters:
    - hub_name -- IoT Hub name.
    - name -- Event hub consumer group name.

    Optional Parameters:
    - event_hub_name -- Event hub endpoint name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot hub consumer-group create", locals())


def list(hub_name, event_hub_name=None, resource_group=None):
    '''
    List event hub consumer groups.

    Required Parameters:
    - hub_name -- IoT Hub name.

    Optional Parameters:
    - event_hub_name -- Event hub endpoint name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot hub consumer-group list", locals())


def show(hub_name, name, event_hub_name=None, resource_group=None):
    '''
    Get the details for an event hub consumer group.

    Required Parameters:
    - hub_name -- IoT Hub name.
    - name -- Event hub consumer group name.

    Optional Parameters:
    - event_hub_name -- Event hub endpoint name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot hub consumer-group show", locals())


def delete(hub_name, name, event_hub_name=None, resource_group=None):
    '''
    Delete an event hub consumer group.

    Required Parameters:
    - hub_name -- IoT Hub name.
    - name -- Event hub consumer group name.

    Optional Parameters:
    - event_hub_name -- Event hub endpoint name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot hub consumer-group delete", locals())

