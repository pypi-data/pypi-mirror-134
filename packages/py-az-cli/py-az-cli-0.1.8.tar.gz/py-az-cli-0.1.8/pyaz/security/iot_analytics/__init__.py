from ... pyaz_utils import _call_az

def list(resource_group, solution_name):
    '''
    List all IoT security Analytics metrics.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - solution_name -- Name of the IoT Security solution
    '''
    return _call_az("az security iot-analytics list", locals())


def show(resource_group, solution_name):
    '''
    Shows IoT Security Analytics metrics.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - solution_name -- Name of the IoT Security solution
    '''
    return _call_az("az security iot-analytics show", locals())

