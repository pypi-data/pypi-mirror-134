from ... pyaz_utils import _call_az
from . import policy, policy_definition


def list(location):
    '''
    

    Required Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    '''
    return _call_az("az network service-endpoint list", locals())

