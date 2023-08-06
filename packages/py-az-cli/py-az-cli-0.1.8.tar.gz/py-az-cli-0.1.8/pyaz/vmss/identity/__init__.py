'''
manage service identities of a VM scaleset.
'''
from ... pyaz_utils import _call_az

def assign(name, resource_group, identities=None, role=None, scope=None):
    '''
    Enable managed service identity on a VMSS.

    Required Parameters:
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - identities -- Space-separated identities to assign. Use '[system]' to refer to the system assigned identity. Default: '[system]'
    - role -- Role name or id the system assigned identity will have
    - scope -- Scope that the system assigned identity can access
    '''
    return _call_az("az vmss identity assign", locals())


def remove(name, resource_group, identities=None):
    '''
    Remove user assigned identities from a VM scaleset.

    Required Parameters:
    - name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - identities -- Space-separated identities to remove. Use '[system]' to refer to the system assigned identity. Default: '[system]'
    '''
    return _call_az("az vmss identity remove", locals())


def show(name, resource_group):
    '''
    display VM scaleset's managed identity info.

    Required Parameters:
    - name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az vmss identity show", locals())

