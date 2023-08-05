'''
Manage network profiles.
'''
from ... pyaz_utils import _call_az

def delete(name, resource_group, yes=None):
    '''
    Delete a network profile.

    Required Parameters:
    - name -- The network profile name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az network profile delete", locals())


def list(resource_group=None):
    '''
    List network profiles.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network profile list", locals())


def show(name, resource_group, expand=None):
    '''
    Get the details of a network profile.

    Required Parameters:
    - name -- The network profile name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - expand -- Expands referenced resources.
    '''
    return _call_az("az network profile show", locals())

