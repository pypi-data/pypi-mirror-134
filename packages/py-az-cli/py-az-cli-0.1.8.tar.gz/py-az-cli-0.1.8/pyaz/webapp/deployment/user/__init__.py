'''
Manage user credentials for deployment.
'''
from .... pyaz_utils import _call_az

def show():
    '''
    Get deployment publishing user.
    '''
    return _call_az("az webapp deployment user show", locals())


def set(user_name, password=None):
    '''
    Update deployment credentials.

    Required Parameters:
    - user_name -- user name

    Optional Parameters:
    - password -- password, will prompt if not specified
    '''
    return _call_az("az webapp deployment user set", locals())

