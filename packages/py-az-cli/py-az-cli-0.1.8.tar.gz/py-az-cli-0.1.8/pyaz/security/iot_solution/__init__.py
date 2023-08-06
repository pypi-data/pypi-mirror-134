from ... pyaz_utils import _call_az

def list(resource_group=None):
    '''
    List all IoT Security solutions.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az security iot-solution list", locals())


def show(resource_group, solution_name):
    '''
    Shows a IoT Security solution.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - solution_name -- Name of the IoT Security solution
    '''
    return _call_az("az security iot-solution show", locals())


def create(display_name, iot_hubs, location, resource_group, solution_name):
    '''
    Create your IoT Security solution.

    Required Parameters:
    - display_name -- Resource display name
    - iot_hubs -- IoT Hub resource IDs
    - location -- location of the resource
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - solution_name -- Name of the IoT Security solution
    '''
    return _call_az("az security iot-solution create", locals())


def delete(resource_group, solution_name):
    '''
    Delete your IoT Security solution.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - solution_name -- Name of the IoT Security solution
    '''
    return _call_az("az security iot-solution delete", locals())


def update(resource_group, solution_name, display_name=None, iot_hubs=None):
    '''
    Update your IoT Security solution.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - solution_name -- Name of the IoT Security solution

    Optional Parameters:
    - display_name -- Resource display name
    - iot_hubs -- IoT Hub resource IDs
    '''
    return _call_az("az security iot-solution update", locals())

