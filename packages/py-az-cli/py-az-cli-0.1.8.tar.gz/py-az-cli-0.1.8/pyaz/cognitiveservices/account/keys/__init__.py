'''
Manage Azure Cognitive Services accounts.
'''
from .... pyaz_utils import _call_az

def regenerate(key_name, name, resource_group):
    '''
    Manage Azure Cognitive Services accounts.

    Required Parameters:
    - key_name -- Key name to generate
    - name -- cognitive service account name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cognitiveservices account keys regenerate", locals())


def list(name, resource_group):
    '''
    Manage Azure Cognitive Services accounts.

    Required Parameters:
    - name -- cognitive service account name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cognitiveservices account keys list", locals())

