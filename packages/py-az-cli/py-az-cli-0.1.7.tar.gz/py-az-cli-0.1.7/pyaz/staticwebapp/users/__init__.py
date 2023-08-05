'''
Manage users of the static app.
'''
from ... pyaz_utils import _call_az

def list(name, authentication_provider=None, resource_group=None):
    '''
    Lists users and assigned roles, limited to users who accepted their invites.

    Required Parameters:
    - name -- Name of the static site

    Optional Parameters:
    - authentication_provider -- Authentication provider of the user identity such as AAD, Facebook, GitHub, Google, Twitter.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az staticwebapp users list", locals())


def invite(authentication_provider, domain, invitation_expiration_in_hours, name, roles, user_details, resource_group=None):
    '''
    Create invitation link for specified user to the static app.

    Required Parameters:
    - authentication_provider -- Authentication provider of the user identity such as AAD, Facebook, GitHub, Google, Twitter.
    - domain -- A domain added to the static app in quotes.
    - invitation_expiration_in_hours -- This value sets when the link will expire in hours. The maximum is 168 (7 days).
    - name -- Name of the static site
    - roles -- Comma-separated default or user-defined role names. Roles that can be assigned to a user are comma separated and case-insensitive (at most 50 roles up to 25 characters each and restricted to 0-9,A-Z,a-z, and _). Define roles in routes.json during root directory of your GitHub repo.
    - user_details -- Email for AAD, Facebook, and Google. Account name (handle) for GitHub and Twitter.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az staticwebapp users invite", locals())


def update(name, roles, authentication_provider=None, resource_group=None, user_details=None, user_id=None):
    '''
    Updates a user entry with the listed roles. Either user details or user id is required.

    Required Parameters:
    - name -- Name of the static site
    - roles -- Comma-separated default or user-defined role names. Roles that can be assigned to a user are comma separated and case-insensitive (at most 50 roles up to 25 characters each and restricted to 0-9,A-Z,a-z, and _). Define roles in routes.json during root directory of your GitHub repo.

    Optional Parameters:
    - authentication_provider -- Authentication provider of the user identity such as AAD, Facebook, GitHub, Google, Twitter.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - user_details -- Email for AAD, Facebook, and Google. Account name (handle) for GitHub and Twitter.
    - user_id -- Given id of registered user.
    '''
    return _call_az("az staticwebapp users update", locals())

