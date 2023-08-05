'''
Identity details of a Recovery Services Vault.
'''
from .... pyaz_utils import _call_az

def assign(name, resource_group, system_assigned=None, user_assigned=None):
    '''
    Assign Identities to Recovery Services vault.

    Required Parameters:
    - name -- Name of the Recovery services vault.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - system_assigned -- Provide this flag to enable system assigned identity for Recovery Services Vault.
    - user_assigned -- Space-separated list of userassigned identities to be assigned to Recovery Services Vault.
    '''
    return _call_az("az backup vault identity assign", locals())


def remove(name, resource_group, system_assigned=None, user_assigned=None):
    '''
    Remove Identities of Recovery Services vault.

    Required Parameters:
    - name -- Name of the Recovery services vault.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - system_assigned -- Provide this flag to remove system assigned identity for Recovery Services Vault.
    - user_assigned -- Space-separated list of userassigned identities to be removed from Recovery Services Vault.
    '''
    return _call_az("az backup vault identity remove", locals())


def show(name, resource_group):
    '''
    Show Identities of Recovery Services vault.

    Required Parameters:
    - name -- Name of the Recovery services vault.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az backup vault identity show", locals())

