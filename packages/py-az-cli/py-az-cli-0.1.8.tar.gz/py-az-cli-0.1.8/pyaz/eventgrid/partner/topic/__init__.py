'''
Manage partner topics.
'''
from .... pyaz_utils import _call_az
from . import event_subscription


def show(name, resource_group):
    '''
    Get the details of a partner topic.

    Required Parameters:
    - name -- Name of the partner topic.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventgrid partner topic show", locals())


def delete(name, resource_group, yes=None):
    '''
    Delete a partner topic.

    Required Parameters:
    - name -- Name of the partner topic.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az eventgrid partner topic delete", locals())


def activate(name, resource_group):
    '''
    Activate a partner topic.

    Required Parameters:
    - name -- Name of the partner topic.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventgrid partner topic activate", locals())


def deactivate(name, resource_group):
    '''
    Deactivate a partner topic.

    Required Parameters:
    - name -- Name of the partner topic.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventgrid partner topic deactivate", locals())


def list(odata_query=None, resource_group=None):
    '''
    List available partner topics.

    Optional Parameters:
    - odata_query -- The OData query used for filtering the list results. Filtering is currently allowed on the Name property only. The supported operations include: CONTAINS, eq (for equal), ne (for not equal), AND, OR and NOT.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventgrid partner topic list", locals())

