'''
Manage shared access keys of a partner namespace.
'''
from ..... pyaz_utils import _call_az

def list(partner_namespace_name, resource_group):
    '''
    List shared access keys of a partner namespace.

    Required Parameters:
    - partner_namespace_name -- Name of the partner namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventgrid partner namespace key list", locals())


def regenerate(key_name, partner_namespace_name, resource_group):
    '''
    Regenerate a shared access key of a partner namespace.

    Required Parameters:
    - key_name -- Key name to regenerate key1 or key2
    - partner_namespace_name -- Name of the partner namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventgrid partner namespace key regenerate", locals())

