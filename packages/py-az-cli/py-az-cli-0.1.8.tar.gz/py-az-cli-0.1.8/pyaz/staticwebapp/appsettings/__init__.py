'''
Manage app settings the static app.
'''
from ... pyaz_utils import _call_az

def list(name, resource_group=None):
    '''
    List app settings of the static app.

    Required Parameters:
    - name -- Name of the static site

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az staticwebapp appsettings list", locals())


def set(name, setting_names, resource_group=None):
    '''
    Add to or change the app settings of the static app.

    Required Parameters:
    - name -- Name of the static site
    - setting_names -- Space-separated app settings in 'key=value' format. 

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az staticwebapp appsettings set", locals())


def delete(name, setting_names, resource_group=None):
    '''
    Delete app settings with given keys of the static app.

    Required Parameters:
    - name -- Name of the static site
    - setting_names -- Space-separated app setting names.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az staticwebapp appsettings delete", locals())

