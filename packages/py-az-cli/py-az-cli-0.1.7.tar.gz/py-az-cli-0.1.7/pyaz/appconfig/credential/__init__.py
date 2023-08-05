'''
Manage credentials for App Configurations.
'''
from ... pyaz_utils import _call_az

def list(name, resource_group=None):
    '''
    List access keys of an App Configuration.

    Required Parameters:
    - name -- Name of the App Configuration. You can configure the default name using `az configure --defaults app_configuration_store=<name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az appconfig credential list", locals())


def regenerate(id, name, resource_group=None):
    '''
    Regenerate an access key for an App Configuration.

    Required Parameters:
    - id -- Id of the key to be regenerated. Can be found using az appconfig credential list command.
    - name -- Name of the App Configuration. You can configure the default name using `az configure --defaults app_configuration_store=<name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az appconfig credential regenerate", locals())

