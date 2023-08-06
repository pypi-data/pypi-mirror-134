'''
Manage partner namespaces.
'''
from .... pyaz_utils import _call_az
from . import event_channel, key


def show(name, resource_group):
    '''
    Get the details of a partner namespace.

    Required Parameters:
    - name -- Name of the partner namespace.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventgrid partner namespace show", locals())


def delete(name, resource_group, yes=None):
    '''
    Delete a partner namespace.

    Required Parameters:
    - name -- Name of the partner namespace.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az eventgrid partner namespace delete", locals())


def list(odata_query=None, resource_group=None):
    '''
    List available partner namespaces.

    Optional Parameters:
    - odata_query -- The OData query used for filtering the list results. Filtering is currently allowed on the Name property only. The supported operations include: CONTAINS, eq (for equal), ne (for not equal), AND, OR and NOT.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventgrid partner namespace list", locals())


def create(name, partner_registration_id, resource_group, location=None, tags=None):
    '''
    Create a partner namespace.

    Required Parameters:
    - name -- Name of the partner namespace.
    - partner_registration_id -- The fully qualified ARM Id of the partner registration that should be associated with this partner namespace. This takes the following format: /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerRegistrations/{partnerRegistrationName}.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az eventgrid partner namespace create", locals())

