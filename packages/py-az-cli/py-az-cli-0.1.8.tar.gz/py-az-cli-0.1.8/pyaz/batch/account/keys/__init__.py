'''
Manage Batch account keys.
'''
from .... pyaz_utils import _call_az

def list(name, resource_group):
    '''
    

    Required Parameters:
    - name -- Name of the Batch account.
    - resource_group -- Name of the resource group
    '''
    return _call_az("az batch account keys list", locals())


def renew(key_name=None, name=None, resource_group=None):
    '''
    Renew keys for a Batch account.

    Optional Parameters:
    - key_name -- Name of the batch account key.
    - name -- Name of the batch account to show. If not specified will display currently set account.
    - resource_group -- Name of the resource group. If not specified will display currently set account.
    '''
    return _call_az("az batch account keys renew", locals())

