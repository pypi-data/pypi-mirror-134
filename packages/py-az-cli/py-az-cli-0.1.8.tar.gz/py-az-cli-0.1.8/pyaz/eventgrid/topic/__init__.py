'''
Manage Azure Event Grid topics.
'''
from ... pyaz_utils import _call_az
from . import key


def show(name, resource_group):
    '''
    Get the details of a topic.

    Required Parameters:
    - name -- Name of the topic.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventgrid topic show", locals())


def delete(name, resource_group):
    '''
    Delete a topic.

    Required Parameters:
    - name -- Name of the topic.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventgrid topic delete", locals())


def list(odata_query=None, resource_group=None):
    '''
    List available topics.

    Optional Parameters:
    - odata_query -- The OData query used for filtering the list results. Filtering is currently allowed on the Name property only. The supported operations include: CONTAINS, eq (for equal), ne (for not equal), AND, OR and NOT.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventgrid topic list", locals())


def create(name, resource_group, extended_location_name=None, extended_location_type=None, identity=None, inbound_ip_rules=None, input_mapping_default_values=None, input_mapping_fields=None, input_schema=None, kind=None, location=None, public_network_access=None, sku=None, tags=None):
    '''
    Create a topic.

    Required Parameters:
    - name -- Name of the topic.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - extended_location_name -- The extended location name if kind==azurearc.
    - extended_location_type -- The extended location type if kind==azurearc.
    - identity -- The managed identity type for the resource.
    - inbound_ip_rules -- None
    - input_mapping_default_values -- When input-schema is specified as customeventschema, this parameter can be used to specify input mappings based on default values. You can use this parameter when your custom schema does not include a field that corresponds to one of the three fields supported by this parameter. Specify space separated mappings in 'key=value' format. Allowed key names are 'subject', 'eventtype', 'dataversion'. The corresponding value names should specify the default values to be used for the mapping and they will be used only when the published event doesn't have a valid mapping for a particular field.
    - input_mapping_fields -- When input-schema is specified as customeventschema, this parameter is used to specify input mappings based on field names. Specify space separated mappings in 'key=value' format. Allowed key names are 'id', 'topic', 'eventtime', 'subject', 'eventtype', 'dataversion'. The corresponding value names should specify the names of the fields in the custom input schema. If a mapping for either 'id' or 'eventtime' is not provided, Event Grid will auto-generate a default value for these two fields.
    - input_schema -- Schema in which incoming events will be published to this topic/domain. If you specify customeventschema as the value for this parameter, you must also provide values for at least one of --input_mapping_default_values / --input_mapping_fields.
    - kind -- The kind of topic resource.
    - location -- Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
    - public_network_access -- This determines if traffic is allowed over public network. By default it is enabled. You can further restrict to specific IPs by configuring.
    - sku -- The Sku name of the resource.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az eventgrid topic create", locals())


def update(name, resource_group, identity=None, inbound_ip_rules=None, public_network_access=None, sku=None, tags=None):
    '''
    Update a topic.

    Required Parameters:
    - name -- Name of the topic.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - identity -- The managed identity type for the resource.
    - inbound_ip_rules -- None
    - public_network_access -- This determines if traffic is allowed over public network. By default it is enabled. You can further restrict to specific IPs by configuring.
    - sku -- The Sku name of the resource.
    - tags -- space-separated tags: key[=value] [key[=value] ...]. Use '' to clear existing tags.
    '''
    return _call_az("az eventgrid topic update", locals())

