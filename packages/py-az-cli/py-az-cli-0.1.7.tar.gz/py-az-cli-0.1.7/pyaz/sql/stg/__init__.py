'''
Manage Server Trust Groups.
'''
from ... pyaz_utils import _call_az

def create(group_member, location, name, resource_group, trust_scope, no_wait=None):
    '''
    Create a Server Trust Group.

    Required Parameters:
    - group_member -- Managed Instance that is to be a member of the group.
                   Specify resource group, subscription id and the name of the instance.
    - location -- The location name of the Server Trust Group.
    - name -- The name of the Server Trust Group.
    - resource_group -- The resource group name
    - trust_scope -- The trust scope of the Server Trust Group.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az sql stg create", locals())


def delete(location, name, resource_group, no_wait=None, yes=None):
    '''
    Delete a Server Trust Group.

    Required Parameters:
    - location -- The location of the Server Trust Group.
    - name -- The name of the Server Trust Group.
    - resource_group -- The resource group name

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az sql stg delete", locals())


def show(location, name, resource_group):
    '''
    Retrieve a Server Trust Group.

    Required Parameters:
    - location -- The location of the Server Trust Group.
    - name -- The name of the Server Trust Group.
    - resource_group -- The resource group name
    '''
    return _call_az("az sql stg show", locals())


def list(resource_group, instance_name=None, location=None):
    '''
    Retrieve a list of Server Trust Groups.

    Required Parameters:
    - resource_group -- The resource group name

    Optional Parameters:
    - instance_name -- Managed Instance name.
    - location -- The location of the Server Trust Group.
    '''
    return _call_az("az sql stg list", locals())

