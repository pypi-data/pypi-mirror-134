'''
Manage network interfaces of a VMSS.
'''
from ... pyaz_utils import _call_az

def list(resource_group, vmss_name):
    '''
    

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vmss_name -- Scale set name. You can configure the default using `az configure --defaults vmss=<name>`
    '''
    return _call_az("az vmss nic list", locals())


def list_vm_nics(instance_id, resource_group, vmss_name):
    '''
    

    Required Parameters:
    - instance_id -- The virtual machine index.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vmss_name -- Scale set name.
    '''
    return _call_az("az vmss nic list-vm-nics", locals())


def show(instance_id, name, resource_group, vmss_name, expand=None):
    '''
    

    Required Parameters:
    - instance_id -- The virtual machine index.
    - name -- The network interface (NIC).
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vmss_name -- Scale set name.

    Optional Parameters:
    - expand -- Expands referenced resources.
    '''
    return _call_az("az vmss nic show", locals())

