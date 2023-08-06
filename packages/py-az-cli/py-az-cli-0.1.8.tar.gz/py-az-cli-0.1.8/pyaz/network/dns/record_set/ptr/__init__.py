from ..... pyaz_utils import _call_az

def show(name, resource_group, zone_name, record_type=None):
    '''
    Get the details of a PTR record set.

    Required Parameters:
    - name -- The name of the record set, relative to the name of the zone.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - zone_name -- The name of the zone.

    Optional Parameters:
    - record_type -- ==SUPPRESS==
    '''
    return _call_az("az network dns record-set ptr show", locals())


def delete(name, resource_group, zone_name, if_match=None, record_type=None, yes=None):
    '''
    Delete a PTR record set and all associated records.

    Required Parameters:
    - name -- The name of the record set, relative to the name of the zone.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - zone_name -- The name of the zone.

    Optional Parameters:
    - if_match -- The etag of the record set. Omit this value to always delete the current record set. Specify the last-seen etag value to prevent accidentally deleting any concurrent changes.
    - record_type -- ==SUPPRESS==
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az network dns record-set ptr delete", locals())


def list(resource_group, zone_name, record_type=None):
    '''
    List all PTR record sets in a zone.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - zone_name -- The name of the zone.

    Optional Parameters:
    - record_type -- ==SUPPRESS==
    '''
    return _call_az("az network dns record-set ptr list", locals())


def create(name, resource_group, zone_name, if_match=None, if_none_match=None, metadata=None, record_set_type=None, target_resource=None, ttl=None):
    '''
    Create an empty PTR record set.

    Required Parameters:
    - name -- The name of the record set, relative to the name of the zone.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - zone_name -- The name of the zone.

    Optional Parameters:
    - if_match -- The etag of the record set. Omit this value to always overwrite the current record set. Specify the last-seen etag value to prevent accidentally overwriting any concurrent changes.
    - if_none_match -- Create the record set only if it does not already exist.
    - metadata -- Metadata in space-separated key=value pairs. This overwrites any existing metadata.
    - record_set_type -- ==SUPPRESS==
    - target_resource -- ID of an Azure resource from which the DNS resource value is taken.
    - ttl -- Record set TTL (time-to-live)
    '''
    return _call_az("az network dns record-set ptr create", locals())


def add_record(ptrdname, record_set_name, resource_group, zone_name, if_none_match=None, ttl=None):
    '''
    Add a PTR record.

    Required Parameters:
    - ptrdname -- PTR target domain name.
    - record_set_name -- The name of the record set relative to the zone. Creates a new record set if one does not exist.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - zone_name -- The name of the zone.

    Optional Parameters:
    - if_none_match -- Create the record set only if it does not already exist.
    - ttl -- Record set TTL (time-to-live)
    '''
    return _call_az("az network dns record-set ptr add-record", locals())


def remove_record(ptrdname, record_set_name, resource_group, zone_name, keep_empty_record_set=None):
    '''
    Remove a PTR record from its record set.

    Required Parameters:
    - ptrdname -- PTR target domain name.
    - record_set_name -- The name of the record set relative to the zone.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - zone_name -- The name of the zone.

    Optional Parameters:
    - keep_empty_record_set -- Keep the empty record set if the last record is removed.
    '''
    return _call_az("az network dns record-set ptr remove-record", locals())


def update(name, resource_group, zone_name, add=None, force_string=None, if_match=None, if_none_match=None, metadata=None, record_type=None, remove=None, set=None, target_resource=None):
    '''
    Update a PTR record set.

    Required Parameters:
    - name -- The name of the record set, relative to the name of the zone.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - zone_name -- The name of the zone.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - if_match -- The etag of the record set. Omit this value to always overwrite the current record set. Specify the last-seen etag value to prevent accidentally overwriting any concurrent changes.
    - if_none_match -- Set to '*' to allow a new record set to be created, but to prevent updating an existing record set. Other values will be ignored.
    - metadata -- Metadata in space-separated key=value pairs. This overwrites any existing metadata.
    - record_type -- ==SUPPRESS==
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    - target_resource -- ID of an Azure resource from which the DNS resource value is taken.
    '''
    return _call_az("az network dns record-set ptr update", locals())

