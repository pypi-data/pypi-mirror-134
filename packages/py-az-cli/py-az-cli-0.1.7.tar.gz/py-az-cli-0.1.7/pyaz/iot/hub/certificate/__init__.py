'''
Manage IoT Hub certificates.
'''
from .... pyaz_utils import _call_az

def list(hub_name, resource_group=None):
    '''
    Lists all certificates contained within an Azure IoT Hub

    Required Parameters:
    - hub_name -- IoT Hub name.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot hub certificate list", locals())


def show(hub_name, name, resource_group=None):
    '''
    Shows information about a particular Azure IoT Hub certificate.

    Required Parameters:
    - hub_name -- IoT Hub name.
    - name -- A friendly name for the certificate.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot hub certificate show", locals())


def create(hub_name, name, path, resource_group=None, verified=None):
    '''
    Create/upload an Azure IoT Hub certificate.

    Required Parameters:
    - hub_name -- IoT Hub name.
    - name -- A friendly name for the certificate.
    - path -- The path to the file containing the certificate.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - verified -- A boolean indicating whether or not the certificate is verified.
    '''
    return _call_az("az iot hub certificate create", locals())


def delete(etag, hub_name, name, resource_group=None):
    '''
    Deletes an Azure IoT Hub certificate.

    Required Parameters:
    - etag -- Entity Tag (etag) of the object.
    - hub_name -- IoT Hub name.
    - name -- A friendly name for the certificate.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot hub certificate delete", locals())


def generate_verification_code(etag, hub_name, name, resource_group=None):
    '''
    Generates a verification code for an Azure IoT Hub certificate.

    Required Parameters:
    - etag -- Entity Tag (etag) of the object.
    - hub_name -- IoT Hub name.
    - name -- A friendly name for the certificate.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot hub certificate generate-verification-code", locals())


def verify(etag, hub_name, name, path, resource_group=None):
    '''
    Verifies an Azure IoT Hub certificate.

    Required Parameters:
    - etag -- Entity Tag (etag) of the object.
    - hub_name -- IoT Hub name.
    - name -- A friendly name for the certificate.
    - path -- The path to the file containing the certificate.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot hub certificate verify", locals())


def update(etag, hub_name, name, path, resource_group=None, verified=None):
    '''
    Update an Azure IoT Hub certificate.

    Required Parameters:
    - etag -- Entity Tag (etag) of the object.
    - hub_name -- IoT Hub name.
    - name -- A friendly name for the certificate.
    - path -- The path to the file containing the certificate.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - verified -- A boolean indicating whether or not the certificate is verified.
    '''
    return _call_az("az iot hub certificate update", locals())

