'''
Manage Azure locks.
'''
from .. pyaz_utils import _call_az

def create(lock_type, name, namespace=None, notes=None, parent=None, resource=None, resource_group=None, resource_type=None):
    '''
    Create a lock.

    Required Parameters:
    - lock_type -- The type of lock restriction.
    - name -- Name of the lock

    Optional Parameters:
    - namespace -- Provider namespace (Ex: 'Microsoft.Provider')
    - notes -- Notes about this lock.
    - parent -- The parent path (Ex: 'resA/myA/resB/myB')
    - resource -- Name or ID of the resource being locked. If an ID is given, other resource arguments should not be given.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_type -- The resource type (Ex: 'resC'). Can also accept namespace/type format (Ex: 'Microsoft.Provider/resC')
    '''
    return _call_az("az lock create", locals())


def delete(ids=None, name=None, namespace=None, parent=None, resource=None, resource_group=None, resource_type=None):
    '''
    Delete a lock.

    Optional Parameters:
    - ids -- One or more resource IDs (space-delimited). If provided, no other "Resource Id" arguments should be specified.
    - name -- Name of the lock
    - namespace -- Provider namespace (Ex: 'Microsoft.Provider')
    - parent -- The parent path (Ex: 'resA/myA/resB/myB')
    - resource -- Name or ID of the resource being locked. If an ID is given, other resource arguments should not be given.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_type -- The resource type (Ex: 'resC'). Can also accept namespace/type format (Ex: 'Microsoft.Provider/resC')
    '''
    return _call_az("az lock delete", locals())


def list(filter_string=None, namespace=None, parent=None, resource=None, resource_group=None, resource_type=None):
    '''
    List lock information.

    Optional Parameters:
    - filter_string -- A query filter to use to restrict the results.
    - namespace -- Provider namespace (Ex: 'Microsoft.Provider')
    - parent -- The parent path (Ex: 'resA/myA/resB/myB')
    - resource -- Name or ID of the resource being locked. If an ID is given, other resource arguments should not be given.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_type -- The resource type (Ex: 'resC'). Can also accept namespace/type format (Ex: 'Microsoft.Provider/resC')
    '''
    return _call_az("az lock list", locals())


def show(ids=None, name=None, namespace=None, parent=None, resource=None, resource_group=None, resource_type=None):
    '''
    Show the properties of a lock

    Optional Parameters:
    - ids -- One or more resource IDs (space-delimited). If provided, no other "Resource Id" arguments should be specified.
    - name -- Name of the lock
    - namespace -- Provider namespace (Ex: 'Microsoft.Provider')
    - parent -- The parent path (Ex: 'resA/myA/resB/myB')
    - resource -- Name or ID of the resource being locked. If an ID is given, other resource arguments should not be given.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_type -- The resource type (Ex: 'resC'). Can also accept namespace/type format (Ex: 'Microsoft.Provider/resC')
    '''
    return _call_az("az lock show", locals())


def update(ids=None, lock_type=None, name=None, namespace=None, notes=None, parent=None, resource=None, resource_group=None, resource_type=None):
    '''
    Update a lock.

    Optional Parameters:
    - ids -- One or more resource IDs (space-delimited). If provided, no other "Resource Id" arguments should be specified.
    - lock_type -- The type of lock restriction.
    - name -- Name of the lock
    - namespace -- Provider namespace (Ex: 'Microsoft.Provider')
    - notes -- Notes about this lock.
    - parent -- The parent path (Ex: 'resA/myA/resB/myB')
    - resource -- Name or ID of the resource being locked. If an ID is given, other resource arguments should not be given.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_type -- The resource type (Ex: 'resC'). Can also accept namespace/type format (Ex: 'Microsoft.Provider/resC')
    '''
    return _call_az("az lock update", locals())

