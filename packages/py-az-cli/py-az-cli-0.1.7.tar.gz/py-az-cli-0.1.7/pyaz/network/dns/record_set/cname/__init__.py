from ..... pyaz_utils import _call_az

def show(name, resource_group, zone_name, record_type=None):
    '''
    Get the details of a CNAME record set.

    Required Parameters:
    - name -- The name of the record set, relative to the name of the zone.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - zone_name -- The name of the zone.

    Optional Parameters:
    - record_type -- ==SUPPRESS==
    '''
    return _call_az("az network dns record-set cname show", locals())


def delete(name, resource_group, zone_name, if_match=None, record_type=None, yes=None):
    '''
    Delete a CNAME record set and its associated record.

    Required Parameters:
    - name -- The name of the record set, relative to the name of the zone.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - zone_name -- The name of the zone.

    Optional Parameters:
    - if_match -- The etag of the record set. Omit this value to always delete the current record set. Specify the last-seen etag value to prevent accidentally deleting any concurrent changes.
    - record_type -- ==SUPPRESS==
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az network dns record-set cname delete", locals())


def list(resource_group, zone_name, record_type=None):
    '''
    List the CNAME record set in a zone.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - zone_name -- The name of the zone.

    Optional Parameters:
    - record_type -- ==SUPPRESS==
    '''
    return _call_az("az network dns record-set cname list", locals())


def create(name, resource_group, zone_name, if_match=None, if_none_match=None, metadata=None, record_set_type=None, target_resource=None, ttl=None):
    '''
    Create an empty CNAME record set.

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
    return _call_az("az network dns record-set cname create", locals())


def set_record(cname, record_set_name, resource_group, zone_name, if_none_match=None, ttl=None):
    '''
    Set the value of a CNAME record.

    Required Parameters:
    - cname -- Value of the cname record-set. It should be Canonical name.
    - record_set_name -- The name of the record set relative to the zone. Creates a new record set if one does not exist.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - zone_name -- The name of the zone.

    Optional Parameters:
    - if_none_match -- Create the record set only if it does not already exist.
    - ttl -- Record set TTL (time-to-live)
    '''
    return _call_az("az network dns record-set cname set-record", locals())


def remove_record(cname, record_set_name, resource_group, zone_name, keep_empty_record_set=None):
    '''
    Remove a CNAME record from its record set.

    Required Parameters:
    - cname -- Value of the cname record-set. It should be Canonical name.
    - record_set_name -- The name of the record set relative to the zone.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - zone_name -- The name of the zone.

    Optional Parameters:
    - keep_empty_record_set -- Keep the empty record set if the last record is removed.
    '''
    return _call_az("az network dns record-set cname remove-record", locals())

