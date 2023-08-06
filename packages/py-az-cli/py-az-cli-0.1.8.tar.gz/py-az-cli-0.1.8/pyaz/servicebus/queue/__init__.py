'''
Manage Azure Service Bus Queue and Authorization Rule
'''
from ... pyaz_utils import _call_az
from . import authorization_rule


def create(name, namespace_name, resource_group, auto_delete_on_idle=None, default_message_time_to_live=None, duplicate_detection_history_time_window=None, enable_batched_operations=None, enable_dead_lettering_on_message_expiration=None, enable_duplicate_detection=None, enable_express=None, enable_partitioning=None, enable_session=None, forward_dead_lettered_messages_to=None, forward_to=None, lock_duration=None, max_delivery_count=None, max_size=None, status=None):
    '''
    Create the Service Bus Queue

    Required Parameters:
    - name -- Name of Queue
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - auto_delete_on_idle -- ISO 8601 timeSpan or duration time format for idle interval after which the queue is automatically deleted. The minimum duration is 5 minutes.
    - default_message_time_to_live -- ISO 8601 timespan or duration time format for default message to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.
    - duplicate_detection_history_time_window -- ISO 8601 timeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes.
    - enable_batched_operations -- Allow server-side batched operations.
    - enable_dead_lettering_on_message_expiration -- A boolean value that indicates whether this queue has dead letter support when a message expires.
    - enable_duplicate_detection -- A boolean value indicating if this queue requires duplicate detection.
    - enable_express -- A boolean value that indicates whether Express Entities are enabled. An express queue holds a message in memory temporarily before writing it to persistent storage.
    - enable_partitioning -- A boolean value that indicates whether the queue is to be partitioned across multiple message brokers.
    - enable_session -- A boolean value indicating whether the queue supports the concept of sessions.
    - forward_dead_lettered_messages_to -- Queue/Topic name to forward the Dead Letter message
    - forward_to -- Queue/Topic name to forward the messages
    - lock_duration -- String ISO 8601 timespan or duration format for duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. The maximum value for LockDuration is 5 minutes; the default value is 1 minute.
    - max_delivery_count -- The maximum delivery count. A message is automatically deadlettered after this number of deliveries. default value is 10.
    - max_size -- Maximum size of queue in megabytes, which is the size of the memory allocated for the queue. Default is 1024. Max for Standard SKU is 5120 and for Premium SKU is 81920
    - status -- Enumerates the possible values for the status of a messaging entity.
    '''
    return _call_az("az servicebus queue create", locals())


def show(name, namespace_name, resource_group):
    '''
    shows the Service Bus Queue Details

    Required Parameters:
    - name -- Name of Queue
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az servicebus queue show", locals())


def list(namespace_name, resource_group, skip=None, top=None):
    '''
    List the Queue by Service Bus Namespace

    Required Parameters:
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - skip -- Skip is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skip parameter that specifies a starting point to use for subsequent calls.
    - top -- May be used to limit the number of results to the most recent N usageDetails.
    '''
    return _call_az("az servicebus queue list", locals())


def delete(name, namespace_name, resource_group):
    '''
    Deletes the Service Bus Queue

    Required Parameters:
    - name -- Name of Queue
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az servicebus queue delete", locals())


def update(name, namespace_name, resource_group, add=None, auto_delete_on_idle=None, default_message_time_to_live=None, duplicate_detection_history_time_window=None, enable_batched_operations=None, enable_dead_lettering_on_message_expiration=None, enable_duplicate_detection=None, enable_express=None, enable_partitioning=None, enable_session=None, force_string=None, forward_dead_lettered_messages_to=None, forward_to=None, lock_duration=None, max_delivery_count=None, max_size=None, remove=None, set=None, status=None):
    '''
    Updates existing Service Bus Queue

    Required Parameters:
    - name -- Name of Queue
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - auto_delete_on_idle -- ISO 8601 timeSpan or duration time format for idle interval after which the queue is automatically deleted. The minimum duration is 5 minutes.
    - default_message_time_to_live -- ISO 8601 timespan or duration time format for default message to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.
    - duplicate_detection_history_time_window -- ISO 8601 timeSpan structure that defines the duration of the duplicate detection history. The default value is 10 minutes.
    - enable_batched_operations -- Allow server-side batched operations.
    - enable_dead_lettering_on_message_expiration -- A boolean value that indicates whether this queue has dead letter support when a message expires.
    - enable_duplicate_detection -- A boolean value indicating if this queue requires duplicate detection.
    - enable_express -- A boolean value that indicates whether Express Entities are enabled. An express queue holds a message in memory temporarily before writing it to persistent storage.
    - enable_partitioning -- A boolean value that indicates whether the queue is to be partitioned across multiple message brokers.
    - enable_session -- A boolean value indicating whether the queue supports the concept of sessions.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - forward_dead_lettered_messages_to -- Queue/Topic name to forward the Dead Letter message
    - forward_to -- Queue/Topic name to forward the messages
    - lock_duration -- String ISO 8601 timespan or duration format for duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. The maximum value for LockDuration is 5 minutes; the default value is 1 minute.
    - max_delivery_count -- The maximum delivery count. A message is automatically deadlettered after this number of deliveries. default value is 10.
    - max_size -- Maximum size of queue in megabytes, which is the size of the memory allocated for the queue. Default is 1024. Max for Standard SKU is 5120 and for Premium SKU is 81920
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - status -- Enumerates the possible values for the status of a messaging entity.
    '''
    return _call_az("az servicebus queue update", locals())

