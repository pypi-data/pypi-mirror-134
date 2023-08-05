'''
Manage Azure Active Directory group owners.
'''
from .... pyaz_utils import _call_az

def list(group):
    '''
    List group owners.

    Required Parameters:
    - group -- group's object id or display name(prefix also works if there is a unique match)
    '''
    return _call_az("az ad group owner list", locals())


def add(group, owner_object_id):
    '''
    Add a group owner.

    Required Parameters:
    - group -- group's object id or display name(prefix also works if there is a unique match)
    - owner_object_id -- owner's object id
    '''
    return _call_az("az ad group owner add", locals())


def remove(group, owner_object_id):
    '''
    Remove a group owner.

    Required Parameters:
    - group -- group's object id or display name(prefix also works if there is a unique match)
    - owner_object_id -- owner's object id
    '''
    return _call_az("az ad group owner remove", locals())

