from .... pyaz_utils import _call_az

def list(lb_name, resource_group):
    '''
    List frontend IP addresses.

    Required Parameters:
    - lb_name -- The name of the load balancer.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network cross-region-lb frontend-ip list", locals())


def show(lb_name, name, resource_group):
    '''
    Get the details of a frontend IP address.

    Required Parameters:
    - lb_name -- The name of the load balancer.
    - name -- The name of the frontend IP configuration
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network cross-region-lb frontend-ip show", locals())


def delete(lb_name, name, resource_group):
    '''
    Delete a frontend IP address.

    Required Parameters:
    - lb_name -- The name of the load balancer.
    - name -- The name of the frontend IP configuration
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network cross-region-lb frontend-ip delete", locals())


def create(lb_name, name, resource_group, public_ip_address=None, public_ip_prefix=None, zone=None):
    '''
    Create a frontend IP address.

    Required Parameters:
    - lb_name -- The load balancer name.
    - name -- The name of the frontend IP configuration
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - public_ip_address -- Name or ID of the existing public IP to associate with the configuration.
    - public_ip_prefix -- Name or ID of a public IP prefix.
    - zone -- Availability zone into which to provision the resource.
    '''
    return _call_az("az network cross-region-lb frontend-ip create", locals())


def update(lb_name, name, resource_group, add=None, force_string=None, public_ip_address=None, public_ip_prefix=None, remove=None, set=None):
    '''
    Update a frontend IP address.

    Required Parameters:
    - lb_name -- The load balancer name.
    - name -- The name of the frontend IP configuration
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - public_ip_address -- Name or ID of the existing public IP to associate with the configuration.
    - public_ip_prefix -- Name or ID of a public IP prefix.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az network cross-region-lb frontend-ip update", locals())

