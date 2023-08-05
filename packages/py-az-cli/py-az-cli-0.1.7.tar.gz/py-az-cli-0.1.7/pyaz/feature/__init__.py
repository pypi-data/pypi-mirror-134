'''
Manage resource provider features.
'''
from .. pyaz_utils import _call_az
from . import registration


def list(namespace=None):
    '''
    List preview features.

    Optional Parameters:
    - namespace -- the resource namespace, aka 'provider'
    '''
    return _call_az("az feature list", locals())


def show(name, namespace):
    '''
    

    Required Parameters:
    - name -- the feature name
    - namespace -- the resource namespace, aka 'provider'
    '''
    return _call_az("az feature show", locals())


def register(name, namespace):
    '''
    register a preview feature.

    Required Parameters:
    - name -- the feature name
    - namespace -- the resource namespace, aka 'provider'
    '''
    return _call_az("az feature register", locals())


def unregister(name, namespace):
    '''
    unregister a preview feature.

    Required Parameters:
    - name -- the feature name
    - namespace -- the resource namespace, aka 'provider'
    '''
    return _call_az("az feature unregister", locals())

