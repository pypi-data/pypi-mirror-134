'''
Manage function app functions.
'''
from ... pyaz_utils import _call_az
from . import keys


def show(function_name, name, resource_group):
    '''
    Get the details of a function.

    Required Parameters:
    - function_name -- Name of the Function
    - name -- Name of the function app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az functionapp function show", locals())


def delete(function_name, name, resource_group):
    '''
    Delete a function.

    Required Parameters:
    - function_name -- Name of the Function
    - name -- Name of the function app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az functionapp function delete", locals())

