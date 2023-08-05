'''
Manage Azure EventHubs namespace and Authorizationrule
'''
from ... pyaz_utils import _call_az
from . import authorization_rule, network_rule, private_endpoint_connection, private_link_resource


def create(name, resource_group, assign_identity=None, capacity=None, cluster_arm_id=None, default_action=None, disable_local_auth=None, enable_auto_inflate=None, enable_kafka=None, enable_trusted_service_access=None, location=None, maximum_throughput_units=None, sku=None, tags=None, zone_redundant=None):
    '''
    Creates the EventHubs Namespace

    Required Parameters:
    - name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - assign_identity -- A boolean value that indicates whether Managed Identity is enabled.
    - capacity -- Capacity for Sku
    - cluster_arm_id -- luster ARM ID of the Namespace
    - default_action -- Default Action for Network Rule Set.
    - disable_local_auth -- A boolean value that indicates whether SAS authentication is enabled/disabled for the Event Hubs
    - enable_auto_inflate -- A boolean value that indicates whether AutoInflate is enabled for eventhub namespace.
    - enable_kafka -- A boolean value that indicates whether Kafka is enabled for eventhub namespace.
    - enable_trusted_service_access -- A boolean value that indicates whether Trusted Service Access is enabled for Network Rule Set.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - maximum_throughput_units -- Upper limit of throughput units when AutoInflate is enabled, vaule should be within 0 to 20 throughput units. ( 0 if AutoInflateEnabled = true)
    - sku -- Namespace SKU.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    - zone_redundant -- Enabling this property creates a Standard EventHubs Namespace in regions supported availability zones
    '''
    return _call_az("az eventhubs namespace create", locals())


def show(name, resource_group):
    '''
    shows the Event Hubs Namespace Details

    Required Parameters:
    - name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventhubs namespace show", locals())


def list(resource_group=None):
    '''
    Lists the EventHubs Namespaces

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventhubs namespace list", locals())


def delete(name, resource_group):
    '''
    Deletes the Namespaces

    Required Parameters:
    - name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventhubs namespace delete", locals())


def exists(name):
    '''
    check for the availability of the given name for the Namespace

    Required Parameters:
    - name -- Namespace name. Name can contain only letters, numbers, and hyphens. The namespace must start with a letter, and it must end with a letter or number.
    '''
    return _call_az("az eventhubs namespace exists", locals())


def update(name, resource_group, add=None, assign_identity=None, capacity=None, default_action=None, disable_local_auth=None, enable_auto_inflate=None, enable_kafka=None, enable_trusted_service_access=None, force_string=None, infra_encryption=None, key_name=None, key_source=None, key_vault_uri=None, key_version=None, maximum_throughput_units=None, remove=None, set=None, sku=None, tags=None):
    '''
    Updates the EventHubs Namespace

    Required Parameters:
    - name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - assign_identity -- A boolean value that indicates whether Managed Identity is enabled.
    - capacity -- Capacity for Sku
    - default_action -- Default Action for Network Rule Set.
    - disable_local_auth -- A boolean value that indicates whether SAS authentication is enabled/disabled for the Event Hubs
    - enable_auto_inflate -- A boolean value that indicates whether AutoInflate is enabled for eventhub namespace.
    - enable_kafka -- A boolean value that indicates whether Kafka is enabled for eventhub namespace.
    - enable_trusted_service_access -- A boolean value that indicates whether Trusted Service Access is enabled for Network Rule Set.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - infra_encryption -- A boolean value that indicates whether Infrastructure Encryption (Double Encryption) is enabled/disabled
    - key_name -- The name of the KeyVault key.
    - key_source -- Encryption key source. Possible values include: 'Microsoft.KeyVault'.
    - key_vault_uri -- The Uri of the KeyVault.
    - key_version -- The version of the KeyVault key to use.
    - maximum_throughput_units -- Upper limit of throughput units when AutoInflate is enabled, vaule should be within 0 to 20 throughput units. ( 0 if AutoInflateEnabled = true)
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - sku -- Namespace SKU.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az eventhubs namespace update", locals())

