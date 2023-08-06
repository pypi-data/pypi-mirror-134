'''
Manage container-based continuous deployment.
'''
from .... pyaz_utils import _call_az

def config(enable_cd, name, resource_group, slot=None):
    '''
    Configure continuous deployment via containers.

    Required Parameters:
    - enable_cd -- enable/disable continuous deployment
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp deployment container config", locals())


def show_cd_url(name, resource_group, slot=None):
    '''
    Get the URL which can be used to configure webhooks for continuous deployment.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp deployment container show-cd-url", locals())

