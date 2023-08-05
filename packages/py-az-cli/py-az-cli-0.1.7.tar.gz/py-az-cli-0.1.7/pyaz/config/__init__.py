'''
Manage Azure CLI configuration.
'''
from .. pyaz_utils import _call_az
from . import param_persist


def set(local=None):
    '''
    Set a configuration.

    Optional Parameters:
    - local -- Set as a local configuration in the working directory.
    '''
    return _call_az("az config set", locals())


def get(local=None):
    '''
    Get a configuration.

    Optional Parameters:
    - local -- Include local configuration. Scan from the working directory up to the root drive, then the global configuration and return the first occurrence.
    '''
    return _call_az("az config get", locals())


def unset(local=None):
    '''
    Unset a configuration.

    Optional Parameters:
    - local -- Include local configuration. Scan from the working directory up to the root drive, then the global configuration and unset the first occurrence.
    '''
    return _call_az("az config unset", locals())

