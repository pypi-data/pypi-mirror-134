'''
Manage function keys.
'''
from .... pyaz_utils import _call_az

def set(function_name, key_name, name, resource_group, key_value=None, slot=None):
    '''
    Create or update a function key.

    Required Parameters:
    - function_name -- Name of the Function
    - key_name -- Name of the key to set.
    - name -- Name of the function app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - key_value -- Value of the new key. If not provided, a value will be generated.
    - slot -- The name of the slot. Defaults to the productions slot if not specified
    '''
    return _call_az("az functionapp function keys set", locals())


def list(function_name, name, resource_group, slot=None):
    '''
    List all function keys.

    Required Parameters:
    - function_name -- Name of the Function
    - name -- Name of the function app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- The name of the slot. Defaults to the productions slot if not specified
    '''
    return _call_az("az functionapp function keys list", locals())


def delete(key_name, name, resource_group, function_name=None, slot=None):
    '''
    Delete a function key.

    Required Parameters:
    - key_name -- Name of the key to set.
    - name -- Name of the function app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - function_name -- Name of the Function
    - slot -- The name of the slot. Defaults to the productions slot if not specified
    '''
    return _call_az("az functionapp function keys delete", locals())

