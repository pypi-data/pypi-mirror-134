'''
Manage network interfaces. See also `az network nic`.
'''
from ... pyaz_utils import _call_az

def add(nics, resource_group, vm_name, primary_nic=None):
    '''
    Add existing NICs to a VM.

    Required Parameters:
    - nics -- Names or IDs of NICs.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vm_name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`

    Optional Parameters:
    - primary_nic -- Name or ID of the primary NIC. If missing, the first NIC in the list will be the primary.
    '''
    return _call_az("az vm nic add", locals())


def remove(nics, resource_group, vm_name, primary_nic=None):
    '''
    Remove NICs from a VM.

    Required Parameters:
    - nics -- Names or IDs of NICs.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vm_name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`

    Optional Parameters:
    - primary_nic -- Name or ID of the primary NIC. If missing, the first NIC in the list will be the primary.
    '''
    return _call_az("az vm nic remove", locals())


def set(nics, resource_group, vm_name, primary_nic=None):
    '''
    Configure settings of a NIC attached to a VM.

    Required Parameters:
    - nics -- Names or IDs of NICs.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vm_name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`

    Optional Parameters:
    - primary_nic -- Name or ID of the primary NIC. If missing, the first NIC in the list will be the primary.
    '''
    return _call_az("az vm nic set", locals())


def show(nic, resource_group, vm_name):
    '''
    Display information for a NIC attached to a VM.

    Required Parameters:
    - nic -- NIC name or ID.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vm_name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    '''
    return _call_az("az vm nic show", locals())


def list(resource_group, vm_name):
    '''
    List the NICs available on a VM.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vm_name -- The name of the Virtual Machine. You can configure the default using `az configure --defaults vm=<name>`
    '''
    return _call_az("az vm nic list", locals())

