'''
Manage creator with maps
'''
from ... pyaz_utils import _call_az

def list(name, resource_group):
    '''
    Get all Creator instances for an Azure Maps Account.

    Required Parameters:
    - name -- The name of the maps account
    - resource_group -- Resource group name
    '''
    return _call_az("az maps creator list", locals())


def show(creator_name, name, resource_group):
    '''
    Get a Maps Creator resource.

    Required Parameters:
    - creator_name -- The name of the Maps Creator instance.
    - name -- The name of the maps account
    - resource_group -- Resource group name
    '''
    return _call_az("az maps creator show", locals())


def create(creator_name, name, resource_group, storage_units, location=None, tags=None):
    '''
    Create a Maps Creator resource. Creator resource will manage Azure resources required to populate a custom set of mapping data. It requires an account to exist before it can be created.

    Required Parameters:
    - creator_name -- The name of the Maps Creator instance.
    - name -- The name of the maps account
    - resource_group -- Resource group name
    - storage_units -- The storage units to be allocated. Integer values from 1 to 100, inclusive.

    Optional Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az maps creator create", locals())


def update(creator_name, name, resource_group, storage_units=None, tags=None):
    '''
    Updates the Maps Creator resource. Only a subset of the parameters may be updated after creation, such as Tags.

    Required Parameters:
    - creator_name -- The name of the Maps Creator instance.
    - name -- The name of the maps account
    - resource_group -- Resource group name

    Optional Parameters:
    - storage_units -- The storage units to be allocated. Integer values from 1 to 100, inclusive.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az maps creator update", locals())


def delete(creator_name, name, resource_group, yes=None):
    '''
    Delete a Maps Creator resource.

    Required Parameters:
    - creator_name -- The name of the Maps Creator instance.
    - name -- The name of the maps account
    - resource_group -- Resource group name

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az maps creator delete", locals())

