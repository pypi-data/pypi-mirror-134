'''
Manage Batch applications.
'''
from ... pyaz_utils import _call_az
from . import package, summary


def list(name, resource_group, maxresults=None):
    '''
    

    Required Parameters:
    - name -- Name of the Batch account.
    - resource_group -- Name of the resource group

    Optional Parameters:
    - maxresults -- The maximum number of items to return in the response.
    '''
    return _call_az("az batch application list", locals())


def show(application_name, name, resource_group):
    '''
    

    Required Parameters:
    - application_name -- The name of the application. This must be unique within the account.
    - name -- Name of the Batch account.
    - resource_group -- Name of the resource group
    '''
    return _call_az("az batch application show", locals())


def create(application_name, name, resource_group, parameters=None):
    '''
    

    Required Parameters:
    - application_name -- The name of the application. This must be unique within the account.
    - name -- Name of the Batch account.
    - resource_group -- Name of the resource group

    Optional Parameters:
    - parameters -- The parameters for the request.
    '''
    return _call_az("az batch application create", locals())


def set(application_name, name, resource_group, allow_updates=None, default_version=None, display_name=None):
    '''
    Update properties for a Batch application.

    Required Parameters:
    - application_name -- The name of the application.
    - name -- Name of the Batch account.
    - resource_group -- Name of the resource group

    Optional Parameters:
    - allow_updates -- Specify to indicate whether packages within the application may be overwritten using the same version string. Specify either 'true' or 'false' to update the property.
    - default_version -- The package to use if a client requests the application but does not specify a version. This property can only be set to the name of an existing package.
    - display_name -- The display name for the application.
    '''
    return _call_az("az batch application set", locals())


def delete(application_name, name, resource_group, yes=None):
    '''
    

    Required Parameters:
    - application_name -- The name of the application. This must be unique within the account.
    - name -- Name of the Batch account.
    - resource_group -- Name of the resource group

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az batch application delete", locals())

