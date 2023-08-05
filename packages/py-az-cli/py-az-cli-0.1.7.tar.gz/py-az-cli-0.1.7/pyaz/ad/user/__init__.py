'''
Manage Azure Active Directory users and user authentication.
'''
from ... pyaz_utils import _call_az

def delete(id):
    '''
    

    Required Parameters:
    - id -- The object ID or principal name of the user for which to get information
    '''
    return _call_az("az ad user delete", locals())


def show(id):
    '''
    

    Required Parameters:
    - id -- The object ID or principal name of the user for which to get information
    '''
    return _call_az("az ad user show", locals())


def list(display_name=None, filter=None, upn=None):
    '''
    List Azure Active Directory users.

    Optional Parameters:
    - display_name -- object's display name or its prefix
    - filter -- OData filter, e.g. --filter "displayname eq 'test' and servicePrincipalType eq 'Application'"
    - upn -- user principal name, e.g. john.doe@contoso.com
    '''
    return _call_az("az ad user list", locals())


def get_member_groups(id, security_enabled_only=None):
    '''
    Get groups of which the user is a member

    Required Parameters:
    - id -- The object ID or principal name of the user for which to get information

    Optional Parameters:
    - security_enabled_only -- If true, only membership in security-enabled groups should be checked. Otherwise, membership in all groups should be checked.
    '''
    return _call_az("az ad user get-member-groups", locals())


def create(display_name, password, user_principal_name, force_change_password_next_login=None, immutable_id=None, mail_nickname=None):
    '''
    Create an Azure Active Directory user.

    Required Parameters:
    - display_name -- object's display name or its prefix
    - password -- user password
    - user_principal_name -- Required. The user principal name (someuser@contoso.com). It must contain one of the verified domains for the tenant.

    Optional Parameters:
    - force_change_password_next_login -- Require the user to change their password the next time they log in. Only valid when --password is specified
    - immutable_id -- This must be specified if you are using a federated domain for the user's userPrincipalName (UPN) property when creating a new user account. It is used to associate an on-premises Active Directory user account with their Azure AD user object.
    - mail_nickname -- mail alias. Defaults to user principal name
    '''
    return _call_az("az ad user create", locals())


def update(id, account_enabled=None, display_name=None, force_change_password_next_login=None, mail_nickname=None, password=None):
    '''
    Update Azure Active Directory users.

    Required Parameters:
    - id -- The object ID or principal name of the user for which to get information

    Optional Parameters:
    - account_enabled -- enable the user account
    - display_name -- object's display name or its prefix
    - force_change_password_next_login -- Require the user to change their password the next time they log in. Only valid when --password is specified
    - mail_nickname -- mail alias. Defaults to user principal name
    - password -- user password
    '''
    return _call_az("az ad user update", locals())

