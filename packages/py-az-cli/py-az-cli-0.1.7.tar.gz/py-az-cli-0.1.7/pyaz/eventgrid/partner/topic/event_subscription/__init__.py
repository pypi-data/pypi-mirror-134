from ..... pyaz_utils import _call_az

def show(name, partner_topic_name, resource_group, include_full_endpoint_url=None, include_static_delivery_attribute_secret=None):
    '''
    Get the details of an event subscription of a partner topic.

    Required Parameters:
    - name -- Name of the event subscription.
    - partner_topic_name -- Name of the partner topic.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - include_full_endpoint_url -- Specify to indicate whether the full endpoint URL should be returned. True if flag present.
    - include_static_delivery_attribute_secret -- Indicate whether any static delivery attribute secrets should be returned. True if flag present.
    '''
    return _call_az("az eventgrid partner topic event-subscription show", locals())


def delete(name, partner_topic_name, resource_group, yes=None):
    '''
    Delete an event subscription of a partner topic

    Required Parameters:
    - name -- Name of the event subscription.
    - partner_topic_name -- Name of the partner topic.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az eventgrid partner topic event-subscription delete", locals())


def list(partner_topic_name, resource_group, odata_query=None):
    '''
    List event subscriptions of a specific partner topic.

    Required Parameters:
    - partner_topic_name -- Name of the partner topic.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - odata_query -- The OData query used for filtering the list results. Filtering is currently allowed on the Name property only. The supported operations include: CONTAINS, eq (for equal), ne (for not equal), AND, OR and NOT.
    '''
    return _call_az("az eventgrid partner topic event-subscription list", locals())


def create(name, partner_topic_name, resource_group, advanced_filter=None, azure_active_directory_application_id_or_uri=None, azure_active_directory_tenant_id=None, deadletter_endpoint=None, delivery_attribute_mapping=None, enable_advanced_filtering_on_arrays=None, endpoint=None, endpoint_type=None, event_delivery_schema=None, event_ttl=None, expiration_date=None, included_event_types=None, labels=None, max_delivery_attempts=None, max_events_per_batch=None, preferred_batch_size_in_kilobytes=None, storage_queue_msg_ttl=None, subject_begins_with=None, subject_case_sensitive=None, subject_ends_with=None):
    '''
    Create a new event subscription for a partner topic

    Required Parameters:
    - name -- Name of the event subscription.
    - partner_topic_name -- Name of the partner topic.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - advanced_filter -- None
    - azure_active_directory_application_id_or_uri -- The Azure Active Directory Application Id or Uri to get the access token that will be included as the bearer token in delivery requests. Applicable only for webhook as a destination
    - azure_active_directory_tenant_id -- The Azure Active Directory Tenant Id to get the access token that will be included as the bearer token in delivery requests. Applicable only for webhook as a destination
    - deadletter_endpoint -- The Azure resource ID of an Azure Storage blob container destination where EventGrid should deadletter undeliverable events for this event subscription.
    - delivery_attribute_mapping -- Add delivery attribute mapping to send additional information via HTTP headers when delivering events. This attribute is valid for all destination types except StorageQueue. Multiple attributes can be specified by using more than one `--delivery-attribute-mapping` argument
    - enable_advanced_filtering_on_arrays -- Allows advanced filters to be evaluated against an array of values instead of expecting a singular value.
    - endpoint -- Endpoint where EventGrid should deliver events matching this event subscription. For webhook endpoint type, this should be the corresponding webhook URL. For other endpoint types, this should be the Azure resource identifier of the endpoint. It is expected that the destination endpoint to be already created and available for use before executing any Event Grid command.
    - endpoint_type -- None
    - event_delivery_schema -- The schema in which events should be delivered for this event subscription. By default, events will be delivered in the same schema in which they are published (based on the corresponding topic's input schema).
    - event_ttl -- Event time to live (in minutes). Must be a number between 1 and 1440.
    - expiration_date -- Date or datetime (in UTC, e.g. '2018-11-30T11:59:59+00:00' or '2018-11-30') after which the event subscription would expire. By default, there is no expiration for the event subscription.
    - included_event_types -- A space-separated list of event types (e.g., Microsoft.Storage.BlobCreated and Microsoft.Storage.BlobDeleted). In order to subscribe to all default event types, do not specify any value for this argument. For event grid topics, event types are customer defined. For Azure events, e.g., Storage Accounts, IoT Hub, etc., you can query their event types using this CLI command 'az eventgrid topic-type list-event-types'.
    - labels -- A space-separated list of labels to associate with this event subscription.
    - max_delivery_attempts -- Maximum number of delivery attempts. Must be a number between 1 and 30.
    - max_events_per_batch -- Maximum number of events in a batch. Must be a number between 1 and 5000.
    - preferred_batch_size_in_kilobytes -- Preferred batch size in kilobytes. Must be a number between 1 and 1024.
    - storage_queue_msg_ttl -- Storage queue message time to live in seconds.
    - subject_begins_with -- An optional string to filter events for an event subscription based on a prefix. Wildcard characters are not supported.
    - subject_case_sensitive -- Specify to indicate whether the subject fields should be compared in a case sensitive manner. True if flag present.
    - subject_ends_with -- An optional string to filter events for an event subscription based on a suffix. Wildcard characters are not supported.
    '''
    return _call_az("az eventgrid partner topic event-subscription create", locals())


def update(name, partner_topic_name, resource_group, advanced_filter=None, deadletter_endpoint=None, delivery_attribute_mapping=None, enable_advanced_filtering_on_arrays=None, endpoint=None, endpoint_type=None, included_event_types=None, labels=None, storage_queue_msg_ttl=None, subject_begins_with=None, subject_ends_with=None):
    '''
    Update an event subscription of a partner topic.

    Required Parameters:
    - name -- Name of the event subscription.
    - partner_topic_name -- Name of the partner topic.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - advanced_filter -- None
    - deadletter_endpoint -- The Azure resource ID of an Azure Storage blob container destination where EventGrid should deadletter undeliverable events for this event subscription.
    - delivery_attribute_mapping -- Add delivery attribute mapping to send additional information via HTTP headers when delivering events. This attribute is valid for all destination types except StorageQueue. Multiple attributes can be specified by using more than one `--delivery-attribute-mapping` argument
    - enable_advanced_filtering_on_arrays -- Allows advanced filters to be evaluated against an array of values instead of expecting a singular value.
    - endpoint -- Endpoint where EventGrid should deliver events matching this event subscription. For webhook endpoint type, this should be the corresponding webhook URL. For other endpoint types, this should be the Azure resource identifier of the endpoint. It is expected that the destination endpoint to be already created and available for use before executing any Event Grid command.
    - endpoint_type -- None
    - included_event_types -- A space-separated list of event types (e.g., Microsoft.Storage.BlobCreated and Microsoft.Storage.BlobDeleted). In order to subscribe to all default event types, do not specify any value for this argument. For event grid topics, event types are customer defined. For Azure events, e.g., Storage Accounts, IoT Hub, etc., you can query their event types using this CLI command 'az eventgrid topic-type list-event-types'.
    - labels -- A space-separated list of labels to associate with this event subscription.
    - storage_queue_msg_ttl -- Storage queue message time to live in seconds.
    - subject_begins_with -- An optional string to filter events for an event subscription based on a prefix. Wildcard characters are not supported.
    - subject_ends_with -- An optional string to filter events for an event subscription based on a suffix. Wildcard characters are not supported.
    '''
    return _call_az("az eventgrid partner topic event-subscription update", locals())

