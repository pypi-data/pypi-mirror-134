from .... pyaz_utils import _call_az

def create(name, resource_group, end_ip_address=None, rule_name=None, start_ip_address=None):
    '''
    Create a new firewall rule for a flexible server.

    Required Parameters:
    - name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - end_ip_address -- The end IP address of the firewall rule. Must be IPv4 format. Use value '0.0.0.0' to represent all Azure-internal IP addresses. 
    - rule_name -- The name of the firewall rule. If name is omitted, default name will be chosen for firewall name. The firewall rule name can only contain 0-9, a-z, A-Z, '-' and '_'. Additionally, the firewall rule name cannot exceed 128 characters. 
    - start_ip_address -- The start IP address of the firewall rule. Must be IPv4 format. Use value '0.0.0.0' to represent all Azure-internal IP addresses. 
    '''
    return _call_az("az mysql flexible-server firewall-rule create", locals())


def delete(name, resource_group, rule_name, yes=None):
    '''
    Delete a firewall rule.

    Required Parameters:
    - name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_name -- The name of the firewall rule. If name is omitted, default name will be chosen for firewall name. The firewall rule name can only contain 0-9, a-z, A-Z, '-' and '_'. Additionally, the firewall rule name cannot exceed 128 characters. 

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az mysql flexible-server firewall-rule delete", locals())


def show(name, resource_group, rule_name):
    '''
    Get the details of a firewall rule.

    Required Parameters:
    - name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_name -- The name of the firewall rule. If name is omitted, default name will be chosen for firewall name. The firewall rule name can only contain 0-9, a-z, A-Z, '-' and '_'. Additionally, the firewall rule name cannot exceed 128 characters. 
    '''
    return _call_az("az mysql flexible-server firewall-rule show", locals())


def list(name, resource_group):
    '''
    List all firewall rules for a flexible server.

    Required Parameters:
    - name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az mysql flexible-server firewall-rule list", locals())


def update(name, resource_group, rule_name, add=None, end_ip_address=None, force_string=None, remove=None, set=None, start_ip_address=None):
    '''
    Update a firewall rule.

    Required Parameters:
    - name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_name -- The name of the firewall rule. If name is omitted, default name will be chosen for firewall name. The firewall rule name can only contain 0-9, a-z, A-Z, '-' and '_'. Additionally, the firewall rule name cannot exceed 128 characters. 

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - end_ip_address -- The end IP address of the firewall rule. Must be IPv4 format. Use value '0.0.0.0' to represent all Azure-internal IP addresses. 
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - start_ip_address -- The start IP address of the firewall rule. Must be IPv4 format. Use value '0.0.0.0' to represent all Azure-internal IP addresses. 
    '''
    return _call_az("az mysql flexible-server firewall-rule update", locals())

