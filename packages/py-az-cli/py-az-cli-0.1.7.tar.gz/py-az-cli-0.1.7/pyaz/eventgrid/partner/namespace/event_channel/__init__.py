from ..... pyaz_utils import _call_az

def show(name, partner_namespace_name, resource_group):
    '''
    Get the details of an event channel under a partner namespace.

    Required Parameters:
    - name -- Name of the event channel.
    - partner_namespace_name -- Name of the partner namespace.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventgrid partner namespace event-channel show", locals())


def delete(name, partner_namespace_name, resource_group, yes=None):
    '''
    Delete a partner namespace.

    Required Parameters:
    - name -- Name of the event channel.
    - partner_namespace_name -- Name of the partner namespace.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az eventgrid partner namespace event-channel delete", locals())


def list(partner_namespace_name, resource_group, odata_query=None):
    '''
    List available partner event-channels.

    Required Parameters:
    - partner_namespace_name -- Name of the partner namespace.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - odata_query -- The OData query used for filtering the list results. Filtering is currently allowed on the Name property only. The supported operations include: CONTAINS, eq (for equal), ne (for not equal), AND, OR and NOT.
    '''
    return _call_az("az eventgrid partner namespace event-channel list", locals())


def create(destination_resource_group_name, destination_subscription_id, destination_topic_name, name, partner_namespace_name, resource_group, source, activation_expiration_date=None, partner_topic_description=None, publisher_filter=None):
    '''
    Create an event channel under a partner namespace.

    Required Parameters:
    - destination_resource_group_name -- Azure Resource Group of the customer creating the event channel. The partner topic associated with the event channel will be created under this resource group.
    - destination_subscription_id -- Azure subscription Id of the customer creating the event channel. The partner topic associated with the event channel will be created under this Azure subscription.
    - destination_topic_name -- Name of the partner topic associated with the event channel.
    - name -- Name of the event channel.
    - partner_namespace_name -- Name of the partner namespace.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - source -- The identifier of the resource that forms the partner source of the events. This represents a unique resource in the partner's resource model.

    Optional Parameters:
    - activation_expiration_date -- Date or datetime in UTC ISO 8601 format (e.g., '2022-02-17T01:59:59+00:00' or '2022-02-17') after which the event channel and corresponding partner topic would expire and get auto deleted. If this time is not specified, the expiration date is set to seven days by default.
    - partner_topic_description -- Friendly description of the corresponding partner topic. This will be helpful to remove any ambiguity of the origin of creation of the partner topic for the customer.
    - publisher_filter -- None
    '''
    return _call_az("az eventgrid partner namespace event-channel create", locals())

