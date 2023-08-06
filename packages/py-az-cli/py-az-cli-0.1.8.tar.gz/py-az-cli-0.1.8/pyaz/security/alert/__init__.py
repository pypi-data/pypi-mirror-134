'''
View security alerts.
'''
from ... pyaz_utils import _call_az

def list(location=None, resource_group=None):
    '''
    List security alerts.

    Optional Parameters:
    - location -- location of the resource
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az security alert list", locals())


def show(location, name, resource_group=None):
    '''
    Shows a security alert.

    Required Parameters:
    - location -- location of the resource
    - name -- name of the resource to be fetched

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az security alert show", locals())


def update(location, name, status, resource_group=None):
    '''
    Updates a security alert status.

    Required Parameters:
    - location -- location of the resource
    - name -- name of the resource to be fetched
    - status -- target status of the alert. possible values are "dismiss" and "activate"

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az security alert update", locals())

