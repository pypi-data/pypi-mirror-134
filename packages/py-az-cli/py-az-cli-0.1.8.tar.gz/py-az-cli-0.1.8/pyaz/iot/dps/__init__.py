'''
Manage Azure IoT Hub Device Provisioning Service.
'''
from ... pyaz_utils import _call_az
from . import access_policy, certificate, linked_hub


def list(resource_group=None):
    '''
    List Azure IoT Hub device provisioning services.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot dps list", locals())


def show(name, resource_group=None):
    '''
    Get the details of an Azure IoT Hub device provisioning service.

    Required Parameters:
    - name -- IoT Provisioning Service name

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot dps show", locals())


def create(name, resource_group, location=None, sku=None, tags=None, unit=None):
    '''
    Create an Azure IoT Hub device provisioning service.

    Required Parameters:
    - name -- IoT Provisioning Service name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - location -- Location of your IoT Provisioning Service. Default is the location of target resource group.
    - sku -- Pricing tier for the IoT provisioning service.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - unit -- Units in your IoT Provisioning Service.
    '''
    return _call_az("az iot dps create", locals())


def delete(name, resource_group):
    '''
    Delete an Azure IoT Hub device provisioning service.

    Required Parameters:
    - name -- IoT Provisioning Service name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot dps delete", locals())


def update(name, resource_group, add=None, force_string=None, remove=None, set=None, tags=None):
    '''
    Update an Azure IoT Hub device provisioning service.

    Required Parameters:
    - name -- IoT Provisioning Service name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az iot dps update", locals())

