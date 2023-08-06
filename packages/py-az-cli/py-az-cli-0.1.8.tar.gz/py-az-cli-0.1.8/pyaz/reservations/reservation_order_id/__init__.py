from ... pyaz_utils import _call_az

def list(subscription_id):
    '''
    Get list of applicable reservation order ids.

    Required Parameters:
    - subscription_id -- Id of the subscription
    '''
    return _call_az("az reservations reservation-order-id list", locals())

