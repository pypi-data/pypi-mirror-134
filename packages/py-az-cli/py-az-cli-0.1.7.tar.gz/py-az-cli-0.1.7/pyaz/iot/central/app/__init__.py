'''
Manage IoT Central applications.
'''
from .... pyaz_utils import _call_az

def create(name, resource_group, subdomain, display_name=None, location=None, no_wait=None, sku=None, template=None):
    '''
    Create an IoT Central application.

    Required Parameters:
    - name -- Give your IoT Central app a unique name so you can find it later.This will be used as the resource name in the Azure portal and CLI.Avoid special characters `-` instead, use lower case letters (a-z), numbers (0-9), and dashes (-)
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - subdomain -- Enter a unique URL. Your app will be accessible via https://<subdomain>.azureiotcentral.com/. Avoid special characters `-` instead, use lower case letters (a-z), numbers (0-9), and dashes (-).

    Optional Parameters:
    - display_name -- Custom display name for the IoT Central app. This will be used in the IoT Central application manager to help you identify your app. Default value is the resource name.
    - location -- Where your app's info and resources are stored. We will default to the location of the target resource group. See documentation for a full list of supported locations.
    - no_wait -- Do not wait for the long-running operation to finish.
    - sku -- Pricing plan for IoT Central application.
    - template -- IoT Central application template name. Default is "Custom application". See documentation for a list of available templates.
    '''
    return _call_az("az iot central app create", locals())


def list(resource_group=None):
    '''
    List IoT Central applications.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot central app list", locals())


def show(name, resource_group=None):
    '''
    Get the details of an IoT Central application.

    Required Parameters:
    - name -- IoT Central application name.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot central app show", locals())


def update(name, resource_group, add=None, force_string=None, remove=None, set=None):
    '''
    Update metadata for an IoT Central application.

    Required Parameters:
    - name -- IoT Central application name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az iot central app update", locals())


def delete(name, resource_group, no_wait=None, yes=None):
    '''
    Delete an IoT Central application.

    Required Parameters:
    - name -- IoT Central application name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az iot central app delete", locals())

