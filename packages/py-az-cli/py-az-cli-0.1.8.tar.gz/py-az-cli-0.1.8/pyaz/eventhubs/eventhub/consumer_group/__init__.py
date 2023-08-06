from .... pyaz_utils import _call_az

def create(eventhub_name, name, namespace_name, resource_group, user_metadata=None):
    '''
    Creates the EventHub ConsumerGroup

    Required Parameters:
    - eventhub_name -- Name of EventHub
    - name -- Name of ConsumerGroup
    - namespace_name -- name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - user_metadata -- Usermetadata is a placeholder to store user-defined string data with maximum length 1024. e.g. it can be used to store descriptive data, such as list of teams and their contact information also user-defined configuration settings can be stored.
    '''
    return _call_az("az eventhubs eventhub consumer-group create", locals())


def show(eventhub_name, name, namespace_name, resource_group):
    '''
    Shows the ConsumerGroup Details

    Required Parameters:
    - eventhub_name -- Name of EventHub
    - name -- Name of ConsumerGroup
    - namespace_name -- name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventhubs eventhub consumer-group show", locals())


def list(eventhub_name, namespace_name, resource_group, skip=None, top=None):
    '''
    List the ConsumerGroup by Eventhub

    Required Parameters:
    - eventhub_name -- Name of EventHub
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - skip -- Skip is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skip parameter that specifies a starting point to use for subsequent calls.
    - top -- May be used to limit the number of results to the most recent N usageDetails.
    '''
    return _call_az("az eventhubs eventhub consumer-group list", locals())


def delete(eventhub_name, name, namespace_name, resource_group):
    '''
    Deletes the ConsumerGroup

    Required Parameters:
    - eventhub_name -- Name of EventHub
    - name -- Name of ConsumerGroup
    - namespace_name -- name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventhubs eventhub consumer-group delete", locals())


def update(eventhub_name, name, namespace_name, resource_group, add=None, force_string=None, remove=None, set=None, user_metadata=None):
    '''
    Updates the EventHub ConsumerGroup

    Required Parameters:
    - eventhub_name -- Name of EventHub
    - name -- Name of ConsumerGroup
    - namespace_name -- name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - user_metadata -- Usermetadata is a placeholder to store user-defined string data with maximum length 1024. e.g. it can be used to store descriptive data, such as list of teams and their contact information also user-defined configuration settings can be stored.
    '''
    return _call_az("az eventhubs eventhub consumer-group update", locals())

