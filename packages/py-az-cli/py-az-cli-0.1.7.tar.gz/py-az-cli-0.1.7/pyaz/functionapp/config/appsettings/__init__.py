'''
Configure function app settings.
'''
from .... pyaz_utils import _call_az

def list(name, resource_group, slot=None):
    '''
    Show settings for a function app.

    Required Parameters:
    - name -- name of the function app.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az functionapp config appsettings list", locals())


def set(name, resource_group, settings=None, slot=None, slot_settings=None):
    '''
    Update a function app's settings.

    Required Parameters:
    - name -- name of the function app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - settings -- space-separated app settings in a format of `<name>=<value>`
    - slot -- the name of the slot. Default to the productions slot if not specified
    - slot_settings -- space-separated slot app settings in a format of `<name>=<value>`
    '''
    return _call_az("az functionapp config appsettings set", locals())


def delete(name, resource_group, setting_names, slot=None):
    '''
    Delete a function app's settings.

    Required Parameters:
    - name -- name of the function app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - setting_names -- space-separated app setting names

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az functionapp config appsettings delete", locals())

