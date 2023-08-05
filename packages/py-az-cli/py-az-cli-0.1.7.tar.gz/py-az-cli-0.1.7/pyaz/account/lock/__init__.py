'''
Manage Azure subscription level locks.
'''
from ... pyaz_utils import _call_az

def create(lock_type, name, notes=None, resource_group=None):
    '''
    Create a subscription lock.

    Required Parameters:
    - lock_type -- The type of lock restriction.
    - name -- Name of the lock

    Optional Parameters:
    - notes -- Notes about this lock.
    - resource_group -- ==SUPPRESS==
    '''
    return _call_az("az account lock create", locals())


def delete(ids=None, name=None, resource_group=None):
    '''
    Delete a subscription lock.

    Optional Parameters:
    - ids -- One or more resource IDs (space-delimited). If provided, no other "Resource Id" arguments should be specified.
    - name -- Name of the lock
    - resource_group -- ==SUPPRESS==
    '''
    return _call_az("az account lock delete", locals())


def list(filter_string=None, resource_group=None):
    '''
    List lock information in the subscription.

    Optional Parameters:
    - filter_string -- A query filter to use to restrict the results.
    - resource_group -- ==SUPPRESS==
    '''
    return _call_az("az account lock list", locals())


def show(ids=None, name=None, resource_group=None):
    '''
    Show the details of a subscription lock

    Optional Parameters:
    - ids -- One or more resource IDs (space-delimited). If provided, no other "Resource Id" arguments should be specified.
    - name -- Name of the lock
    - resource_group -- ==SUPPRESS==
    '''
    return _call_az("az account lock show", locals())


def update(ids=None, lock_type=None, name=None, notes=None, resource_group=None):
    '''
    Update a subscription lock.

    Optional Parameters:
    - ids -- One or more resource IDs (space-delimited). If provided, no other "Resource Id" arguments should be specified.
    - lock_type -- The type of lock restriction.
    - name -- Name of the lock
    - notes -- Notes about this lock.
    - resource_group -- ==SUPPRESS==
    '''
    return _call_az("az account lock update", locals())

