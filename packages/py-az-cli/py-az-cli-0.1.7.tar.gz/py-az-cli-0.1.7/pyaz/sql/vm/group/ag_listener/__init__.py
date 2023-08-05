from ..... pyaz_utils import _call_az

def update(group_name, name, resource_group, add=None, force_string=None, remove=None, set=None, sqlvms=None):
    '''
    Updates an availability group listener.

    Required Parameters:
    - group_name -- Name of the SQL virtual machine group.
    - name -- Name of the availability group listener.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - sqlvms -- Space-separated list of SQL virtual machine instance name or resource IDs that are enrolled into the availability group.
    '''
    return _call_az("az sql vm group ag-listener update", locals())


def show(group_name, name, resource_group):
    '''
    

    Required Parameters:
    - group_name -- Name of the SQL virtual machine group.
    - name -- Name of the availability group listener.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql vm group ag-listener show", locals())


def list(group_name, resource_group):
    '''
    

    Required Parameters:
    - group_name -- Name of the SQL virtual machine group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql vm group ag-listener list", locals())


def delete(group_name, name, resource_group, yes=None):
    '''
    

    Required Parameters:
    - group_name -- Name of the SQL virtual machine group.
    - name -- Name of the availability group listener.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az sql vm group ag-listener delete", locals())


def create(ag_name, group_name, ip_address, load_balancer, name, probe_port, resource_group, sqlvms, subnet, port=None, public_ip=None, vnet_name=None):
    '''
    Creates an availability group listener.

    Required Parameters:
    - ag_name -- Name of the availability group. Please refer to https://docs.microsoft.com/sql/database-engine/availability-groups/windows/use-the-availability-group-wizard-sql-server-management-studio?view=sql-server-2017 to create and availability group
    - group_name -- Name of the SQL virtual machine group.
    - ip_address -- Private IP address bound to the availability group listener.
    - load_balancer -- Name or resource ID of the load balancer.
    - name -- Name of the availability group listener.
    - probe_port -- Probe port.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sqlvms -- Space-separated list of SQL virtual machine instance name or resource IDs that are enrolled into the availability group.
    - subnet -- The name or resource id of the subnet to include in the private IP.

    Optional Parameters:
    - port -- Listener port.
    - public_ip -- Name or resource ID of the public IP.
    - vnet_name -- Name of the virtual network. Provide only if name of the subnet has been provided.
    '''
    return _call_az("az sql vm group ag-listener create", locals())

