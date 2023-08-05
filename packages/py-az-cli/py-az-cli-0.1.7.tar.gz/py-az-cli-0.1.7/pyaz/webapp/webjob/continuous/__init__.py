'''
Allows management operations of continuous webjobs on a web app.
'''
from .... pyaz_utils import _call_az

def list(name, resource_group, slot=None):
    '''
    List all continuous webjobs on a selected web app.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp webjob continuous list", locals())


def remove(name, resource_group, webjob_name, slot=None):
    '''
    Delete a specific continuous webjob.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - webjob_name -- The name of the webjob

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp webjob continuous remove", locals())


def start(name, resource_group, webjob_name, slot=None):
    '''
    Start a specific continuous webjob on a selected web app.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - webjob_name -- The name of the webjob

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp webjob continuous start", locals())


def stop(name, resource_group, webjob_name, slot=None):
    '''
    Stop a specific continuous webjob.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - webjob_name -- The name of the webjob

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp webjob continuous stop", locals())

