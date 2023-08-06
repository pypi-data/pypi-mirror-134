'''
Commands to manage CLI objects cached using the `--defer` argument.
'''
from .. pyaz_utils import _call_az

def list():
    '''
    List the contents of the object cache.
    '''
    return _call_az("az cache list", locals())


def show(name, resource_group, resource_type):
    '''
    Show the contents of a specific object in the cache.

    Required Parameters:
    - name -- The resource name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_type -- The resource type.
    '''
    return _call_az("az cache show", locals())


def delete(name, resource_group, resource_type):
    '''
    Delete an object from the cache.

    Required Parameters:
    - name -- The resource name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_type -- The resource type.
    '''
    return _call_az("az cache delete", locals())


def purge():
    '''
    Clear the entire CLI object cache.
    '''
    return _call_az("az cache purge", locals())

