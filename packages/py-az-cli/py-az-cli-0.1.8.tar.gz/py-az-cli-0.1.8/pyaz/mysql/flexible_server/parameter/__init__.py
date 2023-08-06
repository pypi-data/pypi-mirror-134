from .... pyaz_utils import _call_az

def set(name, resource_group, server_name, source=None, value=None):
    '''
    Update the parameter of a flexible server.

    Required Parameters:
    - name -- The name of the server configuration
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.

    Optional Parameters:
    - source -- Source of the configuration.
    - value -- Value of the configuration.
    '''
    return _call_az("az mysql flexible-server parameter set", locals())


def show(name, resource_group, server_name):
    '''
    Get the parameter for a flexible server."

    Required Parameters:
    - name -- The name of the server configuration
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    '''
    return _call_az("az mysql flexible-server parameter show", locals())


def list(resource_group, server_name):
    '''
    List the parameter values for a flexible server.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    '''
    return _call_az("az mysql flexible-server parameter list", locals())

