from ... pyaz_utils import _call_az

def list():
    '''
    Get all reservation orders
    '''
    return _call_az("az reservations reservation-order list", locals())


def show(reservation_order_id, expand=None):
    '''
    Get a specific reservation order.

    Required Parameters:
    - reservation_order_id -- Order Id of the reservation

    Optional Parameters:
    - expand -- May be used to expand the planInformation.
    '''
    return _call_az("az reservations reservation-order show", locals())


def calculate(applied_scope_type, billing_scope, display_name, quantity, reserved_resource_type, sku, term, applied_scope=None, billing_plan=None, instance_flexibility=None, location=None, renew=None):
    '''
    Calculate price for a reservation order.

    Required Parameters:
    - applied_scope_type -- Type of the Applied Scope to update the reservation with
    - billing_scope -- Subscription that will be charged for purchasing Reservation.
    - display_name -- Friendly name for user to easily identified the reservation.
    - quantity -- Quantity of product for calculating price or purchasing.
    - reserved_resource_type -- Type of the resource for which the skus should be provided.
    - sku -- Sku name, get the sku list by using command az reservations catalog show
    - term -- Available reservation terms for this resource.

    Optional Parameters:
    - applied_scope -- Subscription that the benefit will be applied. Required if --applied-scope-type is Single. Do not specify if --applied-scope-type is Shared.
    - billing_plan -- The billing plan options available for this SKU.
    - instance_flexibility -- Type of the Instance Flexibility to update the reservation with.
    - location -- Values from: `az account list-locations`.
    - renew -- Set this to true will automatically purchase a new reservation on the expiration date time.
    '''
    return _call_az("az reservations reservation-order calculate", locals())


def purchase(applied_scope_type, billing_scope, display_name, quantity, reservation_order_id, reserved_resource_type, sku, term, applied_scope=None, billing_plan=None, instance_flexibility=None, location=None, renew=None):
    '''
    Purchase reservation order

    Required Parameters:
    - applied_scope_type -- Type of the Applied Scope to update the reservation with
    - billing_scope -- Subscription that will be charged for purchasing Reservation.
    - display_name -- Friendly name for user to easily identified the reservation.
    - quantity -- Quantity of product for calculating price or purchasing.
    - reservation_order_id -- Id of reservation order to purchase, generate by `az reservations reservation-order calculate`.
    - reserved_resource_type -- Type of the resource for which the skus should be provided.
    - sku -- Sku name, get the sku list by using command az reservations catalog show
    - term -- Available reservation terms for this resource.

    Optional Parameters:
    - applied_scope -- Subscription that the benefit will be applied. Required if --applied-scope-type is Single. Do not specify if --applied-scope-type is Shared.
    - billing_plan -- The billing plan options available for this SKU.
    - instance_flexibility -- Type of the Instance Flexibility to update the reservation with.
    - location -- Values from: `az account list-locations`.
    - renew -- Set this to true will automatically purchase a new reservation on the expiration date time.
    '''
    return _call_az("az reservations reservation-order purchase", locals())

