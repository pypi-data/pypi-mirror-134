'''
Manage deployment token for the static app
'''
from ... pyaz_utils import _call_az

def list(name, resource_group=None):
    '''
    List the deployment token for the static app.

    Required Parameters:
    - name -- Name of the static site

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az staticwebapp secrets list", locals())


def reset_api_key(name, no_wait=None, resource_group=None):
    '''
    Reset the deployment token for the static app.

    Required Parameters:
    - name -- Name of the static site

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az staticwebapp secrets reset-api-key", locals())

