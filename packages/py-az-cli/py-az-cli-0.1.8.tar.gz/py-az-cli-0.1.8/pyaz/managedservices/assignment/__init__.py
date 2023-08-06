'''
Manage the registration assignments in Azure.
'''
from ... pyaz_utils import _call_az

def create(definition, assignment_id=None, resource_group=None):
    '''
    Creates a new registration assignment.

    Required Parameters:
    - definition -- None

    Optional Parameters:
    - assignment_id -- None
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az managedservices assignment create", locals())


def show(assignment, include_definition=None, resource_group=None):
    '''
    Gets a registration assignment.

    Required Parameters:
    - assignment -- The identifier (guid) or the fully qualified resource id of the registration assignment. When resource id is used, subscription id and resource group parameters are ignored.

    Optional Parameters:
    - include_definition -- When provided, gets the associated registration definition details.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az managedservices assignment show", locals())


def delete(assignment, resource_group=None):
    '''
    Deletes the registration assignment.

    Required Parameters:
    - assignment -- The identifier (guid) or the fully qualified resource id of the registration assignment. When resource id is used, subscription id and resource group parameters are ignored.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az managedservices assignment delete", locals())


def list(include_definition=None, resource_group=None):
    '''
    List all the registration assignments.

    Optional Parameters:
    - include_definition -- When provided, gets the associated registration definition details.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az managedservices assignment list", locals())

