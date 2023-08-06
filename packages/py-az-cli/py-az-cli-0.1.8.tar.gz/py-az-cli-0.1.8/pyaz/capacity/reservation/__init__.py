'''
Manage capacity reservation.
'''
from ... pyaz_utils import _call_az
from . import group


def create(capacity_reservation_group, capacity_reservation_name, resource_group, sku, capacity=None, location=None, no_wait=None, tags=None, zone=None):
    '''
    Create capacity reservation.

    Required Parameters:
    - capacity_reservation_group -- The name of the capacity reservation group.
    - capacity_reservation_name -- The name of the capacity reservation.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sku -- The SKU of the resource for which capacity needs be reserved. Currently VM Skus with the capability called "CapacityReservationSupported" set to true are supported. Refer to List Microsoft.Compute SKUs in a region (https://docs.microsoft.com/rest/api/compute/resourceskus/list) for supported values.

    Optional Parameters:
    - capacity -- Specify the number of virtual machines in the scale set.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - no_wait -- Do not wait for the long-running operation to finish.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - zone -- Availability Zone to use for this capacity reservation. The zone has to be single value and also should be part for the list of zones specified during the capacity reservation group creation. If not provided, the reservation supports only non-zonal deployments. If provided, enforces VM/VMSS using this capacity reservation to be in same zone.
    '''
    return _call_az("az capacity reservation create", locals())


def update(capacity_reservation_group, capacity_reservation_name, resource_group, capacity=None, no_wait=None, tags=None):
    '''
    Update capacity reservation.

    Required Parameters:
    - capacity_reservation_group -- The name of the capacity reservation group.
    - capacity_reservation_name -- The name of the capacity reservation.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - capacity -- Specify the number of virtual machines in the scale set.
    - no_wait -- Do not wait for the long-running operation to finish.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az capacity reservation update", locals())


def delete(capacity_reservation_group, capacity_reservation_name, resource_group, no_wait=None, yes=None):
    '''
    Delete capacity reservation.

    Required Parameters:
    - capacity_reservation_group -- The name of the capacity reservation group.
    - capacity_reservation_name -- The name of the capacity reservation.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az capacity reservation delete", locals())


def show(capacity_reservation_group, capacity_reservation_name, resource_group, instance_view=None):
    '''
    Show capacity reservation.

    Required Parameters:
    - capacity_reservation_group -- The name of the capacity reservation group.
    - capacity_reservation_name -- The name of the capacity reservation.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - instance_view -- Retrieve a snapshot of the runtime properties of the capacity reservation that is managed by the platform and can change outside of control plane operations.
    '''
    return _call_az("az capacity reservation show", locals())


def list(capacity_reservation_group, resource_group):
    '''
    List capacity reservation.

    Required Parameters:
    - capacity_reservation_group -- The name of the capacity reservation group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az capacity reservation list", locals())

