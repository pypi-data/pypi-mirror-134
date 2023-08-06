from ... pyaz_utils import _call_az

def add(name, resource_group, subnet, vnet, skip_delegation_check=None, slot=None):
    '''
    Add a regional virtual network integration to a functionapp

    Required Parameters:
    - name -- name of the function app.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - subnet -- The name or resource ID of the subnet
    - vnet -- The name or resource ID of the Vnet

    Optional Parameters:
    - skip_delegation_check -- Skip check if you do not have permission or the VNet is in another subscription.
    - slot -- The name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az functionapp vnet-integration add", locals())


def list(name, resource_group, slot=None):
    '''
    list the virtual network integrations on a functionapp

    Required Parameters:
    - name -- name of the function app.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- The name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az functionapp vnet-integration list", locals())


def remove(name, resource_group, slot=None):
    '''
    remove a regional virtual network integration from functionapp

    Required Parameters:
    - name -- name of the function app.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- The name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az functionapp vnet-integration remove", locals())

