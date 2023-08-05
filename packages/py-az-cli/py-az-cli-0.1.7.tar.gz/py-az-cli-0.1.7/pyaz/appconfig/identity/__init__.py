'''
Managed identities for App Configurations.
'''
from ... pyaz_utils import _call_az

def assign(name, identities=None, resource_group=None):
    '''
    Update managed identities for an App Configuration.

    Required Parameters:
    - name -- Name of the App Configuration. You can configure the default name using `az configure --defaults app_configuration_store=<name>`

    Optional Parameters:
    - identities -- Accept system-assigned or user-assigned managed identities separated by spaces. Use '[system]' to refer to system-assigned managed identity or a resource ID to refer to user-assigned managed identity. If this argument is not provided or this argument is provided without any value, system-assigned managed identity will be used by default.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az appconfig identity assign", locals())


def remove(name, identities=None, resource_group=None):
    '''
    Remove managed identities for an App Configuration.

    Required Parameters:
    - name -- Name of the App Configuration. You can configure the default name using `az configure --defaults app_configuration_store=<name>`

    Optional Parameters:
    - identities -- Accept system-assigned or user-assigned managed identities separated by spaces. Use '[system]' to refer to system-assigned managed identity, '[all]' for all managed identities or a resource ID to refer user-assigned managed identity. If this argument is not provided or this argument is provided without any value, system-assigned managed identity will be removed by default.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az appconfig identity remove", locals())


def show(name, resource_group=None):
    '''
    Display managed identities for an App Configuration.

    Required Parameters:
    - name -- Name of the App Configuration. You can configure the default name using `az configure --defaults app_configuration_store=<name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az appconfig identity show", locals())

