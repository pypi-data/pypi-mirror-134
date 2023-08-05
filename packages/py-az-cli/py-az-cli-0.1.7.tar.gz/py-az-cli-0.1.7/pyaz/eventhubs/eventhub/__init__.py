'''
Manage Azure EventHubs eventhub and authorization-rule
'''
from ... pyaz_utils import _call_az
from . import authorization_rule, consumer_group


def create(name, namespace_name, resource_group, archive_name_format=None, blob_container=None, capture_interval=None, capture_size_limit=None, destination_name=None, enable_capture=None, message_retention=None, partition_count=None, skip_empty_archives=None, status=None, storage_account=None):
    '''
    Creates the EventHubs Eventhub

    Required Parameters:
    - name -- Name of Eventhub
    - namespace_name -- name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - archive_name_format -- Blob naming convention for archive, e.g. {Namespace}/{EventHub}/{PartitionId}/{Year}/{Month}/{Day}/{Hour}/{Minute}/{Second}. Here all the parameters (Namespace,EventHub .. etc) are mandatory irrespective of order
    - blob_container -- Blob container Name
    - capture_interval -- Allows you to set the frequency with which the capture to Azure Blobs will happen, value should between 60 to 900 seconds
    - capture_size_limit -- Defines the amount of data built up in your Event Hub before an capture operation, value should be between 10485760 to 524288000 bytes
    - destination_name -- Name for capture destination, should be EventHubArchive.AzureBlockBlob.
    - enable_capture -- A boolean value that indicates whether capture description is enabled.
    - message_retention -- Number of days to retain events for this Event Hub, value should be 1 to 7 days and depends on Namespace sku. if Namespace sku is Basic than value should be one and is Manadatory parameter. Namespace sku is standard value should be 1 to 7 days, default is 7 days and is optional parameter
    - partition_count -- Number of partitions created for the Event Hub. By default, allowed values are 2-32. Lower value of 1 is supported with Kafka enabled namespaces. In presence of a custom quota, the upper limit will match the upper limit of the quota.
    - skip_empty_archives -- A boolean value that indicates whether to Skip Empty.
    - status -- Status of Eventhub
    - storage_account -- Name (if within same resource group and not of type Classic Storage) or ARM id of the storage account to be used to create the blobs
    '''
    return _call_az("az eventhubs eventhub create", locals())


def show(name, namespace_name, resource_group):
    '''
    shows the Eventhub Details

    Required Parameters:
    - name -- Name of Eventhub
    - namespace_name -- name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventhubs eventhub show", locals())


def list(namespace_name, resource_group, skip=None, top=None):
    '''
    List the EventHub by Namespace

    Required Parameters:
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - skip -- Skip is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skip parameter that specifies a starting point to use for subsequent calls.
    - top -- May be used to limit the number of results to the most recent N usageDetails.
    '''
    return _call_az("az eventhubs eventhub list", locals())


def delete(name, namespace_name, resource_group):
    '''
    Deletes the Eventhub

    Required Parameters:
    - name -- Name of Eventhub
    - namespace_name -- name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventhubs eventhub delete", locals())


def update(name, namespace_name, resource_group, add=None, archive_name_format=None, blob_container=None, capture_interval=None, capture_size_limit=None, destination_name=None, enable_capture=None, force_string=None, message_retention=None, partition_count=None, remove=None, set=None, skip_empty_archives=None, status=None, storage_account=None):
    '''
    Updates the EventHubs Eventhub

    Required Parameters:
    - name -- Name of Eventhub
    - namespace_name -- name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - archive_name_format -- Blob naming convention for archive, e.g. {Namespace}/{EventHub}/{PartitionId}/{Year}/{Month}/{Day}/{Hour}/{Minute}/{Second}. Here all the parameters (Namespace,EventHub .. etc) are mandatory irrespective of order
    - blob_container -- Blob container Name
    - capture_interval -- Allows you to set the frequency with which the capture to Azure Blobs will happen, value should between 60 to 900 seconds
    - capture_size_limit -- Defines the amount of data built up in your Event Hub before an capture operation, value should be between 10485760 to 524288000 bytes
    - destination_name -- Name for capture destination, should be EventHubArchive.AzureBlockBlob.
    - enable_capture -- A boolean value that indicates whether capture description is enabled.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - message_retention -- Number of days to retain events for this Event Hub, value should be 1 to 7 days and depends on Namespace sku. if Namespace sku is Basic than value should be one and is Manadatory parameter. Namespace sku is standard value should be 1 to 7 days, default is 7 days and is optional parameter
    - partition_count -- Number of partitions created for the Event Hub. By default, allowed values are 2-32. Lower value of 1 is supported with Kafka enabled namespaces. In presence of a custom quota, the upper limit will match the upper limit of the quota.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - skip_empty_archives -- A boolean value that indicates whether to Skip Empty.
    - status -- Status of Eventhub
    - storage_account -- Name (if within same resource group and not of type Classic Storage) or ARM id of the storage account to be used to create the blobs
    '''
    return _call_az("az eventhubs eventhub update", locals())

