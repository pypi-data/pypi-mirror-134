'''
Manage function app deployment slots.
'''
from .... pyaz_utils import _call_az

def list(name, resource_group):
    '''
    List all deployment slots.

    Required Parameters:
    - name -- Name of the function app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az functionapp deployment slot list", locals())


def delete(name, resource_group, slot):
    '''
    Delete a deployment slot.

    Required Parameters:
    - name -- Name of the function app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - slot -- the name of the slot
    '''
    return _call_az("az functionapp deployment slot delete", locals())


def auto_swap(name, resource_group, slot, auto_swap_slot=None, disable=None):
    '''
    Configure deployment slot auto swap.

    Required Parameters:
    - name -- Name of the function app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - slot -- the name of the slot

    Optional Parameters:
    - auto_swap_slot -- target slot to auto swap
    - disable -- disable auto swap
    '''
    return _call_az("az functionapp deployment slot auto-swap", locals())


def swap(name, resource_group, slot, action=None, preserve_vnet=None, target_slot=None):
    '''
    Swap deployment slots for a function app.

    Required Parameters:
    - name -- Name of the function app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - slot -- the name of the slot

    Optional Parameters:
    - action -- swap types. use 'preview' to apply target slot's settings on the source slot first; use 'swap' to complete it; use 'reset' to reset the swap
    - preserve_vnet -- preserve Virtual Network to the slot during swap, default to 'true'
    - target_slot -- target slot to swap, default to 'production'
    '''
    return _call_az("az functionapp deployment slot swap", locals())


def create(name, resource_group, slot, configuration_source=None):
    '''
    Create a deployment slot.

    Required Parameters:
    - name -- name of the function app
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - slot -- the name of the slot

    Optional Parameters:
    - configuration_source -- source slot to clone configurations from. Use function app's name to refer to the production slot
    '''
    return _call_az("az functionapp deployment slot create", locals())

