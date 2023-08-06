'''
Manage template solutions provided and maintained by Independent Software Vendors (ISVs).
'''
from .. pyaz_utils import _call_az
from . import definition


def create(kind, managed_rg_id, name, resource_group, location=None, managedapp_definition_id=None, parameters=None, plan_name=None, plan_product=None, plan_publisher=None, plan_version=None, tags=None):
    '''
    Create a managed application.

    Required Parameters:
    - kind -- the managed application kind. can be marketplace or servicecatalog
    - managed_rg_id -- the resource group managed by the managed application
    - name -- the managed application name
    - resource_group -- the resource group of the managed application

    Optional Parameters:
    - location -- the managed application location
    - managedapp_definition_id -- the full qualified managed application definition id
    - parameters -- JSON formatted string or a path to a file with such content
    - plan_name -- the managed application package plan name
    - plan_product -- the managed application package plan product
    - plan_publisher -- the managed application package plan publisher
    - plan_version -- the managed application package plan version
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az managedapp create", locals())


def delete(name, resource_group):
    '''
    Delete a managed application.

    Required Parameters:
    - name -- The name of the managed application.
    - resource_group -- the resource group of the managed application
    '''
    return _call_az("az managedapp delete", locals())


def show(name=None, resource_group=None):
    '''
    

    Optional Parameters:
    - name -- the managed application name
    - resource_group -- the resource group of the managed application
    '''
    return _call_az("az managedapp show", locals())


def list(resource_group=None):
    '''
    List managed applications.

    Optional Parameters:
    - resource_group -- the resource group of the managed application
    '''
    return _call_az("az managedapp list", locals())

