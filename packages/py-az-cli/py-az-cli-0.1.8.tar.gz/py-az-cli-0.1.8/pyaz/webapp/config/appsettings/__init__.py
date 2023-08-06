'''
Configure web app settings. Updating or removing application settings will cause an app recycle.
'''
from .... pyaz_utils import _call_az

def list(name, resource_group, slot=None):
    '''
    Get the details of a web app's settings.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp config appsettings list", locals())


def set(name, resource_group, settings=None, slot=None, slot_settings=None):
    '''
    Set a web app's settings.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - settings -- space-separated appsettings in a format of `<name>=<value>`
    - slot -- the name of the slot. Default to the productions slot if not specified
    - slot_settings -- space-separated slot appsettings in a format of either `<name>=<value>` or `@<json_file>`
    '''
    return _call_az("az webapp config appsettings set", locals())


def delete(name, resource_group, setting_names, slot=None):
    '''
    Delete web app settings.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - setting_names -- space-separated appsettings names

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp config appsettings delete", locals())

