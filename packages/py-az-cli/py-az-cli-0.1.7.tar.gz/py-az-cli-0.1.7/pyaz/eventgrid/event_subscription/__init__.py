from ... pyaz_utils import _call_az

def create(name, advanced_filter=None, azure_active_directory_application_id_or_uri=None, azure_active_directory_tenant_id=None, deadletter_endpoint=None, deadletter_identity=None, deadletter_identity_endpoint=None, delivery_attribute_mapping=None, delivery_identity=None, delivery_identity_endpoint=None, delivery_identity_endpoint_type=None, enable_advanced_filtering_on_arrays=None, endpoint=None, endpoint_type=None, event_delivery_schema=None, event_ttl=None, expiration_date=None, included_event_types=None, labels=None, max_delivery_attempts=None, max_events_per_batch=None, preferred_batch_size_in_kilobytes=None, source_resource_id=None, storage_queue_msg_ttl=None, subject_begins_with=None, subject_case_sensitive=None, subject_ends_with=None):
    '''
    Create a new event subscription.

    Required Parameters:
    - name -- Name of the event subscription.

    Optional Parameters:
    - advanced_filter -- None
    - azure_active_directory_application_id_or_uri -- The Azure Active Directory Application Id or Uri to get the access token that will be included as the bearer token in delivery requests. Applicable only for webhook as a destination
    - azure_active_directory_tenant_id -- The Azure Active Directory Tenant Id to get the access token that will be included as the bearer token in delivery requests. Applicable only for webhook as a destination
    - deadletter_endpoint -- The Azure resource ID of an Azure Storage blob container destination where EventGrid should deadletter undeliverable events for this event subscription.
    - deadletter_identity -- The identity type of the deadletter destination resource.
    - deadletter_identity_endpoint -- The Azure resource ID of an Azure Storage blob container destination with identity where EventGrid should deadletter undeliverable events for this event subscription.
    - delivery_attribute_mapping -- Add delivery attribute mapping to send additional information via HTTP headers when delivering events. This attribute is valid for all destination types except StorageQueue. Multiple attributes can be specified by using more than one `--delivery-attribute-mapping` argument
    - delivery_identity -- The identity type of the delivery destination resource (e.g., storage queue, or eventhub).
    - delivery_identity_endpoint -- Endpoint with identity where EventGrid should deliver events matching this event subscription. For webhook endpoint type, this should be the corresponding webhook URL. For other endpoint types, this should be the Azure resource identifier of the endpoint.
    - delivery_identity_endpoint_type -- None
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
    - source_resource_id -- Fully qualified identifier of the source Azure resource.
    - storage_queue_msg_ttl -- Storage queue message time to live in seconds.
    - subject_begins_with -- An optional string to filter events for an event subscription based on a prefix. Wildcard characters are not supported.
    - subject_case_sensitive -- Specify to indicate whether the subject fields should be compared in a case sensitive manner. True if flag present.
    - subject_ends_with -- An optional string to filter events for an event subscription based on a suffix. Wildcard characters are not supported.
    '''
    return _call_az("az eventgrid event-subscription create", locals())


def show(name, include_full_endpoint_url=None, include_static_delivery_attribute_secret=None, source_resource_id=None):
    '''
    Get the details of an event subscription.

    Required Parameters:
    - name -- Name of the event subscription.

    Optional Parameters:
    - include_full_endpoint_url -- Specify to indicate whether the full endpoint URL should be returned. True if flag present.
    - include_static_delivery_attribute_secret -- Indicate whether any static delivery attribute secrets should be returned. True if flag present.
    - source_resource_id -- Fully qualified identifier of the source Azure resource.
    '''
    return _call_az("az eventgrid event-subscription show", locals())


def delete(name, source_resource_id=None):
    '''
    Delete an event subscription.

    Required Parameters:
    - name -- Name of the event subscription.

    Optional Parameters:
    - source_resource_id -- Fully qualified identifier of the source Azure resource.
    '''
    return _call_az("az eventgrid event-subscription delete", locals())


def list(location=None, odata_query=None, resource_group=None, source_resource_id=None, topic_type_name=None):
    '''
    List event subscriptions.

    Optional Parameters:
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - odata_query -- The OData query used for filtering the list results. Filtering is currently allowed on the Name property only. The supported operations include: CONTAINS, eq (for equal), ne (for not equal), AND, OR and NOT.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - source_resource_id -- Fully qualified identifier of the source Azure resource.
    - topic_type_name -- Name of the topic type.
    '''
    return _call_az("az eventgrid event-subscription list", locals())


def update(name, add=None, advanced_filter=None, deadletter_endpoint=None, deadletter_identity=None, deadletter_identity_endpoint=None, delivery_attribute_mapping=None, delivery_identity=None, delivery_identity_endpoint=None, delivery_identity_endpoint_type=None, enable_advanced_filtering_on_arrays=None, endpoint=None, endpoint_type=None, force_string=None, included_event_types=None, labels=None, remove=None, set=None, source_resource_id=None, storage_queue_msg_ttl=None, subject_begins_with=None, subject_ends_with=None):
    '''
    Update an event subscription.

    Required Parameters:
    - name -- Name of the event subscription.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - advanced_filter -- None
    - deadletter_endpoint -- The Azure resource ID of an Azure Storage blob container destination where EventGrid should deadletter undeliverable events for this event subscription.
    - deadletter_identity -- The identity type of the deadletter destination resource.
    - deadletter_identity_endpoint -- The Azure resource ID of an Azure Storage blob container destination with identity where EventGrid should deadletter undeliverable events for this event subscription.
    - delivery_attribute_mapping -- Add delivery attribute mapping to send additional information via HTTP headers when delivering events. This attribute is valid for all destination types except StorageQueue. Multiple attributes can be specified by using more than one `--delivery-attribute-mapping` argument
    - delivery_identity -- The identity type of the delivery destination resource (e.g., storage queue, or eventhub).
    - delivery_identity_endpoint -- Endpoint with identity where EventGrid should deliver events matching this event subscription. For webhook endpoint type, this should be the corresponding webhook URL. For other endpoint types, this should be the Azure resource identifier of the endpoint.
    - delivery_identity_endpoint_type -- None
    - enable_advanced_filtering_on_arrays -- Allows advanced filters to be evaluated against an array of values instead of expecting a singular value.
    - endpoint -- Endpoint where EventGrid should deliver events matching this event subscription. For webhook endpoint type, this should be the corresponding webhook URL. For other endpoint types, this should be the Azure resource identifier of the endpoint. It is expected that the destination endpoint to be already created and available for use before executing any Event Grid command.
    - endpoint_type -- None
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - included_event_types -- A space-separated list of event types (e.g., Microsoft.Storage.BlobCreated and Microsoft.Storage.BlobDeleted). In order to subscribe to all default event types, do not specify any value for this argument. For event grid topics, event types are customer defined. For Azure events, e.g., Storage Accounts, IoT Hub, etc., you can query their event types using this CLI command 'az eventgrid topic-type list-event-types'.
    - labels -- A space-separated list of labels to associate with this event subscription.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - source_resource_id -- Fully qualified identifier of the source Azure resource.
    - storage_queue_msg_ttl -- Storage queue message time to live in seconds.
    - subject_begins_with -- An optional string to filter events for an event subscription based on a prefix. Wildcard characters are not supported.
    - subject_ends_with -- An optional string to filter events for an event subscription based on a suffix. Wildcard characters are not supported.
    '''
    return _call_az("az eventgrid event-subscription update", locals())

