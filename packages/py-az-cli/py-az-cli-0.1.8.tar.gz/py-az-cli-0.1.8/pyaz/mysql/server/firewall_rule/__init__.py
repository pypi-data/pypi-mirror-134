from .... pyaz_utils import _call_az

def create(end_ip_address, name, resource_group, server_name, start_ip_address):
    '''
    Create a new firewall rule for a server.

    Required Parameters:
    - end_ip_address -- The end IP address of the firewall rule. Must be IPv4 format. Use value '0.0.0.0' to represent all Azure-internal IP addresses.
    - name -- The name of the firewall rule. The firewall rule name cannot be empty. The firewall rule name can only contain 0-9, a-z, A-Z, '-' and '_'. Additionally, the firewall rule name cannot exceed 128 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - start_ip_address -- The start IP address of the firewall rule. Must be IPv4 format. Use value '0.0.0.0' to represent all Azure-internal IP addresses.
    '''
    return _call_az("az mysql server firewall-rule create", locals())


def delete(name, resource_group, server_name, yes=None):
    '''
    Delete a firewall rule.

    Required Parameters:
    - name -- The name of the firewall rule. The firewall rule name cannot be empty. The firewall rule name can only contain 0-9, a-z, A-Z, '-' and '_'. Additionally, the firewall rule name cannot exceed 128 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az mysql server firewall-rule delete", locals())


def show(name, resource_group, server_name):
    '''
    Get the details of a firewall rule.

    Required Parameters:
    - name -- The name of the firewall rule. The firewall rule name cannot be empty. The firewall rule name can only contain 0-9, a-z, A-Z, '-' and '_'. Additionally, the firewall rule name cannot exceed 128 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    '''
    return _call_az("az mysql server firewall-rule show", locals())


def list(resource_group, server_name):
    '''
    List all firewall rules for a server.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    '''
    return _call_az("az mysql server firewall-rule list", locals())


def update(name, resource_group, server_name, add=None, end_ip_address=None, force_string=None, remove=None, set=None, start_ip_address=None):
    '''
    Update a firewall rule.

    Required Parameters:
    - name -- The name of the firewall rule. The firewall rule name cannot be empty. The firewall rule name can only contain 0-9, a-z, A-Z, '-' and '_'. Additionally, the firewall rule name cannot exceed 128 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - end_ip_address -- The end IP address of the firewall rule. Must be IPv4 format. Use value '0.0.0.0' to represent all Azure-internal IP addresses.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - start_ip_address -- The start IP address of the firewall rule. Must be IPv4 format. Use value '0.0.0.0' to represent all Azure-internal IP addresses.
    '''
    return _call_az("az mysql server firewall-rule update", locals())

