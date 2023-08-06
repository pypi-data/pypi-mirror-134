'''
Manage device streams of an IoT hub.
'''
from .... pyaz_utils import _call_az

def show(name, resource_group=None):
    '''
    Get IoT Hub's device streams endpoints.

    Required Parameters:
    - name -- IoT Hub name.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot hub devicestream show", locals())

