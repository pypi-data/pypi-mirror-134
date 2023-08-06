'''
Manage Azure Active Directory groups.
'''
from ... pyaz_utils import _call_az
from . import member, owner


def delete(group):
    '''
    

    Required Parameters:
    - group -- group's object id or display name(prefix also works if there is a unique match)
    '''
    return _call_az("az ad group delete", locals())


def show(group):
    '''
    

    Required Parameters:
    - group -- group's object id or display name(prefix also works if there is a unique match)
    '''
    return _call_az("az ad group show", locals())


def get_member_groups(group, additional_properties=None, security_enabled_only=None):
    '''
    

    Required Parameters:
    - group -- group's object id or display name(prefix also works if there is a unique match)

    Optional Parameters:
    - additional_properties -- Unmatched properties from the message are deserialized this collection
    - security_enabled_only -- If true, only membership in security-enabled groups should be checked. Otherwise, membership in all groups should be checked.
    '''
    return _call_az("az ad group get-member-groups", locals())


def list(display_name=None, filter=None):
    '''
    

    Optional Parameters:
    - display_name -- object's display name or its prefix
    - filter -- OData filter, e.g. --filter "displayname eq 'test' and servicePrincipalType eq 'Application'"
    '''
    return _call_az("az ad group list", locals())


def create(display_name, mail_nickname, description=None, force=None):
    '''
    Create a group in the directory.

    Required Parameters:
    - display_name -- object's display name or its prefix
    - mail_nickname -- Mail nickname

    Optional Parameters:
    - description -- Group description
    - force -- always create a new group instead of updating the one with same display and mail nickname
    '''
    return _call_az("az ad group create", locals())

