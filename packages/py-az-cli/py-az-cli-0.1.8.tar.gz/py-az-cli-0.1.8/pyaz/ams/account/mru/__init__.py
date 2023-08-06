'''
Manage media reserved units for an Azure Media Services account. This doesn't work with accounts created with 2020-05-01 version of the Media Services API or later. Accounts created this way no longer need to set media reserved units as the system will automaticaly scale up and down based on load.
'''
from .... pyaz_utils import _call_az

def show(name, resource_group):
    '''
    Show the details of media reserved units for an Azure Media Services account. This doesn't work with accounts created with 2020-05-01 version of the Media Services API or later. Accounts created this way no longer need to set media reserved units as the system will automaticaly scale up and down based on load.

    Required Parameters:
    - name -- The name of the Azure Media Services account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams account mru show", locals())


def set(name, resource_group, count=None, type=None):
    '''
    Set the type and number of media reserved units for an Azure Media Services account. This doesn't work with accounts created with 2020-05-01 version of the Media Services API or later. Accounts created this way no longer need to set media reserved units as the system will automaticaly scale up and down based on load.

    Required Parameters:
    - name -- The name of the Azure Media Services account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - count -- The number of the encoding reserved units that you want to be provisioned for this account for concurrent tasks (one unit equals one task).
    - type -- Speed of reserved processing units. The cost of media encoding depends on the pricing tier you choose. See https://azure.microsoft.com/pricing/details/media-services/ for further details. Allowed values: S1, S2, S3.
    '''
    return _call_az("az ams account mru set", locals())

