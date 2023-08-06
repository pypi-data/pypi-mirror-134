'''
Manage deployments for Azure Cognitive Services accounts.
'''
from .... pyaz_utils import _call_az

def create(model_format, model_name, model_version, name, resource_group, scale_capacity, scale_type, deployment_name=None):
    '''
    Create a deployment for Azure Cognitive Services account.

    Required Parameters:
    - model_format -- Cognitive Services account deployment model format.
    - model_name -- Cognitive Services account deployment model name.
    - model_version -- Cognitive Services account deployment model version.
    - name -- cognitive service account name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - scale_capacity -- Cognitive Services account deployment scale settings capacity.
    - scale_type -- Cognitive Services account deployment scale settings scale type.

    Optional Parameters:
    - deployment_name -- Cognitive Services account deployment name
    '''
    return _call_az("az cognitiveservices account deployment create", locals())


def delete(name, resource_group, deployment_name=None):
    '''
    Delete a deployment from Azure Cognitive Services account.

    Required Parameters:
    - name -- cognitive service account name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - deployment_name -- Cognitive Services account deployment name
    '''
    return _call_az("az cognitiveservices account deployment delete", locals())


def show(name, resource_group, deployment_name=None):
    '''
    Show a deployment for Azure Cognitive Services account.

    Required Parameters:
    - name -- cognitive service account name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - deployment_name -- Cognitive Services account deployment name
    '''
    return _call_az("az cognitiveservices account deployment show", locals())


def list(name, resource_group):
    '''
    Show all deployments for Azure Cognitive Services account.

    Required Parameters:
    - name -- cognitive service account name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cognitiveservices account deployment list", locals())

