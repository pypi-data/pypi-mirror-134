'''
Evaluate probe information and define routing rules.
'''
from .... pyaz_utils import _call_az

def list(lb_name, resource_group):
    '''
    List probes.

    Required Parameters:
    - lb_name -- The name of the load balancer.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network lb probe list", locals())


def show(lb_name, name, resource_group):
    '''
    Get the details of a probe.

    Required Parameters:
    - lb_name -- The name of the load balancer.
    - name -- The name of the probe
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network lb probe show", locals())


def delete(lb_name, name, resource_group):
    '''
    Delete a probe.

    Required Parameters:
    - lb_name -- The name of the load balancer.
    - name -- The name of the probe
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network lb probe delete", locals())


def create(lb_name, name, port, protocol, resource_group, interval=None, path=None, threshold=None):
    '''
    Create a probe.

    Required Parameters:
    - lb_name -- The load balancer name.
    - name -- The name of the probe
    - port -- The port to interrogate.
    - protocol -- The protocol to probe.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - interval -- Probing time interval in seconds.
    - path -- The endpoint to interrogate (http only).
    - threshold -- The number of consecutive probe failures before an instance is deemed unhealthy.
    '''
    return _call_az("az network lb probe create", locals())


def update(lb_name, name, resource_group, add=None, force_string=None, interval=None, path=None, port=None, protocol=None, remove=None, set=None, threshold=None):
    '''
    Update a probe.

    Required Parameters:
    - lb_name -- The load balancer name.
    - name -- The name of the probe
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - interval -- Probing time interval in seconds.
    - path -- The endpoint to interrogate (http only).
    - port -- The port to interrogate.
    - protocol -- The protocol to probe.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - threshold -- The number of consecutive probe failures before an instance is deemed unhealthy.
    '''
    return _call_az("az network lb probe update", locals())

