'''
Manage user accounts for a VM.
'''
from ... pyaz_utils import _call_az

def update(name, resource_group, username, no_wait=None, password=None, ssh_key_value=None):
    '''
    Update a user account.

    Required Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - username -- The user name

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - password -- The user password
    - ssh_key_value -- None
    '''
    return _call_az("az vm user update", locals())


def delete(name, resource_group, username, no_wait=None):
    '''
    Delete a user account from a VM.

    Required Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - username -- The user name

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az vm user delete", locals())


def reset_ssh(name, resource_group, no_wait=None):
    '''
    Reset the SSH configuration on a VM.

    Required Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    '''
    return _call_az("az vm user reset-ssh", locals())

