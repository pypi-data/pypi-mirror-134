'''
Manage Azure resource group locks.
'''
from ... pyaz_utils import _call_az

def create(lock_type, name, resource_group, notes=None):
    '''
    Create a resource group lock.

    Required Parameters:
    - lock_type -- The type of lock restriction.
    - name -- Name of the lock
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - notes -- Notes about this lock.
    '''
    return _call_az("az group lock create", locals())


def delete(ids=None, name=None, resource_group=None):
    '''
    Delete a resource group lock.

    Optional Parameters:
    - ids -- One or more resource IDs (space-delimited). If provided, no other "Resource Id" arguments should be specified.
    - name -- Name of the lock
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az group lock delete", locals())


def list(filter_string=None, resource_group=None):
    '''
    List lock information in the resource-group.

    Optional Parameters:
    - filter_string -- A query filter to use to restrict the results.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az group lock list", locals())


def show(ids=None, name=None, resource_group=None):
    '''
    Show the details of a resource group lock

    Optional Parameters:
    - ids -- One or more resource IDs (space-delimited). If provided, no other "Resource Id" arguments should be specified.
    - name -- Name of the lock
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az group lock show", locals())


def update(ids=None, lock_type=None, name=None, notes=None, resource_group=None):
    '''
    Update a resource group lock.

    Optional Parameters:
    - ids -- One or more resource IDs (space-delimited). If provided, no other "Resource Id" arguments should be specified.
    - lock_type -- The type of lock restriction.
    - name -- Name of the lock
    - notes -- Notes about this lock.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az group lock update", locals())

