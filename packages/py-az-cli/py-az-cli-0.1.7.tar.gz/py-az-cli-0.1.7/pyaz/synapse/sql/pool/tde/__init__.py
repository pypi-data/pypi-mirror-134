'''
Manage a SQL pool's transparent data encryption.
'''
from ..... pyaz_utils import _call_az

def set(name, resource_group, status, transparent_data_encryption_name, workspace_name):
    '''
    Set a SQL pool's transparent data encryption configuration.

    Required Parameters:
    - name -- The SQL pool name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - status -- Status of the transparent data encryption.
    - transparent_data_encryption_name -- Name of the transparent data encryption.
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse sql pool tde set", locals())


def show(name, resource_group, transparent_data_encryption_name, workspace_name):
    '''
    Get a SQL pool's transparent data encryption configuration.

    Required Parameters:
    - name -- The SQL pool name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - transparent_data_encryption_name -- Name of the transparent data encryption.
    - workspace_name -- The workspace name.
    '''
    return _call_az("az synapse sql pool tde show", locals())

