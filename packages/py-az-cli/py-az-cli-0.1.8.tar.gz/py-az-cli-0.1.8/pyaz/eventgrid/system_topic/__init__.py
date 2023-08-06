from ... pyaz_utils import _call_az
from . import event_subscription


def show(name, resource_group):
    '''
    Get the details of a system topic.

    Required Parameters:
    - name -- Name of the system topic.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventgrid system-topic show", locals())


def delete(name, resource_group, yes=None):
    '''
    Delete a system topic.

    Required Parameters:
    - name -- Name of the system topic.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az eventgrid system-topic delete", locals())


def list(odata_query=None, resource_group=None):
    '''
    List available system topics.

    Optional Parameters:
    - odata_query -- The OData query used for filtering the list results. Filtering is currently allowed on the Name property only. The supported operations include: CONTAINS, eq (for equal), ne (for not equal), AND, OR and NOT.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventgrid system-topic list", locals())


def create(name, resource_group, source, topic_type, identity=None, location=None, tags=None):
    '''
    Create a system topic.

    Required Parameters:
    - name -- Name of the system topic.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - source -- The ARM Id for the topic, e.g., /subscriptions/{SubId}/resourceGroups/{RgName}/providers/Microsoft.Storage/storageAccounts/{AccountName}
    - topic_type -- Name of the topic type.

    Optional Parameters:
    - identity -- The managed identity type for the resource.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az eventgrid system-topic create", locals())


def update(name, resource_group, identity=None, tags=None):
    '''
    Update a system topic.

    Required Parameters:
    - name -- Name of the system topic.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - identity -- The managed identity type for the resource.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az eventgrid system-topic update", locals())

