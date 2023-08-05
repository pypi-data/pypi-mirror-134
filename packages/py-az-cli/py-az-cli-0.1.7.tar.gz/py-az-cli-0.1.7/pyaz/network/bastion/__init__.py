'''
Manage Azure bastion host.
'''
from ... pyaz_utils import _call_az

def create(name, public_ip_address, resource_group, vnet_name, location=None, scale_units=None, sku=None, tags=None):
    '''
    Create a Azure bastion host machine.

    Required Parameters:
    - name -- Name of the bastion host.
    - public_ip_address -- Name or ID of the Azure public IP. The SKU of the public IP must be Standard.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vnet_name -- Name of the virtual network. It must have a subnet called AzureBastionSubnet.

    Optional Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - scale_units -- The scale units for the Bastion Host resource, which minimum is 2 and maximum is 50.
    - sku -- The SKU of this Bastion Host.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az network bastion create", locals())


def show(name, resource_group):
    '''
    Show a Azure bastion host machine.

    Required Parameters:
    - name -- Name of the bastion host.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network bastion show", locals())


def list(resource_group=None):
    '''
    List all Azure bastion host machines.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network bastion list", locals())


def ssh(auth_type, name, resource_group, target_resource_id, resource_port=None, ssh_key=None, username=None):
    '''
    SSH to a virtual machine using Tunneling from Azure Bastion.

    Required Parameters:
    - auth_type -- Auth type to use for SSH connections.
    - name -- Name of the bastion host.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - target_resource_id -- ResourceId of the target Virtual Machine.

    Optional Parameters:
    - resource_port -- Resource port of the target VM to which the bastion will connect.
    - ssh_key -- SSH key file location for SSH connections.
    - username -- User name for SSH connections.
    '''
    return _call_az("az network bastion ssh", locals())


def rdp(name, resource_group, target_resource_id, resource_port=None):
    '''
    RDP to target Virtual Machine using Tunneling from Azure Bastion.

    Required Parameters:
    - name -- Name of the bastion host.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - target_resource_id -- ResourceId of the target Virtual Machine.

    Optional Parameters:
    - resource_port -- Resource port of the target VM to which the bastion will connect.
    '''
    return _call_az("az network bastion rdp", locals())


def tunnel(name, port, resource_group, resource_port, target_resource_id, timeout=None):
    '''
    Show a Azure bastion host machine.

    Required Parameters:
    - name -- Name of the bastion host.
    - port -- Local port to use for the tunneling.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_port -- Resource port of the target VM to which the bastion will connect.
    - target_resource_id -- ResourceId of the target Virtual Machine.

    Optional Parameters:
    - timeout -- Timeout for connection to bastion host tunnel.
    '''
    return _call_az("az network bastion tunnel", locals())


def delete(name, resource_group):
    '''
    Delete a Azure bastion host machine.

    Required Parameters:
    - name -- Name of the bastion host.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network bastion delete", locals())

