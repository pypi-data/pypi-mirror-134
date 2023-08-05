'''
Manage Azure Cognitive Services accounts.
'''
from .. pyaz_utils import _call_az
from . import account, commitment_tier


def list(resource_group=None):
    '''
    Manage Azure Cognitive Services accounts.

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cognitiveservices list", locals())

