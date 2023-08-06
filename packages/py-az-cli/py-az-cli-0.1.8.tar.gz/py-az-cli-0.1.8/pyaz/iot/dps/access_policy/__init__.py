from .... pyaz_utils import _call_az

def list(dps_name, resource_group):
    '''
    List all shared access policies in an Azure IoT Hub device provisioning service.

    Required Parameters:
    - dps_name -- IoT Provisioning Service name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot dps access-policy list", locals())


def show(access_policy_name, dps_name, resource_group):
    '''
    Show details of a shared access policies in an Azure IoT Hub device provisioning service.

    Required Parameters:
    - access_policy_name -- A friendly name for DPS access policy.
    - dps_name -- IoT Provisioning Service name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot dps access-policy show", locals())


def create(access_policy_name, dps_name, resource_group, rights, no_wait=None, primary_key=None, secondary_key=None):
    '''
    Create a new shared access policy in an Azure IoT Hub device provisioning service.

    Required Parameters:
    - access_policy_name -- A friendly name for DPS access policy.
    - dps_name -- IoT Provisioning Service name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rights -- Access rights for the IoT provisioning service. Use space-separated list for multiple rights.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - primary_key -- Primary SAS key value.
    - secondary_key -- Secondary SAS key value.
    '''
    return _call_az("az iot dps access-policy create", locals())


def update(access_policy_name, dps_name, resource_group, no_wait=None, primary_key=None, rights=None, secondary_key=None):
    '''
    Update a shared access policy in an Azure IoT Hub device provisioning service.

    Required Parameters:
    - access_policy_name -- A friendly name for DPS access policy.
    - dps_name -- IoT Provisioning Service name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - primary_key -- Primary SAS key value.
    - rights -- Access rights for the IoT provisioning service. Use space-separated list for multiple rights.
    - secondary_key -- Secondary SAS key value.
    '''
    return _call_az("az iot dps access-policy update", locals())


def delete(access_policy_name, dps_name, resource_group, no_wait=None):
    '''
    Delete a shared access policies in an Azure IoT Hub device provisioning service.

    Required Parameters:
    - access_policy_name -- A friendly name for DPS access policy.
    - dps_name -- IoT Provisioning Service name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az iot dps access-policy delete", locals())

