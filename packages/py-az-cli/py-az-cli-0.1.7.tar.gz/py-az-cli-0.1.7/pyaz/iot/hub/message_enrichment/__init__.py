from .... pyaz_utils import _call_az

def create(endpoints, key, name, value, resource_group=None):
    '''
    Create a message enrichment for chosen endpoints in your IoT Hub

    Required Parameters:
    - endpoints -- Endpoint(s) to apply enrichments to. Use a space-separated list for multiple endpoints.
    - key -- The enrichment's key.
    - name -- IoT Hub name.
    - value -- The enrichment's value.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot hub message-enrichment create", locals())


def list(name, resource_group=None):
    '''
    Get information on all message enrichments for your IoT Hub

    Required Parameters:
    - name -- IoT Hub name.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot hub message-enrichment list", locals())


def delete(key, name, resource_group=None):
    '''
    Delete a message enrichment in your IoT hub (by key)

    Required Parameters:
    - key -- The enrichment's key.
    - name -- IoT Hub name.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot hub message-enrichment delete", locals())


def update(endpoints, key, name, value, resource_group=None):
    '''
    Update a message enrichment in your IoT hub (by key)

    Required Parameters:
    - endpoints -- Endpoint(s) to apply enrichments to. Use a space-separated list for multiple endpoints.
    - key -- The enrichment's key.
    - name -- IoT Hub name.
    - value -- The enrichment's value.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot hub message-enrichment update", locals())

