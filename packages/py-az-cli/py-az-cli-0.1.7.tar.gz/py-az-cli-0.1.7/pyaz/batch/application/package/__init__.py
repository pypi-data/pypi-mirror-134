'''
Manage Batch application packages.
'''
from .... pyaz_utils import _call_az

def create(application_name, name, package_file, resource_group, version_name):
    '''
    Create a Batch application package record and activate it.

    Required Parameters:
    - application_name -- The name of the application.
    - name -- Name of the Batch account.
    - package_file -- The path of the application package in zip format
    - resource_group -- Name of the resource group
    - version_name -- The version name of the application.
    '''
    return _call_az("az batch application package create", locals())


def delete(application_name, name, resource_group, version_name, yes=None):
    '''
    

    Required Parameters:
    - application_name -- The name of the application. This must be unique within the account.
    - name -- Name of the Batch account.
    - resource_group -- Name of the resource group
    - version_name -- The version of the application.

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az batch application package delete", locals())


def show(application_name, name, resource_group, version_name):
    '''
    

    Required Parameters:
    - application_name -- The name of the application. This must be unique within the account.
    - name -- Name of the Batch account.
    - resource_group -- Name of the resource group
    - version_name -- The version of the application.
    '''
    return _call_az("az batch application package show", locals())


def activate(application_name, format, name, resource_group, version_name):
    '''
    Activates a Batch application package.

    Required Parameters:
    - application_name -- The name of the application.
    - format -- The format of the application package binary file.
    - name -- Name of the Batch account.
    - resource_group -- Name of the resource group
    - version_name -- The version name of the application.
    '''
    return _call_az("az batch application package activate", locals())


def list(application_name, name, resource_group, maxresults=None):
    '''
    

    Required Parameters:
    - application_name -- The name of the application. This must be unique within the account.
    - name -- Name of the Batch account.
    - resource_group -- Name of the resource group

    Optional Parameters:
    - maxresults -- The maximum number of items to return in the response.
    '''
    return _call_az("az batch application package list", locals())

