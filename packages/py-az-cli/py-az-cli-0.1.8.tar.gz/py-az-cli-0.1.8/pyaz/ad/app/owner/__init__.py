'''
Manage application owners.
'''
from .... pyaz_utils import _call_az

def list(id):
    '''
    List application owners.

    Required Parameters:
    - id -- identifier uri, application id, or object id of the application
    '''
    return _call_az("az ad app owner list", locals())


def add(id, owner_object_id):
    '''
    Add an application owner.

    Required Parameters:
    - id -- identifier uri, application id, or object id
    - owner_object_id -- owner's object id
    '''
    return _call_az("az ad app owner add", locals())


def remove(id, owner_object_id):
    '''
    Remove an application owner.

    Required Parameters:
    - id -- identifier uri, application id, or object id
    - owner_object_id -- owner's object id
    '''
    return _call_az("az ad app owner remove", locals())

