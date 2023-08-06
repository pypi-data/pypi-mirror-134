'''
Managed Service Identities
'''
from .. pyaz_utils import _call_az

def create(name, resource_group, location=None, tags=None):
    '''
    

    Required Parameters:
    - name -- The name of the identity resource.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az identity create", locals())


def show(name, resource_group):
    '''
    

    Required Parameters:
    - name -- The name of the identity resource.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az identity show", locals())


def delete(name, resource_group):
    '''
    

    Required Parameters:
    - name -- The name of the identity resource.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az identity delete", locals())


def list(resource_group=None):
    '''
    List Managed Service Identities

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az identity list", locals())


def list_operations():
    '''
    Lists available operations for the Managed Identity provider
    '''
    return _call_az("az identity list-operations", locals())

