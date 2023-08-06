'''
Manage reservation entities
'''
from ... pyaz_utils import _call_az

def list(reservation_order_id):
    '''
    Get all reservations.

    Required Parameters:
    - reservation_order_id -- Order Id of the reservation
    '''
    return _call_az("az reservations reservation list", locals())


def show(reservation_id, reservation_order_id, expand=None):
    '''
    Get details of a reservation.

    Required Parameters:
    - reservation_id -- Id of the Reservation Item
    - reservation_order_id -- Order Id of the reservation

    Optional Parameters:
    - expand -- Supported value of this query is renewProperties
    '''
    return _call_az("az reservations reservation show", locals())


def list_history(reservation_id, reservation_order_id):
    '''
    Get history of a reservation.

    Required Parameters:
    - reservation_id -- Id of the Reservation Item
    - reservation_order_id -- Order Id of the reservation
    '''
    return _call_az("az reservations reservation list-history", locals())


def update(applied_scope_type, reservation_id, reservation_order_id, applied_scopes=None, instance_flexibility=None):
    '''
    Updates the applied scopes of the reservation.

    Required Parameters:
    - applied_scope_type -- None
    - reservation_id -- None
    - reservation_order_id -- None

    Optional Parameters:
    - applied_scopes -- None
    - instance_flexibility -- None
    '''
    return _call_az("az reservations reservation update", locals())


def split(quantity_1, quantity_2, reservation_id, reservation_order_id):
    '''
    Split a reservation.

    Required Parameters:
    - quantity_1 -- None
    - quantity_2 -- None
    - reservation_id -- None
    - reservation_order_id -- None
    '''
    return _call_az("az reservations reservation split", locals())


def merge(reservation_id_1, reservation_id_2, reservation_order_id):
    '''
    Merge two reservations.

    Required Parameters:
    - reservation_id_1 -- None
    - reservation_id_2 -- None
    - reservation_order_id -- None
    '''
    return _call_az("az reservations reservation merge", locals())

