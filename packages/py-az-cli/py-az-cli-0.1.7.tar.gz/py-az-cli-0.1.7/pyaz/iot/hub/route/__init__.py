'''
Manage routes of an IoT hub.
'''
from .... pyaz_utils import _call_az

def create(endpoint_name, hub_name, route_name, source_type, condition=None, enabled=None, resource_group=None):
    '''
    Create a route in IoT Hub.

    Required Parameters:
    - endpoint_name -- Name of the routing endpoint.
    - hub_name -- IoT Hub name.
    - route_name -- Name of the Route.
    - source_type -- Source of the route.

    Optional Parameters:
    - condition -- Condition that is evaluated to apply the routing rule.
    - enabled -- A boolean indicating whether to enable route to the Iot hub.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot hub route create", locals())


def show(hub_name, route_name, resource_group=None):
    '''
    Get information about the route in IoT Hub.

    Required Parameters:
    - hub_name -- IoT Hub name.
    - route_name -- Name of the Route.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az iot hub route show", locals())


def list(hub_name, resource_group=None, source_type=None):
    '''
    Get all the routes in IoT Hub.

    Required Parameters:
    - hub_name -- IoT Hub name.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - source_type -- Source of the route.
    '''
    return _call_az("az iot hub route list", locals())


def delete(hub_name, resource_group=None, route_name=None, source_type=None):
    '''
    Delete all or mentioned route for your IoT Hub.

    Required Parameters:
    - hub_name -- IoT Hub name.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - route_name -- Name of the Route.
    - source_type -- Source of the route.
    '''
    return _call_az("az iot hub route delete", locals())


def update(hub_name, route_name, condition=None, enabled=None, endpoint_name=None, resource_group=None, source_type=None):
    '''
    Update a route in IoT Hub.

    Required Parameters:
    - hub_name -- IoT Hub name.
    - route_name -- Name of the Route.

    Optional Parameters:
    - condition -- Condition that is evaluated to apply the routing rule.
    - enabled -- A boolean indicating whether to enable route to the Iot hub.
    - endpoint_name -- Name of the routing endpoint.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - source_type -- Source of the route.
    '''
    return _call_az("az iot hub route update", locals())


def test(hub_name, app_properties=None, body=None, resource_group=None, route_name=None, source_type=None, system_properties=None):
    '''
    Test all routes or mentioned route in IoT Hub.

    Required Parameters:
    - hub_name -- IoT Hub name.

    Optional Parameters:
    - app_properties -- App properties of the route message.
    - body -- Body of the route message.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - route_name -- Name of the Route.
    - source_type -- Source of the route.
    - system_properties -- System properties of the route message.
    '''
    return _call_az("az iot hub route test", locals())

