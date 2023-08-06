from ... pyaz_utils import _call_az

def show(origin_group_name, profile_name, resource_group):
    '''
    

    Required Parameters:
    - origin_group_name -- Name of the origin group.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az afd origin-group show", locals())


def list(profile_name, resource_group):
    '''
    

    Required Parameters:
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az afd origin-group list", locals())


def create(additional_latency_in_milliseconds, origin_group_name, probe_path, probe_protocol, probe_request_type, profile_name, resource_group, sample_size, successful_samples_required, probe_interval_in_seconds=None):
    '''
    Creates a new origin group within the specified profile.

    Required Parameters:
    - additional_latency_in_milliseconds -- The additional latency in milliseconds for probes to fall into the lowest latency bucket.
    - origin_group_name -- Name of the origin group.
    - probe_path -- The path relative to the origin that is used to determine the health of the origin.
    - probe_protocol -- Protocol to use for health probe.
    - probe_request_type -- The type of health probe request that is made.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - sample_size -- The number of samples to consider for load balancing decisions.
    - successful_samples_required -- The number of samples within the sample period that must succeed.

    Optional Parameters:
    - probe_interval_in_seconds -- The number of seconds between health probes.
    '''
    return _call_az("az afd origin-group create", locals())


def update(origin_group_name, profile_name, resource_group, additional_latency_in_milliseconds=None, probe_interval_in_seconds=None, probe_path=None, probe_protocol=None, probe_request_type=None, sample_size=None, successful_samples_required=None):
    '''
    Creates a new origin group within the specified profile.

    Required Parameters:
    - origin_group_name -- Name of the origin group.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - additional_latency_in_milliseconds -- The additional latency in milliseconds for probes to fall into the lowest latency bucket.
    - probe_interval_in_seconds -- The number of seconds between health probes.
    - probe_path -- The path relative to the origin that is used to determine the health of the origin.
    - probe_protocol -- Protocol to use for health probe.
    - probe_request_type -- The type of health probe request that is made.
    - sample_size -- The number of samples to consider for load balancing decisions.
    - successful_samples_required -- The number of samples within the sample period that must succeed.
    '''
    return _call_az("az afd origin-group update", locals())


def delete(origin_group_name, profile_name, resource_group, yes=None):
    '''
    Deletes an existing origin group within the specified profile.

    Required Parameters:
    - origin_group_name -- Name of the origin group.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az afd origin-group delete", locals())

