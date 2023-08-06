'''
Manage capacity reservation group.
'''
from .... pyaz_utils import _call_az

def create(capacity_reservation_group, resource_group, location=None, tags=None, zones=None):
    '''
    Create capacity reservation group.

    Required Parameters:
    - capacity_reservation_group -- The name of the capacity reservation group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - zones -- Availability Zones to use for this capacity reservation group. If not provided, the group supports only regional resources in the region. If provided, enforces each capacity reservation in the group to be in one of the zones.
    '''
    return _call_az("az capacity reservation group create", locals())


def update(capacity_reservation_group, resource_group, tags=None):
    '''
    Update capacity reservation group.

    Required Parameters:
    - capacity_reservation_group -- The name of the capacity reservation group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az capacity reservation group update", locals())


def delete(capacity_reservation_group, resource_group, yes=None):
    '''
    Delete capacity reservation group.

    Required Parameters:
    - capacity_reservation_group -- The name of the capacity reservation group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az capacity reservation group delete", locals())


def show(capacity_reservation_group, resource_group, instance_view=None):
    '''
    Show capacity reservation group.

    Required Parameters:
    - capacity_reservation_group -- The name of the capacity reservation group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - instance_view -- Retrieve the list of instance views of the capacity reservations under the capacity reservation group which is a snapshot of the runtime properties of a capacity reservation that is managed by the platform and can change outside of control plane operations.
    '''
    return _call_az("az capacity reservation group show", locals())


def list(resource_group, vm_instance=None, vmss_instance=None):
    '''
    List the capacity reservation groups.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - vm_instance -- Retrieve the Virtual Machine Instance which are associated to capacity reservation group in the response.
    - vmss_instance -- Retrieve the ScaleSet VM Instance which are associated to capacity reservation group in the response.
    '''
    return _call_az("az capacity reservation group list", locals())

