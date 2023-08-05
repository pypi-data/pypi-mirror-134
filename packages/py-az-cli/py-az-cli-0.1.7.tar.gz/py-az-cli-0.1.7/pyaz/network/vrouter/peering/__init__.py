'''
Manage the virtual router peering.
'''
from .... pyaz_utils import _call_az

def create(name, peer_asn, peer_ip, resource_group, vrouter_name):
    '''
    Create a virtual router peering.

    Required Parameters:
    - name -- The name of the Virtual Router Peering
    - peer_asn -- Peer ASN. Its range is from 1 to 4294967295.
    - peer_ip -- Peer IP address.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vrouter_name -- The name of the Virtual Router.
    '''
    return _call_az("az network vrouter peering create", locals())


def update(name, resource_group, vrouter_name, add=None, force_string=None, peer_asn=None, peer_ip=None, remove=None, set=None):
    '''
    Update a virtual router peering.

    Required Parameters:
    - name -- The name of the Virtual Router Peering
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vrouter_name -- The name of the Virtual Router.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - peer_asn -- Peer ASN. Its range is from 1 to 4294967295.
    - peer_ip -- Peer IP address.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az network vrouter peering update", locals())


def delete(name, resource_group, vrouter_name):
    '''
    Delete a virtual router peering.

    Required Parameters:
    - name -- The name of the Virtual Router Peering
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vrouter_name -- The name of the Virtual Router.
    '''
    return _call_az("az network vrouter peering delete", locals())


def show(name, resource_group, vrouter_name):
    '''
    Show a virtual router peering

    Required Parameters:
    - name -- The name of the Virtual Router Peering
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vrouter_name -- The name of the Virtual Router.
    '''
    return _call_az("az network vrouter peering show", locals())


def list(resource_group, vrouter_name):
    '''
    List all virtual router peerings under a resource group.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - vrouter_name -- The name of the Virtual Router.
    '''
    return _call_az("az network vrouter peering list", locals())

