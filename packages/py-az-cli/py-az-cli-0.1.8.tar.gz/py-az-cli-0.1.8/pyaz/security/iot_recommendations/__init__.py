from ... pyaz_utils import _call_az

def list(resource_group, solution_name):
    '''
    List all yours IoT Security solution aggregated recommendations.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - solution_name -- Name of the IoT Security solution
    '''
    return _call_az("az security iot-recommendations list", locals())


def show(name, resource_group, solution_name):
    '''
    Shows a single aggregated recommendation of yours IoT Security solution.

    Required Parameters:
    - name -- name of the resource to be fetched
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - solution_name -- Name of the IoT Security solution
    '''
    return _call_az("az security iot-recommendations show", locals())

