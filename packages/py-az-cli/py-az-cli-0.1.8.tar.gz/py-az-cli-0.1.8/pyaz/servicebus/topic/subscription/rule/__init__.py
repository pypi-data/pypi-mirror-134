'''
Manage Azure Service Bus Rule
'''
from ..... pyaz_utils import _call_az

def create(name, namespace_name, resource_group, subscription_name, topic_name, action_compatibility_level=None, action_sql_expression=None, content_type=None, correlation_id=None, enable_action_preprocessing=None, enable_correlation_preprocessing=None, enable_sql_preprocessing=None, filter_sql_expression=None, label=None, message_id=None, reply_to=None, reply_to_session_id=None, session_id=None, to=None):
    '''
    Create the ServiceBus Rule for Subscription

    Required Parameters:
    - name -- Name of Rule
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - subscription_name -- Name of Subscription
    - topic_name -- Name of Topic

    Optional Parameters:
    - action_compatibility_level -- This property is reserved for future use. An integer value showing the compatibility level, currently hard-coded to 20.
    - action_sql_expression -- Action SQL expression.
    - content_type -- Content type of message.
    - correlation_id -- Identifier of correlation.
    - enable_action_preprocessing -- A boolean value that indicates whether the rule action requires preprocessing.
    - enable_correlation_preprocessing -- A boolean value that indicates whether the rule action requires preprocessing.
    - enable_sql_preprocessing -- A boolean value that indicates whether the rule action requires preprocessing.
    - filter_sql_expression -- SQL expression. e.g. myproperty=test
    - label -- Application specific label.
    - message_id -- Identifier of message.
    - reply_to -- Address of the queue to reply to.
    - reply_to_session_id -- Session identifier to reply to.
    - session_id -- Session identifier
    - to -- Address to send to.
    '''
    return _call_az("az servicebus topic subscription rule create", locals())


def show(name, namespace_name, resource_group, subscription_name, topic_name):
    '''
    Shows ServiceBus Rule Details

    Required Parameters:
    - name -- Name of Rule
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - subscription_name -- Name of Subscription
    - topic_name -- Name of Topic
    '''
    return _call_az("az servicebus topic subscription rule show", locals())


def list(namespace_name, resource_group, subscription_name, topic_name, skip=None, top=None):
    '''
    List the ServiceBus Rule by Subscription

    Required Parameters:
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - subscription_name -- Name of Subscription
    - topic_name -- Name of Topic

    Optional Parameters:
    - skip -- Skip is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skip parameter that specifies a starting point to use for subsequent calls.
    - top -- May be used to limit the number of results to the most recent N usageDetails.
    '''
    return _call_az("az servicebus topic subscription rule list", locals())


def delete(name, namespace_name, resource_group, subscription_name, topic_name):
    '''
    Deletes the ServiceBus Rule

    Required Parameters:
    - name -- Name of Rule
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - subscription_name -- Name of Subscription
    - topic_name -- Name of Topic
    '''
    return _call_az("az servicebus topic subscription rule delete", locals())


def update(name, namespace_name, resource_group, subscription_name, topic_name, action_compatibility_level=None, action_sql_expression=None, add=None, content_type=None, correlation_id=None, enable_action_preprocessing=None, enable_correlation_preprocessing=None, enable_sql_preprocessing=None, filter_sql_expression=None, force_string=None, label=None, message_id=None, remove=None, reply_to=None, reply_to_session_id=None, session_id=None, set=None, to=None):
    '''
    Updates the ServiceBus Rule for Subscription

    Required Parameters:
    - name -- Name of Rule
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - subscription_name -- Name of Subscription
    - topic_name -- Name of Topic

    Optional Parameters:
    - action_compatibility_level -- This property is reserved for future use. An integer value showing the compatibility level, currently hard-coded to 20.
    - action_sql_expression -- Action SQL expression.
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - content_type -- Content type of message.
    - correlation_id -- Identifier of correlation.
    - enable_action_preprocessing -- A boolean value that indicates whether the rule action requires preprocessing.
    - enable_correlation_preprocessing -- A boolean value that indicates whether the rule action requires preprocessing.
    - enable_sql_preprocessing -- A boolean value that indicates whether the rule action requires preprocessing.
    - filter_sql_expression -- SQL expression. e.g. myproperty=test
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - label -- Application specific label.
    - message_id -- Identifier of message.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - reply_to -- Address of the queue to reply to.
    - reply_to_session_id -- Session identifier to reply to.
    - session_id -- Session identifier
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - to -- Address to send to.
    '''
    return _call_az("az servicebus topic subscription rule update", locals())

