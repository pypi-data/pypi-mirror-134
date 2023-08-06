'''
See catalog of available reservations
'''
from ... pyaz_utils import _call_az

def show(reserved_resource_type, subscription_id, location=None):
    '''
    Get catalog of available reservation.

    Required Parameters:
    - reserved_resource_type -- The type of the resource for which the skus should be provided.
    - subscription_id -- Id of the subscription

    Optional Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    '''
    return _call_az("az reservations catalog show", locals())

