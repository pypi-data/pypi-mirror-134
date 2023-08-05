'''
Manage Azure Maps account keys.
'''
from .... pyaz_utils import _call_az

def renew(key, name, resource_group):
    '''
    Regenerate either the primary or secondary key for use with the Maps APIs. The old key will stop working immediately.

    Required Parameters:
    - key -- Whether the operation refers to the primary or secondary key
    - name -- The name of the maps account
    - resource_group -- Resource group name
    '''
    return _call_az("az maps account keys renew", locals())


def list(name, resource_group):
    '''
    Get the keys to use with the Maps APIs. A key is used to authenticate and authorize access to the Maps REST APIs. Only one key is needed at a time; two are given to provide seamless key regeneration.

    Required Parameters:
    - name -- The name of the maps account
    - resource_group -- Resource group name
    '''
    return _call_az("az maps account keys list", locals())

