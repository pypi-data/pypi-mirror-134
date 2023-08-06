'''
Manage Azure Active Directory group members.
'''
from .... pyaz_utils import _call_az

def list(group):
    '''
    

    Required Parameters:
    - group -- group's object id or display name(prefix also works if there is a unique match)
    '''
    return _call_az("az ad group member list", locals())


def add(group, member_id, additional_properties=None):
    '''
    

    Required Parameters:
    - group -- group's object id or display name(prefix also works if there is a unique match)
    - member_id -- The object ID of the contact, group, user, or service principal

    Optional Parameters:
    - additional_properties -- Unmatched properties from the message are deserialized this collection
    '''
    return _call_az("az ad group member add", locals())


def remove(group, member_id):
    '''
    

    Required Parameters:
    - group -- group's object id or display name(prefix also works if there is a unique match)
    - member_id -- The object ID of the contact, group, user, or service principal
    '''
    return _call_az("az ad group member remove", locals())


def check(group, member_id):
    '''
    Check if a member is in a group.

    Required Parameters:
    - group -- group's object id or display name(prefix also works if there is a unique match)
    - member_id -- The object ID of the contact, group, user, or service principal
    '''
    return _call_az("az ad group member check", locals())

