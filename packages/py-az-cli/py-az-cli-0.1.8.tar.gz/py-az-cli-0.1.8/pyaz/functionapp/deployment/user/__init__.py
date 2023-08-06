'''
Manage user credentials for deployment.
'''
from .... pyaz_utils import _call_az

def set(user_name, password=None):
    '''
    Update deployment credentials.

    Required Parameters:
    - user_name -- user name

    Optional Parameters:
    - password -- password, will prompt if not specified
    '''
    return _call_az("az functionapp deployment user set", locals())


def show():
    return _call_az("az functionapp deployment user show", locals())

