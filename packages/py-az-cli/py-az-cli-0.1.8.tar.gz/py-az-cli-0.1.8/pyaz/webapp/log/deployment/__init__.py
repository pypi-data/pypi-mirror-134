'''
Manage web app deployment logs.
'''
from .... pyaz_utils import _call_az

def show(name, resource_group, deployment_id=None, slot=None):
    '''
    Show deployment logs of the latest deployment, or a specific deployment if deployment-id is specified.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - deployment_id -- Deployment ID. If none specified, returns the deployment logs of the latest deployment.
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp log deployment show", locals())


def list(name, resource_group, slot=None):
    '''
    List deployments associated with web app

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp log deployment list", locals())

