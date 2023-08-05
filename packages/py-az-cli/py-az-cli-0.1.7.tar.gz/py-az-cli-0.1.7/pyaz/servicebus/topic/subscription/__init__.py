'''
Manage Azure Service Bus Subscription
'''
from .... pyaz_utils import _call_az
from . import rule


def create(name, namespace_name, resource_group, topic_name, auto_delete_on_idle=None, dead_letter_on_filter_exceptions=None, default_message_time_to_live=None, enable_batched_operations=None, enable_dead_lettering_on_message_expiration=None, enable_session=None, forward_dead_lettered_messages_to=None, forward_to=None, lock_duration=None, max_delivery_count=None, status=None):
    '''
    Create the ServiceBus Subscription

    Required Parameters:
    - name -- Name of Subscription
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - topic_name -- Name of Topic

    Optional Parameters:
    - auto_delete_on_idle -- ISO 8601 timeSpan  or duration time format for idle interval after which the topic is automatically deleted. The minimum duration is 5 minutes.
    - dead_letter_on_filter_exceptions -- Allow dead lettering when filter evaluation exceptions occur.
    - default_message_time_to_live -- ISO 8601 or duration time format for Default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.
    - enable_batched_operations -- Allow server-side batched operations.
    - enable_dead_lettering_on_message_expiration -- A boolean Value that indicates whether a subscription has dead letter support when a message expires.
    - enable_session -- A boolean value indicating if a subscription supports the concept of sessions.
    - forward_dead_lettered_messages_to -- Queue/Topic name to forward the Dead Letter message
    - forward_to -- Queue/Topic name to forward the messages
    - lock_duration -- ISO 8601 or duration format (day:minute:seconds) for lock duration timespan for the subscription. The default value is 1 minute.
    - max_delivery_count -- Number of maximum deliveries.
    - status -- Enumerates the possible values for the status of a messaging entity.
    '''
    return _call_az("az servicebus topic subscription create", locals())


def show(name, namespace_name, resource_group, topic_name):
    '''
    Shows Service Bus Subscription Details

    Required Parameters:
    - name -- Name of Subscription
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - topic_name -- Name of Topic
    '''
    return _call_az("az servicebus topic subscription show", locals())


def list(namespace_name, resource_group, topic_name, skip=None, top=None):
    '''
    List the Subscription by Service Bus Topic

    Required Parameters:
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - topic_name -- Name of Topic

    Optional Parameters:
    - skip -- Skip is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skip parameter that specifies a starting point to use for subsequent calls.
    - top -- May be used to limit the number of results to the most recent N usageDetails.
    '''
    return _call_az("az servicebus topic subscription list", locals())


def delete(name, namespace_name, resource_group, topic_name):
    '''
    Deletes the Service Bus Subscription

    Required Parameters:
    - name -- Name of Subscription
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - topic_name -- Name of Topic
    '''
    return _call_az("az servicebus topic subscription delete", locals())


def update(name, namespace_name, resource_group, topic_name, add=None, auto_delete_on_idle=None, dead_letter_on_filter_exceptions=None, default_message_time_to_live=None, enable_batched_operations=None, enable_dead_lettering_on_message_expiration=None, enable_session=None, force_string=None, forward_dead_lettered_messages_to=None, forward_to=None, lock_duration=None, max_delivery_count=None, remove=None, set=None, status=None):
    '''
    Updates the ServiceBus Subscription

    Required Parameters:
    - name -- Name of Subscription
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - topic_name -- Name of Topic

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - auto_delete_on_idle -- ISO 8601 timeSpan  or duration time format for idle interval after which the topic is automatically deleted. The minimum duration is 5 minutes.
    - dead_letter_on_filter_exceptions -- Allow dead lettering when filter evaluation exceptions occur.
    - default_message_time_to_live -- ISO 8601 or duration time format for Default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.
    - enable_batched_operations -- Allow server-side batched operations.
    - enable_dead_lettering_on_message_expiration -- A boolean Value that indicates whether a subscription has dead letter support when a message expires.
    - enable_session -- A boolean value indicating if a subscription supports the concept of sessions.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - forward_dead_lettered_messages_to -- Queue/Topic name to forward the Dead Letter message
    - forward_to -- Queue/Topic name to forward the messages
    - lock_duration -- ISO 8601 or duration format (day:minute:seconds) for lock duration timespan for the subscription. The default value is 1 minute.
    - max_delivery_count -- Number of maximum deliveries.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - status -- Enumerates the possible values for the status of a messaging entity.
    '''
    return _call_az("az servicebus topic subscription update", locals())

