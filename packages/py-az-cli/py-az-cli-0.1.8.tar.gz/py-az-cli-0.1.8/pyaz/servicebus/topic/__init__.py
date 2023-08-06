'''
Manage Azure Service Bus Topic and Authorization Rule
'''
from ... pyaz_utils import _call_az
from . import authorization_rule, subscription


def create(name, namespace_name, resource_group, auto_delete_on_idle=None, default_message_time_to_live=None, duplicate_detection_history_time_window=None, enable_batched_operations=None, enable_duplicate_detection=None, enable_express=None, enable_ordering=None, enable_partitioning=None, max_size=None, status=None):
    '''
    Create the Service Bus Topic

    Required Parameters:
    - name -- Name of Topic
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - auto_delete_on_idle -- ISO 8601 timespan or duration time format for idle interval after which the topic is automatically deleted. The minimum duration is 5 minutes.
    - default_message_time_to_live -- ISO 8601 or duration time format for Default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.
    - duplicate_detection_history_time_window -- ISO 8601 timespan or duration time format for structure that defines the duration of the duplicate detection history. The default value is 10 minutes.
    - enable_batched_operations -- Allow server-side batched operations.
    - enable_duplicate_detection -- A boolean value indicating if this topic requires duplicate detection.
    - enable_express -- A boolean value that indicates whether Express Entities are enabled. An express topic holds a message in memory temporarily before writing it to persistent storage.
    - enable_ordering -- A boolean value that indicates whether the topic supports ordering.
    - enable_partitioning -- A boolean value that indicates whether the topic to be partitioned across multiple message brokers is enabled.
    - max_size -- Maximum size of topic in megabytes, which is the size of the memory allocated for the topic. Default is 1024. Max for Standard SKU is 5120 and for Premium SKU is 81920
    - status -- Enumerates the possible values for the status of a messaging entity.
    '''
    return _call_az("az servicebus topic create", locals())


def show(name, namespace_name, resource_group):
    '''
    Shows the Service Bus Topic Details

    Required Parameters:
    - name -- Name of Topic
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az servicebus topic show", locals())


def list(namespace_name, resource_group, skip=None, top=None):
    '''
    List the Topic by Service Bus Namespace

    Required Parameters:
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - skip -- Skip is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skip parameter that specifies a starting point to use for subsequent calls.
    - top -- May be used to limit the number of results to the most recent N usageDetails.
    '''
    return _call_az("az servicebus topic list", locals())


def delete(name, namespace_name, resource_group):
    '''
    Deletes the Service Bus Topic

    Required Parameters:
    - name -- Name of Topic
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az servicebus topic delete", locals())


def update(name, namespace_name, resource_group, add=None, auto_delete_on_idle=None, default_message_time_to_live=None, duplicate_detection_history_time_window=None, enable_batched_operations=None, enable_duplicate_detection=None, enable_express=None, enable_ordering=None, enable_partitioning=None, force_string=None, max_size=None, remove=None, set=None, status=None):
    '''
    Updates the Service Bus Topic

    Required Parameters:
    - name -- Name of Topic
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - auto_delete_on_idle -- ISO 8601 timespan or duration time format for idle interval after which the topic is automatically deleted. The minimum duration is 5 minutes.
    - default_message_time_to_live -- ISO 8601 or duration time format for Default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.
    - duplicate_detection_history_time_window -- ISO 8601 timespan or duration time format for structure that defines the duration of the duplicate detection history. The default value is 10 minutes.
    - enable_batched_operations -- Allow server-side batched operations.
    - enable_duplicate_detection -- A boolean value indicating if this topic requires duplicate detection.
    - enable_express -- A boolean value that indicates whether Express Entities are enabled. An express topic holds a message in memory temporarily before writing it to persistent storage.
    - enable_ordering -- A boolean value that indicates whether the topic supports ordering.
    - enable_partitioning -- A boolean value that indicates whether the topic to be partitioned across multiple message brokers is enabled.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - max_size -- Maximum size of topic in megabytes, which is the size of the memory allocated for the topic. Default is 1024. Max for Standard SKU is 5120 and for Premium SKU is 81920
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - status -- Enumerates the possible values for the status of a messaging entity.
    '''
    return _call_az("az servicebus topic update", locals())

