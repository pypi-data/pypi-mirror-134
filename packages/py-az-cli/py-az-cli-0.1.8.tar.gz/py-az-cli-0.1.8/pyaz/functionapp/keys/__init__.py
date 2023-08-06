'''
Manage function app keys.
'''
from ... pyaz_utils import _call_az

def set(key_name, key_type, name, resource_group, key_value=None, slot=None):
    '''
    Create or update a function app key.

    Required Parameters:
    - key_name -- Name of the key to set.
    - key_type -- Type of key.
    - name -- Name of the function app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - key_value -- Value of the new key. If not provided, a value will be generated.
    - slot -- The name of the slot. Defaults to the productions slot if not specified
    '''
    return _call_az("az functionapp keys set", locals())


def list(name, resource_group, slot=None):
    '''
    List all function app keys.

    Required Parameters:
    - name -- Name of the function app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- The name of the slot. Defaults to the productions slot if not specified
    '''
    return _call_az("az functionapp keys list", locals())


def delete(key_name, key_type, name, resource_group, slot=None):
    '''
    Delete a function app key.

    Required Parameters:
    - key_name -- Name of the key to set.
    - key_type -- Type of key.
    - name -- Name of the function app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- The name of the slot. Defaults to the productions slot if not specified
    '''
    return _call_az("az functionapp keys delete", locals())

