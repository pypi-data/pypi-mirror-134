'''
Manage Azure IoT Hub Device Provisioning Service certificates.
'''
from .... pyaz_utils import _call_az

def list(dps_name, resource_group):
    '''
    List all certificates contained within an Azure IoT Hub device provisioning service

    Required Parameters:
    - dps_name -- IoT Provisioning Service name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot dps certificate list", locals())


def show(certificate_name, dps_name, resource_group):
    '''
    Show information about a particular Azure IoT Hub Device Provisioning Service certificate.

    Required Parameters:
    - certificate_name -- A friendly name for the certificate.
    - dps_name -- IoT Provisioning Service name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot dps certificate show", locals())


def create(certificate_name, dps_name, path, resource_group, verified=None):
    '''
    Create/upload an Azure IoT Hub Device Provisioning Service certificate.

    Required Parameters:
    - certificate_name -- A friendly name for the certificate.
    - dps_name -- IoT Provisioning Service name
    - path -- The path to the file containing the certificate.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - verified -- A boolean indicating whether or not the certificate is verified.
    '''
    return _call_az("az iot dps certificate create", locals())


def delete(certificate_name, dps_name, etag, resource_group):
    '''
    Delete an Azure IoT Hub Device Provisioning Service certificate.

    Required Parameters:
    - certificate_name -- A friendly name for the certificate.
    - dps_name -- IoT Provisioning Service name
    - etag -- Entity Tag (etag) of the object.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot dps certificate delete", locals())


def generate_verification_code(certificate_name, dps_name, etag, resource_group):
    '''
    Generate a verification code for an Azure IoT Hub Device Provisioning Service certificate.

    Required Parameters:
    - certificate_name -- A friendly name for the certificate.
    - dps_name -- IoT Provisioning Service name
    - etag -- Entity Tag (etag) of the object.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot dps certificate generate-verification-code", locals())


def verify(certificate_name, dps_name, etag, path, resource_group):
    '''
    Verify an Azure IoT Hub Device Provisioning Service certificate.

    Required Parameters:
    - certificate_name -- A friendly name for the certificate.
    - dps_name -- IoT Provisioning Service name
    - etag -- Entity Tag (etag) of the object.
    - path -- The path to the file containing the certificate.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot dps certificate verify", locals())


def update(certificate_name, dps_name, etag, path, resource_group, verified=None):
    '''
    Update an Azure IoT Hub Device Provisioning Service certificate.

    Required Parameters:
    - certificate_name -- A friendly name for the certificate.
    - dps_name -- IoT Provisioning Service name
    - etag -- Entity Tag (etag) of the object.
    - path -- The path to the file containing the certificate.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - verified -- A boolean indicating whether or not the certificate is verified.
    '''
    return _call_az("az iot dps certificate update", locals())

