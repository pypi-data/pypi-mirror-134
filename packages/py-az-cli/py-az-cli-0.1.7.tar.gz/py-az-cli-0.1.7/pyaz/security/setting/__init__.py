'''
View your security settings.
'''
from ... pyaz_utils import _call_az

def list():
    '''
    List security settings.
    '''
    return _call_az("az security setting list", locals())


def show(name):
    '''
    Shows a security setting.

    Required Parameters:
    - name -- The name of the setting
    '''
    return _call_az("az security setting show", locals())


def update(enabled, name):
    '''
    Updates a security setting.

    Required Parameters:
    - enabled -- Enable or disable the setting status.
    - name -- The name of the setting
    '''
    return _call_az("az security setting update", locals())

