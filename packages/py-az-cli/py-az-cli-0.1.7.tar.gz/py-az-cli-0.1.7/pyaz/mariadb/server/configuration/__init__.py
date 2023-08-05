'''
Manage configuration values for a server.
'''
from .... pyaz_utils import _call_az

def set(name, resource_group, server_name, value=None):
    '''
    Update the configuration of a server.

    Required Parameters:
    - name -- The name of the configuration
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.

    Optional Parameters:
    - value -- Value of the configuration. If not provided, configuration value will be set to default.
    '''
    return _call_az("az mariadb server configuration set", locals())


def show(name, resource_group, server_name):
    '''
    Get the configuration for a server."

    Required Parameters:
    - name -- The name of the server configuration.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    '''
    return _call_az("az mariadb server configuration show", locals())


def list(resource_group, server_name):
    '''
    List the configuration values for a server.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - server_name -- Name of the server. The name can contain only lowercase letters, numbers, and the hyphen (-) character. Minimum 3 characters and maximum 63 characters.
    '''
    return _call_az("az mariadb server configuration list", locals())

