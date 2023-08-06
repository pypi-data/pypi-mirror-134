'''
Allows management operations of triggered webjobs on a web app.
'''
from .... pyaz_utils import _call_az

def list(name, resource_group, slot=None):
    '''
    List all triggered webjobs hosted on a web app.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp webjob triggered list", locals())


def remove(name, resource_group, webjob_name, slot=None):
    '''
    Delete a specific triggered webjob hosted on a web app.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - webjob_name -- The name of the webjob

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp webjob triggered remove", locals())


def run(name, resource_group, webjob_name, slot=None):
    '''
    Run a specific triggered webjob hosted on a web app.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - webjob_name -- The name of the webjob

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp webjob triggered run", locals())


def log(name, resource_group, webjob_name, slot=None):
    '''
    Get history of a specific triggered webjob hosted on a web app.

    Required Parameters:
    - name -- name of the web app. If left unspecified, a name will be randomly generated. You can configure the default using `az configure --defaults web=<name>`
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - webjob_name -- The name of the webjob

    Optional Parameters:
    - slot -- the name of the slot. Default to the productions slot if not specified
    '''
    return _call_az("az webapp webjob triggered log", locals())

